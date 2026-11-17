---
layout: page
ref: publications
title: Scripta
permalink: /la/scripta/
description: Libri, capitula, articuli et recensiones Nicolai Vaughan.
---

{% for group in site.data.publications %}
## {{ site.data.i18n.la.sections[group.section] | default: group.section }}

<ol class="publications">
  {% for pub in group.items %}
    {% include publication.html pub=pub %}
  {% endfor %}
</ol>
{% endfor %}

Vide etiam paginas meas in [Google Scholar](https://scholar.google.com/citations?user={{ site.google_scholar_id }}), [ORCID](https://orcid.org/{{ site.orcid_id }}) et [Academia]({{ site.academia_url }}).
