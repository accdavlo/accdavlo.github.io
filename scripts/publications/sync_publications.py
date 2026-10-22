#!/usr/bin/env python3
"""Keep _publications in sync with arXiv and the published journal versions.

What it does, in order:
  1. Queries arXiv for the author's papers.
     - a paper not yet on the website gets a new post, a BibTeX file and its PDF;
     - a paper with a new arXiv version gets its PDF re-downloaded.
  2. For every post that is still a preprint (no `doi`, venue arXiv/preprint),
     looks for the published version (arXiv DOI field, OpenAlex, Crossref).
     If found: updates venue/doi/citation in the post and replaces the BibTeX.

Only the standard library is used. Run from anywhere:
    python scripts/publications/sync_publications.py [--dry-run] [--report out.md]
        [--pr-body pr.md] [--new-papers new.txt]

The GitHub workflow pushes changes to papers already on the website directly,
and opens a pull request with the files listed in --new-papers.

Optional environment variables:
    OPENALEX_API_KEY  free key from https://openalex.org/settings/api
    CONTACT_EMAIL     sent to Crossref/OpenAlex to use their "polite" pool
"""
import argparse
import json
import os
import re
import sys
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from difflib import SequenceMatcher
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
POSTS_DIR = ROOT / "_publications"
PDF_DIR = ROOT / "files" / "publications"
BIB_DIR = PDF_DIR / "bib"
STATE_FILE = HERE / "state.json"
CONFIG_FILE = HERE / "config.json"

USER_AGENT = "davidetorlo.it publication sync (https://github.com/accdavlo/accdavlo.github.io)"
TITLE_MATCH = 0.88  # minimum similarity to consider two titles the same paper
PREPRINT_VENUE = re.compile(r"arxiv|preprint|submitted|in review", re.I)
ARXIV_ID = re.compile(r"(\d{4}\.\d{4,5})(?:v(\d+))?")
PUBLISHED_TYPES = {"journal-article", "proceedings-article", "book-chapter"}
STOPWORDS = {"a", "an", "the", "of", "for", "and", "on", "in", "to", "with", "via", "by", "from", "its", "their"}
NAME_PARTICLES = {"de", "di", "da", "del", "della", "van", "von", "der", "den", "le", "la", "dos", "du"}

ATOM = {"a": "http://www.w3.org/2005/Atom", "x": "http://arxiv.org/schemas/atom"}

DRY_RUN = False


# ---------------------------------------------------------------- utilities

def http_get(url, accept=None, retries=3):
    """GET a URL, retrying on transient errors. Returns bytes, or None on 404."""
    headers = {"User-Agent": USER_AGENT}
    if accept:
        headers["Accept"] = accept
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=90) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return None
            if attempt == retries - 1:
                raise
        except (urllib.error.URLError, TimeoutError):
            if attempt == retries - 1:
                raise
        time.sleep(5 * 2 ** attempt)


def get_json(url):
    data = http_get(url, accept="application/json")
    return json.loads(data) if data else None


def norm_title(s):
    s = re.sub(r"<[^>]+>", " ", s or "")
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    return " ".join(re.sub(r"[^a-z0-9]+", " ", s.lower()).split())


def similarity(a, b):
    return SequenceMatcher(None, norm_title(a), norm_title(b)).ratio()


def clean_ws(s):
    return " ".join((s or "").split())


def yaml_single(s):
    return "'" + s.replace("'", "''") + "'"


def yaml_double(s):
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def write_bytes(path, data):
    if not DRY_RUN:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)


def write_text(path, text):
    write_bytes(path, text.encode("utf-8"))


def rel(path):
    return path.relative_to(ROOT).as_posix()


# ---------------------------------------------------------------- authors

def split_name(full):
    """'Mario Ricchiuto' -> ('Ricchiuto', 'Mario'); 'Elise Le Mélédo' -> ('Le Mélédo', 'Elise')."""
    parts = clean_ws(full).split(" ")
    if len(parts) == 1:
        return parts[0], ""
    i = len(parts) - 1
    while i > 1 and parts[i - 1].lower() in NAME_PARTICLES:
        i -= 1
    return " ".join(parts[i:]), " ".join(parts[:i])


def initials(given):
    """'Chi-Wang' -> 'C.W.', 'Davide' -> 'D.'"""
    return "".join(p[0] + "." for p in re.split(r"[\s\-.]+", given) if p)


