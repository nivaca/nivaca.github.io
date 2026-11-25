---
layout: page
ref: coding
title: Código
permalink: /es/programacion/
description: Programas, scripts y herramientas de programación de Nicolás Vaughan.
---

Escribo programas sobre todo en [Python](https://www.python.org/): herramientas de línea de comandos, programas de escritorio con PySide6 (Qt) y complementos para KDE Plasma. Los scripts de Bash se encargan de las compilaciones y de las tareas menores. Buena parte de mi trabajo con textos se hace en XML: los codifico en [TEI](https://tei-c.org/), escribo personalizaciones ODD con sus esquemas RelaxNG y sus reglas Schematron, consulto los documentos con XPath y los transformo con XSLT, casi siempre a [LaTeX](https://www.latex-project.org/), que compongo con LuaLaTeX. Trabajo en [Emacs](https://www.gnu.org/software/emacs/) y escribo Emacs Lisp (Elisp) para él: mi propia configuración y paquetes como [py-schematron.el](#py-schematron-el). He escrito también algo de TypeScript, para una extensión de VS Code. Mi código está en [GitHub](https://github.com/{{ site.github_username }}) y en [Codeberg](https://codeberg.org/{{ site.codeberg_username }}).

<ul class="projects">
  <li class="project project-featured" id="py-words">
    <p class="feature-label">Proyecto principal</p>
    <h2><a href="https://codeberg.org/{{ site.codeberg_username }}/py-words">py-words: un diccionario latino con morfología</a></h2>
    <p class="project-role">2026 · v3.31 · en <a href="https://codeberg.org/{{ site.codeberg_username }}/py-words">Codeberg</a> y <a href="https://github.com/{{ site.github_username }}/py-words">GitHub</a></p>
    <a class="project-shot" href="{{ "/es/programacion/py-words/" | relative_url }}"><img src="{{ "/images/py-words/gui_es.webp" | relative_url }}" alt="La ventana de py-words en modo oscuro, con las entradas de perspicio" loading="lazy"></a>
    <p><b>py-words</b> es un diccionario latín-inglés-latín y latín-español-latín escrito en Python. Partió de WORDS, de William Whitaker, pero el código y los datos se rediseñaron, y ahora incluye el diccionario inglés de Lewis y Short y los españoles de Echave-Sustaeta y De Miguel. Analiza palabras latinas flexionadas, y líneas enteras de latín, en sus formas y sus entradas de diccionario, con los significados en inglés o en español, y busca el latín de palabras inglesas o españolas. Funciona en una ventana, en la línea de comandos, en la terminal o en el navegador, y solo necesita Python 3.13 o posterior. Funciona también en KRunner, el lanzador de KDE Plasma, y como aplicación de Android, que lleva consigo el diccionario entero y no necesita conexión a internet.</p>
    <p><a class="button button-primary" href="{{ "/py-words/" | relative_url }}"><i class="fas fa-book-open" aria-hidden="true"></i> Pruébelo en el navegador</a>
      <a class="button" href="https://nivaca.pythonanywhere.com/"><i class="fas fa-server" aria-hidden="true"></i> Sitio espejo</a>
      <a class="button" href="{{ "/es/programacion/py-words/" | relative_url }}"><i class="fas fa-info-circle" aria-hidden="true"></i> Más información</a></p>
  </li>

  <li class="project project-featured" id="py-pdftools">
    <p class="feature-label">Proyecto principal</p>
    <h2><a href="https://github.com/{{ site.github_username }}/py-pdftools">py-pdftools: anotar, censurar, foliar e imponer documentos PDF, y leerlos con OCR, en un solo programa</a></h2>
    <p class="project-role">2026 · v1.15.0 · en <a href="https://codeberg.org/{{ site.codeberg_username }}/py-pdftools">Codeberg</a> y <a href="https://github.com/{{ site.github_username }}/py-pdftools">GitHub</a></p>
    <a class="project-shot" href="{{ "/es/programacion/py-pdftools/" | relative_url }}"><img src="{{ "/images/py-pdftools/annotate_es.webp" | relative_url }}" alt="py-pdftools en el modo Anotar" loading="lazy"></a>
    <p><b>py-pdftools</b> edita documentos PDF: los anota y los censura; cambia sus etiquetas de página, encabezados, pies de página, marcas de agua y el orden de sus páginas; los impone para imprimirlos y lee con tesseract el texto de sus páginas escaneadas. Reúne en una sola ventana y una sola línea de comandos siete programas que escribí antes que él (py-annotate, py-redact, py-foliation, py-imposition, py-pdfocr, pdf-word-finder y pdf2iso), y les añade formularios, firmas digitales, contraseñas, marcadores, y la combinación, división y exportación de documentos. Está en inglés y en español, y está escrito en Python con PyMuPDF, pikepdf, reportlab y PySide6; se instala como AppImage para Linux, como paquete de Fedora o de Debian, con instaladores para Linux, macOS y Windows o desde el código fuente con Python 3.14 o posterior.</p>
    <p><a class="button button-primary" href="{{ "/es/programacion/py-pdftools/" | relative_url }}"><i class="fas fa-info-circle" aria-hidden="true"></i> Más información</a></p>
  </li>

  <li class="project">
    <h2><a href="https://github.com/{{ site.github_username }}/py-wk">py-wk: el Wiktionary desde la terminal o el escritorio</a></h2>
    <p class="project-role">2026 · v1.18 · en <a href="https://codeberg.org/{{ site.codeberg_username }}/py-wk">Codeberg</a> y <a href="https://github.com/{{ site.github_username }}/py-wk">GitHub</a></p>
    <p><b>py-wk</b> es una interfaz en Python para consultar palabras en el <a href="https://en.wiktionary.org">Wiktionary inglés</a> sin abrir el navegador. Viene como herramienta de línea de comandos, como interfaz de terminal a pantalla completa y como ventana de escritorio, y las tres comparten el mismo código. Muestra la entrada completa, no solo las definiciones: etimología, pronunciación, ejemplos y citas, notas de uso, tablas de flexión, sinónimos, términos derivados y relacionados, descendientes y traducciones, de todas las lenguas de la página o solo de las que uno elija (solo latín, por ejemplo, o latín y español). También busca en los títulos de las páginas y produce JSON estructurado para otros programas. Solo necesita Python 3.15 o posterior y su biblioteca estándar (más Tkinter para la ventana), y hay además una AppImage autónoma para Linux.</p>
  </li>

  <li class="project">
    <h2><a href="https://github.com/{{ site.github_username }}/krunner-py-wk">krunner-py-wk: el Wiktionary en KRunner</a></h2>
    <p class="project-role">2026 · v1.1 · en <a href="https://codeberg.org/{{ site.codeberg_username }}/krunner-py-wk">Codeberg</a> y <a href="https://github.com/{{ site.github_username }}/krunner-py-wk">GitHub</a></p>
    <p><b>krunner-py-wk</b> lleva <a href="https://github.com/{{ site.github_username }}/py-wk">py-wk</a> a <a href="https://userbase.kde.org/Plasma/Krunner">KRunner</a>, en KDE Plasma 6: al escribir <code>wk</code> y una palabra aparecen sus entradas del Wiktionary, una por cada categoría gramatical en cada lengua, con la línea del lema y las primeras definiciones. Las lenguas se eligen en la propia consulta (<code>wk rosa @la</code> para solo latín), funcionan las expresiones de varias palabras, y una palabra sin página sugiere títulos parecidos. Enter abre la entrada en la ventana de py-wk, y otras acciones copian la entrada completa o la abren en el Wiktionary. Las búsquedas esperan a que uno deje de escribir y corren en un hilo aparte, de modo que KRunner nunca se cuelga; los resultados recientes quedan en caché. Una pequeña ventana de configuración fija el prefijo, las lenguas y el número de resultados y de definiciones. Está escrito en Python y necesita Python 3.14 o posterior, py-wk y la biblioteca de D-Bus para Python.</p>
  </li>

  <li class="project" id="wk">
    <h2><a href="https://github.com/{{ site.github_username }}/wk-android">wk: Wiktionary Reader</a></h2>
    <p class="project-role">2026 · v1.4 · en <a href="https://codeberg.org/{{ site.codeberg_username }}/wk-android">Codeberg</a> y <a href="https://github.com/{{ site.github_username }}/wk-android">GitHub</a></p>
    <p><b>wk: Wiktionary Reader</b> es una pequeña aplicación para leer el <a href="https://en.wiktionary.org">Wiktionary inglés</a> en Android, hermana de <a href="https://github.com/{{ site.github_username }}/py-wk">py-wk</a>. Se escribe una palabra en cualquier lengua, con sugerencias del Wiktionary mientras se escribe, y la aplicación muestra la entrada completa, con los estilos del sitio adaptados al teléfono: las tablas anchas se desplazan horizontalmente dentro de su recuadro, los títulos de las secciones se abren y se cierran al tocarlos, y una barra arriba muestra las lenguas de la página, primero las preferidas y las demás ocultas, pero a un toque. Los enlaces a otras entradas se abren en la aplicación, en la lengua que corresponde, y los demás, en el navegador. Desde cualquier aplicación puede consultarse una palabra: se la selecciona y se elige <i>Buscar en Wiktionary</i>, o se comparte un texto con wk. Las páginas se guardan una semana, así que una palabra ya vista se abre al instante, y la aplicación sigue el modo claro u oscuro del sistema. La interfaz está en inglés y en español. Está escrita en Kotlin, solo con el marco de Android y sin otras bibliotecas (el APK final pesa unos 80 KB), y necesita Android 10 o posterior.</p>
  </li>

  <li class="project">
    <h2><a href="https://github.com/{{ site.github_username }}/krunner-abbr">krunner-abbr: expansor de abreviaturas para KDE Plasma</a></h2>
    <p class="project-role">2026 · v2.0.1 · en <a href="https://codeberg.org/{{ site.codeberg_username }}/krunner-abbr">Codeberg</a> y <a href="https://github.com/{{ site.github_username }}/krunner-abbr">GitHub</a></p>
    <p><b>krunner-abbr</b> es un complemento de <a href="https://userbase.kde.org/Plasma/Krunner">KRunner</a> para Plasma 6, escrito en Python, que expande abreviaturas: se escribe <code>abbr</code> y una abreviatura, se pulsa Enter, y la expansión queda copiada en el portapapeles. Las abreviaturas están en un archivo TOML y admiten marcadores para fechas, el portapapeles, texto escrito, cuadros de diálogo y comandos de shell, con filtros encadenables para limpiar el texto (mayúsculas de título, unir las líneas del texto copiado de un PDF, cambiar las comillas, ordenar). Trae ejemplos para LaTeX y Markdown, para latín (números romanos, macrones) y para obtener el BibTeX de un DOI, y una ventana de configuración con vista previa en vivo. Necesita Python 3.14 o posterior.</p>
  </li>

  <li class="project">
    <h2><a href="https://github.com/{{ site.github_username }}/QuickView">QuickView: vista rápida de archivos para KDE Plasma</a></h2>
    <p class="project-role">2026 · v1.0.4 · en <a href="https://codeberg.org/{{ site.codeberg_username }}/QuickView">Codeberg</a> y <a href="https://github.com/{{ site.github_username }}/QuickView">GitHub</a></p>
    <p><b>QuickView</b> es una bifurcación reelaborada del <a href="https://github.com/MustaphaAlioglou/QuickView">QuickView de Mustapha Alioglou</a>, un visor de vista rápida para KDE Plasma 6, al estilo de Quick Look en macOS: se selecciona un archivo en Dolphin, se pulsa la barra espaciadora y aparece un panel flotante con la vista previa; las flechas recorren la carpeta o pasan por los archivos de una selección múltiple. Muestra imágenes, PDF (con búsqueda y una barra lateral con el índice), libros EPUB compuestos en páginas, Markdown renderizado, código fuente con resaltado de sintaxis, HTML, audio y video, el contenido de archivos comprimidos, hojas de cálculo con su cuadrícula y documentos de oficina compuestos en páginas mediante LibreOffice. Un demonio residente hace que el panel aparezca en unos 20 ms, y cada analizador corre en un entorno aislado de bubblewrap, sin acceso a la red ni al sistema de archivos. La bifurcación añade compatibilidad con el LibreOffice de Flathub, corrige un fallo que podía dejar el panel colgado, divide el demonio en módulos más pequeños y hace más seguro el instalador. Está escrito en Python con PySide6 y necesita Python 3.15 o posterior y bubblewrap.</p>
  </li>

  <li class="project" id="py-slowdown">
    <h2><a href="https://github.com/{{ site.github_username }}/py-slowdown">py-slowdown: reproducir música más lenta o más rápida sin cambiarle la altura</a></h2>
    <p class="project-role">2026 · v1.3.1 · en <a href="https://codeberg.org/{{ site.codeberg_username }}/py-slowdown">Codeberg</a> y <a href="https://github.com/{{ site.github_username }}/py-slowdown">GitHub</a></p>
    <p><b>py-slowdown</b> reproduce audio más lento o más rápido sin cambiarle la altura. Está hecho para la música: para practicar una pieza y sacarla de oído, oyendo un pasaje una y otra vez a una velocidad que se pueda seguir. Abre archivos de audio y el sonido de archivos de video y los muestra como forma de onda, con marcadores. La velocidad va de 0,25× a 3× y se cambia mientras suena; el estiramiento lo hace la biblioteca Rubber Band. La altura se mueve en semitonos y cents. Una selección se repite sin cortes y puede guardarse como bucle; puede dejar oír una parte de la mezcla (un canal, la mezcla sin su centro, los graves), contar antes de tocar como un metrónomo y exportar lo que se oye. De cada archivo recuerda cómo se tocó, también en un archivo <code>.slx</code> que viaja con la grabación. Está en inglés y en español, escrito en Python con PySide6, PyAV y NumPy, y viene con instaladores para Windows, macOS y Linux, como AppImage, como paquete de Fedora o de Debian, o desde el código fuente con Python 3.14 o posterior. Slowdown, su versión para Android, abre los mismos archivos <code>.slx</code> en el teléfono.</p>
    <p><a class="button button-primary" href="{{ "/es/programacion/py-slowdown/" | relative_url }}"><i class="fas fa-info-circle" aria-hidden="true"></i> Más información</a></p>
  </li>

  <li class="project" id="py-schematron">
    <h2><a href="https://github.com/{{ site.github_username }}/py-schematron">py-schematron: validación Schematron de TEI-XML desde la terminal</a></h2>
    <p class="project-role">2026 · v2.7 · en <a href="https://codeberg.org/{{ site.codeberg_username }}/py-schematron">Codeberg</a> y <a href="https://github.com/{{ site.github_username }}/py-schematron">GitHub</a></p>
    <p><b>py-schematron</b> es un script de Python que valida documentos TEI-XML contra las reglas Schematron incluidas en un ODD (o en un <code>.sch</code> ya extraído, o recogidas de un esquema RelaxNG generado a partir de un ODD, que son las reglas que Jing ignora), y las ejecuta con Saxon. A diferencia de oXygen, que se detiene sin avisar al llegar a cien errores, informa de todas las infracciones, con el recuento por regla y, si se le pide, el número de línea y el <code>xml:id</code> de cada elemento infractor, y dice exactamente cuántas omitió cuando la lista tiene un tope. Devuelve un código de salida distinto de cero si hay infracciones, de modo que puede usarse en un Makefile o en un hook de pre-commit. Necesita Python 3.15 o posterior, <code>saxonche</code> y <code>lxml</code>.</p>
    <p class="continued">También encuentra por su cuenta el esquema a partir de las declaraciones <code>&lt;?xml-model?&gt;</code> del documento, y un script de shell que lo acompaña, <code>py-schematron-all.sh</code>, añade la validación estructural contra RelaxNG con jing y da un solo veredicto para las dos validaciones. Su informe en JSON alimenta los dos complementos para editores descritos más abajo, cada uno en su propio repositorio: la extensión <a href="#schematron-validator">Schematron Validator</a> para VS Code y [py-schematron.el](#py-schematron-el) para Emacs.</p>
  </li>

  <li class="project" id="schematron-validator">
    <h2><a href="https://marketplace.visualstudio.com/items?itemName=NicolasVaughan.validate-schematron">Schematron Validator: validación de TEI-XML mientras se escribe en VS Code</a></h2>
    <p class="project-role">2026 · v0.12.0 · en el <a href="https://marketplace.visualstudio.com/items?itemName=NicolasVaughan.validate-schematron">Visual Studio Marketplace</a> · código fuente en <a href="https://codeberg.org/{{ site.codeberg_username }}/py-schematron-vscode">Codeberg</a> y <a href="https://github.com/{{ site.github_username }}/py-schematron-vscode">GitHub</a></p>
    <p><b>Schematron Validator</b> es una extensión de VS Code que lleva <a href="#py-schematron">py-schematron</a> al editor. Valida archivos XML y TEI contra reglas Schematron (de un <code>.sch</code>, de un ODD o de un esquema RelaxNG con reglas incluidas) mientras se escribe, al abrir y al guardar, incluidos los cambios sin guardar. Cada infracción queda subrayada en el elemento culpable y aparece en el panel de problemas, con la gravedad que indica el <code>role</code> de la regla. Si el esquema es RelaxNG y <a href="https://relaxng.org/jclark/jing.html">jing</a> está instalado, se añaden también los errores estructurales, y el XML mal formado se señala donde se abrió la etiqueta rota. El esquema se toma de la declaración <code>&lt;?xml-model?&gt;</code> del documento o se fija en la configuración; un indicador en la barra de estado muestra si el archivo está limpio, y hay comandos para elegir el intérprete de Python o volver a descargar un esquema que cambió en su origen. El script viene incluido; la extensión necesita Python 3.15 o posterior con <code>saxonche</code> y <code>lxml</code>, y su página explica paso a paso cómo instalarlos.</p>
    <p><a class="button button-primary" href="https://marketplace.visualstudio.com/items?itemName=NicolasVaughan.validate-schematron"><i class="fas fa-download" aria-hidden="true"></i> Instalar desde el Marketplace</a></p>
  </li>

  <li class="project" id="py-schematron-el">
    <h2><a href="https://github.com/{{ site.github_username }}/py-schematron.el">py-schematron.el: validación de TEI-XML en Emacs mientras se escribe, con Flycheck o Flymake</a></h2>
    <p class="project-role">2026 · v1.0.2 · en <a href="https://codeberg.org/{{ site.codeberg_username }}/py-schematron.el">Codeberg</a> y <a href="https://github.com/{{ site.github_username }}/py-schematron.el">GitHub</a></p>
    <p><b>py-schematron.el</b> es un paquete de Emacs que lleva <a href="#py-schematron">py-schematron</a> al editor, con Flycheck si está instalado o, si no, con Flymake, que viene con Emacs. Valida mientras se escribe, al abrir y al guardar, todo buffer que tenga una declaración <code>&lt;?xml-model?&gt;</code>; los cambios sin guardar se validan en una copia temporal privada, así que el archivo en disco nunca se modifica. Cada problema queda subrayado, con su mensaje cuando el cursor está encima y la capa que lo detectó (Schematron, RelaxNG o, si el documento está mal formado, XML), y la línea de modo muestra los recuentos; un comando muestra el informe completo del archivo, en texto, con cada línea enlazada al documento. Si el esquema es RelaxNG, valida también la estructura con <a href="https://relaxng.org/jclark/jing.html">jing</a> y le pasa el esquema, convertido con trang, a nxml-mode, para que el autocompletado ofrezca los elementos y atributos que el esquema admite en la posición del cursor. Como las reglas de un esquema pueden leer archivos y acceder a URL, solo valida los documentos que figuran en <code>trusted-content</code>, la lista de contenido de confianza de Emacs. Necesita Emacs 31 o posterior y Python 3.15 o posterior con <code>saxonche</code> y <code>lxml</code>; jing y trang son opcionales.</p>
  </li>

  <li class="project" id="odd2rng">
    <h2><a href="https://github.com/{{ site.github_username }}/ODD2RNG">ODD2RNG: esquemas RELAX NG a partir de ODD de TEI, desde la línea de comandos</a></h2>
    <p class="project-role">2026 · v1.3 · en <a href="https://codeberg.org/{{ site.codeberg_username }}/ODD2RNG">Codeberg</a> y <a href="https://github.com/{{ site.github_username }}/ODD2RNG">GitHub</a></p>
    <p><b>ODD2RNG</b> convierte un ODD de TEI en su esquema RELAX NG sin abrir oXygen. Ejecuta las mismas dos transformaciones de las TEI Stylesheets, con los mismos parámetros, que el escenario <i>TEI ODD to RELAX NG XML</i> de oXygen, de modo que el esquema que escribe es idéntico al de oXygen salvo por la fecha de generación en el comentario de cabecera (se comprobó con el ODD del proyecto SMTrad). Por defecto escribe <code>out/NOMBRE.rng</code> junto al ODD, como oXygen, y solo reemplaza el esquema anterior cuando el nuevo está completo, para que ningún editor ni validador lo lea a medio escribir; su última línea dice si el esquema es nuevo, si cambió o si quedó igual salvo por la fecha, es decir, si hay algo que valga la pena registrar en git. Las TEI Stylesheets y la fuente de TEI (<code>p5subset.xml</code>) pueden venir de un clon del repositorio de TEI o de la copia que trae oXygen; sus ubicaciones se guardan en un archivo de configuración, y un instalador pone el comando en el PATH. Necesita Python 3.15 o posterior con <code>saxonche</code>.</p>
  </li>
</ul>

## Otros programas

<ol class="publications">
  {% for pub in site.data.software %}
    {% include publication.html pub=pub %}
  {% endfor %}
</ol>

## Las herramientas que uso

En mis computadores uso únicamente [GNU/Linux](https://es.wikipedia.org/wiki/Controversia_por_la_denominaci%C3%B3n_GNU/Linux).
Ahora estoy, muy a gusto, en la distribución [Fedora Linux](https://fedoraproject.org/) (versión 45), con el escritorio [KDE Plasma](https://kde.org/plasma-desktop/) 6.
Durante muchos años usé [Manjaro Linux](https://manjaro.org/) y también [Arch Linux](https://archlinux.org/) a secas, pero me parecieron bastante inestables y difíciles para el trabajo diario.

Mi editor de cabecera, para escribir y para programar, es [GNU Emacs](https://www.gnu.org/s/emacs/) (versión 31), que configuro en Emacs Lisp. En él llevo mis notas con [Org mode](https://orgmode.org/) y [Org-roam](https://www.orgroam.com/), escribo LaTeX con [AUCTeX](https://www.gnu.org/software/auctex/) y RefTeX, trabajo con Git mediante [Magit](https://magit.vc/) y edito TEI con nxml-mode y mi propio [py-schematron.el](#py-schematron-el).
Para proyectos en TEI, personalizaciones ODD y XSLT uso también [Oxygen XML Editor](https://www.oxygenxml.com/).
Para cambios rápidos uso Vim o Sublime Text, y [Visual Studio Code](https://code.visualstudio.com/) sobre todo para probar mi extensión [Schematron Validator](#schematron-validator).

En la terminal uso [Ghostty](https://ghostty.org/) con el shell [fish](https://fishshell.com/) y tmux, y algunas herramientas de línea de comandos: ripgrep y fd para buscar, fzf, bat, eza, zoxide, atuin para el historial del shell y delta para leer diffs.

Para Python uso [uv](https://docs.astral.sh/uv/), que se ocupa de las versiones de Python, los entornos y las dependencias; para las pruebas, pytest.
Empaqueto mis programas como RPM para Fedora (los construyo con rpmbuild y los publico en [Copr](https://copr.fedorainfracloud.org/)) y como AppImage para las demás distribuciones.
El código está en [Codeberg](https://codeberg.org/{{ site.codeberg_username }}) y en [GitHub](https://github.com/{{ site.github_username }}), que manejo desde la terminal con tea y gh.
Uso [Claude Code](https://claude.com/product/claude-code) para probar y publicar código.

Fuera del editor, ejecuto transformaciones XSLT y consultas XPath con [Saxon](https://www.saxonica.com/), y valido y convierto esquemas RELAX NG con [Jing](https://relaxng.org/jclark/jing.html) y [Trang](https://relaxng.org/jclark/trang.html).
Compongo mis textos con LuaLaTeX, de [TeX Live](https://tug.org/texlive/), y uso Biber para las bibliografías, que guardo en [Zotero](https://www.zotero.org/) con la extensión Better BibTeX; [Pandoc](https://pandoc.org/) se encarga de convertir entre los demás formatos.

Hice este sitio con [Jekyll](https://jekyllrb.com), un generador de sitios estáticos; el diseño partió de un tema de [S.V. Miller](https://svmiller.com/).
Su código fuente está [en GitHub](https://github.com/{{ site.github_username }}/nivaca.github.io).
