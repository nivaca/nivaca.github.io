---
layout: page
title: Publications
permalink: /publications/
description: Books, chapters, articles and reviews by Nicolás Vaughan.
---

{% for group in site.data.publications %}
## {{ group.section }}

<ol class="publications">
  {% for pub in group.items %}
    {% include publication.html pub=pub %}
  {% endfor %}
</ol>
{% endfor %}

See also my profiles on [Google Scholar](https://scholar.google.com/citations?user={{ site.google_scholar_id }}), [ORCID](https://orcid.org/{{ site.orcid_id }}) and [Academia]({{ site.academia_url }}).