def short_authors(names):
    """[(surname, given)] -> 'Barsukow, W. and Torlo, D.' (style already used on the site)."""
    return " and ".join(f"{s}, {initials(g)}" if g else s for s, g in names)


# ---------------------------------------------------------------- posts

class Post:
    def __init__(self, path):
        self.path = path
        text = path.read_text(encoding="utf-8")
        m = re.match(r"---\s*\n(.*?)\n---[ \t]*\n?(.*)", text, re.S)
        if not m:
            raise ValueError(f"{path}: no front matter")
        self.front, self.body = m.group(1), m.group(2)
        self.changed = False

    def get(self, key):
        m = re.search(rf"^{key}:[ \t]*(.*)$", self.front, re.M)
        if not m:
            return None
        v = m.group(1).strip()
        if len(v) >= 2 and v[0] == v[-1] == "'":
            return v[1:-1].replace("''", "'")
        if len(v) >= 2 and v[0] == v[-1] == '"':
            return v[1:-1].replace('\\"', '"').replace("\\\\", "\\")
        return v

    def set(self, key, raw_value):
        """Set a front matter field; raw_value must already be valid YAML."""
        line = f"{key}: {raw_value}"
        if re.search(rf"^{key}:", self.front, re.M):
            new = re.sub(rf"^{key}:.*$", lambda _: line, self.front, count=1, flags=re.M)
        else:
            new = self.front + "\n" + line
        if new != self.front:
            self.front = new
            self.changed = True

    def arxiv_id(self):
        m = ARXIV_ID.search(self.get("arxiv") or "")
        return m.group(1) if m else None

    def is_preprint(self):
        return not self.get("doi") and bool(PREPRINT_VENUE.search(self.get("venue") or ""))

    def autoupdate(self):
        return (self.get("autoupdate") or "").lower() not in ("false", "no", "0")

    def save(self):
        if self.changed:
            write_text(self.path, f"---\n{self.front}\n---\n{self.body}")
            self.changed = False


def load_posts():
    return [Post(p) for p in sorted(POSTS_DIR.glob("*.md"))]


# ---------------------------------------------------------------- arXiv

class ArxivEntry:
    def __init__(self, e):
        url = e.find("a:id", ATOM).text
        m = ARXIV_ID.search(url)
        self.id, self.version = m.group(1), int(m.group(2) or 1)
        self.title = clean_ws(e.find("a:title", ATOM).text)
        self.abstract = clean_ws(e.find("a:summary", ATOM).text)
        self.published = e.find("a:published", ATOM).text[:10]
        self.authors = [split_name(a.find("a:name", ATOM).text) for a in e.findall("a:author", ATOM)]
        doi = e.find("x:doi", ATOM)
        self.doi = doi.text.strip() if doi is not None else None

    @property
    def abs_url(self):
        return f"https://arxiv.org/abs/{self.id}"


def fetch_arxiv(cfg):
    surname, initial = cfg["author_surname"], cfg["author_initial"]
    url = ("https://export.arxiv.org/api/query?search_query=au:" + urllib.parse.quote(surname)
           + "&max_results=500&sortBy=submittedDate&sortOrder=ascending")
    # The arXiv API occasionally answers with an empty feed: retry before giving up.
    for attempt in range(4):
        root = ET.fromstring(http_get(url))
        entries = [ArxivEntry(e) for e in root.findall("a:entry", ATOM)]
        if entries:
            break
        time.sleep(10 * (attempt + 1))
    else:
        sys.exit("arXiv returned no entries; aborting without touching anything.")
    # Keep only papers by *this* author (same surname, matching first initial).
    return [e for e in entries
            if any(s.lower() == surname.lower() and g[:1].upper() == initial for s, g in e.authors)]


def download_arxiv_pdf(entry, dest):
    data = http_get(f"https://arxiv.org/pdf/{entry.id}v{entry.version}")
    if not data or not data.startswith(b"%PDF"):
        raise RuntimeError(f"arXiv:{entry.id}v{entry.version} did not return a PDF")
    write_bytes(dest, data)


# ---------------------------------------------------------------- OpenAlex / Crossref

