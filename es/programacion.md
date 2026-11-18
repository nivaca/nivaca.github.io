---
layout: page
ref: coding
title: Código
permalink: /es/programacion/
description: Programas, scripts y herramientas de programación de Nicolás Vaughan.
---

Escribo programas sobre todo en [Python](https://www.python.org/), y también en XML/TEI y en [LaTeX](https://www.latex-project.org/). Mi código está en [GitHub](https://github.com/{{ site.github_username }}) y en [Codeberg](https://codeberg.org/{{ site.codeberg_username }}).

<ul class="projects">
  <li class="project">
    <h2><a href="https://codeberg.org/{{ site.codeberg_username }}/py-words">py-words: un diccionario latino con morfología</a></h2>
    <p class="project-role">2026 · v3.20 · en <a href="https://codeberg.org/{{ site.codeberg_username }}/py-words">Codeberg</a> y <a href="https://github.com/{{ site.github_username }}/py-words">GitHub</a></p>
    <p><b>py-words</b> es un diccionario latín-inglés-latín y latín-español-latín escrito en Python. Partió de WORDS, de William Whitaker, pero el código y los datos se rediseñaron, y ahora incluye el diccionario inglés de Lewis y Short y los españoles de Echave-Sustaeta y De Miguel. Analiza palabras latinas flexionadas, y líneas enteras de latín, en sus formas y sus entradas de diccionario, con los significados en inglés o en español, y busca el latín de palabras inglesas o españolas. Funciona en una ventana, en la línea de comandos, en la terminal o en el navegador, y solo necesita Python 3.13 o posterior.</p>
    <p><a class="button button-primary" href="{{ "/py-words/" | relative_url }}"><i class="fas fa-book-open" aria-hidden="true"></i> Pruébelo en el navegador</a></p>
  </li>

  <li class="project">
    <h2><a href="https://github.com/{{ site.github_username }}/krunner-py-words">krunner-py-words: py-words en KRunner</a></h2>
    <p class="project-role">2026 · v1.1.1 · en <a href="https://codeberg.org/{{ site.codeberg_username }}/krunner-py-words">Codeberg</a> y <a href="https://github.com/{{ site.github_username }}/krunner-py-words">GitHub</a></p>
    <p><b>krunner-py-words</b> lleva py-words a <a href="https://userbase.kde.org/Plasma/Krunner">KRunner</a>, en KDE Plasma 6: basta escribir <code>pw</code> y una palabra latina, o una línea entera de latín, para que sus entradas aparezcan mientras se escribe, cada una con su forma de diccionario, su significado y las formas analizadas (<code>amīc-ōrum GEN.PL</code>). Con <code>pw ~e</code> va en sentido contrario, de una palabra inglesa o española al latín. Enter abre la búsqueda en la ventana de py-words, y otras acciones copian los resultados de una entrada o abren la búsqueda en el diccionario en línea. Los resultados siguen la configuración de py-words; una pequeña ventana de configuración propia fija el prefijo, el idioma de los significados y de la interfaz, y el número de resultados. El programa se queda en memoria con el diccionario cargado, así que cada consulta es rápida. Está escrito en Python con la biblioteca de D-Bus, y se instala como paquete de Fedora en Copr, que trae py-words consigo, o desde el código fuente con Python 3.14 o posterior.</p>
  </li>

  <li class="project">
    <h2><a href="https://github.com/{{ site.github_username }}/py-wtk">py-wtk: el Wiktionary desde la terminal o el escritorio</a></h2>
    <p class="project-role">2026 · v1.13 · en <a href="https://codeberg.org/{{ site.codeberg_username }}/py-wtk">Codeberg</a> y <a href="https://github.com/{{ site.github_username }}/py-wtk">GitHub</a></p>
    <p><b>py-wtk</b> es una interfaz en Python para consultar palabras en el <a href="https://en.wiktionary.org">Wiktionary inglés</a> sin abrir el navegador. Viene como herramienta de línea de comandos, como interfaz de terminal a pantalla completa y como ventana de escritorio, y las tres comparten el mismo código. Muestra la entrada completa, no solo las definiciones: etimología, pronunciación, ejemplos y citas, notas de uso, tablas de flexión, sinónimos, términos derivados y relacionados, descendientes y traducciones, de todas las lenguas de la página o solo de las que uno elija (solo latín, por ejemplo, o latín y español). También busca en los títulos de las páginas y produce JSON estructurado para otros programas. Solo necesita Python 3.15 o posterior y su biblioteca estándar (más Tkinter para la ventana), y hay además una AppImage autónoma para Linux.</p>
  </li>

  <li class="project">
    <h2><a href="https://github.com/{{ site.github_username }}/krunner-py-wtk">krunner-py-wtk: el Wiktionary en KRunner</a></h2>
    <p class="project-role">2026 · v1.0.1 · en <a href="https://codeberg.org/{{ site.codeberg_username }}/krunner-py-wtk">Codeberg</a> y <a href="https://github.com/{{ site.github_username }}/krunner-py-wtk">GitHub</a></p>
    <p><b>krunner-py-wtk</b> lleva <a href="https://github.com/{{ site.github_username }}/py-wtk">py-wtk</a> a <a href="https://userbase.kde.org/Plasma/Krunner">KRunner</a>, en KDE Plasma 6: al escribir <code>wtk</code> y una palabra aparecen sus entradas del Wiktionary, una por cada categoría gramatical en cada lengua, con la línea del lema y las primeras definiciones. Las lenguas se eligen en la propia consulta (<code>wtk rosa @la</code> para solo latín), funcionan las expresiones de varias palabras, y una palabra sin página sugiere títulos parecidos. Enter abre la entrada en la ventana de py-wtk, y otras acciones copian la entrada completa o la abren en el Wiktionary. Las búsquedas esperan a que uno deje de escribir y corren en un hilo aparte, de modo que KRunner nunca se cuelga; los resultados recientes quedan en caché. Una pequeña ventana de configuración fija el prefijo, las lenguas y el número de resultados y de definiciones. Está escrito en Python y necesita Python 3.14 o posterior, py-wtk y la biblioteca de D-Bus para Python.</p>
  </li>

  <li class="project">
    <h2><a href="https://github.com/{{ site.github_username }}/krunner-abbr">krunner-abbr: expansor de abreviaturas para KDE Plasma</a></h2>
    <p class="project-role">2026 · v2.0.1 · en <a href="https://codeberg.org/{{ site.codeberg_username }}/krunner-abbr">Codeberg</a> y <a href="https://github.com/{{ site.github_username }}/krunner-abbr">GitHub</a></p>
    <p><b>krunner-abbr</b> es un complemento de <a href="https://userbase.kde.org/Plasma/Krunner">KRunner</a> para Plasma 6, escrito en Python, que expande abreviaturas: se escribe <code>abbr</code> y una abreviatura, se pulsa Enter, y la expansión queda copiada en el portapapeles. Las abreviaturas están en un archivo TOML y admiten marcadores para fechas, el portapapeles, texto escrito, cuadros de diálogo y comandos de shell, con filtros encadenables para limpiar el texto (mayúsculas de título, unir las líneas del texto copiado de un PDF, cambiar las comillas, ordenar). Trae ejemplos para LaTeX y Markdown, para latín (números romanos, macrones) y para obtener el BibTeX de un DOI, y una ventana de configuración con vista previa en vivo. Necesita Python 3.14 o posterior.</p>
  </li>

  <li class="project">
    <h2><a href="https://github.com/{{ site.github_username }}/QuickView">QuickView: vista rápida de archivos para KDE Plasma</a></h2>
    <p class="project-role">2026 · v0.2.5 · en <a href="https://github.com/{{ site.github_username }}/QuickView">GitHub</a></p>
    <p><b>QuickView</b> es una bifurcación reelaborada del <a href="https://github.com/MustaphaAlioglou/QuickView">QuickView de Mustapha Alioglou</a>, un visor de vista rápida para KDE Plasma 6, al estilo de Quick Look en macOS: se selecciona un archivo en Dolphin, se pulsa la barra espaciadora y aparece un panel flotante con la vista previa; las flechas recorren la carpeta o pasan por los archivos de una selección múltiple. Muestra imágenes, PDF (con búsqueda y una barra lateral con el índice), libros EPUB compuestos en páginas, Markdown renderizado, código fuente con resaltado de sintaxis, HTML, audio y video, el contenido de archivos comprimidos, hojas de cálculo con su cuadrícula y documentos de oficina compuestos en páginas mediante LibreOffice. Un demonio residente hace que el panel aparezca en unos 20 ms, y cada analizador corre en un entorno aislado de bubblewrap, sin acceso a la red ni al sistema de archivos. La bifurcación añade compatibilidad con el LibreOffice de Flathub, corrige un fallo que podía dejar el panel colgado, divide el demonio en módulos más pequeños y hace más seguro el instalador. Está escrito en Python con PySide6 y necesita Python 3.15 o posterior y bubblewrap.</p>
  </li>

  <li class="project">
    <h2><a href="https://github.com/{{ site.github_username }}/py-imposition">py-imposition: imposición de PDF desde la línea de comandos</a></h2>
    <p class="project-role">2026 · v0.9 · en <a href="https://codeberg.org/{{ site.codeberg_username }}/py-imposition">Codeberg</a> y <a href="https://github.com/{{ site.github_username }}/py-imposition">GitHub</a></p>
    <p><b>py-imposition</b> prepara archivos PDF para la impresión y la encuadernación desde la línea de comandos. Hace cuadernillos (encuadernación americana, grapada o de corte y apilado, con compensación del desplazamiento y encuadernación de derecha a izquierda), pliegos con varias páginas por cara y montajes repetidos, y puede reordenar, recortar, desplazar y escalar páginas, añadir sangrado, marcas de corte y de plegado, números de página y sellos, combinar datos variables, y dividir o unir documentos. Los comandos se pueden encadenar, guardar como secuencias reutilizables o asociar a carpetas vigiladas que procesan los PDF que van llegando. Está escrito en Python con pikepdf y ReportLab, y necesita Python 3.15 o posterior.</p>
  </li>

  <li class="project">
    <h2><a href="https://github.com/{{ site.github_username }}/pdf-word-finder">pdf-word-finder: en qué páginas de un PDF está una palabra</a></h2>
    <p class="project-role">2026 · v1.4 · en <a href="https://codeberg.org/{{ site.codeberg_username }}/pdf-word-finder">Codeberg</a> y <a href="https://github.com/{{ site.github_username }}/pdf-word-finder">GitHub</a></p>
    <p><b>pdf-word-finder</b> busca en un PDF una lista de palabras, frases o expresiones regulares e informa en qué páginas aparece cada una, una línea por término, como en el índice de un libro. Da los números de página impresos en el libro (números romanos en los preliminares, numeraciones que vuelven a empezar en otros volúmenes) y no la posición de la página en el archivo, y avisa cuando el PDF no tiene etiquetas de página en lugar de inventarlas. Funciona en la línea de comandos o en una ventana, y solo necesita Python 3.9 o posterior y <code>pypdf</code>; si PyMuPDF está disponible, lo usa para leer en mejor orden las páginas con columnas, notas al pie o aparato crítico.</p>
  </li>

  <li class="project">
    <h2><a href="https://github.com/{{ site.github_username }}/py-foliation">py-foliation: cambiar las etiquetas de página de un PDF</a></h2>
    <p class="project-role">2026 · v0.8 · en <a href="https://codeberg.org/{{ site.codeberg_username }}/py-foliation">Codeberg</a> y <a href="https://github.com/{{ site.github_username }}/py-foliation">GitHub</a></p>
    <p><b>py-foliation</b> cambia las etiquetas de página de los documentos PDF, es decir, la numeración que muestra el visor. Un libro cuyos preliminares van numerados i, ii, iii y cuyo texto empieza de nuevo en 1 puede mostrar esos números en el visor, en vez del simple 1, 2, 3 de las páginas del archivo; solo cambian las etiquetas, y las páginas quedan como estaban. Las etiquetas se definen por intervalos, cada uno con su primera página, su estilo (arábigo, romano o letras, en mayúsculas o minúsculas, o sin número), el número por el que empieza y un prefijo, de modo que un apéndice pueda numerarse App-1, App-2, o la última página llamarse Cubierta. Tiene una ventana para ver y editar las etiquetas página por página, con deshacer y rehacer, y una línea de comandos para hacer lo mismo en scripts; la ventana puede copiar el comando que da las mismas etiquetas a otro archivo. La interfaz está en inglés y en español. Está escrito en Python con pikepdf y PySide6, y se instala como AppImage para Linux, como paquete de Fedora en Copr o desde el código fuente con Python 3.15 o posterior.</p>
  </li>

  <li class="project" id="py-redact">
    <h2><a href="https://github.com/{{ site.github_username }}/py-redact">py-redact: censurar documentos PDF</a></h2>
    <p class="project-role">2026 · v0.4.5 · en <a href="https://codeberg.org/{{ site.codeberg_username }}/py-redact">Codeberg</a> y <a href="https://github.com/{{ site.github_username }}/py-redact">GitHub</a></p>
    <p><b>py-redact</b> censura documentos PDF. Uno marca en las páginas lo que debe desaparecer, y en la copia censurada todo lo que queda bajo cada marca se elimina para siempre: el texto, letra por letra, la parte de las imágenes que cubre, los dibujos que tapa y las anotaciones y campos de formulario que toca. No es lo mismo que dibujar un rectángulo negro, que oculta el texto a la vista pero lo deja en el archivo; py-redact lo elimina, y después de guardar revisa la copia para asegurarse de que ya no se puede leer nada de lo que había bajo una marca. El hueco puede rellenarse con un color o quedar como está, con un texto encima como <code>CENSURADO</code> o un código de exención de la FOIA. Hay varias maneras de marcar: arrastrar sobre el texto o dibujar un recuadro, buscar y marcar todas las apariciones de una palabra, de una lista de palabras o de un patrón (números de teléfono, direcciones de correo, números de tarjeta y de identidad, fechas, cuentas bancarias), y repetir una marca en otras páginas. También puede quitar la información oculta de un documento (metadatos, adjuntos, marcadores, comentarios, texto oculto, scripts) y guardar la copia como PDF/A o PDF/X mediante <a href="#py-pdfconform">py-pdfconform</a>. La ventana está en inglés y en español. Está escrito en Python con PyMuPDF y PySide6, y se instala como AppImage para Linux, como paquete de Fedora en Copr o desde el código fuente con Python 3.14 o posterior.</p>
  </li>

  <li class="project" id="py-pdfconform">
    <h2><a href="https://github.com/{{ site.github_username }}/py-pdfconform">py-pdfconform: convertir archivos PDF a PDF/A y PDF/X-4</a></h2>
    <p class="project-role">2026 · v1.2.1 · en <a href="https://codeberg.org/{{ site.codeberg_username }}/py-pdfconform">Codeberg</a> y <a href="https://github.com/{{ site.github_username }}/py-pdfconform">GitHub</a></p>
    <p><b>py-pdfconform</b> convierte archivos PDF a dos normas ISO: PDF/A, para la conservación a largo plazo (PDF/A-1b, 2b y 3b), y PDF/X-4, para la imprenta. Es un solo script de línea de comandos. Ghostscript hace la conversión; pikepdf abre antes los archivos cifrados o dañados y, después, recupera los metadatos perdidos y corrige lo que Ghostscript deja mal. Luego se comprueba cada resultado: los PDF/A con veraPDF, si está instalado, y los PDF/X-4 con una revisión estructural propia. Avisa de todo lo que una norma lo obliga a descartar (JavaScript, adjuntos, anotaciones en PDF/X, transparencias convertidas en imágenes en PDF/A-1b), nunca sobrescribe el archivo de entrada y devuelve códigos de salida aptos para scripts. Necesita Python 3.14 o posterior, Ghostscript 10 o posterior y pikepdf.</p>
  </li>

  <li class="project" id="py-xmlvalidate">
    <h2><a href="https://github.com/{{ site.github_username }}/py-xmlvalidate">py-xmlvalidate: validación Schematron de TEI-XML desde la terminal</a></h2>
    <p class="project-role">2026 · v1.17 · en <a href="https://codeberg.org/{{ site.codeberg_username }}/py-xmlvalidate">Codeberg</a> y <a href="https://github.com/{{ site.github_username }}/py-xmlvalidate">GitHub</a></p>
    <p><b>py-xmlvalidate</b> es un script de Python que valida documentos TEI-XML contra las reglas Schematron incluidas en un ODD (o en un <code>.sch</code> ya extraído, o recogidas de un esquema RelaxNG generado a partir de un ODD, que son las reglas que Jing ignora), y las ejecuta con Saxon. A diferencia de oXygen, que se detiene sin avisar al llegar a cien errores, informa de todas las infracciones, con el recuento por regla y, si se le pide, el número de línea y el <code>xml:id</code> de cada elemento infractor, y dice exactamente cuántas omitió cuando la lista tiene un tope. Devuelve un código de salida distinto de cero si hay infracciones, de modo que puede usarse en un Makefile o en un hook de pre-commit. Necesita Python 3.15 o posterior, <code>saxonche</code> y <code>lxml</code>.</p>
    <p class="continued">También encuentra por su cuenta el esquema a partir de las declaraciones <code>&lt;?xml-model?&gt;</code> del documento, y un script de shell que lo acompaña, <code>py-xmlvalidate-all.sh</code>, añade la validación estructural contra RelaxNG con jing y da un solo veredicto para las dos validaciones. Su informe en JSON alimenta los dos complementos para editores descritos más abajo, cada uno en su propio repositorio: la extensión <a href="#schematron-validator">Schematron Validator</a> para VS Code y <a href="#py-xmlvalidate-emacs">py-xmlvalidate para Emacs</a>.</p>
  </li>

  <li class="project" id="schematron-validator">
    <h2><a href="https://marketplace.visualstudio.com/items?itemName=NicolasVaughan.validate-schematron">Schematron Validator: validación de TEI-XML mientras se escribe en VS Code</a></h2>
    <p class="project-role">2026 · v0.6.0 · en el <a href="https://marketplace.visualstudio.com/items?itemName=NicolasVaughan.validate-schematron">Visual Studio Marketplace</a> · código fuente en <a href="https://codeberg.org/{{ site.codeberg_username }}/py-xmlvalidate-vscode">Codeberg</a> y <a href="https://github.com/{{ site.github_username }}/py-xmlvalidate-vscode">GitHub</a></p>
    <p><b>Schematron Validator</b> es una extensión de VS Code que lleva <a href="#py-xmlvalidate">py-xmlvalidate</a> al editor. Valida archivos XML y TEI contra reglas Schematron (de un <code>.sch</code>, de un ODD o de un esquema RelaxNG con reglas incluidas) mientras se escribe, al abrir y al guardar, incluidos los cambios sin guardar. Cada infracción queda subrayada en el elemento culpable y aparece en el panel de problemas, con la gravedad que indica el <code>role</code> de la regla. Si el esquema es RelaxNG y <a href="https://relaxng.org/jclark/jing.html">jing</a> está instalado, se añaden también los errores estructurales, y el XML mal formado se señala donde se abrió la etiqueta rota. El esquema se toma de la declaración <code>&lt;?xml-model?&gt;</code> del documento o se fija en la configuración; un indicador en la barra de estado muestra si el archivo está limpio, y hay comandos para elegir el intérprete de Python o volver a descargar un esquema que cambió en su origen. El script viene incluido; la extensión necesita Python 3.15 o posterior con <code>saxonche</code> y <code>lxml</code>, y su página explica paso a paso cómo instalarlos.</p>
    <p><a class="button button-primary" href="https://marketplace.visualstudio.com/items?itemName=NicolasVaughan.validate-schematron"><i class="fas fa-download" aria-hidden="true"></i> Instalar desde el Marketplace</a></p>
  </li>

  <li class="project" id="py-xmlvalidate-emacs">
    <h2><a href="https://github.com/{{ site.github_username }}/py-xmlvalidate-emacs">py-xmlvalidate para Emacs: validación de TEI-XML mientras se escribe, con Flycheck o Flymake</a></h2>
    <p class="project-role">2026 · v0.3.0 · en <a href="https://codeberg.org/{{ site.codeberg_username }}/py-xmlvalidate-emacs">Codeberg</a> y <a href="https://github.com/{{ site.github_username }}/py-xmlvalidate-emacs">GitHub</a></p>
    <p><b>py-xmlvalidate para Emacs</b> es un paquete de Emacs que lleva <a href="#py-xmlvalidate">py-xmlvalidate</a> al editor, con Flycheck si está instalado o, si no, con Flymake, que viene con Emacs. Valida mientras se escribe, al abrir y al guardar, todo buffer que tenga una declaración <code>&lt;?xml-model?&gt;</code>; los cambios sin guardar se validan en una copia temporal privada, así que el archivo en disco nunca se modifica. Cada problema queda subrayado, con su mensaje cuando el cursor está encima y la capa que lo detectó (Schematron, RelaxNG o, si el documento está mal formado, XML), y la línea de modo muestra los recuentos; un comando muestra el informe completo del archivo, en texto, con cada línea enlazada al documento. Si el esquema es RelaxNG, valida también la estructura con <a href="https://relaxng.org/jclark/jing.html">jing</a> y le pasa el esquema, convertido con trang, a nxml-mode, para que el autocompletado ofrezca los elementos y atributos que el esquema admite en la posición del cursor. Como las reglas de un esquema pueden leer archivos y acceder a URL, solo valida los documentos que figuran en <code>trusted-content</code>, la lista de contenido de confianza de Emacs. Necesita Emacs 31 o posterior y Python 3.15 o posterior con <code>saxonche</code> y <code>lxml</code>; jing y trang son opcionales.</p>
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
Ahora estoy, muy a gusto, en la distribución [Fedora Linux](https://fedoraproject.org/) con el escritorio [KDE Plasma](https://kde.org/plasma-desktop/).
Durante muchos años usé [Manjaro Linux](https://manjaro.org/) y también [Arch Linux](https://archlinux.org/) a secas, pero me parecieron bastante inestables y difíciles para el trabajo diario.

Mi editor de cabecera, para escribir y para programar, es [GNU Emacs](https://www.gnu.org/s/emacs/), aunque a menudo recurro a [Neovim](https://neovim.io/), [Visual Studio Code](https://code.visualstudio.com/), [PyCharm](https://www.jetbrains.com/pycharm/) y [Oxygen XML Editor](https://www.oxygenxml.com/), según lo que necesite.

Hice este sitio con [Jekyll](https://jekyllrb.com), un generador de sitios estáticos; el diseño partió de un tema de [S.V. Miller](https://svmiller.com/).
Su código fuente está [en GitHub](https://github.com/{{ site.github_username }}/nivaca.github.io).
