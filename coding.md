---
layout: page
ref: coding
title: Coding
permalink: /coding/
description: Software, scripts and programming tools by Nicolás Vaughan.
---

I write software mostly in [Python](https://www.python.org/): command-line tools, desktop programs with PySide6 (Qt) and plugins for KDE Plasma. Bash scripts take care of the builds and the smaller jobs. Much of my work with texts is done in XML: I encode them in [TEI](https://tei-c.org/), write ODD customisations with their RelaxNG schemas and Schematron rules, query the documents with XPath and transform them with XSLT, most often into [LaTeX](https://www.latex-project.org/), which I typeset with LuaLaTeX. I work in [Emacs](https://www.gnu.org/software/emacs/), and write Emacs Lisp (Elisp) for it: my own configuration and packages such as [py-schematron.el](#py-schematron-el). I have also written some TypeScript, for a VS Code extension. My code is on [GitHub](https://github.com/{{ site.github_username }}) and [Codeberg](https://codeberg.org/{{ site.codeberg_username }}).

<ul class="projects">
  <li class="project project-featured" id="py-words">
    <p class="feature-label">Main project</p>
    <h2><a href="https://codeberg.org/{{ site.codeberg_username }}/py-words">py-words: a Latin dictionary with morphology</a></h2>
    <p class="project-role">2026 · v3.31 · on <a href="https://codeberg.org/{{ site.codeberg_username }}/py-words">Codeberg</a> and <a href="https://github.com/{{ site.github_username }}/py-words">GitHub</a></p>
    <a class="project-shot" href="{{ "/coding/py-words/" | relative_url }}"><img src="{{ "/images/py-words/gui_en.webp" | relative_url }}" alt="The window of py-words in dark mode, showing the entries of perspicio" loading="lazy"></a>
    <p><b>py-words</b> is a Latin-English-Latin and Latin-Spanish-Latin dictionary written in Python. It started from William Whitaker's WORDS, but both code and data have been redesigned, and it now includes Lewis and Short's English dictionary and the Spanish ones of Echave-Sustaeta and De Miguel. It analyses inflected Latin words, and whole lines of Latin, into their forms and dictionary entries, with meanings in English or Spanish, and finds the Latin for English or Spanish words. It runs in a window, on the command line, in the terminal or in a web browser, and needs only Python 3.13 or later. It also works in KRunner, the launcher of KDE Plasma, and as an Android app that carries the whole dictionary and needs no Internet connection.</p>
    <p><a class="button button-primary" href="{{ "/py-words/" | relative_url }}"><i class="fas fa-book-open" aria-hidden="true"></i> Try it in your browser</a>
      <a class="button" href="https://nivaca.pythonanywhere.com/"><i class="fas fa-server" aria-hidden="true"></i> Mirror</a>
      <a class="button" href="{{ "/coding/py-words/" | relative_url }}"><i class="fas fa-info-circle" aria-hidden="true"></i> More about it</a></p>
  </li>

  <li class="project project-featured" id="py-pdftools">
    <p class="feature-label">Main project</p>
    <h2><a href="https://github.com/{{ site.github_username }}/py-pdftools">py-pdftools: annotate, redact, label, impose and OCR PDF documents in one program</a></h2>
    <p class="project-role">2026 · v1.15.0 · on <a href="https://codeberg.org/{{ site.codeberg_username }}/py-pdftools">Codeberg</a> and <a href="https://github.com/{{ site.github_username }}/py-pdftools">GitHub</a></p>
    <a class="project-shot" href="{{ "/coding/py-pdftools/" | relative_url }}"><img src="{{ "/images/py-pdftools/annotate_en.webp" | relative_url }}" alt="py-pdftools in the mode Annotate" loading="lazy"></a>
    <p><b>py-pdftools</b> edits PDF documents: it annotates and redacts them, changes their page labels, headers, footers, watermarks and the order of their pages, imposes them for printing, and reads the text of their scanned pages with tesseract. It brings together, in one window and one command line, seven programs I wrote before it (py-annotate, py-redact, py-foliation, py-imposition, py-pdfocr, pdf-word-finder and pdf2iso), and adds forms, digital signatures, passwords, bookmarks, and the combining, splitting and exporting of documents. It is in English and Spanish, and is written in Python with PyMuPDF, pikepdf, reportlab and PySide6; it comes as an AppImage for Linux, as Fedora and Debian packages, with installers for Linux, macOS and Windows, or from the source with Python 3.14 or later.</p>
    <p><a class="button button-primary" href="{{ "/coding/py-pdftools/" | relative_url }}"><i class="fas fa-info-circle" aria-hidden="true"></i> More about it</a></p>
  </li>

  <li class="project">
    <h2><a href="https://github.com/{{ site.github_username }}/py-wk">py-wk: Wiktionary from the terminal or the desktop</a></h2>
    <p class="project-role">2026 · v1.18 · on <a href="https://codeberg.org/{{ site.codeberg_username }}/py-wk">Codeberg</a> and <a href="https://github.com/{{ site.github_username }}/py-wk">GitHub</a></p>
    <p><b>py-wk</b> is a Python interface to the <a href="https://en.wiktionary.org">English Wiktionary</a> for looking up words without opening a web browser. It comes as a command-line tool, a full-screen terminal interface and a desktop window, all sharing the same code. It shows the complete entry, not only the definitions: etymology, pronunciation, examples and quotations, usage notes, inflection tables, synonyms, derived and related terms, descendants and translations, for all the languages on the page or only those you choose (only Latin, say, or Latin and Spanish). It can also search page titles and output structured JSON for use in other programs. It needs only Python 3.15 or later and its standard library (plus Tkinter for the window), and there is also a self-contained AppImage for Linux.</p>
  </li>

  <li class="project">
    <h2><a href="https://github.com/{{ site.github_username }}/krunner-py-wk">krunner-py-wk: Wiktionary in KRunner</a></h2>
    <p class="project-role">2026 · v1.1 · on <a href="https://codeberg.org/{{ site.codeberg_username }}/krunner-py-wk">Codeberg</a> and <a href="https://github.com/{{ site.github_username }}/krunner-py-wk">GitHub</a></p>
    <p><b>krunner-py-wk</b> brings <a href="https://github.com/{{ site.github_username }}/py-wk">py-wk</a> to <a href="https://userbase.kde.org/Plasma/Krunner">KRunner</a> in KDE Plasma 6: type <code>wk</code> and a word, and its Wiktionary entries appear, one for each part of speech in each language, with the headword line and the first definitions. Languages can be chosen in the query itself (<code>wk rosa @la</code> for Latin only), expressions of several words work, and a word without a page suggests similar titles. Enter opens the entry in py-wk's window, and other actions copy the full entry or open it on Wiktionary. Lookups wait for a pause in typing and run on a separate thread, so KRunner never hangs, and recent results are cached. A small settings window sets the prefix, the languages and the number of results and definitions shown. It is written in Python and needs Python 3.14 or later, py-wk and the D-Bus bindings for Python.</p>
  </li>

  <li class="project" id="wk">
    <h2><a href="https://github.com/{{ site.github_username }}/wk-android">wk: Wiktionary Reader</a></h2>
    <p class="project-role">2026 · v1.4 · on <a href="https://codeberg.org/{{ site.codeberg_username }}/wk-android">Codeberg</a> and <a href="https://github.com/{{ site.github_username }}/wk-android">GitHub</a></p>
    <p><b>wk: Wiktionary Reader</b> is a small Android app for reading the <a href="https://en.wiktionary.org">English Wiktionary</a>, the Android sibling of <a href="https://github.com/{{ site.github_username }}/py-wk">py-wk</a>. You type a word in any language, with suggestions from Wiktionary as you type, and it shows the whole entry, with the styles of the site adapted to a phone: wide tables scroll sideways in their own box, the titles of the sections open and close at a touch, and a bar at the top lists the languages of the page, those you prefer first and the others hidden but one touch away. Links to other entries open in the app, in the right language, and other links open in the browser. A word can be looked up from any app, by selecting it and choosing <i>Look up in Wiktionary</i>, or by sharing a text with wk. Pages are kept for a week, so a word seen again opens at once, and the app follows the light or dark mode of the system. The interface is in English and Spanish. It is written in Kotlin with only the Android framework, no other libraries (the release APK is about 80 KB), and needs Android 10 or later.</p>
  </li>

  <li class="project">
    <h2><a href="https://github.com/{{ site.github_username }}/krunner-abbr">krunner-abbr: abbreviation expander for KDE Plasma</a></h2>
    <p class="project-role">2026 · v2.0.1 · on <a href="https://codeberg.org/{{ site.codeberg_username }}/krunner-abbr">Codeberg</a> and <a href="https://github.com/{{ site.github_username }}/krunner-abbr">GitHub</a></p>
    <p><b>krunner-abbr</b> is a <a href="https://userbase.kde.org/Plasma/Krunner">KRunner</a> plugin for Plasma 6, written in Python, that expands abbreviations: type <code>abbr</code> and an abbreviation, press Enter, and the expansion is copied to the clipboard. Abbreviations live in a TOML file and can use placeholders for dates, the clipboard, typed text, input dialogs and shell commands, with chainable filters to clean up text (title case, unwrapping text copied from PDFs, quote conversion, sorting). It comes with examples for LaTeX and Markdown, Latin (Roman numerals, macrons), and fetching BibTeX from a DOI, plus a settings dialog with a live preview. It needs Python 3.14 or later.</p>
  </li>

  <li class="project">
    <h2><a href="https://github.com/{{ site.github_username }}/QuickView">QuickView: Quick Look-style file previews for KDE Plasma</a></h2>
    <p class="project-role">2026 · v1.0.4 · on <a href="https://codeberg.org/{{ site.codeberg_username }}/QuickView">Codeberg</a> and <a href="https://github.com/{{ site.github_username }}/QuickView">GitHub</a></p>
    <p><b>QuickView</b> is a reworked fork of <a href="https://github.com/MustaphaAlioglou/QuickView">Mustapha Alioglou's QuickView</a>, a macOS Quick Look-style previewer for KDE Plasma 6: select a file in Dolphin, press Space, and a floating preview panel appears; arrow keys walk the folder or page through a multi-file selection. It previews images, PDFs (with search and a contents sidebar), EPUB books laid out as pages, rendered Markdown, syntax-highlighted source code, HTML, audio and video, archive listings, spreadsheets as real grids, and office documents laid out as pages through LibreOffice. A resident daemon makes the panel appear in about 20 ms, and every parser runs in a bubblewrap sandbox with no network or filesystem access. The fork adds support for the Flathub LibreOffice, fixes a bug that could leave the panel hanging, splits the daemon into smaller modules and hardens the installer. It is written in Python with PySide6 and needs Python 3.15 or later and bubblewrap.</p>
  </li>

  <li class="project" id="py-slowdown">
    <h2><a href="https://github.com/{{ site.github_username }}/py-slowdown">py-slowdown: play audio slower or faster without changing its pitch</a></h2>
    <p class="project-role">2026 · v1.0 · on <a href="https://codeberg.org/{{ site.codeberg_username }}/py-slowdown">Codeberg</a> and <a href="https://github.com/{{ site.github_username }}/py-slowdown">GitHub</a></p>
    <p><b>py-slowdown</b> plays audio slower or faster without changing its pitch. It is meant for transcribing recordings (lectures, interviews, dictations) and for learning music by ear. It opens audio files and the sound of video files (MP3, M4A, FLAC, WAV, Ogg, Opus and whatever else FFmpeg reads) and shows them as a waveform with a time ruler, where a click moves the position and the wheel scrolls and zooms. The speed goes from 0.25× to 3× and can be changed while it plays; the stretching is done by the Rubber Band Library with its highest-quality engine, and at 1× the file is played sample for sample, as it is. Bookmarks, each with an optional label, are added at the playing position or anywhere on the waveform, listed in a side panel and exported as text; for each file it remembers its bookmarks and the point where it was left. Everything can be done from the keyboard, and the interface is in English and Spanish. It is written in Python with PySide6, PyAV, NumPy and sounddevice, and comes as an AppImage for Linux, a Fedora package on Copr, a Debian package, or from the source with Python 3.14 or later and the Rubber Band Library.</p>
  </li>

  <li class="project" id="py-schematron">
    <h2><a href="https://github.com/{{ site.github_username }}/py-schematron">py-schematron: Schematron validation for TEI-XML from the terminal</a></h2>
    <p class="project-role">2026 · v2.7 · on <a href="https://codeberg.org/{{ site.codeberg_username }}/py-schematron">Codeberg</a> and <a href="https://github.com/{{ site.github_username }}/py-schematron">GitHub</a></p>
    <p><b>py-schematron</b> is a Python script that checks TEI-XML documents against the Schematron rules embedded in an ODD (or in an already-extracted <code>.sch</code>, or harvested from an ODD-generated RelaxNG schema, the rules Jing ignores), running them with Saxon. Unlike oXygen, which silently stops after a hundred errors, it reports every violation, with counts per rule and, if asked, the line number and <code>xml:id</code> of each offender, and says exactly how many it left out when the listing is capped. It returns a non-zero exit code on violations, so it can run in a Makefile or a pre-commit hook. It needs Python 3.15 or later, <code>saxonche</code> and <code>lxml</code>.</p>
    <p class="continued">It also finds the schema on its own from the document's <code>&lt;?xml-model?&gt;</code> declarations, and a companion shell script, <code>py-schematron-all.sh</code>, adds the structural check against RelaxNG with jing and gives one verdict for both. Its JSON report drives the two editor plugins described below, each in a repository of its own: the <a href="#schematron-validator">Schematron Validator</a> extension for VS Code and [py-schematron.el](#py-schematron-el) for Emacs.</p>
  </li>

  <li class="project" id="schematron-validator">
    <h2><a href="https://marketplace.visualstudio.com/items?itemName=NicolasVaughan.validate-schematron">Schematron Validator: TEI-XML validation as you type in VS Code</a></h2>
    <p class="project-role">2026 · v0.12.0 · on the <a href="https://marketplace.visualstudio.com/items?itemName=NicolasVaughan.validate-schematron">Visual Studio Marketplace</a> · source on <a href="https://codeberg.org/{{ site.codeberg_username }}/py-schematron-vscode">Codeberg</a> and <a href="https://github.com/{{ site.github_username }}/py-schematron-vscode">GitHub</a></p>
    <p><b>Schematron Validator</b> is a VS Code extension that brings <a href="#py-schematron">py-schematron</a> into the editor. It checks XML and TEI files against Schematron rules (from a <code>.sch</code>, an ODD, or a RelaxNG schema with embedded rules) as you type, on open and on save, unsaved edits included. Each violation is underlined on the offending element and listed in the Problems panel, with its severity taken from the rule's <code>role</code>. If the schema is RelaxNG and <a href="https://relaxng.org/jclark/jing.html">jing</a> is installed, structural errors are added too, and badly formed XML is flagged where the broken tag was opened. The schema is found from the document's <code>&lt;?xml-model?&gt;</code> declaration or set in the settings; a status-bar indicator shows whether the file is clean, and commands let you pick the Python interpreter or re-download a schema that changed upstream. The script comes bundled; the extension needs Python 3.15 or later with <code>saxonche</code> and <code>lxml</code>, and its page walks you through installing them.</p>
    <p><a class="button button-primary" href="https://marketplace.visualstudio.com/items?itemName=NicolasVaughan.validate-schematron"><i class="fas fa-download" aria-hidden="true"></i> Install from the Marketplace</a></p>
  </li>

  <li class="project" id="py-schematron-el">
    <h2><a href="https://github.com/{{ site.github_username }}/py-schematron.el">py-schematron.el: TEI-XML validation as you type in Emacs, with Flycheck or Flymake</a></h2>
    <p class="project-role">2026 · v1.0.2 · on <a href="https://codeberg.org/{{ site.codeberg_username }}/py-schematron.el">Codeberg</a> and <a href="https://github.com/{{ site.github_username }}/py-schematron.el">GitHub</a></p>
    <p><b>py-schematron.el</b> is an Emacs package that brings <a href="#py-schematron">py-schematron</a> into the editor, with Flycheck when it is installed, or with Flymake, which comes with Emacs. It checks every buffer that has an <code>&lt;?xml-model?&gt;</code> declaration as you type, on opening and on saving; unsaved changes are checked from a private temporary copy, so the file itself is never written. Each problem is underlined, with its message when the cursor is on it and the layer that found it (Schematron, RelaxNG, or XML when the document is not well formed), and the mode line shows the counts; a report command gives the full text report of the file, each line linked to the document. When the schema is RelaxNG, it also checks the structure with <a href="https://relaxng.org/jclark/jing.html">jing</a> and hands the schema, converted with trang, to nxml-mode, so that completion offers the elements and attributes the schema allows where the cursor is. Since a schema's rules can read files and fetch URLs, it only checks documents listed in Emacs's <code>trusted-content</code>. It needs Emacs 31 or later and Python 3.15 or later with <code>saxonche</code> and <code>lxml</code>; jing and trang are optional.</p>
  </li>

  <li class="project" id="odd2rng">
    <h2><a href="https://github.com/{{ site.github_username }}/ODD2RNG">ODD2RNG: RELAX NG schemas from TEI ODDs, from the command line</a></h2>
    <p class="project-role">2026 · v1.3 · on <a href="https://codeberg.org/{{ site.codeberg_username }}/ODD2RNG">Codeberg</a> and <a href="https://github.com/{{ site.github_username }}/ODD2RNG">GitHub</a></p>
    <p><b>ODD2RNG</b> turns a TEI ODD into its RELAX NG schema without opening oXygen. It runs the same two transformations of the TEI Stylesheets, with the same parameters, as oXygen's <i>TEI ODD to RELAX NG XML</i> scenario, so the schema it writes is identical to oXygen's except for the generation date in its header comment (compared on the ODD of the SMTrad project). By default it writes <code>out/NAME.rng</code> next to the ODD, as oXygen does, and replaces the old schema only once the new one is complete, so an editor or a validator never reads it half-written; its last line says whether the schema is new, changed, or unchanged apart from the date, that is, whether there is anything worth committing. The TEI Stylesheets and the TEI source (<code>p5subset.xml</code>) can come from a clone of the TEI repository or from inside oXygen; their locations are kept in a configuration file, and an installer puts the command on the PATH. It needs Python 3.15 or later with <code>saxonche</code>.</p>
  </li>
</ul>

## Other software

<ol class="publications">
  {% for pub in site.data.software %}
    {% include publication.html pub=pub %}
  {% endfor %}
</ol>

## Tools I use

I use only [GNU/Linux](https://en.wikipedia.org/wiki/GNU/Linux_naming_controversy) on my machines.
Currently I am happily on the [Fedora Linux](https://fedoraproject.org/) distribution (version 45), with the [KDE Plasma](https://kde.org/plasma-desktop/) 6 desktop.
For many years I used the [Manjaro Linux](https://manjaro.org/) distribution, as well as (vanilla) [Arch Linux](https://archlinux.org/), but found them pretty unstable and hard to use on a daily basis.

My main editor, for writing and for coding, is [GNU Emacs](https://www.gnu.org/s/emacs/) (version 31), which I configure in Emacs Lisp. In it I keep my notes with [Org mode](https://orgmode.org/) and [Org-roam](https://www.orgroam.com/), write LaTeX with [AUCTeX](https://www.gnu.org/software/auctex/) and RefTeX, work with Git through [Magit](https://magit.vc/), and edit TEI with nxml-mode and my own [py-schematron.el](#py-schematron-el).
For TEI projects, ODD customisations and XSLT I also use [Oxygen XML Editor](https://www.oxygenxml.com/).
For quick edits I use Vim or Sublime Text, and [Visual Studio Code](https://code.visualstudio.com/) mostly to try my [Schematron Validator](#schematron-validator) extension.

In the terminal I use [Ghostty](https://ghostty.org/) with the [fish](https://fishshell.com/) shell and tmux, and a few command-line tools: ripgrep and fd to search, fzf, bat, eza, zoxide, atuin for the shell history, and delta to read diffs.

For Python I use [uv](https://docs.astral.sh/uv/), which takes care of the Python versions, the environments and the dependencies; for the tests, pytest.
I package my programs as RPMs for Fedora, built with rpmbuild and published on [Copr](https://copr.fedorainfracloud.org/), and as AppImages for other distributions.
The code is on [Codeberg](https://codeberg.org/{{ site.codeberg_username }}) and [GitHub](https://github.com/{{ site.github_username }}), which I use from the terminal with tea and gh.
I use [Claude Code](https://claude.com/product/claude-code) for testing and publishing code.

Outside the editor, I run XSLT transformations and XPath queries with [Saxon](https://www.saxonica.com/), and validate and convert RELAX NG schemas with [Jing](https://relaxng.org/jclark/jing.html) and [Trang](https://relaxng.org/jclark/trang.html).
I typeset with LuaLaTeX from [TeX Live](https://tug.org/texlive/), with Biber for the bibliographies, which I keep in [Zotero](https://www.zotero.org/) with the Better BibTeX extension; [Pandoc](https://pandoc.org/) takes care of the other conversions between formats.

I built this website with the static site generator [Jekyll](https://jekyllrb.com); the design started from a theme by [S.V. Miller](https://svmiller.com/).
Its source code is available [on GitHub](https://github.com/{{ site.github_username }}/nivaca.github.io).