def openalex_works(orcid):
    params = {"filter": f"author.orcid:{orcid}", "per-page": "200",
              "select": "id,doi,title,type,primary_location"}
    if os.environ.get("OPENALEX_API_KEY"):
        params["api_key"] = os.environ["OPENALEX_API_KEY"]
    if os.environ.get("CONTACT_EMAIL"):
        params["mailto"] = os.environ["CONTACT_EMAIL"]
    works, page = [], 1
    while True:
        params["page"] = str(page)
        data = get_json("https://api.openalex.org/works?" + urllib.parse.urlencode(params))
        works += data["results"]
        if len(data["results"]) < 200:
            return works
        page += 1


def crossref_url(path, **params):
    if os.environ.get("CONTACT_EMAIL"):
        params["mailto"] = os.environ["CONTACT_EMAIL"]
    return "https://api.crossref.org/" + path + ("?" + urllib.parse.urlencode(params) if params else "")


def crossref_work(doi):
    data = get_json(crossref_url("works/" + urllib.parse.quote(doi)))
    return data["message"] if data else None


def crossref_search(title, surname):
    data = get_json(crossref_url("works", **{"query.bibliographic": title, "query.author": surname,
                                             "rows": "5", "select": "DOI,title,type"}))
    return data["message"]["items"] if data else []


def bare_doi(doi):
    return re.sub(r"^https?://(dx\.)?doi\.org/", "", doi or "").strip().lower()


def is_arxiv_doi(doi):
    return bare_doi(doi).startswith("10.48550/")


def format_bibtex(raw, key=None):
    """Pretty-print a one-line BibTeX record (as returned by doi.org), optionally renaming its key."""
    m = re.match(r"\s*@(\w+)\s*\{\s*([^,]+),(.*)\}\s*$", raw, re.S)
    if not m:
        return raw.strip() + "\n"
    kind, old_key, body = m.groups()
    fields, cur, depth, quoted = [], "", 0, False
    for ch in body:
        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
        elif ch == '"' and depth == 0:
            quoted = not quoted
        if ch == "," and depth == 0 and not quoted:
            fields.append(cur.strip())
            cur = ""
        else:
            cur += ch
    fields.append(cur.strip())
    fields = [f for f in fields if f]
    lines = [f"@{kind}{{{key or old_key.strip()},"] + [f"  {f}," for f in fields]
    lines[-1] = lines[-1].rstrip(",")
    return "\n".join(lines) + "\n}\n"


def bib_key(path):
    m = re.search(r"@\w+\s*\{\s*([^,\s]+)\s*,", path.read_text(encoding="utf-8")) if path.exists() else None
    return m.group(1) if m else None


# ---------------------------------------------------------------- report

class Report:
    def __init__(self):
        self.sections = {"New papers": [], "Updated PDFs (new arXiv version)": [],
                         "Now published": [], "Warnings": []}
        self.new_files = []  # files belonging to new papers (go to a pull request, not pushed directly)

    def add(self, section, line):
        self.sections[section].append(line)
        print(f"[{section}] {line}")

    def markdown(self, sections=None):
        out = ["Automatic update of the publications from arXiv / Crossref / OpenAlex.", ""]
        for title, lines in self.sections.items():
            if lines and (sections is None or title in sections):
                out += [f"### {title}", *[f"- {l}" for l in lines], ""]
        if self.sections["New papers"] and (sections is None or "New papers" in sections):
            out += ["", "**Please review the generated excerpt and citation of the new posts before merging.**"]
        return "\n".join(out) + "\n"


# ---------------------------------------------------------------- step 1: arXiv

def match_post(entry, posts, state):
    known = state["arxiv"].get(entry.id)
    if known:
        for p in posts:
            if rel(p.path) == known.get("post"):
                return p
    by_id = [p for p in posts if p.arxiv_id() == entry.id]
    if by_id:
        return max(by_id, key=lambda p: similarity(p.get("title"), entry.title))
    best = max(posts, key=lambda p: similarity(p.get("title"), entry.title), default=None)
    if best and similarity(best.get("title"), entry.title) >= TITLE_MATCH:
        return best
    return None


def slugify(title, n=5):
    words = [w for w in norm_title(title).split() if w not in STOPWORDS]
    return "-".join(words[:n])


def unique_key(base):
    key, i = base, 1
    while (BIB_DIR / f"{key}.bib").exists() or (PDF_DIR / f"{key}.pdf").exists():
        i += 1
        key = f"{base}{i}"
    return key


def first_sentence(text, limit=300):
    m = re.match(r"(.+?[.!?])(\s|$)", text)
    s = m.group(1) if m else text
    return s if len(s) <= limit else s[:limit].rsplit(" ", 1)[0] + "…"


