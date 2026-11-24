---
layout: page
ref: py-words
title: py-words
subtitle: Un diccionario latín-inglés-latín y latín-español-latín con morfología
permalink: /es/programacion/py-words/
description: py-words, un diccionario latino con morfología, de Nicolás Vaughan, en todas sus formas (ventana, línea de comandos, terminal, web, KRunner y Android), cómo instalarlo y sus versiones.
---

py-words analiza palabras latinas flexionadas, y líneas enteras de latín, en sus formas y sus entradas de diccionario, con los significados en inglés o en español, y busca el latín de palabras inglesas o españolas. Empezó como una traducción fiel a Python de *WORDS*, de William Whitaker, a partir de la versión en Ada que se mantiene en [mk270/whitakers-words](https://github.com/mk270/whitakers-words). Luego lo rehíce como Python corriente, con los mismos análisis, una salida más clara y sus datos en XML; desde entonces el diccionario ha crecido con Lewis y Short, con De Miguel y Echave-Sustaeta para el español y con la lista de palabras medievales de Latham.

<div class="buttons">
  <a class="button button-primary" href="{{ "/py-words/" | relative_url }}"><i class="fas fa-book-open" aria-hidden="true"></i> Abrir py-words en línea</a>
  <a class="button" href="https://nivaca.pythonanywhere.com/"><i class="fas fa-server" aria-hidden="true"></i> Sitio espejo</a>
  <a class="button" href="https://codeberg.org/{{ site.codeberg_username }}/py-words/releases"><i class="fas fa-download" aria-hidden="true"></i> Descargas</a>
</div>

<dl class="facts">
  <dt>Versión</dt><dd>3.31 (24 de noviembre de 2026)</dd>
  <dt>Programas</dt><dd>una ventana, la línea de comandos, la terminal a pantalla completa y una página web; también en KRunner y en Android</dd>
  <dt>Diccionario</dt><dd>93&nbsp;370 entradas, con significados en inglés y en español</dd>
  <dt>Interfaz</dt><dd>inglés, español y latín medieval</dd>
  <dt>Requisitos</dt><dd>Python 3.13 o posterior y su biblioteca estándar, nada más (los instaladores y la AppImage traen su propio Python)</dd>
  <dt>Licencia</dt><dd>Licencia Pública General de GNU, versión 3 o posterior</dd>
  <dt>Código</dt><dd><a href="https://codeberg.org/{{ site.codeberg_username }}/py-words">Codeberg</a> y <a href="https://github.com/{{ site.github_username }}/py-words">GitHub</a></dd>
</dl>

## Qué ofrece

Escriba *laudatus* y py-words le dice qué puede ser:

<pre><code>laudatus
  laudo, laudare, laudavi, laudatus  verb, 1st conjugation  [XXXAX]
    recommend; praise, approve, extol; call upon, name; deliver eulogy on;
    laudat-us      PRF.PASS.PTCP.NOM.SG.M
    participle + est  3SG.PRF.PASS.IND
</code></pre>

Cada entrada muestra sus partes principales y su gramática, entre corchetes los códigos de su época, su frecuencia y su fuente, el significado y cada una de las formas que la palabra puede ser, escrita como raíz y desinencia, con las vocales largas marcadas (*amīc-ōrum*, *am-ābat*). Los análisis usan las abreviaturas de las *Leipzig Glossing Rules* (`GEN.PL`, `2SG.PRF.ACT.IND`), y en la ventana y en la página web cada código y cada abreviatura se explican solos al pasar el ratón por encima. Los prefijos, sufijos y enclíticos van en una línea propia, igual que los recursos con que se halló la palabra: grafías medievales (*michi*, *ecclesie*, *hystorie*), perfectos sincopados, dos palabras escritas como una. Una palabra con una errata no se pierde, porque la búsqueda aproximada prueba las grafías que difieren en una letra (*amcius* encuentra *amicus*).

La búsqueda va también en sentido contrario, de una palabra inglesa o española al latín. Y la ventana, la terminal, la línea de comandos y la página web pueden mostrar, en lugar de las entradas propias de py-words, las de [Logeion](https://logeion.uchicago.edu), los diccionarios latinos de la Universidad de Chicago (Lewis y Short, Gaffiot, Georges, Du Cange, el DMLBS y otros). Logeion no analiza las formas flexionadas, así que py-words analiza primero la palabra y le pide a Logeion sus lemas.

## Los programas

Todos comparten el mismo diccionario, los mismos ajustes y el mismo historial de búsquedas.

### La ventana

`words_gui.py` es la manera habitual de usarlo: un cuadro de búsqueda, la dirección (del latín al inglés o al español, o al revés), el idioma de los significados y los resultados, donde un clic sobre la primera palabra de una entrada, o un doble clic sobre cualquier palabra, la busca. Tiene modo oscuro, una ayuda, ajustes y los dos editores del diccionario.

<figure class="screenshot">
  <img src="{{ "/images/py-words/gui_es.webp" | relative_url }}" alt="La ventana de py-words en modo oscuro, con las entradas de perspicio" loading="lazy">
  <figcaption>La ventana, en modo oscuro, con <i>perspicio</i>.</figcaption>
</figure>

### La línea de comandos

`words.py` recibe las palabras como argumentos (`python3 words.py rem acu tetigisti`) o las lee una línea tras otra en una sesión interactiva, donde comandos como `~E` cambian la dirección y `~H` muestra la ayuda. También lee archivos, y su salida puede guardarse en un archivo.

<figure class="screenshot">
  <img src="{{ "/images/py-words/cli_es.webp" | relative_url }}" alt="py-words en la línea de comandos" loading="lazy">
  <figcaption>La línea de comandos interactiva.</figcaption>
</figure>

### La terminal, a pantalla completa

`words_tui.py` es la ventana dentro de una terminal: una línea para buscar, los resultados debajo y las teclas de función en la última línea (F2 cambia la dirección; F5, el idioma de los significados; F6, el de la interfaz; F8 pasa a Logeion). No necesita más que curses, que Python trae en Linux y macOS.

<figure class="screenshot">
  <img src="{{ "/images/py-words/tui_es.webp" | relative_url }}" alt="py-words a pantalla completa en una terminal" loading="lazy">
  <figcaption>La versión de pantalla completa para la terminal.</figcaption>
</figure>

### La página web

`words_web.py` arranca un pequeño servidor web en el computador y abre el navegador en él. La página tiene todo lo que tiene la ventana, salvo los editores, y cada búsqueda tiene su propia dirección, de modo que puede guardarse en los marcadores. El mismo programa, en un servidor público, es el diccionario en línea: [py-words.uniandes.edu.co](https://py-words.uniandes.edu.co/), con un sitio espejo en [nivaca.pythonanywhere.com](https://nivaca.pythonanywhere.com/). Allí cada visitante tiene sus propios ajustes y sus búsquedas anteriores, guardados en las cookies de su navegador y nunca en el servidor.

<figure class="screenshot">
  <img src="{{ "/images/py-words/web_es.webp" | relative_url }}" alt="La página web de py-words" loading="lazy">
  <figcaption>La página web, igual a la que está en línea.</figcaption>
</figure>

### En KRunner (KDE Plasma)

[krunner-py-words](https://github.com/{{ site.github_username }}/krunner-py-words) (versión 1.1.2) pone el diccionario en KRunner, el lanzador de KDE Plasma 6. Escriba `pw` y una palabra latina, o una línea entera, y las entradas aparecen mientras escribe, cada una con su forma de diccionario, su significado y sus formas; `pw ~e friend` va del inglés o del español al latín. Enter abre la búsqueda en la ventana de py-words, y otras acciones copian los resultados o abren la búsqueda en línea. El complemento se queda en memoria con el diccionario cargado, así que cada consulta es rápida. Sigue los ajustes de py-words y tiene una pequeña ventana de configuración propia (`pw ?`) para el prefijo, los idiomas y el número de resultados. En Fedora, su paquete en [Copr](https://copr.fedorainfracloud.org/coprs/nivaca/krunner-py-words/) trae py-words consigo.

### En Android

[py-words para Android](https://github.com/{{ site.github_username }}/py-words-android) (versión 2.7) lleva dentro el propio py-words, con sus datos y un Python 3.13 para correrlo, así que funciona en el teléfono sin internet. Un menú cambia la fuente al sitio en línea, y viceversa; las dos muestran la misma página, y al cambiar de fuente se conserva la búsqueda que hay en pantalla. La primera vez, el diccionario tarda unos segundos en cargar en el teléfono; después, menos. Desde cualquier aplicación puede consultarse una palabra o una línea de latín: se selecciona y se elige *Buscar en py-words*, o se comparte el texto con la aplicación. Está escrita en Kotlin, con Chaquopy para correr Python, y necesita Android 10 o posterior en un dispositivo ARM de 64 bits. Se instala desde sus versiones publicadas ([Codeberg](https://codeberg.org/{{ site.codeberg_username }}/py-words-android/releases), [GitHub](https://github.com/{{ site.github_username }}/py-words-android/releases)), con [Obtainium](https://github.com/ImranR98/Obtainium) o desde mi propio repositorio de F-Droid, [nivaca.codeberg.page/fdroid](https://nivaca.codeberg.page/fdroid/). Los tres usan el mismo APK firmado, de modo que cualquiera de ellos actualiza a los otros.

<figure class="screenshot phone">
  <img src="{{ "/images/py-words/android.webp" | relative_url }}" alt="py-words para Android, con el análisis de arma y la entrada del DMLBS en Logeion" loading="lazy">
  <figcaption>py-words para Android, con Logeion como fuente.</figcaption>
</figure>

## Idiomas

Los programas hablan inglés, español o latín medieval: sus menús, mensajes, ayuda y ajustes, los editores y los comentarios del archivo de configuración. El idioma se elige con un botón que muestra su código (EN, ES, LA), y la elección se guarda para todos los programas. Los significados están en inglés o en español; con la interfaz en latín, quedan en uno de esos dos. Los significados en español vienen de los diccionarios latín-español de De Miguel y de Echave-Sustaeta dondequiera que tengan la palabra, y los demás se tradujeron del inglés. Pueden añadirse otros idiomas, con un archivo XML para cada uno.

## El diccionario

El diccionario es un archivo XML de 93&nbsp;370 entradas; sus flexiones, formas irregulares, afijos y vocales largas están en archivos aparte. Viene de estas obras:

- *WORDS*, de William Whitaker (1936–2010): los análisis, las flexiones y las entradas originales.
- R. E. Latham, *Revised Medieval Latin Word-List from British and Irish Sources* (1965): acepciones medievales, palabras nuevas y variantes gráficas.
- J. Echave-Sustaeta, *Lengua latina. Vocabulario básico*: entradas corregidas y añadidas, en inglés y en español.
- C. T. Lewis y C. Short, *A Latin Dictionary* (1879), tomado de la Perseus Digital Library: 6653 palabras raras, 1783 nombres y las definiciones inglesas de 30&nbsp;601 entradas.
- R. de Miguel y el marqués de Morante, *Nuevo diccionario latino-español etimológico* (1867): 25&nbsp;149 palabras y nombres, y la mayor parte de los significados en español.
- *Collatinus*, de Yves Ouvrard y Philippe Verkerk: las vocales largas de las raíces y de las desinencias.

Dos editores, uno en una ventana y otro en la terminal, añaden, corrigen y borran entradas, y un verificador comprueba los datos.

## Instalación

Cada versión está firmada y se publica en [Codeberg](https://codeberg.org/{{ site.codeberg_username }}/py-words/releases) y en [GitHub](https://github.com/{{ site.github_username }}/py-words/releases).

| Sistema | Cómo |
|---|---|
| Windows 10 o posterior | un instalador (`.exe`), con su propio Python |
| macOS 11 o posterior | un instalador (`.pkg`), para Apple silicon o Intel |
| Linux | un instalador (`.run`) o una AppImage, ambos con su propio Python |
| Fedora | `sudo dnf copr enable nivaca/py-words` y luego `sudo dnf install py-words` |
| Debian, Ubuntu | un paquete `.deb` firmado |
| Android | la aplicación, desde sus versiones publicadas, Obtainium o F-Droid (véase arriba) |
| Cualquier sistema con Python 3.13 | el zip, o un clon del repositorio: `python3 words_gui.py` |

Los instaladores y los paquetes añaden entradas al menú y un comando `py-words` (`py-words` abre la ventana; `py-words cli amicus` busca una palabra). Para usarlo desde el código fuente no hay nada que compilar: la carpeta es el programa.

## Documentación

- El manual de usuario, en PDF: [español](https://github.com/{{ site.github_username }}/py-words/blob/main/docs/MANUAL_es.pdf), [inglés](https://github.com/{{ site.github_username }}/py-words/blob/main/docs/MANUAL_en.pdf), [latín medieval](https://github.com/{{ site.github_username }}/py-words/blob/main/docs/MANUAL_la.pdf).
- El README, que lo explica todo por extenso: [español](https://github.com/{{ site.github_username }}/py-words/blob/main/README_es.md), [inglés](https://github.com/{{ site.github_username }}/py-words/blob/main/README.md), [latín](https://github.com/{{ site.github_username }}/py-words/blob/main/README_la.md).
- La [descripción de py-words](https://github.com/{{ site.github_username }}/py-words/blob/main/docs/DESCRIPCI%C3%93N_es.md) y el [registro de cambios](https://github.com/{{ site.github_username }}/py-words/blob/main/CHANGELOG_es.md).

## Versiones

Los pasos principales, desde la primera versión hasta la actual. El [registro de cambios](https://github.com/{{ site.github_username }}/py-words/blob/main/CHANGELOG_es.md) tiene todas las versiones.

<ul class="history">
  <li><span class="when">1.0</span><span>La primera versión pública: <i>WORDS</i> en Python, a partir de su versión en Ada, con sus datos en XML.</span></li>
  <li><span class="when">1.4–1.6</span><span>Los análisis, escritos con las abreviaturas de las <i>Leipzig Glossing Rules</i>; un diálogo de ajustes; las búsquedas, recordadas de una sesión a otra.</span></li>
  <li><span class="when">1.7, 1.8</span><span>La versión de pantalla completa para la terminal (<code>words_tui.py</code>) y la página web (<code>words_web.py</code>).</span></li>
  <li><span class="when">2.0, 2.1</span><span>Significados en otros idiomas además del inglés, y todo el diccionario y la interfaz en español.</span></li>
  <li><span class="when">2.2–2.12</span><span>El modo oscuro; el diccionario en línea; una búsqueda aproximada para las erratas; una ayuda en cada programa; una ventana más clara.</span></li>
  <li><span class="when">2.13–2.15<br>oct. 2026</span><span>Empieza el repositorio. El diccionario, cotejado con Echave-Sustaeta y con la lista medieval de Latham: 44&nbsp;380 entradas.</span></li>
  <li><span class="when">3.0<br>23 oct.</span><span>Las vocales largas, tomadas de Collatinus; más grafías medievales; la licencia pasa a ser la GPL de GNU, versión 3 o posterior.</span></li>
  <li><span class="when">3.2<br>25 oct.</span><span>Entran Lewis y Short y De Miguel: 93&nbsp;370 entradas, con los significados en español reescritos a partir de De Miguel y Echave-Sustaeta.</span></li>
  <li><span class="when">3.5–3.10<br>nov.</span><span>Una AppImage para Linux; la página web en un servidor público, con los ajustes de cada visitante en cookies; un paquete RPM firmado para Fedora.</span></li>
  <li><span class="when">3.17–3.23</span><span>Logeion como segunda fuente, en todos los programas.</span></li>
  <li><span class="when">3.26–3.29</span><span>El manual en inglés, español y latín medieval; un paquete <code>.deb</code>; el idioma de la interfaz en la ventana principal; instaladores para Windows, macOS y Linux.</span></li>
  <li><span class="when">3.30, 3.31<br>22–24 nov.</span><span>Cada archivo de una versión, firmado, con sus sumas de verificación; las maneras de obtener la aplicación de Android.</span></li>
</ul>
