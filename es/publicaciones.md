---
layout: page
ref: publications
title: Publicaciones
permalink: /es/publicaciones/
description: Libros, capítulos, artículos y reseñas de Nicolás Vaughan.
---

{% for group in site.data.publications %}
## {{ site.data.i18n.es.sections[group.section] | default: group.section }}

<ol class="publications">
  {% for pub in group.items %}
    {% include publication.html pub=pub %}
  {% endfor %}
</ol>
{% endfor %}

Véanse también mis perfiles en [Google Scholar](https://scholar.google.com/citations?user={{ site.google_scholar_id }}), [ORCID](https://orcid.org/{{ site.orcid_id }}) y [Academia]({{ site.academia_url }}).
