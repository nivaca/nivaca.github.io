---
layout: page
ref: py-pdftools
title: py-pdftools
subtitle: Anotar, censurar, foliar e imponer documentos PDF, y leerlos con OCR, en un solo programa
permalink: /es/programacion/py-pdftools/
description: py-pdftools, un programa de Nicolás Vaughan para anotar, censurar, foliar e imponer documentos PDF y leerlos con OCR, con sus modos, su línea de comandos, cómo instalarlo y sus versiones.
---

py-pdftools edita documentos PDF. Los anota y los censura, cambia sus etiquetas de página, encabezados, pies de página, marcas de agua y el orden de sus páginas, los impone para imprenta y lee el texto de sus páginas escaneadas. Tiene una ventana y una línea de comandos, ambas en inglés y en español, y funciona en Linux, Windows y macOS.

<div class="buttons">
  <a class="button button-primary" href="https://codeberg.org/{{ site.codeberg_username }}/py-pdftools/releases"><i class="fas fa-download" aria-hidden="true"></i> Descargas</a>
  <a class="button" href="https://github.com/{{ site.github_username }}/py-pdftools/blob/main/docs/MANUAL_es.pdf"><i class="fas fa-file-pdf" aria-hidden="true"></i> Manual</a>
</div>

<dl class="facts">
  <dt>Versión</dt><dd>1.19.0 (25 de noviembre de 2026)</dd>
  <dt>Programas</dt><dd>una ventana (<code>py-pdftools-gui</code>) y una línea de comandos (<code>py-pdftools</code>)</dd>
  <dt>Interfaz</dt><dd>inglés y español</dd>
  <dt>Escrito en</dt><dd>Python, con PyMuPDF, pikepdf, reportlab y PySide6 (Qt)</dd>
  <dt>Requisitos</dt><dd>Python 3.14 o posterior (la AppImage, los instaladores para Windows y macOS y los paquetes traen lo que necesitan); Ghostscript para PDF/A y PDF/X, tesseract para el OCR, pyHanko para las firmas digitales</dd>
  <dt>Licencia</dt><dd>Licencia Pública General de GNU, versión 3 o posterior</dd>
  <dt>Código</dt><dd><a href="https://codeberg.org/{{ site.codeberg_username }}/py-pdftools">Codeberg</a> y <a href="https://github.com/{{ site.github_username }}/py-pdftools">GitHub</a></dd>
</dl>

## De dónde viene

py-pdftools nació de seis programas que escribí antes, cada uno para un tipo de trabajo con documentos PDF. Habían crecido uno al lado del otro y compartían mucho: la traducción de la interfaz, la configuración, la conversión a PDF/A y PDF/X, el empaquetado. Un mismo documento, por lo demás, solía pasar por varios de ellos: se anotaba, luego se censuraba, luego recibía sus etiquetas de página y por último se imponía para imprenta. Así que los reuní en noviembre de 2026. Su código se copió en py-pdftools, que no necesita tenerlos instalados; cada uno sigue como estaba, con su propio repositorio.

