---
layout: archive
title: "Publications and Talks"
permalink: /publicationsList/
author_profile: true
---

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}


## Articles and Preprints
<ol reversed>{% for post in site.publications reversed %}
  {% include archive-single-publication.html %}
{% endfor %}</ol>

## Talks
<ul>{% for post in site.talks reversed %}
  {% include archive-single-talk-cv.html %}
{% endfor %}</ul>
