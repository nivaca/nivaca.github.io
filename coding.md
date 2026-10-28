---
layout: page
title: Coding
permalink: /coding/
description: Software, scripts and programming tools by Nicolás Vaughan.
---

I write software mostly in [Python](https://www.python.org/), along with XML/TEI and [LaTeX](https://www.latex-project.org/). My code is on [GitHub](https://github.com/{{ site.github_username }}) and [Codeberg](https://codeberg.org/{{ site.codeberg_username }}).

<ul class="projects">
  <li class="project">
    <h2><a href="https://codeberg.org/{{ site.codeberg_username }}/py-words">py-words: a Latin dictionary with morphology</a></h2>
    <p class="project-role">Author (2026) · on <a href="https://codeberg.org/{{ site.codeberg_username }}/py-words">Codeberg</a> and <a href="https://github.com/{{ site.github_username }}/py-words">GitHub</a></p>
    <p><b>py-words</b> is a Latin-English-Latin and Latin-Spanish-Latin dictionary written in Python. It started from William Whitaker's WORDS, but both code and data have been redesigned, and it now includes Lewis and Short's English dictionary and the Spanish ones of Echave-Sustaeta and De Miguel. It analyses inflected Latin words, and whole lines of Latin, into their forms and dictionary entries, with meanings in English or Spanish, and finds the Latin for English or Spanish words. It runs in a window, on the command line, in the terminal or in a web browser, and needs only Python 3.11 or later.</p>
    <p><a class="button button-primary" href="{{ "/py-words/" | relative_url }}"><i class="fas fa-book-open" aria-hidden="true"></i> Try it in your browser</a></p>
  </li>

  <li class="project">
    <h2><a href="https://github.com/{{ site.github_username }}/krunner-abbr">krunner-abbr: abbreviation expander for KDE Plasma</a></h2>
    <p class="project-role">Author (2026) · on <a href="https://github.com/{{ site.github_username }}/krunner-abbr">GitHub</a></p>
    <p><b>krunner-abbr</b> is a <a href="https://userbase.kde.org/Plasma/Krunner">KRunner</a> plugin for Plasma 6, written in Python, that expands abbreviations: type <code>abbr</code> and an abbreviation, press Enter, and the expansion is copied to the clipboard. Abbreviations live in a TOML file and can use placeholders for dates, the clipboard, typed text, input dialogs and shell commands, with chainable filters to clean up text (title case, unwrapping text copied from PDFs, quote conversion, sorting). It comes with examples for LaTeX and Markdown, Latin (Roman numerals, macrons), and fetching BibTeX from a DOI, plus a settings dialog with a live preview.</p>
  </li>

  <li class="project">
    <h2><a href="https://github.com/{{ site.github_username }}/pdf-word-finder">pdf-word-finder: find which pages of a PDF a word is on</a></h2>
    <p class="project-role">Author (2026) · on <a href="https://github.com/{{ site.github_username }}/pdf-word-finder">GitHub</a></p>
    <p><b>pdf-word-finder</b> searches a PDF for a list of words, phrases or regular expressions and reports the pages each one appears on, one line per term, in the form of a book index. It gives the page numbers printed in the book (roman numerals in the front matter, restarts in later volumes) rather than the PDF's position in the file, and warns when the PDF has no page labels instead of making them up. It runs on the command line or in a window, and needs only Python 3.9 or later and <code>pypdf</code>, using PyMuPDF when available for better reading order in pages with columns, footnotes or critical apparatus.</p>
  </li>

  <li class="project">
    <h2><a href="https://github.com/{{ site.github_username }}/validate">validate: Schematron validation for TEI-XML from the terminal</a></h2>
    <p class="project-role">Author (2026) · on <a href="https://github.com/{{ site.github_username }}/validate">GitHub</a></p>
    <p><b>validate</b> is a Python script that checks TEI-XML documents against the Schematron rules embedded in an ODD (or in an already-extracted <code>.sch</code>, or harvested from an ODD-generated RelaxNG schema, the rules Jing ignores), running them with Saxon. Unlike oXygen, which silently stops after a hundred errors, it reports every violation, with counts per rule and, if asked, the line number and <code>xml:id</code> of each offender, and says exactly how many it left out when the listing is capped. It returns a non-zero exit code on violations, so it can run in a Makefile or a pre-commit hook. It needs Python 3.9 or later, <code>saxonche</code> and <code>lxml</code>.</p>
  </li>

  <li class="project">
    <h2><a href="https://doi.org/10.47397/tb/42-2/tb131vaughan-tei">TEI-XML to LaTeX workflow</a></h2>
    <p class="project-role">Author (2021) · <i>TUGboat</i> 42 (2)</p>
    <p>A workflow for typesetting critical editions encoded in TEI-XML with LaTeX, and the lessons learned building it.</p>
  </li>
</ul>

## Other software

<ol class="publications">
  {% for pub in site.data.software %}
    {% include publication.html pub=pub %}
  {% endfor %}
</ol>

## Tools I use

I exclusively use [GNU/Linux](https://en.wikipedia.org/wiki/GNU/Linux_naming_controversy) on my machines.
Currently I am happily on the [Fedora Linux](https://fedoraproject.org/) distribution with the [KDE Plasma](https://kde.org/plasma-desktop/) desktop.
For many years I used the [Manjaro Linux](https://manjaro.org/) distribution, as well as (vanilla) [Arch Linux](https://archlinux.org/), but found them pretty unstable and hard to use on a daily basis.

I mostly use [GNU Emacs](https://www.gnu.org/s/emacs/) as my general editor (writing and coding), but frequently resort to [Neovim](https://neovim.io/), [Visual Studio Code](https://code.visualstudio.com/), [PyCharm](https://www.jetbrains.com/pycharm/), and [Oxygen XML Editor](https://www.oxygenxml.com/), depending on my needs.

I built this website with the static site generator [Jekyll](https://jekyllrb.com); the design started from a theme by [S.V. Miller](https://svmiller.com/).
Its source code is available [on GitHub](https://github.com/{{ site.github_username }}/nivaca.github.io).
