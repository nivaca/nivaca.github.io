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
  </li>

  <li class="project">
    <h2><a href="https://github.com/{{ site.github_username }}/krunner-py-words">krunner-py-words: py-words in KRunner</a></h2>
    <p class="project-role">2026 · v1.1.1 · on <a href="https://codeberg.org/{{ site.codeberg_username }}/krunner-py-words">Codeberg</a> and <a href="https://github.com/{{ site.github_username }}/krunner-py-words">GitHub</a></p>
    <p><b>krunner-py-words</b> brings py-words to <a href="https://userbase.kde.org/Plasma/Krunner">KRunner</a> in KDE Plasma 6: type <code>pw</code> and a Latin word, or a whole line of Latin, and its entries appear as you type, each with its dictionary form, its meaning and the analysed forms (<code>amīc-ōrum GEN.PL</code>). With <code>pw ~e</code> it goes the other way, from an English or Spanish word to the Latin. Enter opens the search in the py-words window, and other actions copy the results of an entry or open the search in the online dictionary. The results follow the settings of py-words, and a small settings window of its own sets the prefix, the language of the meanings and of the interface, and the number of results. The runner stays in memory with the dictionary loaded, so each query is quick. It is written in Python with the D-Bus bindings, and comes as a Fedora package on Copr, which brings py-words with it, or from the source with Python 3.14 or later.</p>
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
    <p><b>py-imposition</b> prepares PDFs for printing and binding from the command line. It makes booklets (perfect, saddle-stitched or cut-and-stack, with creep and right-to-left binding), n-up sheets and step-and-repeat layouts, and it can shuffle, trim, shift and scale pages, add bleeds, crop and fold marks, page numbers and stamps, merge variable data, and split or join documents. Commands can be chained, saved as reusable sequences, or attached to hot folders that process whatever PDFs land in them. It is written in Python with pikepdf and ReportLab.</p>
  </li>

  <li class="project">
    <h2><a href="https://github.com/{{ site.github_username }}/pdf-word-finder">pdf-word-finder: find which pages of a PDF a word is on</a></h2>
    <p class="project-role">2026 · v1.4 · on <a href="https://codeberg.org/{{ site.codeberg_username }}/pdf-word-finder">Codeberg</a> and <a href="https://github.com/{{ site.github_username }}/pdf-word-finder">GitHub</a></p>
    <p><b>pdf-word-finder</b> searches a PDF for a list of words, phrases or regular expressions and reports the pages each one appears on, one line per term, in the form of a book index. It gives the page numbers printed in the book (roman numerals in the front matter, restarts in later volumes) rather than the PDF's position in the file, and warns when the PDF has no page labels instead of making them up. It runs on the command line or in a window, and needs only Python 3.9 or later and <code>pypdf</code>, using PyMuPDF when available for better reading order in pages with columns, footnotes or critical apparatus.</p>
  </li>

  <li class="project">
    <h2><a href="https://github.com/{{ site.github_username }}/py-foliation">py-foliation: change the page labels of PDF documents</a></h2>
    <p class="project-role">2026 · v0.1 · on <a href="https://codeberg.org/{{ site.codeberg_username }}/py-foliation">Codeberg</a> and <a href="https://github.com/{{ site.github_username }}/py-foliation">GitHub</a></p>
    <p><b>py-foliation</b> changes the page labels of PDF documents: the numbering a PDF viewer shows for their pages. A book whose front matter is numbered i, ii, iii and whose text starts again at 1 can show those numbers in the viewer, instead of the plain 1, 2, 3 of the pages of the file; only the labels change, and the pages are left as they are. Labels are set as ranges, each with its first page, its style (arabic, roman or letters, upper or lower case, or no number), the number it starts at and a prefix, so that an appendix can run App-1, App-2 or a last page be called Cover. It has a window for seeing and editing the labels page by page, with undo and redo, and a command line for doing the same in scripts; the window can copy the command that gives the same labels to another file. The interface is in English and Spanish. It is written in Python with pikepdf and PySide6, and comes as an AppImage for Linux, a Fedora package on Copr, or from the source with Python 3.12 or later.</p>
  </li>

  <li class="project" id="py-redact">
    <h2><a href="https://github.com/{{ site.github_username }}/py-redact">py-redact: redact PDF documents</a></h2>
    <p class="project-role">2026 · v0.4.3 · on <a href="https://codeberg.org/{{ site.codeberg_username }}/py-redact">Codeberg</a> and <a href="https://github.com/{{ site.github_username }}/py-redact">GitHub</a></p>
    <p><b>py-redact</b> redacts PDF documents. You mark on the pages what must go, and in the redacted copy whatever lies under each mark is removed for good: the text, letter by letter, the part of the images under it, the drawings it covers, and the annotations and form fields that touch it. This is not the same as drawing a black rectangle, which hides the text from the eye but leaves it in the file; py-redact takes it out, and after saving checks the copy to make sure nothing that was under a mark can still be read. The place can be filled with a colour or left as it is, with a text such as <code>REDACTED</code> or a FOIA exemption code written over it. There are several ways to mark: drag over text or draw a box, find and mark every occurrence of a word, a list of words or a pattern (phone numbers, e-mail addresses, card and identity numbers, dates, bank accounts), and repeat a mark on other pages. It can also remove a document's hidden information (metadata, attachments, bookmarks, comments, hidden text, scripts), and save the copy as PDF/A or PDF/X through <a href="#py-pdfconform">py-pdfconform</a>. The window is in English and Spanish. It is written in Python with PyMuPDF and PySide6, and comes as an AppImage for Linux, a Fedora package on Copr, or from the source with Python 3.14 or later.</p>
  </li>

  <li class="project" id="py-pdfconform">
    <h2><a href="https://github.com/{{ site.github_username }}/py-pdfconform">py-pdfconform: convert PDF files to PDF/A and PDF/X-4</a></h2>
    <p class="project-role">2026 · v1.1 · on <a href="https://codeberg.org/{{ site.codeberg_username }}/py-pdfconform">Codeberg</a> and <a href="https://github.com/{{ site.github_username }}/py-pdfconform">GitHub</a></p>
    <p><b>py-pdfconform</b> converts PDF files to two ISO standards: PDF/A for long-term archiving (PDF/A-1b, 2b and 3b) and PDF/X-4 for printing. It is a single command-line script. Ghostscript does the conversion itself; pikepdf opens encrypted or damaged files before it and, after it, restores lost metadata and corrects what Ghostscript leaves wrong. Each result is then checked: PDF/A files with veraPDF, if it is installed, and PDF/X-4 files with a structural check of its own. It warns about everything a standard forces it to drop (JavaScript, attachments, annotations in PDF/X, transparency flattened to images in PDF/A-1b), never writes over the input, and returns exit codes fit for scripts. It needs Python 3.14 or later, Ghostscript 10 or later and pikepdf.</p>
  </li>

  <li class="project" id="py-xmlvalidate">
    <h2><a href="https://github.com/{{ site.github_username }}/py-xmlvalidate">py-xmlvalidate: Schematron validation for TEI-XML from the terminal</a></h2>
    <p class="project-role">2026 · v1.14 · on <a href="https://codeberg.org/{{ site.codeberg_username }}/py-xmlvalidate">Codeberg</a> and <a href="https://github.com/{{ site.github_username }}/py-xmlvalidate">GitHub</a></p>
    <p><b>py-xmlvalidate</b> is a Python script that checks TEI-XML documents against the Schematron rules embedded in an ODD (or in an already-extracted <code>.sch</code>, or harvested from an ODD-generated RelaxNG schema, the rules Jing ignores), running them with Saxon. Unlike oXygen, which silently stops after a hundred errors, it reports every violation, with counts per rule and, if asked, the line number and <code>xml:id</code> of each offender, and says exactly how many it left out when the listing is capped. It returns a non-zero exit code on violations, so it can run in a Makefile or a pre-commit hook. It needs Python 3.15 or later, <code>saxonche</code> and <code>lxml</code>.</p>
    <p class="continued">It also finds the schema on its own from the document's <code>&lt;?xml-model?&gt;</code> declarations, and its JSON report drives the <a href="#schematron-validator">Schematron Validator</a> extension for VS Code, described below.</p>
  </li>

  <li class="project" id="schematron-validator">
    <h2><a href="https://marketplace.visualstudio.com/items?itemName=NicolasVaughan.validate-schematron">Schematron Validator: TEI-XML validation as you type in VS Code</a></h2>
    <p class="project-role">2026 · v0.5.10 · on the <a href="https://marketplace.visualstudio.com/items?itemName=NicolasVaughan.validate-schematron">Visual Studio Marketplace</a> · source on <a href="https://codeberg.org/{{ site.codeberg_username }}/py-xmlvalidate">Codeberg</a> and <a href="https://github.com/{{ site.github_username }}/py-xmlvalidate">GitHub</a></p>
    <p><b>Schematron Validator</b> is a VS Code extension that brings <a href="#py-xmlvalidate">py-xmlvalidate</a> into the editor. It checks XML and TEI files against Schematron rules (from a <code>.sch</code>, an ODD, or a RelaxNG schema with embedded rules) as you type, on open and on save, unsaved edits included. Each violation is underlined on the offending element and listed in the Problems panel, with its severity taken from the rule's <code>role</code>. If the schema is RelaxNG and <a href="https://relaxng.org/jclark/jing.html">jing</a> is installed, structural errors are added too, and badly formed XML is flagged where the broken tag was opened. The schema is found from the document's <code>&lt;?xml-model?&gt;</code> declaration or set in the settings; a status-bar indicator shows whether the file is clean, and commands let you pick the Python interpreter or re-download a schema that changed upstream. The script comes bundled; the extension needs Python 3.15 or later with <code>saxonche</code> and <code>lxml</code>, and its page walks you through installing them.</p>
    <p><a class="button button-primary" href="https://marketplace.visualstudio.com/items?itemName=NicolasVaughan.validate-schematron"><i class="fas fa-download" aria-hidden="true"></i> Install from the Marketplace</a></p>
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