def create_post(entry):
    year = entry.published[:4]
    first_word = next((w for w in norm_title(entry.title).split() if w not in STOPWORDS), "paper")
    key = unique_key(f"{norm_title(entry.authors[0][0]).replace(' ', '')}{year}{first_word}")
    slug = f"{entry.published}-{slugify(entry.title)}"
    path = POSTS_DIR / f"{slug}.md"

    citation = f"{short_authors(entry.authors)} ({year}), {entry.title}, arXiv:{entry.id}."
    front = "\n".join([
        f"title: {yaml_double(entry.title)}",
        "collection: publications",
        f"permalink: /publication/{slug}",
        f"excerpt: {yaml_single(first_sentence(entry.abstract))}",
        f"date: {entry.published}",
        "venue: 'ArXiv'",
        f"paperurl: '{entry.abs_url}'",
        f"arxiv: '{entry.abs_url}'",
        f"citation: {yaml_single(citation)}",
        f"pdf: /files/publications/{key}.pdf",
        f"bib: /files/publications/bib/{key}.bib",
    ])
    authors_bib = " and ".join(f"{s}, {g}" if g else s for s, g in entry.authors)
    bib = (f"@article{{{key},\n  title={{{entry.title}}},\n  author={{{authors_bib}}},\n"
           f"  journal={{arXiv preprint arXiv:{entry.id}}},\n  year={{{year}}}\n}}\n")

    pdf_path, bib_path = PDF_DIR / f"{key}.pdf", BIB_DIR / f"{key}.bib"
    download_arxiv_pdf(entry, pdf_path)
    write_text(bib_path, bib)
    write_text(path, f"---\n{front}\n---\n{entry.abstract}\n")
    return path, pdf_path, bib_path


def sync_arxiv(entries, posts, state, cfg, report, refresh_pdfs):
    ignore = set(cfg.get("ignore_arxiv", []))
    for entry in entries:
        if entry.id in ignore:
            continue
        post = match_post(entry, posts, state)

        if post is None:
            # Not recorded in the state: it is picked up there once the pull request is merged.
            path, pdf, bib = create_post(entry)
            if not DRY_RUN:
                posts.append(Post(path))
            report.new_files += [rel(path), rel(pdf), rel(bib)]
            report.add("New papers", f"[{entry.title}]({entry.abs_url}) → `{rel(path)}`")
            continue

        if post.arxiv_id() != entry.id:
            report.add("Warnings", f"`{rel(post.path)}` matches arXiv:{entry.id} by title, "
                                   f"but its `arxiv` field is `{post.get('arxiv')}`")

        known = state["arxiv"].get(entry.id)
        state["arxiv"][entry.id] = {"version": entry.version, "post": rel(post.path)}
        first_seen = known is None
        newer = not first_seen and entry.version > known.get("version", 0)
        refresh = first_seen and refresh_pdfs and post.is_preprint()
        if not (newer or refresh):
            continue
        pdf = post.get("pdf")
        if not pdf:
            report.add("Warnings", f"`{rel(post.path)}` has no `pdf` field; arXiv v{entry.version} not downloaded")
        elif not post.autoupdate():
            report.add("Warnings", f"arXiv:{entry.id}v{entry.version} available but `{rel(post.path)}` "
                                   "has `autoupdate: false`")
        else:
            download_arxiv_pdf(entry, ROOT / pdf.lstrip("/"))
            report.add("Updated PDFs (new arXiv version)",
                       f"{post.get('title')} → v{entry.version} (`{pdf}`)")


# ---------------------------------------------------------------- step 2: published versions

