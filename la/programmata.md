---
layout: page
ref: coding
title: Programmata
permalink: /la/programmata/
description: Programmata, scripta et instrumenta programmandi Nicolai Vaughan.
---

Programmata scribo maxime lingua [Python](https://www.python.org/): instrumenta ex linea mandatorum, programmata in fenestra cum PySide6 (Qt) et additamenta pro KDE Plasma. Scripta Bash compilationes et minora negotia curant. Magna pars laboris mei circa textus in XML versatur: eos secundum normas [TEI](https://tei-c.org/) noto, accommodationes ODD cum schematibus RelaxNG et regulis Schematron scribo, documenta per XPath interrogo et per XSLT transformo, plerumque in [LaTeX](https://www.latex-project.org/), quem cum LuaLaTeX compono. In [Emacs](https://www.gnu.org/software/emacs/) laboro, et ad eius usum lingua Emacs Lisp (Elisp) scribo: ordinationem meam propriam et fasciculos ut [py-schematron.el](#py-schematron-el). Aliquid etiam lingua TypeScript scripsi, pro extensione VS Code. Fontes programmatum meorum in [GitHub](https://github.com/{{ site.github_username }}) et in [Codeberg](https://codeberg.org/{{ site.codeberg_username }}) reperiuntur.

<ul class="projects">
  <li class="project project-featured" id="py-words">
    <p class="feature-label">Opus precipuum</p>
    <h2><a href="https://codeberg.org/{{ site.codeberg_username }}/py-words">py-words: lexicon Latinum cum morphologia</a></h2>
    <p class="project-role">2026 · v3.31 · in <a href="https://codeberg.org/{{ site.codeberg_username }}/py-words">Codeberg</a> et <a href="https://github.com/{{ site.github_username }}/py-words">GitHub</a></p>
    <a class="project-shot" href="{{ "/la/programmata/py-words/" | relative_url }}"><img src="{{ "/images/py-words/gui_la.webp" | relative_url }}" alt="Fenestra py-words in modo obscuro, articulos vocis perspicio ostendens" loading="lazy"></a>
    <p><b>py-words</b> lexicon est Latino-Anglicum et Latino-Hispanicum, in utramque partem, lingua Python scriptum. Ex programmate WORDS Guillelmi Whitaker ortum est, sed et codex et data de novo ordinata sunt, et nunc lexicon Anglicum Lewis et Short continet et Hispanica Echave-Sustaeta et De Miguel. Voces Latinas declinatas vel coniugatas, et integros versus, in formas suas et lemmata resolvit, cum significationibus Anglice vel Hispanice redditis, et voces Latinas pro Anglicis aut Hispanicis invenit. In fenestra, in linea mandatorum, in terminali vel in navigatro operatur, et nichil aliud quam Python 3.13 aut recentiorem requirit. Operatur etiam in KRunner, instrumento KDE Plasma ad programmata incipienda, et ut applicatio Android, que totum lexicon secum fert nec rete requirit.</p>
    <p><a class="button button-primary" href="{{ "/py-words/" | relative_url }}"><i class="fas fa-book-open" aria-hidden="true"></i> In navigatro tuo experire</a>
      <a class="button" href="https://nivaca.pythonanywhere.com/"><i class="fas fa-server" aria-hidden="true"></i> Speculum</a>
      <a class="button" href="{{ "/la/programmata/py-words/" | relative_url }}"><i class="fas fa-info-circle" aria-hidden="true"></i> Plura de eo</a></p>
  </li>

  <li class="project project-featured" id="py-pdftools">
    <p class="feature-label">Opus precipuum</p>
    <h2><a href="https://github.com/{{ site.github_username }}/py-pdftools">py-pdftools: documenta PDF uno programmate annotare, expungere, foliare, imponere et per OCR legere</a></h2>
    <p class="project-role">2026 · v1.16.0 · in <a href="https://codeberg.org/{{ site.codeberg_username }}/py-pdftools">Codeberg</a> et <a href="https://github.com/{{ site.github_username }}/py-pdftools">GitHub</a></p>
    <a class="project-shot" href="{{ "/la/programmata/py-pdftools/" | relative_url }}"><img src="{{ "/images/py-pdftools/annotate_en.webp" | relative_url }}" alt="py-pdftools in modo Annotare" loading="lazy"></a>
    <p><b>py-pdftools</b> documenta PDF tractat: ea annotat et expungit, titulos, capita et calces paginarum, signa aquatica et ordinem earum mutat, ad impressionem imponit, et textum paginarum in imagines translatarum per tesseract legit. Septem programmata que ante ipsum scripsi (py-annotate, py-redact, py-foliation, py-imposition, py-pdfocr, pdf-word-finder et pdf2iso) in una fenestra et una linea mandatorum coniungit, et eis addit formulas, subscriptiones digitales, verba arcana, signacula, et documenta coniungere, dividere et exportare. Anglice et Hispanice loquitur, et lingua Python cum PyMuPDF, pikepdf, reportlab et PySide6 scriptum est; vel ut AppImage pro Linux, vel ut fasciculus Fedore aut Debian, vel per programmata instituendi pro Linux, macOS et Windows, vel ex fontibus cum Python 3.14 aut recentiore instituitur.</p>
    <p><a class="button button-primary" href="{{ "/la/programmata/py-pdftools/" | relative_url }}"><i class="fas fa-info-circle" aria-hidden="true"></i> Plura de eo</a></p>
  </li>

  <li class="project">
    <h2><a href="https://github.com/{{ site.github_username }}/py-wk">py-wk: Victionarium ex terminali vel ex mensa</a></h2>
    <p class="project-role">2026 · v1.18 · in <a href="https://codeberg.org/{{ site.codeberg_username }}/py-wk">Codeberg</a> et <a href="https://github.com/{{ site.github_username }}/py-wk">GitHub</a></p>
    <p><b>py-wk</b> interfacies est lingua Python scripta ad voces in <a href="https://en.wiktionary.org">Victionario Anglico</a> inquirendas sine navigatro. Tribus modis prebetur, ut instrumentum linee mandatorum, ut interfacies terminalis totum quadrum occupans et ut fenestra mense, que omnia eundem codicem habent. Articulum integrum ostendit, non tantum definitiones: etymologiam, pronuntiationem, exempla et citationes, notas de usu, tabulas flexionum, synonyma, vocabula derivata et cognata, descendentia et translationes, omnium linguarum pagine vel earum tantum quas elegeris (solius Latine, verbi gratia, vel Latine et Hispanice). Titulos quoque paginarum inquirit et JSON ordinatum aliis programmatibus reddit. Nichil aliud quam Python 3.15 aut recentiorem cum bibliotheca eius ordinaria requirit (et Tkinter pro fenestra), et prebetur etiam AppImage per se constans pro Linux.</p>
  </li>

  <li class="project">
    <h2><a href="https://github.com/{{ site.github_username }}/krunner-py-wk">krunner-py-wk: Victionarium in KRunner</a></h2>
    <p class="project-role">2026 · v1.1 · in <a href="https://codeberg.org/{{ site.codeberg_username }}/krunner-py-wk">Codeberg</a> et <a href="https://github.com/{{ site.github_username }}/krunner-py-wk">GitHub</a></p>
    <p><b>krunner-py-wk</b> <a href="https://github.com/{{ site.github_username }}/py-wk">py-wk</a> in <a href="https://userbase.kde.org/Plasma/Krunner">KRunner</a>, in KDE Plasma 6, transfert: scribe <code>wk</code> et vocem, et articuli eius ex Victionario apparent, singuli pro singulis partibus orationis in singulis linguis, cum linea lemmatis et primis definitionibus. Lingue in ipsa inquisitione eliguntur (<code>wk rosa @la</code> pro sola Latina), locutiones plurium vocum admittuntur, et vox sine pagina titulos similes suggerit. Clavis Enter articulum in fenestra py-wk aperit; alie actiones articulum integrum exscribunt aut in Victionario aperiunt. Inquisitiones expectant donec scribere cesses et in filo separato currunt, ita ut KRunner numquam hereat; inventa recentia in memoria servantur. Parva fenestra optionum prefixum, linguas et numerum inventorum ac definitionum statuit. Lingua Python scriptum est, et Python 3.14 aut recentiorem, py-wk et nexus D-Bus pro Python requirit.</p>
  </li>

  <li class="project" id="wk">
    <h2><a href="https://github.com/{{ site.github_username }}/wk-android">wk: Wiktionary Reader</a></h2>
    <p class="project-role">2026 · v1.4 · in <a href="https://codeberg.org/{{ site.codeberg_username }}/wk-android">Codeberg</a> et <a href="https://github.com/{{ site.github_username }}/wk-android">GitHub</a></p>
    <p><b>wk: Wiktionary Reader</b> parvum programma est pro Android ad <a href="https://en.wiktionary.org">Victionarium Anglicum</a> legendum, quasi <a href="https://github.com/{{ site.github_username }}/py-wk">py-wk</a> in telephono. Scribe vocem cuiuslibet lingue, Victionario dum scribis voces suggerente, et programma articulum integrum ostendit, formis situs ad telephonum accommodatis: tabule latiores in suo quadro in transversum moventur, tituli sectionum tactu aperiuntur et clauduntur, et series in summo linguas pagine enumerat, primo loco quas prefers, ceteras occultas sed uno tactu paratas. Nexus ad alios articulos in ipso programmate aperiuntur, in lingua debita, ceteri in navigatro. Ex quolibet programmate vox inquiri potest: elige eam et preme <i>Look up in Wiktionary</i>, vel textum cum wk communica. Pagine per hebdomadam servantur, ita ut vox iam visa statim aperiatur, et programma modum clarum vel obscurum systematis sequitur. Interfacies Anglice et Hispanice loquitur. Lingua Kotlin scriptum est, solis instrumentis ipsius Android, nulla alia bibliotheca adhibita (fasciculus APK editionis circiter 80 KB occupat), et Android 10 aut recentiorem requirit.</p>
  </li>

  <li class="project">
    <h2><a href="https://github.com/{{ site.github_username }}/krunner-abbr">krunner-abbr: abbreviationes in KDE Plasma explicare</a></h2>
    <p class="project-role">2026 · v2.0.1 · in <a href="https://codeberg.org/{{ site.codeberg_username }}/krunner-abbr">Codeberg</a> et <a href="https://github.com/{{ site.github_username }}/krunner-abbr">GitHub</a></p>
    <p><b>krunner-abbr</b> additamentum est <a href="https://userbase.kde.org/Plasma/Krunner">KRunner</a> pro Plasma 6, lingua Python scriptum, quod abbreviationes explicat: scribe <code>abbr</code> et abbreviationem, preme Enter, et verba plene scripta in memoriam transcriptoriam exscribuntur. Abbreviationes in documento TOML servantur et loca vacua admittunt pro diebus, pro memoria transcriptoria, pro textu scripto, pro fenestris interrogationis et pro mandatis terminalis, cum colis inter se concatenandis ad textum purgandum (litteras initiales more titulorum maiusculas faciendas, lineas textus ex PDF exscripti coniungendas, signa citationis mutanda, lineas ordinandas). Exempla affert pro LaTeX et Markdown, pro lingua Latina (numeros Romanos, apices) et pro BibTeX ex DOI petendo, necnon fenestram optionum cum prospectu vivo. Python 3.14 aut recentiorem requirit.</p>
  </li>

  <li class="project">
    <h2><a href="https://github.com/{{ site.github_username }}/QuickView">QuickView: documenta in KDE Plasma celeriter inspicere</a></h2>
    <p class="project-role">2026 · v1.0.4 · in <a href="https://codeberg.org/{{ site.codeberg_username }}/QuickView">Codeberg</a> et <a href="https://github.com/{{ site.github_username }}/QuickView">GitHub</a></p>
    <p><b>QuickView</b> furca est retractata <a href="https://github.com/MustaphaAlioglou/QuickView">programmatis QuickView Mustaphe Alioglou</a>, instrumenti ad documenta celeriter inspicienda in KDE Plasma 6, more Quick Look in macOS: elige documentum in Dolphin, preme clavem spatii, et tabula fluitans cum prospectu apparet; sagitte per directorium discurrunt vel per documenta simul electa transeunt. Imagines ostendit, PDF (cum inquisitione et indice laterali), libros EPUB in paginas compositos, Markdown redditum, codicem fontium cum syntaxi coloribus distincta, HTML, sonos et pelliculas, contenta archivorum compressorum, tabulas calculatorias in suis cancellis, et documenta officii per LibreOffice in paginas composita. Demon semper presens efficit ut tabula intra viginti fere millesimas secundi appareat, et quilibet analysator in carcere bubblewrap currit, sine accessu ad rete vel ad systema documentorum. Furca subsidium pro LibreOffice ex Flathub addit, vitium corrigit quo tabula herere poterat, demonem in modulos minores dividit et institutorem tutiorem reddit. Lingua Python cum PySide6 scriptum est, et Python 3.15 aut recentiorem et bubblewrap requirit.</p>
  </li>

  <li class="project" id="py-slowdown">
    <h2><a href="https://github.com/{{ site.github_username }}/py-slowdown">py-slowdown: musicam tardius vel celerius reddere, altitudine soni non mutata</a></h2>
    <p class="project-role">2026 · v1.4.0 · in <a href="https://codeberg.org/{{ site.codeberg_username }}/py-slowdown">Codeberg</a> et <a href="https://github.com/{{ site.github_username }}/py-slowdown">GitHub</a></p>
    <p><b>py-slowdown</b> sonos tardius vel celerius reddit, altitudine soni non mutata. Ad musicam factum est: ad carmen meditandum et auribus discendum, eodem loco iterum atque iterum audito ea celeritate quam quis sequi possit. Documenta sonora et sonum pellicularum aperit, eaque ut figuram undarum cum signaculis ostendit. Celeritas a 0,25× ad 3× procedit et, dum sonus currit, mutari potest; extensionem facit bibliotheca Rubber Band. Altitudo soni per semitonia et centesimas movetur. Pars electa sine intervallo iteratur et ut circulus servari potest; programma partem tantum soni permixti reddere potest (unum canalem, sonum sine medio suo, sonos graves), ante sonum more metronomi numerare, et quod auditur exportare. Cuiusque documenti meminit quomodo redditum sit, etiam in documento <code>.slx</code> quod cum recitatione migrat. Interfacies Anglice et Hispanice loquitur; lingua Python cum PySide6, PyAV et NumPy scriptum est, et per institutores pro Windows, macOS et Linux, ut AppImage, ut fasciculus Fedore vel Debian, vel ex fontibus cum Python 3.14 aut recentiore instituitur. Slowdown, forma eius pro Android, eadem documenta <code>.slx</code> in telephono aperit.</p>
    <p><a class="button button-primary" href="{{ "/la/programmata/py-slowdown/" | relative_url }}"><i class="fas fa-info-circle" aria-hidden="true"></i> Plura de eo</a></p>
  </li>

  <li class="project" id="py-schematron">
    <h2><a href="https://github.com/{{ site.github_username }}/py-schematron">py-schematron: TEI-XML secundum Schematron ex terminali probare</a></h2>
    <p class="project-role">2026 · v2.7 · in <a href="https://codeberg.org/{{ site.codeberg_username }}/py-schematron">Codeberg</a> et <a href="https://github.com/{{ site.github_username }}/py-schematron">GitHub</a></p>
    <p><b>py-schematron</b> scriptum est lingua Python, quod documenta TEI-XML secundum regulas Schematron in ODD inclusas probat (vel in documento <code>.sch</code> iam extracto, vel ex schemate RelaxNG ab ODD genito collectas, que sunt regule quas Jing negligit), easque per Saxon exsequitur. Non sicut oXygen, quod post centum errores tacite cessat, omnia peccata refert, cum numero pro singulis regulis et, si petitur, numero linee et <code>xml:id</code> uniuscuiusque elementi peccantis, et dicit quot omiserit cum index certo numero terminatur. Si qua peccata sunt, codicem exitus a 0 diversum reddit, ita ut in Makefile vel in hamo pre-commit adhiberi possit. Python 3.15 aut recentiorem, <code>saxonche</code> et <code>lxml</code> requirit.</p>
    <p class="continued">Schema etiam per se invenit ex declarationibus <code>&lt;?xml-model?&gt;</code> documenti, et scriptum aliud quod ei adiungitur, <code>py-schematron-all.sh</code>, structuram secundum RelaxNG per jing insuper probat et unam de utraque probatione sententiam reddit. Relatio quam py-schematron in forma JSON reddit duo additamenta editorum infra descripta alit, quorum utrumque proprium repositorium habet: extensionem <a href="#schematron-validator">Schematron Validator</a> pro VS Code et [py-schematron.el](#py-schematron-el) pro Emacs.</p>
  </li>

  <li class="project" id="schematron-validator">
    <h2><a href="https://marketplace.visualstudio.com/items?itemName=NicolasVaughan.validate-schematron">Schematron Validator: TEI-XML in VS Code dum scribis probare</a></h2>
    <p class="project-role">2026 · v0.12.0 · in <a href="https://marketplace.visualstudio.com/items?itemName=NicolasVaughan.validate-schematron">Visual Studio Marketplace</a> · fontes in <a href="https://codeberg.org/{{ site.codeberg_username }}/py-schematron-vscode">Codeberg</a> et <a href="https://github.com/{{ site.github_username }}/py-schematron-vscode">GitHub</a></p>
    <p><b>Schematron Validator</b> extensio est pro VS Code que <a href="#py-schematron">py-schematron</a> in editorem transfert. Documenta XML et TEI secundum regulas Schematron (ex <code>.sch</code>, ex ODD, vel ex schemate RelaxNG regulis instructo) probat dum scribis, cum aperiuntur et cum servantur, mutationibus nondum servatis comprehensis. Quodque peccatum in elemento peccante sublineatur et in tabula problematum recensetur, cum gravitate ex attributo <code>role</code> regule sumpta. Si schema RelaxNG est et <a href="https://relaxng.org/jclark/jing.html">jing</a> institutum, errores structure etiam adduntur, et XML male formatum ibi signatur ubi signum fractum apertum est. Schema ex declaratione <code>&lt;?xml-model?&gt;</code> documenti sumitur vel in optionibus statuitur; index in linea status ostendit utrum documentum mundum sit, et mandata te sinunt interpretem Python eligere aut schema, quod in fonte suo mutatum est, iterum depromere. Scriptum una cum extensione prebetur; extensio Python 3.15 aut recentiorem cum <code>saxonche</code> et <code>lxml</code> requirit, et pagina eius docet quomodo ea instituantur.</p>
    <p><a class="button button-primary" href="https://marketplace.visualstudio.com/items?itemName=NicolasVaughan.validate-schematron"><i class="fas fa-download" aria-hidden="true"></i> Ex Marketplace institue</a></p>
  </li>

  <li class="project" id="py-schematron-el">
    <h2><a href="https://github.com/{{ site.github_username }}/py-schematron.el">py-schematron.el: TEI-XML in Emacs dum scribis probare, per Flycheck aut Flymake</a></h2>
    <p class="project-role">2026 · v1.0.2 · in <a href="https://codeberg.org/{{ site.codeberg_username }}/py-schematron.el">Codeberg</a> et <a href="https://github.com/{{ site.github_username }}/py-schematron.el">GitHub</a></p>
    <p><b>py-schematron.el</b> fasciculus est pro Emacs qui <a href="#py-schematron">py-schematron</a> in editorem transfert, per Flycheck, si institutum est, sin minus per Flymake, quod una cum ipso Emacs prebetur. Omne documentum apertum quod declarationem <code>&lt;?xml-model?&gt;</code> habet probat dum scribis, cum aperitur et cum servatur; mutationes nondum servate in exemplari temporario et privato probantur, ita ut in ipsum documentum nichil umquam scribatur. Quodque peccatum sublineatur, et nuntius eius ostenditur cum cursor in eo stat, una cum probatione que illud invenit (Schematron, RelaxNG, vel XML, si documentum male formatum est), et linea modi numeros peccatorum ostendit; mandatum quoddam relationem integram documenti verbis expressam reddit, singulis lineis cum documento coniunctis. Si schema RelaxNG est, structuram etiam per <a href="https://relaxng.org/jclark/jing.html">jing</a> probat et schema, per trang conversum, ipsi nxml-mode tradit, ut ea elementa et attributa proponantur que schema eo loco ubi cursor stat permittit. Quoniam regule schematis documenta legere et ex rete petere possunt, sola documenta probat que in <code>trusted-content</code>, id est in indice rerum quibus Emacs fidem habet, recensentur. Emacs 31 aut recentiorem requirit, et Python 3.15 aut recentiorem cum <code>saxonche</code> et <code>lxml</code>; jing et trang non sunt necessaria.</p>
  </li>

  <li class="project" id="odd2rng">
    <h2><a href="https://github.com/{{ site.github_username }}/ODD2RNG">ODD2RNG: schemata RELAX NG ex ODD TEI facta, ex linea mandatorum</a></h2>
    <p class="project-role">2026 · v1.3 · in <a href="https://codeberg.org/{{ site.codeberg_username }}/ODD2RNG">Codeberg</a> et <a href="https://github.com/{{ site.github_username }}/ODD2RNG">GitHub</a></p>
    <p><b>ODD2RNG</b> ODD TEI in schema RELAX NG quod ei respondet convertit, oXygen non aperto. Easdem duas transformationes TEI Stylesheets, eisdem parametris, exsequitur quas exsequitur scenarium <i>TEI ODD to RELAX NG XML</i> ipsius oXygen, unde schema quod scribit idem est ac schema oXygen, excepto die generationis in commentario capitis (collatione in ODD incepti SMTrad facta). Nisi aliter iubetur, <code>out/NOMEN.rng</code> iuxta ODD scribit, sicut oXygen, nec schema vetus novo commutat nisi hoc iam perfecto, ne editor vel probator semiscriptum legat; ultima linea dicit utrum schema novum sit, an mutatum, an idem preter diem, id est utrum aliquid sit quod in git committere opere pretium sit. TEI Stylesheets et fons TEI (<code>p5subset.xml</code>) ex exemplari repositorii TEI vel ex eo quod in oXygen inest sumi possunt; loca eorum in documento optionum servantur, et programma instituendi mandatum in PATH ponit. Python 3.15 aut recentiorem cum <code>saxonche</code> requirit.</p>
  </li>
</ul>

## Alia programmata

<ol class="publications">
  {% for pub in site.data.software %}
    {% include publication.html pub=pub %}
  {% endfor %}
</ol>

## Instrumenta quibus utor

In machinis meis solo [GNU/Linux](https://la.wikipedia.org/wiki/GNU/Linux) utor.
Nunc libenter distributione [Fedora Linux](https://fedoraproject.org/) (versione 45) cum mensa [KDE Plasma](https://kde.org/plasma-desktop/) 6 fruor.
Per multos annos distributione [Manjaro Linux](https://manjaro.org/) et etiam [Arch Linux](https://archlinux.org/) pura usus sum, sed eas satis instabiles et ad cotidianum usum difficiles inveni.

Precipuus editor meus, ad scribendum et programmandum, est [GNU Emacs](https://www.gnu.org/s/emacs/) (versione 31), quem lingua Emacs Lisp ordino. In eo notas meas per [Org mode](https://orgmode.org/) et [Org-roam](https://www.orgroam.com/) servo, LaTeX per [AUCTeX](https://www.gnu.org/software/auctex/) et RefTeX scribo, Git per [Magit](https://magit.vc/) tracto, et documenta TEI per nxml-mode et per meum [py-schematron.el](#py-schematron-el) tracto.
Ad incepta TEI, accommodationes ODD et XSLT etiam [Oxygen XML Editor](https://www.oxygenxml.com/) adhibeo.
Ad mutationes celeres Vim vel Sublime Text adhibeo, et [Visual Studio Code](https://code.visualstudio.com/) maxime ut extensionem meam [Schematron Validator](#schematron-validator) experiar.

In terminali [Ghostty](https://ghostty.org/) cum testa [fish](https://fishshell.com/) et tmux utor, et paucis instrumentis linee mandatorum: ripgrep et fd ad inquirendum, fzf, bat, eza, zoxide, atuin pro historia mandatorum, et delta ad differentias legendas.

In lingua Python [uv](https://docs.astral.sh/uv/) utor, quod versiones Python, ambitus et dependentias curat, et pytest ad probationes.
Programmata mea in fasciculos RPM pro Fedora, per rpmbuild confectos et in [Copr](https://copr.fedorainfracloud.org/) editos, et in AppImage pro ceteris distributionibus redigo.
Fontes in [Codeberg](https://codeberg.org/{{ site.codeberg_username }}) et [GitHub](https://github.com/{{ site.github_username }}) servantur; utroque situ ex terminali per tea et gh utor.
[Claude Code](https://claude.com/product/claude-code) ad codicem probandum et edendum adhibeo.

Extra editorem XSLT et XPath per [Saxon](https://www.saxonica.com/) exsequor, et schemata RELAX NG per [Jing](https://relaxng.org/jclark/jing.html) et [Trang](https://relaxng.org/jclark/trang.html) probo et converto.
Ad typos componendos LuaLaTeX ex [TeX Live](https://tug.org/texlive/) adhibeo, cum Biber ad bibliographias, quas in [Zotero](https://www.zotero.org/) cum extensione Better BibTeX servo; [Pandoc](https://pandoc.org/) ceteras conversiones inter formas curat.

Hunc situm per [Jekyll](https://jekyllrb.com), generatorem situum staticorum, construxi; forma eius ex themate [S.V. Miller](https://svmiller.com/) orta est.
Fontes eius [in GitHub](https://github.com/{{ site.github_username }}/nivaca.github.io) patent.
