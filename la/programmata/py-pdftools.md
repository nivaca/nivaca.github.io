---
layout: page
ref: py-pdftools
title: py-pdftools
subtitle: Documenta PDF uno programmate annotare, expungere, foliare, imponere et per OCR legere
permalink: /la/programmata/py-pdftools/
description: py-pdftools, programma a Nicolao Vaughan scriptum ad documenta PDF annotanda, expungenda, folianda, imponenda et per OCR legenda; modi eius, linea mandatorum, quomodo instituatur, et editiones eius.
---

py-pdftools documenta PDF tractat. Ea annotat et expungit, titulos paginarum, capita et calces, signa aquatica et ordinem paginarum mutat, ad impressionem imponit, et textum paginarum in imagines translatarum legit. Fenestram et lineam mandatorum habet, que ambe Anglice et Hispanice loquuntur, et in Linux, Windows et macOS currit.

<div class="buttons">
  <a class="button button-primary" href="https://codeberg.org/{{ site.codeberg_username }}/py-pdftools/releases"><i class="fas fa-download" aria-hidden="true"></i> Fasciculi</a>
  <a class="button" href="https://github.com/{{ site.github_username }}/py-pdftools/blob/main/docs/MANUAL_en.pdf"><i class="fas fa-file-pdf" aria-hidden="true"></i> Manuale</a>
</div>

<dl class="facts">
  <dt>Editio</dt><dd>1.23.0 (die XXVII mensis Novembris anni MMXXVI)</dd>
  <dt>Programmata</dt><dd>fenestra (<code>py-pdftools-gui</code>) et linea mandatorum (<code>py-pdftools</code>)</dd>
  <dt>Interfacies</dt><dd>Anglica et Hispanica</dd>
  <dt>Scriptum</dt><dd>lingua Python, cum PyMuPDF, pikepdf, reportlab et PySide6 (Qt)</dd>
  <dt>Requirit</dt><dd>Python 3.14 aut recentiorem (AppImage, institutores pro Windows et macOS et fasciculi secum ferunt quod eis opus est); Ghostscript ad PDF/A et PDF/X, tesseract ad OCR, pyHanko ad subscriptiones digitales</dd>
  <dt>Licentia</dt><dd>GNU General Public License, versio 3 aut posterior</dd>
  <dt>Fontes</dt><dd>in <a href="https://codeberg.org/{{ site.codeberg_username }}/py-pdftools">Codeberg</a> et <a href="https://github.com/{{ site.github_username }}/py-pdftools">GitHub</a></dd>
</dl>

## Unde ortum sit

py-pdftools ex sex programmatibus crevit que antea scripseram, singulis ad unum genus laboris in documentis PDF destinatis. Iuxta se invicem creverant, et multa communia habebant: translationem interfaciei, configurationem, conversionem in PDF/A et PDF/X, confectionem fasciculorum. Idem preterea documentum sepe per plura eorum transibat: annotabatur, deinde expungebatur, deinde titulis paginarum instruebatur, deinde ad impressionem imponebatur. Itaque ea mense Novembri anni MMXXVI in unum coegi. Codex eorum in py-pdftools exscriptus est, quod ideo ea instituta non requirit; singula autem ut erant manent, quodque cum repositorio suo.

