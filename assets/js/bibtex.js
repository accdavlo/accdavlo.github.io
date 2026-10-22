/*
 * BibTeX panels for the publication pages.
 *
 * A link `<a class="bib-toggle" href="/files/.../x.bib">` opens, below the
 * entry, a panel with the BibTeX record and Copy / Download buttons. The
 * record is fetched from the .bib file on first use. Without JavaScript the
 * link still opens the .bib file.
 */
(function () {
  "use strict";

  var cache = {};
  var counter = 0;

  function el(tag, attrs, children) {
    var node = document.createElement(tag);
    Object.keys(attrs || {}).forEach(function (k) {
      if (k === "text") node.textContent = attrs[k];
      else node.setAttribute(k, attrs[k]);
    });
    (children || []).forEach(function (c) { node.appendChild(c); });
    return node;
  }

  function button(icon, label, cls) {
    return el("button", { type: "button", "class": "bib-box__btn " + (cls || "") }, [
      el("i", { "class": "fas fa-fw " + icon, "aria-hidden": "true" }),
      el("span", { text: label })
    ]);
  }

  function copyText(text) {
    if (navigator.clipboard && window.isSecureContext) {
      return navigator.clipboard.writeText(text);
    }
    // Fallback for old browsers / plain http
    return new Promise(function (resolve, reject) {
      var area = el("textarea", { readonly: "", style: "position:fixed;top:-1000px;opacity:0" });
      area.value = text;
      document.body.appendChild(area);
      area.select();
      var ok = document.execCommand("copy");
      document.body.removeChild(area);
      ok ? resolve() : reject();
    });
  }

  function loadBib(url) {
    if (!cache[url]) {
      cache[url] = fetch(url).then(function (r) {
        if (!r.ok) throw new Error(r.status);
        return r.text();
      }).then(function (t) { return t.trim(); });
    }
    return cache[url];
  }

  function buildPanel(link) {
    var id = "bib-box-" + (++counter);
    var url = link.getAttribute("href");
    var code = el("code", { text: "Loading…" });
    var pre = el("pre", { "class": "bib-box__code", tabindex: "0" }, [code]);
    var copy = button("fa-copy", "Copy", "bib-box__copy");
    var download = el("a", { "class": "bib-box__btn", href: url, download: "" }, [
      el("i", { "class": "fas fa-fw fa-download", "aria-hidden": "true" }),
      el("span", { text: ".bib" })
    ]);
    var close = el("button", { type: "button", "class": "bib-box__btn bib-box__close", "aria-label": "Close" }, [
      el("i", { "class": "fas fa-fw fa-times", "aria-hidden": "true" })
    ]);
    var status = el("span", { "class": "sr-only", "aria-live": "polite" });
    var panel = el("div", { "class": "bib-box", id: id, role: "region", "aria-label": "BibTeX citation" }, [
      el("div", { "class": "bib-box__bar" }, [
        el("span", { "class": "bib-box__title", text: "BibTeX" }),
        el("span", { "class": "bib-box__actions" }, [copy, download, close])
      ]),
      pre,
      status
    ]);

    copy.disabled = true;
    loadBib(url).then(function (text) {
      code.textContent = text;
      copy.disabled = false;
    }).catch(function () {
      code.textContent = "Could not load the BibTeX record. Use the .bib button to download it.";
    });

    var resetTimer;
    copy.addEventListener("click", function () {
      copyText(code.textContent).then(function () {
        copy.classList.add("is-done");
        copy.querySelector("i").className = "fas fa-fw fa-check";
        copy.querySelector("span").textContent = "Copied";
        status.textContent = "BibTeX copied to clipboard";
        clearTimeout(resetTimer);
        resetTimer = setTimeout(function () {
          copy.classList.remove("is-done");
          copy.querySelector("i").className = "fas fa-fw fa-copy";
          copy.querySelector("span").textContent = "Copy";
          status.textContent = "";
        }, 2000);
      }).catch(function () {
        // Clipboard refused: select the text so the visitor can press Ctrl+C
        var range = document.createRange();
        range.selectNodeContents(code);
        var sel = window.getSelection();
        sel.removeAllRanges();
        sel.addRange(range);
      });
    });

    close.addEventListener("click", function () { toggle(link, false); link.focus(); });
    panel.addEventListener("keydown", function (e) {
      if (e.key === "Escape") { toggle(link, false); link.focus(); }
    });

    link.setAttribute("aria-controls", id);
    return panel;
  }

  function panelFor(link) {
    var id = link.getAttribute("aria-controls");
    return id ? document.getElementById(id) : null;
  }

  function toggle(link, open) {
    var panel = panelFor(link);
    if (open === undefined) open = !panel || panel.hidden;
    if (open && !panel) {
      panel = buildPanel(link);
      // Each entry provides a `.bib-slot` where the panel goes; fall back to after the link.
      var item = link.closest(".archive__item, .page__content");
      var slot = item && item.querySelector(".bib-slot");
      (slot || link.parentNode).appendChild(panel);
    }
    if (panel) panel.hidden = !open;
    link.setAttribute("aria-expanded", open ? "true" : "false");
    link.classList.toggle("is-open", open);
  }

  document.addEventListener("click", function (e) {
    var link = e.target.closest && e.target.closest("a.bib-toggle");
    if (!link || e.ctrlKey || e.metaKey || e.shiftKey || e.button !== 0) return;
    e.preventDefault();
    toggle(link);
  });
})();
