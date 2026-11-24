---
layout: page
ref: py-words
title: py-words
subtitle: Lexicon Latino-Anglico-Latinum et Latino-Hispanico-Latinum cum morphologia
permalink: /la/programmata/py-words/
description: py-words, lexicon Latinum cum morphologia a Nicolao Vaughan confectum, in omnibus eius formis (fenestra, linea mandatorum, terminali, pagina interretiali, KRunner et Android); quomodo instituatur, et editiones eius.
---

py-words voces Latinas flexas, et integras lineas Latinas, in formas suas et in articulos lexici resolvit, cum significationibus Anglice vel Hispanice redditis, et voces Latinas pro Anglicis vel Hispanicis invenit. Initium eius fuit fidelis translatio programmatis *WORDS* Guillelmi Whitaker in linguam Python, ex versione Ada que servatur in [mk270/whitakers-words](https://github.com/mk270/whitakers-words). Deinde ipsum ut codicem Python usitatum denuo disposui, cum eisdem analysibus, inventis clarioribus et datis in XML; et postea lexicon crevit ex Lewis et Short, ex De Miguel et Echave-Sustaeta pro parte Hispanica, et ex indice verborum medii evi Latham.

<div class="buttons">
  <a class="button button-primary" href="{{ "/py-words/" | relative_url }}"><i class="fas fa-book-open" aria-hidden="true"></i> py-words in rete aperi</a>
  <a class="button" href="https://nivaca.pythonanywhere.com/"><i class="fas fa-server" aria-hidden="true"></i> Speculum</a>
  <a class="button" href="https://codeberg.org/{{ site.codeberg_username }}/py-words/releases"><i class="fas fa-download" aria-hidden="true"></i> Fasciculi</a>
</div>

<dl class="facts">
  <dt>Editio</dt><dd>3.31 (die XXIV mensis Novembris anni MMXXVI)</dd>
  <dt>Programmata</dt><dd>fenestra, linea mandatorum, terminale totum quadrum occupans, pagina interretialis; etiam in KRunner et in Android</dd>
  <dt>Lexicon</dt><dd>93.370 articuli, cum significationibus Anglicis et Hispanicis</dd>
  <dt>Interfacies</dt><dd>Anglica, Hispanica et Latina medii evi</dd>
  <dt>Requirit</dt><dd>Python 3.13 aut recentiorem cum bibliotheca eius communi, nec quicquam amplius (institutores et AppImage proprium Python secum ferunt)</dd>
  <dt>Licentia</dt><dd>GNU General Public License, versio 3 aut posterior</dd>
  <dt>Fontes</dt><dd>in <a href="https://codeberg.org/{{ site.codeberg_username }}/py-words">Codeberg</a> et <a href="https://github.com/{{ site.github_username }}/py-words">GitHub</a></dd>
</dl>

## Quid prebeat

Scribe *laudatus*, et py-words dicit quid esse possit:

<pre><code>laudatus
  laudo, laudare, laudavi, laudatus  verb, 1st conjugation  [XXXAX]
    recommend; praise, approve, extol; call upon, name; deliver eulogy on;
    laudat-us      PRF.PASS.PTCP.NOM.SG.M
    participle + est  3SG.PRF.PASS.IND
</code></pre>

Quisque articulus ostendit partes principales et grammaticam, notas etatis, frequentie et fontis inter uncos, significationem, et omnes formas quas vox esse potest, radice a terminatione distincta, vocalibus longis notatis (*amīc-ōrum*, *am-ābat*). Analyses abbreviationibus Leipzig Glossing Rules scribuntur (`GEN.PL`, `2SG.PRF.ACT.IND`), et in fenestra et in pagina interretiali quelibet nota et quelibet abbreviatio, mure super eam posito, se ipsam explicat. Prefixa, suffixa et enclitica lineam propriam habent, et similiter artificia quibus opus fuit ut vox inveniretur: orthographie medii evi (*michi*, *ecclesie*, *hystorie*), perfecta syncopata, due voces ut una scripte. Vox cum errore scripta non perditur: inquisitio approximata orthographias una littera distantes temptat (*amcius* invenit *amicus*).

Inquisitio etiam in partem contrariam procedit, a voce Anglica vel Hispanica ad Latinam. Fenestra autem, terminale, linea mandatorum et pagina interretialis possunt, loco articulorum ipsius py-words, articulos [Logeion](https://logeion.uchicago.edu) ostendere, quod dictionaria Latina Universitatis Chicagiensis complectitur (Lewis et Short, Gaffiot, Georges, Du Cange, DMLBS et alia). Logeion formas flexas non resolvit; ideo py-words vocem primo resolvit, et a Logeion lemmata eius petit.

## Programmata

Omnia eodem lexico, eisdem optionibus et eadem historia inquisitionum utuntur.

### Fenestra

`words_gui.py` via usitata est qua programma adhibetur: area inquisitionis, directio (a Latino in Anglicum vel Hispanicum, vel e contrario), lingua significationum, et inventa, in quibus ictus muris in prima voce articuli, vel duplex ictus in quacumque voce, eam querit. Modum obscurum habet, ductum auxilii, optiones et duos editores lexici.

<figure class="screenshot">
  <img src="{{ "/images/py-words/gui_la.webp" | relative_url }}" alt="Fenestra py-words in modo obscuro, articulos vocis perspicio ostendens" loading="lazy">
  <figcaption>Fenestra, in modo obscuro, <i>perspicio</i> quesito.</figcaption>
</figure>

### Linea mandatorum

`words.py` voces ut argumenta accipit (`python3 words.py rem acu tetigisti`), vel eas lineam post lineam in modo interlocutorio legit, ubi mandata ut `~E` directionem mutant et `~H` auxilium ostendit. Fasciculos quoque legit, et inventa eius in fasciculo servari possunt.

<figure class="screenshot">
  <img src="{{ "/images/py-words/cli_la.webp" | relative_url }}" alt="py-words in linea mandatorum" loading="lazy">
  <figcaption>Linea mandatorum, in modo interlocutorio.</figcaption>
</figure>

### Terminale, totum quadrum occupans

`words_tui.py` est fenestra in terminali: linea ad querendum, inventa infra, et claves functionum in ultima linea ostense (F2 directionem mutat, F5 linguam significationum, F6 linguam interfaciei, F8 ad Logeion transit). Nichil requirit nisi curses, quam bibliothecam Python in Linux et macOS habet.

<figure class="screenshot">
  <img src="{{ "/images/py-words/tui_la.webp" | relative_url }}" alt="py-words in terminali, totum quadrum occupans" loading="lazy">
  <figcaption>Versio terminalis totum quadrum occupans.</figcaption>
</figure>

### Pagina interretialis

`words_web.py` parvum servitrum interretiale in computatro incipit et navigatrum ad id aperit. Pagina omnia habet que fenestra, editoribus exceptis, et quelibet inquisitio suam inscriptionem habet, ita ut inter signacula servari possit. Idem programma, in servitro publico, est lexicon in rete: [py-words.uniandes.edu.co](https://py-words.uniandes.edu.co/), cum speculo ad [nivaca.pythonanywhere.com](https://nivaca.pythonanywhere.com/). Ibi quisque visitator suas optiones et inquisitiones priores habet, in crustulis (cookies) navigatri sui servatas, numquam in servitro.

<figure class="screenshot">
  <img src="{{ "/images/py-words/web_la.webp" | relative_url }}" alt="Pagina interretialis py-words" loading="lazy">
  <figcaption>Pagina interretialis, eadem que in rete est.</figcaption>
</figure>

### In KRunner (KDE Plasma)

[krunner-py-words](https://github.com/{{ site.github_username }}/krunner-py-words) (editio 1.1.2) lexicon in KRunner ponit, instrumentum quo in KDE Plasma 6 programmata aperiuntur. Scribe `pw` et vocem Latinam, vel integram lineam, et articuli dum scribis apparent, quisque cum lemmate, significatione et formis suis; `pw ~e friend` ab Anglico vel Hispanico in Latinum procedit. Clavis Enter inquisitionem in fenestra py-words aperit, et alie actiones inventa exscribunt vel inquisitionem in rete aperiunt. Programma, lexico onerato, in memoria manet, ita ut quelibet inquisitio celeris sit. Optiones py-words sequitur, et parvam fenestram optionum propriam habet (`pw ?`), pro prefixo, linguis et numero inventorum. In Fedora, fasciculus eius in [Copr](https://copr.fedorainfracloud.org/coprs/nivaca/krunner-py-words/) py-words secum affert.

### In Android

[py-words pro Android](https://github.com/{{ site.github_username }}/py-words-android) (editio 2.7) ipsum py-words in se continet, cum datis eius et Python 3.13 quo currit, ita ut in telephono sine rete operetur. Per tabellam fons a telephono ad situm in rete transfertur, et rursus ad telephonum; uterque eandem paginam ostendit, et mutato fonte inquisitio in quadro manet. Prima vice lexicon in telephono paucis momentis oneratur, postea celerius. Vox vel linea Latina ex quolibet programmate queri potest, eam eligendo et *Look up in py-words* premendo, vel textum cum programmate communicando. Programma lingua Kotlin scriptum est, cum Chaquopy, per quod Python currit, et Android 10 aut recentiorem in machina ARM 64 bitorum requirit. Institui potest ex editionibus eius ([Codeberg](https://codeberg.org/{{ site.codeberg_username }}/py-words-android/releases), [GitHub](https://github.com/{{ site.github_username }}/py-words-android/releases)), per [Obtainium](https://github.com/ImranR98/Obtainium), vel ex meo repositorio F-Droid, [nivaca.codeberg.page/fdroid](https://nivaca.codeberg.page/fdroid/); omnes tres vie eodem fasciculo APK obsignato utuntur, ita ut quelibet renovet quod per ceteras institutum est.

<figure class="screenshot phone">
  <img src="{{ "/images/py-words/android.webp" | relative_url }}" alt="py-words pro Android, cum analysi vocis arma et articulo DMLBS ex Logeion" loading="lazy">
  <figcaption>py-words pro Android, cum Logeion ut fonte.</figcaption>
</figure>

## Lingue

Programmata Anglice, Hispanice vel Latine medii evi loquuntur: tabelle, nuntii, auxilium et optiones eorum, editores, et commentarii fasciculi configurationis. Lingua eligitur per bullam que notam eius ostendit (EN, ES, LA), et electio pro omnibus programmatibus servatur. Significationes sunt Anglice vel Hispanice; cum interfacie Latina in altera harum duarum manent. Significationes Hispanice ex dictionariis Latino-Hispanicis De Miguel et Echave-Sustaeta sumuntur ubicumque vocem habent, et cetere ex Anglico translate sunt. Alie lingue addi possunt, singulis fasciculis XML.

## Lexicon

Lexicon est fasciculus XML 93.370 articulorum, cuius flexiones, forme irregulares, affixa et vocales longe in fasciculis propriis servantur. Ex his operibus venit:

- *WORDS*, auctore Guillelmo Whitaker (1936–2010): analyses, flexiones et articuli originales.
- R. E. Latham, *Revised Medieval Latin Word-List from British and Irish Sources* (1965): sensus medii evi, voces nove et orthographie varie.
- J. Echave-Sustaeta, *Lengua latina. Vocabulario básico*: articuli correcti et additi, Anglice et Hispanice.
- C. T. Lewis et C. Short, *A Latin Dictionary* (1879), ex Perseus Digital Library: 6.653 voces rare, 1.783 nomina propria, et definitiones Anglice 30.601 articulorum.
- R. de Miguel et marchio de Morante, *Nuevo diccionario latino-español etimológico* (1867): 25.149 voces et nomina propria, et plereque significationes Hispanice.
- *Collatinus*, auctoribus Yves Ouvrard et Philippe Verkerk: vocales longe radicum et terminationum.

Duo editores, alter in fenestra, alter in terminali, articulos addunt, corrigunt et delent, et examinator data probat.

## Quomodo instituatur

Omnes editiones obsignate sunt, et in [Codeberg](https://codeberg.org/{{ site.codeberg_username }}/py-words/releases) et [GitHub](https://github.com/{{ site.github_username }}/py-words/releases) inveniuntur.

| Systema | Quomodo |
|---|---|
| Windows 10 vel posterius | institutor (`.exe`), cum proprio Python |
| macOS 11 vel posterius | institutor (`.pkg`), pro Apple silicon vel Intel |
| Linux | institutor (`.run`), vel AppImage, ambo cum proprio Python |
| Fedora | `sudo dnf copr enable nivaca/py-words`, deinde `sudo dnf install py-words` |
| Debian, Ubuntu | fasciculus `.deb` obsignatus |
| Android | programma, ex editionibus eius, per Obtainium vel ex F-Droid (vide supra) |
| Ubicumque est Python 3.13 | fasciculus zip, vel exemplar repositorii: `python3 words_gui.py` |

Institutores et fasciculi locos in tabella applicationum et mandatum `py-words` addunt (`py-words` fenestram aperit, `py-words cli amicus` vocem querit). Ut programma ex fontibus adhibeatur, nichil construendum est: capsula ipsa est programma.

## De programmate scripta

- Manuale usuarii, in forma PDF: [Latine medii evi](https://github.com/{{ site.github_username }}/py-words/blob/main/docs/MANUAL_la.pdf), [Anglice](https://github.com/{{ site.github_username }}/py-words/blob/main/docs/MANUAL_en.pdf), [Hispanice](https://github.com/{{ site.github_username }}/py-words/blob/main/docs/MANUAL_es.pdf).
- README, ubi omnia fusius exponuntur: [Latine](https://github.com/{{ site.github_username }}/py-words/blob/main/README_la.md), [Anglice](https://github.com/{{ site.github_username }}/py-words/blob/main/README.md), [Hispanice](https://github.com/{{ site.github_username }}/py-words/blob/main/README_es.md).
- [Quomodo py-words factum sit](https://github.com/{{ site.github_username }}/py-words/blob/main/docs/DESCRIPTION.md) (Anglice), et [index mutationum](https://github.com/{{ site.github_username }}/py-words/blob/main/CHANGELOG.md).

## Editiones

Precipui gradus, a prima editione usque ad presentem. [Index mutationum](https://github.com/{{ site.github_username }}/py-words/blob/main/CHANGELOG.md) omnes editiones habet.

<ul class="history">
  <li><span class="when">1.0</span><span>Prima editio publica: <i>WORDS</i> in Python, ex versione eius Ada, cum datis in XML.</span></li>
  <li><span class="when">1.4–1.6</span><span>Analyses abbreviationibus Leipzig Glossing Rules scripte; dialogus optionum; inquisitiones ab una sessione in aliam memorie mandate.</span></li>
  <li><span class="when">1.7, 1.8</span><span>Versio terminalis totum quadrum occupans (<code>words_tui.py</code>) et pagina interretialis (<code>words_web.py</code>).</span></li>
  <li><span class="when">2.0, 2.1</span><span>Significationes in aliis linguis quam Anglica, et totum lexicon et interfacies Hispanice.</span></li>
  <li><span class="when">2.2–2.12</span><span>Modus obscurus; lexicon in rete; inquisitio approximata pro erroribus scribendi; ductus auxilii in quolibet programmate; fenestra clarior.</span></li>
  <li><span class="when">2.13–2.15<br>Oct. MMXXVI</span><span>Repositorium incipit. Lexicon cum Echave-Sustaeta et cum indice verborum medii evi Latham collatum: 44.380 articuli.</span></li>
  <li><span class="when">3.0<br>XXIII Oct.</span><span>Vocales longe, ex Collatino; plures orthographie medii evi; licentia fit GNU GPL, versio 3 aut posterior.</span></li>
  <li><span class="when">3.2<br>XXV Oct.</span><span>Lewis et Short et De Miguel additi: 93.370 articuli, significationibus Hispanicis ex De Miguel et Echave-Sustaeta denuo scriptis.</span></li>
  <li><span class="when">3.5–3.10<br>Nov.</span><span>AppImage pro Linux; pagina interretialis in servitro publico, optionibus cuiusque visitatoris in crustulis servatis; fasciculus RPM obsignatus pro Fedora.</span></li>
  <li><span class="when">3.17–3.23</span><span>Logeion ut alter fons, in omni programmate.</span></li>
  <li><span class="when">3.26–3.29</span><span>Manuale Anglice, Hispanice et Latine medii evi; fasciculus <code>.deb</code>; lingua interfaciei in fenestra principali; institutores pro Windows, macOS et Linux.</span></li>
  <li><span class="when">3.30, 3.31<br>XXII–XXIV Nov.</span><span>Omnes cuiusque editionis fasciculi obsignati, cum summis probatoriis suis; vie ad programma pro Android habendum.</span></li>
</ul>
