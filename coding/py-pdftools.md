---
layout: page
ref: py-pdftools
title: py-pdftools
subtitle: Annotate, redact, label, impose and OCR PDF documents in one program
permalink: /coding/py-pdftools/
description: py-pdftools, a program by Nicolás Vaughan to annotate, redact, label, impose and OCR PDF documents, with its modes, its command line, how to install it, and its versions.
---

py-pdftools edits PDF documents. It annotates and redacts them, changes their page labels, headers, footers, watermarks and the order of their pages, imposes them for printing, and reads the text of their scanned pages. It has a window and a command line, both in English and in Spanish, and runs on Linux, Windows and macOS.

<div class="buttons">
  <a class="button button-primary" href="https://codeberg.org/{{ site.codeberg_username }}/py-pdftools/releases"><i class="fas fa-download" aria-hidden="true"></i> Downloads</a>
  <a class="button" href="https://github.com/{{ site.github_username }}/py-pdftools/blob/main/docs/MANUAL_en.pdf"><i class="fas fa-file-pdf" aria-hidden="true"></i> Manual</a>
</div>

<dl class="facts">
  <dt>Version</dt><dd>1.19.0 (25 November 2026)</dd>
  <dt>Programs</dt><dd>a window (<code>py-pdftools-gui</code>) and a command line (<code>py-pdftools</code>)</dd>
  <dt>Interface</dt><dd>English and Spanish</dd>
  <dt>Written in</dt><dd>Python, with PyMuPDF, pikepdf, reportlab and PySide6 (Qt)</dd>
  <dt>Needs</dt><dd>Python 3.14 or later (the AppImage, the installers for Windows and macOS and the packages bring what they need); Ghostscript for PDF/A and PDF/X, tesseract for OCR, pyHanko for digital signatures</dd>
  <dt>Licence</dt><dd>GNU General Public License, version 3 or later</dd>
  <dt>Code</dt><dd><a href="https://codeberg.org/{{ site.codeberg_username }}/py-pdftools">Codeberg</a> and <a href="https://github.com/{{ site.github_username }}/py-pdftools">GitHub</a></dd>
</dl>

## Where it comes from

py-pdftools grew out of six programs I wrote earlier, each for one kind of work on PDF documents. They had grown side by side, and they shared much: the translation of the interface, the configuration, the conversion to PDF/A and PDF/X, the packaging. The same document, besides, often went through several of them: annotated, then redacted, then given its page labels, then imposed for printing. So I brought them together in November 2026. Their code was copied into py-pdftools, which does not need them installed; each one stays as it was, with its own repository.