| Programma | Quid in py-pdftools factum sit |
|---|---|
| [py-annotate](https://github.com/{{ site.github_username }}/py-annotate) | modus Annotare (Annotate), et ipsa fenestra: pagine, imaguncule et tabule laterales eius |
| [py-redact](https://github.com/{{ site.github_username }}/py-redact) | modus Expungere (Redact) |
| [py-foliation](https://github.com/{{ site.github_username }}/py-foliation) | modus Foliare (Foliate), et mandata `labels`, `view`, `header-footer`, `watermark` et `pages` |
| [py-imposition](https://github.com/{{ site.github_username }}/py-imposition) | modus Imponere (Impose), et mandata sub `impose` |
| [py-pdfocr](https://github.com/{{ site.github_username }}/py-pdfocr) | modus OCR, et mandatum `ocr` |
| [pdf-word-finder](https://github.com/{{ site.github_username }}/pdf-word-finder) | Instrumenta > Index vocum (Tools > Word index), et mandatum `find-words` |

Septimum, [pdf2iso](https://github.com/{{ site.github_username }}/pdf2iso), totum receptum est: exemplaria PDF/A et PDF/X facit, nec iam seorsum instituitur. Documenta per priora programmata facta ut antea leguntur.

## Modi

Series bullarum in summa fenestra (vel Ctrl+1 usque ad Ctrl+6) eligit quid fenestra faciat. Quisque modus suam tabularum instrumentorum et tabularum lateralium dispositionem servat, etiam cum programma iterum aperitur, et una est historia omnium: mandatum Revocare (Undo) omnia que in documento facta sunt, in quolibet modo, retro percurrit.

- **Legere** (Read): pagine et imaguncule earum, cum instrumentis ad querendum, ad paginas percurrendas et ad amplificandum.
- **OCR**: tesseract textum paginarum in imagines translatarum legit, qui in documento scribitur, invisibilis, sub imaginibus paginarum, ut inveniri, exscribi et notari possit. Voces de quibus tesseract dubitavit iuxta imagines suas ostenduntur, ut prius corrigantur. Pagine transverse aut inverse translate erigi possunt, et notitie linguarum accuratiores quibus tesseract utitur per ipsum programma e rete trahuntur.
- **Expungere**: quadra super ea que tollenda sunt, vel manu ducta, vel super textum posita, vel per inquisitionem inventa, cum notis expunctionis. Ut signa expunctionis ipsius PDF servantur, et nichil tollitur donec exemplar expunctum scribatur: documentum novum, numquam id quod apertum est, in quo probatur num sub aliquo quadro textus adhuc legi possit. Mandatum Quere textum tectum (Find covered text) textum querit qui solum expunctus videtur, sed in fasciculo sub quadro nigro vel imagine adhuc latet.
- **Annotare**: illuminationes, note, quadra textus, figure, delineationes, nexus et sigilla (sive usitata, sive propria ex imagine vel pagina facta), ut annotationes PDF usitate scripta, cum tabula laterali que eas enumerat, querit, cribrat et ordinat.
- **Foliare**: tituli paginarum (numeri Romani, numeri foliorum, prefixa), capita et calces cum numeris Bates, signa aquatica, aspectus documenti cum aperitur, et ordo paginarum, que omnia statim ac fiunt ostenduntur.
- **Imponere**: libelli, plures pagine in una facie, dispositiones repetite, margines excedentes et note sectionis, series et directoria vigilata, que omnia, antequam serventur vel adhibeantur, inspici possunt.

<figure class="screenshot">
  <img src="{{ "/images/py-pdftools/annotate_en.webp" | relative_url }}" alt="py-pdftools in modo Annotare" loading="lazy">
  <figcaption>Modus Annotare.</figcaption>
</figure>

<figure class="screenshot">
  <img src="{{ "/images/py-pdftools/redact_en.webp" | relative_url }}" alt="py-pdftools in modo Expungere, cum quadro super lineam" loading="lazy">
  <figcaption>Modus Expungere: quadrum super lineam, quod in omnibus paginis a secunda deinceps ponitur.</figcaption>
</figure>

<figure class="screenshot">
  <img src="{{ "/images/py-pdftools/pages_en.webp" | relative_url }}" alt="py-pdftools in modo Foliare, cum intervallis titulorum paginarum" loading="lazy">
  <figcaption>Modus Foliare: nullus titulus in frontispicio, deinde 1, 2, 3, et titulus in calce pagine.</figcaption>
</figure>

<figure class="screenshot">
  <img src="{{ "/images/py-pdftools/impose_en.webp" | relative_url }}" alt="py-pdftools in modo Imponere, libellum conficiens" loading="lazy">
  <figcaption>Modus Imponere: libellus.</figcaption>
</figure>

## Ultra sex programmata

py-pdftools multa quoque facit que nullum ex prioribus programmatibus faciebat:

- formulas implet, numeris et diebus earum probatis et summis sine JavaScript computatis, et valores earum exportat et importat (JSON, CSV, XFDF, FDF);
- documenta subscriptione digitali obsignat, per testimonium digitale, sive visibiliter sive non, et subscriptiones eorum probat: num queque integra et valida sit, quis subscripserit, et quid post eam mutatum sit;
- documenta verbis arcanis munit, cifris AES-256 clausa;
- signacula et nexus tractat, et fasciculos adiunctos enumerat, aperit et addit;
- fasciculos, vel quasdam eorum paginas, in unum coniungit, documenta PDF ex imaginibus conficit, documenta dividit (post certum numerum paginarum, ad eorum signacula, vel secundum magnitudinem), et paginas in reticulo magnarum imaguncularum ordinat;
- paginas ut imagines, imagines documenti, vel textum eius (Markdown, HTML vel textum simplicem) exportat, et exemplaria minora facit, vel exemplaria in alia versione PDF;
- duo documenta PDF paginatim comparat, et eosdem gradus (OCR, caput pagine, signum aquaticum, magnitudinem minorem, PDF/A) in multis fasciculis simul exsequitur;
- paginas, titulis suis designatas, invenit in quibus singule voces alicuius indicis apparent, easque in lineis ad indicem libri paratis reddit.

Fenestra documenta in schedulis aperit, duo iuxta se ostendere potest, et inquisitionem celerem habet que ad quamque litteram scriptam invenit. In occulto currens manere potest, cum icone in area systematis, ut documenta statim aperiantur.

## Linea mandatorum

Mandata in genera distribuuntur, et `py-pdftools COMMAND -h` quodque explicat:

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

`py-pdftools pdf2iso` est ipsa linea mandatorum programmatis pdf2iso, et `py-pdftools completion bash|fish|zsh` scriptum completionis pro testa (shell) imprimit.

## Quomodo instituatur

Omnes editiones in [Codeberg](https://codeberg.org/{{ site.codeberg_username }}/py-pdftools/releases) et [GitHub](https://github.com/{{ site.github_username }}/py-pdftools/releases) inveniuntur. Omnis fasciculus et omnis nota (tag) eadem clave obsignantur, et quelibet editio summas probatorias fasciculorum suorum habet.

| Systema | Quomodo |
|---|---|
| Windows 10 vel posterius | institutor (`.exe`), pro uno usuario vel pro omnibus |
| macOS 15 vel posterius, Apple silicon | imago disci (`.dmg`) |
| Fedora 45 et posteriores | `sudo dnf copr enable nivaca/py-pdftools`, deinde `sudo dnf install py-pdftools` |
| Debian 12, Ubuntu 22.04 et posteriores | fasciculus `.deb` alicuius editionis, vel meum repositorium APT obsignatum, [github.com/nivaca/apt](https://github.com/{{ site.github_username }}/apt) |
| Quodlibet systema Linux | AppImage, quod proprium Python, Qt et bibliothecas secum fert |
| Linux, macOS, Windows | scripta instituendi in fontibus (`install/install.sh`, `install\install.bat`), cum Python 3.14 aut recentiore |
| Ex fontibus | `uv run py-pdftools-gui`, cum [uv](https://docs.astral.sh/uv/) |

## De programmate scripta

- Manuale usuarii, in forma PDF, cum imaginibus fenestre et dialogorum eius: [Anglice](https://github.com/{{ site.github_username }}/py-pdftools/blob/main/docs/MANUAL_en.pdf), [Hispanice](https://github.com/{{ site.github_username }}/py-pdftools/blob/main/docs/MANUAL_es.pdf).
- README: [Anglice](https://github.com/{{ site.github_username }}/py-pdftools/blob/main/README.md), [Hispanice](https://github.com/{{ site.github_username }}/py-pdftools/blob/main/README_es.md).
- [Quomodo py-pdftools factum sit](https://github.com/{{ site.github_username }}/py-pdftools/blob/main/docs/DESCRIPTION.md) (Anglice), et [index mutationum](https://github.com/{{ site.github_username }}/py-pdftools/blob/main/CHANGELOG.md).

## Editiones

py-pdftools recens est: prima eius editio die XIX mensis Novembris anni MMXXVI prodiit. Hic precipui gradus ex eo tempore; [index mutationum](https://github.com/{{ site.github_username }}/py-pdftools/blob/main/CHANGELOG.md) omnes editiones habet.

<ul class="history">
  <li><span class="when">0.1.0<br>XIX Nov.</span><span>py-annotate, py-redact, py-foliation et py-imposition in una fenestra et una linea mandatorum, Anglice et Hispanice.</span></li>
  <li><span class="when">0.2.0</span><span>Quinque modi, ordine laboris in documento (Legere, Expungere, Annotare, Foliare, Imponere), quisque cum sua fenestre dispositione; pdf2iso receptum.</span></li>
  <li><span class="when">0.4.0–1.0.0<br>XX Nov.</span><span>OCR, ex py-pdfocr, et deinde modus OCR; electio textus; cursus in occulto.</span></li>
  <li><span class="when">1.1.0–1.4.0<br>XX Nov.</span><span>Signacula, nexus, schedule et aspectus divisus; inquisitio textus tecti; verba arcana; fasciculorum coniunctio et documenta PDF ex imaginibus; exemplaria minora, formule et subscriptiones digitales.</span></li>
  <li><span class="when">1.5.0–1.7.0<br>XXI Nov.</span><span>Tabelle in genera distribute; initium celerius, programmate cum sessione incepto; navigatio per paginas et proprietates documenti.</span></li>
  <li><span class="when">1.8.0</span><span>Index vocum, ex pdf-word-finder: sextum programma.</span></li>
  <li><span class="when">1.10.0–1.12.0<br>XXIII Nov.</span><span>Fasciculi adiuncti; tabella Instrumenta, cum ordinatore paginarum, gradibus in pluribus fasciculis exsecutis et historia mutationum; sigilla propria; inquisitio dum scribitur.</span></li>
  <li><span class="when">1.13.0</span><span>Tabella Quere (Find), cum omni inquisitione, in omni modo.</span></li>
  <li><span class="when">1.14.0<br>XXIV Nov.</span><span>Documenta subscriptione digitali obsignata, tribus gradibus simplicibus, cum testimonio digitali in dialogo facto si nullum adest.</span></li>
  <li><span class="when">1.15.0<br>XXIV Nov.</span><span>Omnis inquisitio tam celeris quam inquisitio dum scribitur: quaque pagina semel lecta, in unum indicem documenti.</span></li>
  <li><span class="when">1.16.0<br>XXV Nov.</span><span>Institutores pro Windows et macOS quibus nichil aliud opus est; tabella Annotare (Annotate) in tabellas minores divisa; signum commentariorum; annotationes legibiles in paginis magnis in imagines translatis.</span></li>
  <li><span class="when">1.17.0–1.19.0<br>XXV Nov.</span><span>Exemplaria cum paginis in imagines translatis; Ctrl+W documentum claudit, non programma; exemplaria minora que omnes colores servant; textus voce systematis recitatus; quattuor nove colorum species (themes) et icones eligende.</span></li>
</ul>