def find_published_doi(post, arxiv_by_id, oa_works, cfg):
    title = post.get("title")
    candidates = []
    entry = arxiv_by_id.get(post.arxiv_id())
    if entry and entry.doi:
        candidates.append(entry.doi)
    for w in oa_works:
        if w.get("doi") and not is_arxiv_doi(w["doi"]) and similarity(w.get("title"), title) >= TITLE_MATCH:
            candidates.append(w["doi"])
    try:
        for item in crossref_search(title, cfg["author_surname"]):
            if item.get("type") in PUBLISHED_TYPES and similarity((item.get("title") or [""])[0], title) >= TITLE_MATCH:
                candidates.append(item["DOI"])
    except Exception as e:  # Crossref search is only one of the sources
        print(f"Crossref search failed for {title!r}: {e}")

    seen = set()
    for doi in candidates:
        doi = bare_doi(doi)
        if doi in seen or is_arxiv_doi(doi):
            continue
        seen.add(doi)
        work = crossref_work(doi)
        if not work or work.get("type") not in PUBLISHED_TYPES:
            continue
        # Guard against wrong DOIs: the title must match and the author must be on the paper.
        if similarity((work.get("title") or [""])[0], title) < TITLE_MATCH - 0.1:
            continue
        if not any((a.get("family") or "").lower() == cfg["author_surname"].lower() for a in work.get("author", [])):
            continue
        return doi, work
    return None, None


def journal_citation(work):
    names = [(a.get("family", ""), a.get("given", "")) for a in work.get("author", [])]
    year = (work.get("issued") or work.get("published") or {}).get("date-parts", [[None]])[0][0]
    venue = (work.get("container-title") or [""])[0]
    where = venue
    if work.get("volume"):
        where += f", {work['volume']}"
        if work.get("issue"):
            where += f"({work['issue']})"
    pages = work.get("page") or work.get("article-number")
    if pages:
        where += f", {pages}"
    title = clean_ws(re.sub(r"<[^>]+>", "", (work.get("title") or [""])[0]))
    return f"{short_authors(names)} ({year}), {title}, {where}.", venue


def sync_published(posts, arxiv_by_id, oa_works, cfg, report):
    for post in posts:
        if not post.is_preprint() or not post.autoupdate():
            continue
        doi, work = find_published_doi(post, arxiv_by_id, oa_works, cfg)
        if not doi:
            continue
        citation, venue = journal_citation(work)
        doi_url = f"https://doi.org/{doi}"
        post.set("venue", yaml_single(venue))
        post.set("paperurl", yaml_single(doi_url))
        post.set("doi", yaml_single(doi_url))
        post.set("citation", yaml_single(citation))

        raw_bib = http_get(doi_url, accept="application/x-bibtex")
        if raw_bib:
            bib_path = ROOT / post.get("bib").lstrip("/") if post.get("bib") else BIB_DIR / f"{post.path.stem}.bib"
            write_text(bib_path, format_bibtex(raw_bib.decode("utf-8"), key=bib_key(bib_path)))
            post.set("bib", "/" + rel(bib_path))
        post.save()
        report.add("Now published", f"{post.get('title')} → *{venue}* ([{doi}]({doi_url}))")


# ---------------------------------------------------------------- main

def main():
    global DRY_RUN
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dry-run", action="store_true", help="report what would change, write nothing")
    ap.add_argument("--report", type=Path, help="write a markdown summary to this file")
    ap.add_argument("--pr-body", type=Path, help="write the new-papers summary (pull request body) to this file")
    ap.add_argument("--new-papers", type=Path, help="write the list of files of new papers to this file")
    ap.add_argument("--refresh-pdfs", action="store_true",
                    help="on first sight of a paper, re-download the latest arXiv PDF of preprint posts")
    args = ap.parse_args()
    DRY_RUN = args.dry_run

    cfg = json.loads(CONFIG_FILE.read_text())
    state = json.loads(STATE_FILE.read_text()) if STATE_FILE.exists() else {"arxiv": {}}
    posts = load_posts()
    report = Report()

    entries = fetch_arxiv(cfg)
    print(f"arXiv: {len(entries)} papers")
    sync_arxiv(entries, posts, state, cfg, report, args.refresh_pdfs)

    try:
        oa_works = openalex_works(cfg["orcid"])
        print(f"OpenAlex: {len(oa_works)} works")
    except Exception as e:
        oa_works = []
        report.add("Warnings", f"OpenAlex unavailable ({e}); used arXiv/Crossref only")

    sync_published(posts, {e.id: e for e in entries}, oa_works, cfg, report)

    if not DRY_RUN:
        STATE_FILE.write_text(json.dumps(state, indent=2, sort_keys=True) + "\n")
    md = report.markdown()
    if args.report:
        args.report.write_text(md)
    if args.pr_body:
        args.pr_body.write_text(report.markdown(sections={"New papers", "Warnings"}))
    if args.new_papers:
        args.new_papers.write_text("".join(f + "\n" for f in report.new_files))
    print("\n" + md)


if __name__ == "__main__":
    main()