| Program | What it became in py-pdftools |
|---|---|
| [py-annotate](https://github.com/{{ site.github_username }}/py-annotate) | the mode Annotate, and the window itself: its pages, thumbnails and panels |
| [py-redact](https://github.com/{{ site.github_username }}/py-redact) | the mode Redact |
| [py-foliation](https://github.com/{{ site.github_username }}/py-foliation) | the mode Foliate, and the commands `labels`, `view`, `header-footer`, `watermark` and `pages` |
| [py-imposition](https://github.com/{{ site.github_username }}/py-imposition) | the mode Impose, and the commands under `impose` |
| [py-pdfocr](https://github.com/{{ site.github_username }}/py-pdfocr) | the mode OCR, and the command `ocr` |
| [pdf-word-finder](https://github.com/{{ site.github_username }}/pdf-word-finder) | Tools > Word index, and the command `find-words` |

A seventh, [pdf2iso](https://github.com/{{ site.github_username }}/pdf2iso), came in whole: it makes the copies as PDF/A and PDF/X, and is no longer installed apart. Documents made with the earlier programs are read as before.

## The modes

A bar at the top of the window (or Ctrl+1 to Ctrl+6) chooses what the window does. Each mode keeps its own arrangement of toolbars and panels, also the next time the program is opened, and there is one history for all of them: Undo goes back through everything done to the document, in any mode.

- **Read**: the pages and their thumbnails, with the tools to find, move through the pages and zoom.
- **OCR**: tesseract reads the text of the scanned pages, and it is written into the document, invisible, under the pictures of the pages, so that it can be found, copied and marked. The words tesseract was not sure of are shown beside their pictures, to be corrected first. Pages scanned sideways or upside down can be turned, and tesseract's more accurate language models are downloaded from the program.
- **Redact**: boxes over what is to be removed, drawn by hand, put over text, or found by a search, with redaction codes. They are saved as the PDF's own redaction marks, and nothing is removed until the redacted copy is written: a new file, never the one open, which is checked for any text still readable under a box. Find covered text looks for text that only seems redacted, still in the file under a black box or a picture.
- **Annotate**: highlights, notes, text boxes, shapes, drawings, links and stamps (the standard ones, and stamps of one's own made of a picture or a page), written as ordinary PDF annotations, with a panel that lists, searches, filters and sorts them.
- **Foliate**: page labels (roman numbers, folios, prefixes), headers and footers with Bates numbers, watermarks, the view when the document is opened, and the order of the pages, all shown as soon as they are made.
- **Impose**: booklets, n-up, step and repeat, bleeds and crop marks, sequences and hot folders, previewed before they are saved or applied.

<figure class="screenshot">
  <img src="{{ "/images/py-pdftools/annotate_en.webp" | relative_url }}" alt="py-pdftools in the mode Annotate" loading="lazy">
  <figcaption>The mode Annotate.</figcaption>
</figure>

<figure class="screenshot">
  <img src="{{ "/images/py-pdftools/redact_en.webp" | relative_url }}" alt="py-pdftools in the mode Redact, with a box over a line" loading="lazy">
  <figcaption>The mode Redact: a box over a line, which goes on every page from the second.</figcaption>
</figure>

<figure class="screenshot">
  <img src="{{ "/images/py-pdftools/pages_en.webp" | relative_url }}" alt="py-pdftools in the mode Foliate, with the ranges of page labels" loading="lazy">
  <figcaption>The mode Foliate: no label on the title page, then 1, 2, 3, and the label in the footer.</figcaption>
</figure>

<figure class="screenshot">
  <img src="{{ "/images/py-pdftools/impose_en.webp" | relative_url }}" alt="py-pdftools in the mode Impose, making a booklet" loading="lazy">
  <figcaption>The mode Impose: a booklet.</figcaption>
</figure>

## Beyond the six programs

py-pdftools also does much that none of the earlier programs did:

- fills forms, with their numbers and dates checked and their sums worked out without JavaScript, and exports and imports their values (JSON, CSV, XFDF, FDF);
- signs documents with a digital ID, visibly or not, and checks their signatures: whether each is intact and valid, who signed, and what changed after it;
- protects documents with passwords, encrypted with AES-256;
- edits bookmarks and links, and lists, opens and adds attached files;
- combines files, or some of their pages, makes PDFs of pictures, splits documents (every so many pages, at their bookmarks, or by size), and puts pages in order in a grid of large thumbnails;
- exports pages as pictures, the pictures of the document, or its text (Markdown, HTML or plain text), and makes smaller copies, or copies as another PDF version;
- compares two PDFs page by page, and runs the same steps (OCR, a header, a watermark, a smaller size, PDF/A) on many files at once;
- finds the pages where each word of a list appears, by their labels, as lines ready for the index of a book.

The window opens documents in tabs, can show two side by side, and has a quick search that finds at every letter typed. It can keep running in the background, with an icon in the tray, so that documents open at once.

## The command line

The commands come in groups, and `py-pdftools COMMAND -h` explains each one:

<pre><code>py-pdftools labels set book.pdf 1:r 9:D -i      # i, ii ... from page 1; 1, 2 ... from page 9
py-pdftools header-footer book.pdf --footer-center 'Page $pagelabel' -i
py-pdftools watermark book.pdf --text DRAFT --opacity 30% -i
py-pdftools pages book.pdf --move 201-214 9 --delete LAST -i
py-pdftools impose booklet book.pdf -o booklet.pdf
py-pdftools ocr scan.pdf -l lat+spa --rotate --report
py-pdftools find-words book.pdf amor "re:virtu(s|tem|tis)" --sort
py-pdftools combine a.pdf b.pdf:2-5 -o all.pdf
py-pdftools export text book.pdf
</code></pre>

`py-pdftools pdf2iso` is pdf2iso's own command line, and `py-pdftools completion bash|fish|zsh` prints a completion script for the shell.

## Installing it

Every release is on [Codeberg](https://codeberg.org/{{ site.codeberg_username }}/py-pdftools/releases) and [GitHub](https://github.com/{{ site.github_username }}/py-pdftools/releases). Every file and every tag is signed with the same key, and each release has the checksums of its files.

| System | How |
|---|---|
| Windows 10 or later | an installer (`.exe`), for one user or for everyone |
| macOS 15 or later, Apple silicon | a disk image (`.dmg`) |
| Fedora 45 and later | `sudo dnf copr enable nivaca/py-pdftools`, then `sudo dnf install py-pdftools` |
| Debian 12, Ubuntu 22.04 and later | the `.deb` of a release, or my signed APT repository, [github.com/nivaca/apt](https://github.com/{{ site.github_username }}/apt) |
| Any Linux | the AppImage, which brings its own Python, Qt and libraries |
| Linux, macOS, Windows | the install scripts in the source (`install/install.sh`, `install\install.bat`), with Python 3.14 or later |
| From the source | `uv run py-pdftools-gui`, with [uv](https://docs.astral.sh/uv/) |

## Documentation

- The user manual, in PDF, with pictures of the window and its dialogs: [English](https://github.com/{{ site.github_username }}/py-pdftools/blob/main/docs/MANUAL_en.pdf), [Spanish](https://github.com/{{ site.github_username }}/py-pdftools/blob/main/docs/MANUAL_es.pdf).
- The README: [English](https://github.com/{{ site.github_username }}/py-pdftools/blob/main/README.md), [Spanish](https://github.com/{{ site.github_username }}/py-pdftools/blob/main/README_es.md).
- [How py-pdftools was made](https://github.com/{{ site.github_username }}/py-pdftools/blob/main/docs/DESCRIPTION.md), and the [changelog](https://github.com/{{ site.github_username }}/py-pdftools/blob/main/CHANGELOG.md).

## Versions

py-pdftools is young: its first version came out on 19 November 2026. The main steps since then; the [changelog](https://github.com/{{ site.github_username }}/py-pdftools/blob/main/CHANGELOG.md) has every version.

<ul class="history">
  <li><span class="when">0.1.0<br>19 Nov.</span><span>py-annotate, py-redact, py-foliation and py-imposition in one window and one command line, in English and Spanish.</span></li>
  <li><span class="when">0.2.0</span><span>Five modes, in the order of the work on a document (Read, Redact, Annotate, Foliate, Impose), each with its own arrangement of the window; pdf2iso brought in.</span></li>
  <li><span class="when">0.4.0–1.0.0<br>20 Nov.</span><span>OCR, from py-pdfocr, and then the mode OCR; text selection; running in the background.</span></li>
  <li><span class="when">1.1.0–1.4.0<br>20 Nov.</span><span>Bookmarks, links, tabs and a split view; finding covered text; passwords; combining files and PDFs of pictures; smaller copies, forms and digital signatures.</span></li>
  <li><span class="when">1.5.0–1.7.0<br>21 Nov.</span><span>The menus in groups; a quicker start, with the program started with the session; page navigation and the properties of a document.</span></li>
  <li><span class="when">1.8.0</span><span>The word index, from pdf-word-finder: the sixth program.</span></li>
  <li><span class="when">1.10.0–1.12.0<br>23 Nov.</span><span>Attached files; a menu Tools, with the page sorter, steps run on several files and the history of changes; stamps of one's own; the search as you type.</span></li>
  <li><span class="when">1.13.0</span><span>A menu Find, with every search, in every mode.</span></li>
  <li><span class="when">1.14.0<br>24 Nov.</span><span>Signing digitally, in three plain steps, with a digital ID made in the dialog if there is none.</span></li>
  <li><span class="when">1.15.0<br>24 Nov.</span><span>Every search as quick as the search as you type: each page read once, into one index of the document.</span></li>
  <li><span class="when">1.16.0<br>25 Nov.</span><span>Installers for Windows and macOS that need nothing else; the menu Annotate in submenus; a sign for comments; annotations readable on large scanned pages.</span></li>
  <li><span class="when">1.17.0–1.19.0<br>25 Nov.</span><span>Copies with the pages as pictures; Close document (Ctrl+W) closes the document, not the program; smaller copies that keep every colour; reading aloud with the system's voice; four more colour themes and a choice of icons.</span></li>
</ul>
