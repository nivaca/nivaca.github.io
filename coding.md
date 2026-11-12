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
    <p class="project-role">2026 · v3.11 · on <a href="https://codeberg.org/{{ site.codeberg_username }}/py-words">Codeberg</a> and <a href="https://github.com/{{ site.github_username }}/py-words">GitHub</a></p>
    <p><b>py-words</b> is a Latin-English-Latin and Latin-Spanish-Latin dictionary written in Python. It started from William Whitaker's WORDS, but both code and data have been redesigned, and it now includes Lewis and Short's English dictionary and the Spanish ones of Echave-Sustaeta and De Miguel. It analyses inflected Latin words, and whole lines of Latin, into their forms and dictionary entries, with meanings in English or Spanish, and finds the Latin for English or Spanish words. It runs in a window, on the command line, in the terminal or in a web browser, and needs only Python 3.11 or later.</p>
    <p><a class="button button-primary" href="{{ "/py-words/" | relative_url }}"><i class="fas fa-book-open" aria-hidden="true"></i> Try it in your browser</a></p>
    <p class="alt-link">WebAssembly version here: <a href="https://nicolasvaughan.org/py-words/browser/">nicolasvaughan.org/py-words/browser/</a></p>
  </li>

  <li class="project">
    <h2><a href="https://github.com/{{ site.github_username }}/py-wtk">py-wtk: Wiktionary from the terminal or the desktop</a></h2>
    <p class="project-role">2026 · v1.8 · on <a href="https://codeberg.org/{{ site.codeberg_username }}/py-wtk">Codeberg</a> and <a href="https://github.com/{{ site.github_username }}/py-wtk">GitHub</a></p>
    <p><b>py-wtk</b> is a Python interface to the <a href="https://en.wiktionary.org">English Wiktionary</a> for looking up words without opening a web browser. It comes as a command-line tool, a full-screen terminal interface and a desktop window, all sharing the same code. It shows the complete entry, not only the definitions: etymology, pronunciation, examples and quotations, usage notes, inflection tables, synonyms, derived and related terms, descendants and translations, for all the languages on the page or only those you choose (only Latin, say, or Latin and Spanish). It can also search page titles and output structured JSON for use in other programs. It needs only Python 3.11 or later and its standard library (plus Tkinter for the window), and there is also a self-contained AppImage for Linux.</p>
  </li>

  <li class="project">
    <h2><a href="https://github.com/{{ site.github_username }}/krunner-py-wtk">krunner-py-wtk: Wiktionary in KRunner</a></h2>
    <p class="project-role">2026 · v1.0 · on <a href="https://codeberg.org/{{ site.codeberg_username }}/krunner-py-wtk">Codeberg</a> and <a href="https://github.com/{{ site.github_username }}/krunner-py-wtk">GitHub</a></p>
    <p><b>krunner-py-wtk</b> brings <a href="https://github.com/{{ site.github_username }}/py-wtk">py-wtk</a> to <a href="https://userbase.kde.org/Plasma/Krunner">KRunner</a> in KDE Plasma 6: type <code>wtk</code> and a word, and its Wiktionary entries appear, one for each part of speech in each language, with the headword line and the first definitions. Languages can be chosen in the query itself (<code>wtk rosa @la</code> for Latin only), expressions of several words work, and a word without a page suggests similar titles. Enter opens the entry in py-wtk's window, and other actions copy the full entry or open it on Wiktionary. Lookups wait for a pause in typing and run on a separate thread, so KRunner never hangs, and recent results are cached. A small settings window sets the prefix, the languages and the number of results and definitions shown. It is written in Python and needs py-wtk and the Python D-Bus bindings.</p>
  </li>

  <li class="project">
    <h2><a href="https://github.com/{{ site.github_username }}/krunner-abbr">krunner-abbr: abbreviation expander for KDE Plasma</a></h2>
    <p class="project-role">2026 · v2.0 · on <a href="https://codeberg.org/{{ site.codeberg_username }}/krunner-abbr">Codeberg</a> and <a href="https://github.com/{{ site.github_username }}/krunner-abbr">GitHub</a></p>
    <p><b>krunner-abbr</b> is a <a href="https://userbase.kde.org/Plasma/Krunner">KRunner</a> plugin for Plasma 6, written in Python, that expands abbreviations: type <code>abbr</code> and an abbreviation, press Enter, and the expansion is copied to the clipboard. Abbreviations live in a TOML file and can use placeholders for dates, the clipboard, typed text, input dialogs and shell commands, with chainable filters to clean up text (title case, unwrapping text copied from PDFs, quote conversion, sorting). It comes with examples for LaTeX and Markdown, Latin (Roman numerals, macrons), and fetching BibTeX from a DOI, plus a settings dialog with a live preview.</p>
  </li>

  <li class="project">
    <h2><a href="https://github.com/{{ site.github_username }}/QuickView">QuickView: Quick Look-style file previews for KDE Plasma</a></h2>
    <p class="project-role">2026 · v0.1.3 · on <a href="https://github.com/{{ site.github_username }}/QuickView">GitHub</a></p>
    <p><b>QuickView</b> is a reworked fork of <a href="https://github.com/MustaphaAlioglou/QuickView">Mustapha Alioglou's QuickView</a>, a macOS Quick Look-style previewer for KDE Plasma 6: select a file in Dolphin, press Space, and a floating preview panel appears; arrow keys walk the folder or page through a multi-file selection. It previews images, PDFs (with search and a contents sidebar), EPUB books laid out as pages, rendered Markdown, syntax-highlighted source code, HTML, audio and video, archive listings, spreadsheets as real grids, and office documents laid out as pages through LibreOffice. A resident daemon makes the panel appear in about 20 ms, and every parser runs in a bubblewrap sandbox with no network or filesystem access. The fork adds support for the Flathub LibreOffice, fixes a bug that could leave the panel hanging, splits the daemon into smaller modules and hardens the installer. It is written in Python with PySide6 and needs Python 3.10 or later and bubblewrap.</p>
  </li>

  <li class="project">
    <h2><a href="https://github.com/{{ site.github_username }}/py-imposition">py-imposition: a command-line PDF imposition toolkit</a></h2>
    <p class="project-role">2026 · v0.8 · on <a href="https://codeberg.org/{{ site.codeberg_username }}/py-imposition">Codeberg</a> and <a href="https://github.com/{{ site.github_username }}/py-imposition">GitHub</a></p>
    <p><b>py-imposition</b> prepares PDFs for printing and binding from the command line, covering the feature set of the Quite Imposing Plus plug-in for Acrobat without needing Acrobat. It makes booklets (perfect, saddle-stitched or cut-and-stack, with creep and right-to-left binding), n-up sheets and step-and-repeat layouts, and it can shuffle, trim, shift and scale pages, add bleeds, crop and fold marks, page numbers and stamps, merge variable data, and split or join documents. Commands can be chained, saved as reusable sequences, or attached to hot folders that process whatever PDFs land in them. It is written in Python with pikepdf and ReportLab.</p>
  </li>

  <li class="project">
    <h2><a href="https://github.com/{{ site.github_username }}/pdf-word-finder">pdf-word-finder: find which pages of a PDF a word is on</a></h2>
    <p class="project-role">2026 · v1.4 · on <a href="https://codeberg.org/{{ site.codeberg_username }}/pdf-word-finder">Codeberg</a> and <a href="https://github.com/{{ site.github_username }}/pdf-word-finder">GitHub</a></p>
    <p><b>pdf-word-finder</b> searches a PDF for a list of words, phrases or regular expressions and reports the pages each one appears on, one line per term, in the form of a book index. It gives the page numbers printed in the book (roman numerals in the front matter, restarts in later volumes) rather than the PDF's position in the file, and warns when the PDF has no page labels instead of making them up. It runs on the command line or in a window, and needs only Python 3.9 or later and <code>pypdf</code>, using PyMuPDF when available for better reading order in pages with columns, footnotes or critical apparatus.</p>
  </li>

  <li class="project">
    <h2><a href="https://github.com/{{ site.github_username }}/validate">validate: Schematron validation for TEI-XML from the terminal</a></h2>
    <p class="project-role">2026 · v1.4 · on <a href="https://codeberg.org/{{ site.codeberg_username }}/validate">Codeberg</a> and <a href="https://github.com/{{ site.github_username }}/validate">GitHub</a></p>
    <p><b>validate</b> is a Python script that checks TEI-XML documents against the Schematron rules embedded in an ODD (or in an already-extracted <code>.sch</code>, or harvested from an ODD-generated RelaxNG schema, the rules Jing ignores), running them with Saxon. Unlike oXygen, which silently stops after a hundred errors, it reports every violation, with counts per rule and, if asked, the line number and <code>xml:id</code> of each offender, and says exactly how many it left out when the listing is capped. It returns a non-zero exit code on violations, so it can run in a Makefile or a pre-commit hook. It needs Python 3.9 or later, <code>saxonche</code> and <code>lxml</code>.</p>
  </li>

  <li class="project">
    <h2><a href="https://doi.org/10.47397/tb/42-2/tb131vaughan-tei">TEI-XML to LaTeX workflow</a></h2>
    <p class="project-role">2021 · <i>TUGboat</i> 42 (2)</p>
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