| Programa | Lo que llegó a ser en py-pdftools |
|---|---|
| [py-annotate](https://github.com/{{ site.github_username }}/py-annotate) | el modo Anotar, y la ventana misma: sus páginas, miniaturas y paneles |
| [py-redact](https://github.com/{{ site.github_username }}/py-redact) | el modo Censurar |
| [py-foliation](https://github.com/{{ site.github_username }}/py-foliation) | el modo Foliar, y los comandos `labels`, `view`, `header-footer`, `watermark` y `pages` |
| [py-imposition](https://github.com/{{ site.github_username }}/py-imposition) | el modo Imponer, y los comandos que van bajo `impose` |
| [py-pdfocr](https://github.com/{{ site.github_username }}/py-pdfocr) | el modo OCR, y el comando `ocr` |
| [pdf-word-finder](https://github.com/{{ site.github_username }}/pdf-word-finder) | Herramientas > Índice de palabras, y el comando `find-words` |

Un séptimo, [pdf2iso](https://github.com/{{ site.github_username }}/pdf2iso), entró entero: hace las copias en PDF/A y PDF/X, y ya no se instala aparte. Los documentos hechos con los programas anteriores se leen como antes.

## Los modos

Una barra en la parte de arriba de la ventana (o Ctrl+1 a Ctrl+6) elige qué hace la ventana. Cada modo guarda su propia disposición de barras de herramientas y paneles, también para la próxima vez que se abra el programa, y hay un solo historial para todos: Deshacer recorre todo lo que se le hizo al documento, en cualquier modo.

- **Leer**: las páginas y sus miniaturas, con las herramientas para buscar, recorrer las páginas y cambiar el tamaño.
- **OCR**: tesseract lee el texto de las páginas escaneadas, y ese texto se escribe en el documento, invisible, bajo las imágenes de las páginas, para que se pueda buscar, copiar y marcar. Las palabras de las que tesseract no estuvo seguro se muestran junto a sus imágenes, para corregirlas antes. Las páginas escaneadas de lado o al revés pueden girarse, y los modelos más precisos de tesseract se descargan desde el propio programa.
- **Censurar**: recuadros sobre lo que debe quitarse, dibujados a mano, puestos sobre un texto o hallados con una búsqueda, con códigos de censura. Se guardan como las marcas de censura del propio PDF, y nada se quita hasta que se escribe la copia censurada: un archivo nuevo, nunca el que está abierto, en el que se comprueba que bajo ningún recuadro quede texto legible. Buscar texto cubierto encuentra el texto que solo parece censurado y sigue en el archivo bajo un recuadro negro o una imagen.
- **Anotar**: resaltados, notas, cuadros de texto, formas, dibujos, enlaces y sellos (los estándar, y sellos propios hechos de una imagen o de una página), escritos como anotaciones PDF corrientes, con un panel que las lista, las busca, las filtra y las ordena.
- **Foliar**: etiquetas de página (números romanos, folios, prefijos), encabezados y pies de página con números Bates, marcas de agua, la vista al abrir el documento y el orden de las páginas, y todo se ve en cuanto se hace.
- **Imponer**: folletos, n-up, paso y repetición, sangrados y marcas de corte, secuencias y carpetas vigiladas, con una vista previa antes de guardarlos o aplicarlos.

<figure class="screenshot">
  <img src="{{ "/images/py-pdftools/annotate_es.webp" | relative_url }}" alt="py-pdftools en el modo Anotar" loading="lazy">
  <figcaption>El modo Anotar.</figcaption>
</figure>

<figure class="screenshot">
  <img src="{{ "/images/py-pdftools/redact_es.webp" | relative_url }}" alt="py-pdftools en el modo Censurar, con un recuadro sobre un renglón" loading="lazy">
  <figcaption>El modo Censurar: un recuadro sobre un renglón, que va en todas las páginas desde la segunda.</figcaption>
</figure>

<figure class="screenshot">
  <img src="{{ "/images/py-pdftools/pages_es.webp" | relative_url }}" alt="py-pdftools en el modo Foliar, con los intervalos de etiquetas de página" loading="lazy">
  <figcaption>El modo Foliar: la portada sin etiqueta, luego 1, 2, 3, y la etiqueta en el pie de página.</figcaption>
</figure>

<figure class="screenshot">
  <img src="{{ "/images/py-pdftools/impose_es.webp" | relative_url }}" alt="py-pdftools en el modo Imponer, haciendo un folleto" loading="lazy">
  <figcaption>El modo Imponer: un folleto.</figcaption>
</figure>

## Más allá de los seis programas

py-pdftools hace también muchas cosas que no hacía ninguno de los programas anteriores:

- rellena formularios, con sus números y fechas comprobados y sus sumas calculadas sin JavaScript, y exporta e importa sus valores (JSON, CSV, XFDF, FDF);
- firma documentos con un ID digital, de forma visible o no, y comprueba sus firmas: si cada una está intacta y es válida, quién firmó y qué cambió después;
- protege documentos con contraseñas, cifrados con AES-256;
- edita marcadores y enlaces, y lista, abre y añade archivos adjuntos;
- combina archivos, o algunas de sus páginas, hace PDF de imágenes, divide documentos (cada tantas páginas, en sus marcadores o por tamaño) y ordena las páginas en una cuadrícula de miniaturas grandes;
- exporta las páginas como imágenes, las imágenes del documento o su texto (Markdown, HTML o texto simple), y hace copias más pequeñas o copias como otra versión de PDF;
- compara dos PDF página por página, y aplica los mismos pasos (OCR, un encabezado, una marca de agua, un tamaño menor, PDF/A) a muchos archivos a la vez;
- encuentra las páginas en que aparece cada palabra de una lista, según sus etiquetas, en renglones listos para el índice de un libro.

La ventana abre los documentos en pestañas, puede mostrar dos lado a lado y tiene una búsqueda rápida que encuentra a cada letra que se escribe. Puede seguir funcionando en segundo plano, con un icono en la bandeja, para que los documentos se abran al instante.

## La línea de comandos

Los comandos van por grupos, y `py-pdftools COMANDO -h` explica cada uno:

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

`py-pdftools pdf2iso` es la línea de comandos propia de pdf2iso, y `py-pdftools completion bash|fish|zsh` escribe un script de completado para el shell.

## Instalación

Cada versión se publica en [Codeberg](https://codeberg.org/{{ site.codeberg_username }}/py-pdftools/releases) y en [GitHub](https://github.com/{{ site.github_username }}/py-pdftools/releases). Cada archivo y cada etiqueta de git están firmados con la misma clave, y cada versión trae las sumas de verificación de sus archivos.

| Sistema | Cómo |
|---|---|
| Windows 10 o posterior | un instalador (`.exe`), para un usuario o para todos |
| macOS 15 o posterior, Apple silicon | una imagen de disco (`.dmg`) |
| Fedora 45 y posteriores | `sudo dnf copr enable nivaca/py-pdftools` y luego `sudo dnf install py-pdftools` |
| Debian 12, Ubuntu 22.04 y posteriores | el `.deb` de una versión, o mi repositorio APT firmado, [github.com/nivaca/apt](https://github.com/{{ site.github_username }}/apt) |
| Cualquier Linux | la AppImage, que trae su propio Python, Qt y bibliotecas |
| Linux, macOS, Windows | los scripts de instalación del código fuente (`install/install.sh`, `install\install.bat`), con Python 3.14 o posterior |
| Desde el código fuente | `uv run py-pdftools-gui`, con [uv](https://docs.astral.sh/uv/) |

## Documentación

- El manual de usuario, en PDF, con imágenes de la ventana y de sus diálogos: [español](https://github.com/{{ site.github_username }}/py-pdftools/blob/main/docs/MANUAL_es.pdf), [inglés](https://github.com/{{ site.github_username }}/py-pdftools/blob/main/docs/MANUAL_en.pdf).
- El README: [español](https://github.com/{{ site.github_username }}/py-pdftools/blob/main/README_es.md), [inglés](https://github.com/{{ site.github_username }}/py-pdftools/blob/main/README.md).
- La [descripción de py-pdftools](https://github.com/{{ site.github_username }}/py-pdftools/blob/main/docs/DESCRIPCI%C3%93N_es.md) y el [registro de cambios](https://github.com/{{ site.github_username }}/py-pdftools/blob/main/CHANGELOG_es.md).

## Versiones

py-pdftools es joven: su primera versión salió el 19 de noviembre de 2026. Siguen los pasos principales desde entonces; el [registro de cambios](https://github.com/{{ site.github_username }}/py-pdftools/blob/main/CHANGELOG_es.md) tiene todas las versiones.

<ul class="history">
  <li><span class="when">0.1.0<br>19 nov.</span><span>py-annotate, py-redact, py-foliation y py-imposition en una sola ventana y una sola línea de comandos, en inglés y en español.</span></li>
  <li><span class="when">0.2.0</span><span>Cinco modos, en el orden del trabajo sobre un documento (Leer, Censurar, Anotar, Foliar, Imponer), cada uno con su propia disposición de la ventana; entra pdf2iso.</span></li>
  <li><span class="when">0.4.0–1.0.0<br>20 nov.</span><span>El OCR, tomado de py-pdfocr, y luego el modo OCR; la selección de texto; el funcionamiento en segundo plano.</span></li>
  <li><span class="when">1.1.0–1.4.0<br>20 nov.</span><span>Marcadores, enlaces, pestañas y una vista dividida; la búsqueda de texto cubierto; contraseñas; la combinación de archivos y los PDF de imágenes; copias más pequeñas, formularios y firmas digitales.</span></li>
  <li><span class="when">1.5.0–1.7.0<br>21 nov.</span><span>Los menús, por grupos; un arranque más rápido, con el programa iniciado junto con la sesión; la navegación por las páginas y las propiedades de un documento.</span></li>
  <li><span class="when">1.8.0</span><span>El índice de palabras, tomado de pdf-word-finder: el sexto programa.</span></li>
  <li><span class="when">1.10.0–1.12.0<br>23 nov.</span><span>Archivos adjuntos; un menú Herramientas, con el clasificador de páginas, los pasos aplicados a varios archivos y el historial de cambios; sellos propios; la búsqueda mientras se escribe.</span></li>
  <li><span class="when">1.13.0</span><span>Un menú Buscar, con todas las búsquedas, en todos los modos.</span></li>
  <li><span class="when">1.14.0<br>24 nov.</span><span>La firma digital, en tres pasos sencillos, con un ID digital creado en el mismo diálogo si no hay ninguno.</span></li>
  <li><span class="when">1.15.0<br>24 nov.</span><span>Todas las búsquedas, tan rápidas como la búsqueda mientras se escribe: cada página se lee una sola vez, en un único índice del documento.</span></li>
  <li><span class="when">1.16.0<br>25 nov.</span><span>Instaladores para Windows y macOS que no necesitan nada más; el menú Anotar en submenús; una señal para los comentarios; anotaciones legibles en páginas escaneadas grandes.</span></li>
  <li><span class="when">1.17.0–1.19.0<br>25 nov.</span><span>Copias con las páginas como imágenes; Cerrar el documento (Ctrl+W) cierra el documento y no el programa; copias más pequeñas que conservan todos los colores; la lectura en voz alta, con la voz del sistema; cuatro temas de color más y la elección de los iconos.</span></li>
</ul>
