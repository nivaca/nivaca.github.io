---
layout: page
ref: py-slowdown
title: py-slowdown
subtitle: Reproducir música más lenta o más rápida sin cambiarle la altura, en el escritorio y en Android
permalink: /es/programacion/py-slowdown/
description: py-slowdown, un reproductor de Nicolás Vaughan que cambia la velocidad de la música sin cambiarle la altura, en Linux, Windows, macOS y Android; cómo instalarlo y sus versiones.
---

py-slowdown reproduce audio más lento o más rápido sin cambiarle la altura. Está hecho para la música: para practicar una pieza y sacarla de oído, oyendo un pasaje una y otra vez a una velocidad que se pueda seguir. El archivo se ve como una forma de onda, los mandos de siempre lo recorren y los marcadores guardan los lugares a los que se quiere volver. Lo que hace además de reproducir, como la cuenta previa, el tempo o la altura en semitonos, está pensado para músicos; no es una herramienta para transcribir la voz hablada. Funciona en Linux, Windows y macOS, y Slowdown, su versión para Android, hace casi lo mismo en el teléfono.

<div class="buttons">
  <a class="button button-primary" href="https://codeberg.org/{{ site.codeberg_username }}/py-slowdown/releases"><i class="fas fa-download" aria-hidden="true"></i> Descargas</a>
  <a class="button" href="https://codeberg.org/{{ site.codeberg_username }}/slowdown-android/releases"><i class="fab fa-android" aria-hidden="true"></i> Aplicación para Android</a>
</div>

<dl class="facts">
  <dt>Versión</dt><dd>1.6.1 (26 de noviembre de 2026); Slowdown para Android 1.2 (25 de noviembre de 2026)</dd>
  <dt>Programas</dt><dd>una ventana para Linux, Windows y macOS; una aplicación para Android</dd>
  <dt>Motor</dt><dd>la biblioteca Rubber Band, con su motor R3, el de mayor calidad</dd>
  <dt>Interfaz</dt><dd>inglés y español</dd>
  <dt>Requisitos</dt><dd>nada más, con los instaladores y los paquetes (traen su propio Python, Qt, FFmpeg y Rubber Band); desde el código fuente, Python 3.14 o posterior y la biblioteca Rubber Band; en el teléfono, Android 12 o posterior en un dispositivo ARM de 64 bits</dd>
  <dt>Licencia</dt><dd>GNU General Public License, versión 3 o posterior</dd>
  <dt>Código</dt><dd>py-slowdown en <a href="https://codeberg.org/{{ site.codeberg_username }}/py-slowdown">Codeberg</a> y <a href="https://github.com/{{ site.github_username }}/py-slowdown">GitHub</a>; Slowdown para Android en <a href="https://codeberg.org/{{ site.codeberg_username }}/slowdown-android">Codeberg</a> y <a href="https://github.com/{{ site.github_username }}/slowdown-android">GitHub</a></dd>
</dl>

<figure class="screenshot">
  <img src="{{ "/images/py-slowdown/main_es.webp" | relative_url }}" alt="La ventana de py-slowdown, con una grabación al 75 % y dos marcadores" loading="lazy">
  <figcaption>Una grabación al 75 %, con dos marcadores.</figcaption>
</figure>

## Lo que hace

Abre archivos de audio y el sonido de los de video: MP3, M4A, MP4, FLAC, WAV, AIFF, Ogg, Opus, WMA y lo demás que lea FFmpeg. El archivo aparece como forma de onda, con una regla de tiempos, donde un clic mueve la posición y la rueda desplaza la vista y la acerca o aleja; un archivo largo se puede reproducir mientras todavía se lee, y la segunda vez toda su forma de onda aparece enseguida.

La velocidad va de 0,25× a 3× y se cambia mientras suena, con una perilla o desde una lista de velocidades que usted elige (50 %, 75 %, 100 %…). El estiramiento lo hace la [biblioteca Rubber Band](https://breakfastquay.com/rubberband/), con su motor R3, por medio de un enlace pequeño, propio de py-slowdown; a 1× el archivo suena tal cual, muestra por muestra, sin pasar por Rubber Band. Se puede elegir, en cambio, una calidad más liviana, que usa la mitad del procesador, o el motor anterior, R2, de ataques más nítidos. La altura sube o baja con dos perillas, en semitonos (de −12 a +12) y en cents (de −50 a +50, para afinar una grabación con un instrumento), sin cambiar la velocidad, y una voz o un instrumento puede conservar sus formantes, y con ellos su timbre.

Una pausa lleva la posición de vuelta adonde empezó a sonar, para que Espacio toque otra vez el mismo pasaje. Una selección se repite sin fin y sin cortes: el final del pasaje entra en su principio con un fundido breve, a cualquier velocidad, y las selecciones pueden guardarse como bucles con un nombre. Los marcadores, cada uno con su nombre, se ponen en la posición de reproducción o en cualquier punto de la forma de onda, se listan en un panel lateral y se exportan como texto.

Para trabajar una pieza tiene algunas herramientas más:

- **Oír** deja oír una parte de la mezcla: un canal, los dos en uno, la mezcla sin su centro (donde suelen estar la voz y el solo), solo los graves, o todo menos los graves. Un ecualizador de cinco bandas, de 60 Hz a 12 kHz, sube o baja cada una con su perilla.
- **Cuenta previa** da los golpes de un metrónomo antes de tocar. Su tempo puede seguir la velocidad, y se puede medir marcando el pulso. Con el primer pulso de la grabación marcado, la grabación entra en el pulso más cercano, empiece donde empiece.
- **Exportar el audio** guarda la grabación, o la selección, como suena (a la velocidad y la altura elegidas, y como se oye, si se pide), en WAV, FLAC, MP3 u Opus.

De cada archivo recuerda sus marcadores, sus bucles, el punto donde se dejó y cómo se tocó, y la próxima vez continúa desde allí. Todo eso se escribe además en un archivo con el nombre de la grabación y la extensión `.slx`, junto a ella o en una carpeta elegida, de modo que viaja con la grabación; abrir el `.slx` abre la grabación. El programa abre también los archivos de Transcribe! (`.xsc`), con sus secciones como marcadores, sus bucles, su primer pulso y su tempo, y su velocidad. Todo se puede hacer con el teclado, y las teclas se pueden cambiar, también para un pedal que mande teclas.

## En Android

[Slowdown para Android](https://github.com/{{ site.github_username }}/slowdown-android) (versión 1.2) es el mismo programa para el teléfono. Tiene el mismo motor, lee y escribe los mismos archivos `.slx`, y su ventana está dispuesta y coloreada como la de py-slowdown: la forma de onda, los botones de la reproducción, las perillas de la velocidad, el volumen y la altura, y el panel de los marcadores y los bucles. Un toque en la forma de onda mueve la posición, arrastrar desplaza la vista y pellizcar acerca o aleja alrededor de los dedos. Cambia la velocidad y la altura como el programa de escritorio, repite una selección o el archivo entero sin cortes, guarda bucles y marcadores con nombre y recuerda cómo se tocó cada archivo. MP3, FLAC, WAV y AIFF los decodifica la aplicación misma, una canción de cinco minutos en medio segundo; los demás formatos, los códecs de Android, más despacio. Se puede usar un teclado o un pedal, con las mismas teclas que en py-slowdown, y el botón de los auriculares reproduce y pausa.

Desde la versión 1.2 tiene también la cuenta previa, las maneras de oír y la exportación del audio (en WAV o M4A), sigue sonando con la pantalla apagada, y sus archivos `.slx` pueden exportarse y cargarse, o guardarse en una carpeta elegida, junto a las grabaciones. Está escrita en Kotlin, con el motor de sonido en C++, y necesita Android 12 o posterior en un dispositivo ARM de 64 bits. Puede instalarse desde sus versiones publicadas ([Codeberg](https://codeberg.org/{{ site.codeberg_username }}/slowdown-android/releases), [GitHub](https://github.com/{{ site.github_username }}/slowdown-android/releases)), con [Obtainium](https://github.com/ImranR98/Obtainium) o desde mi propio repositorio de F-Droid, [nivaca.codeberg.page/fdroid](https://nivaca.codeberg.page/fdroid/); los tres usan el mismo APK firmado, así que cualquiera de ellos actualiza a los otros.

## Cómo instalarlo

Cada versión está firmada y se publica en [Codeberg](https://codeberg.org/{{ site.codeberg_username }}/py-slowdown/releases) y [GitHub](https://github.com/{{ site.github_username }}/py-slowdown/releases). Los instaladores traen todo lo que el programa necesita, así que no hay que instalar nada más.

| Sistema | Cómo |
|---|---|
| Windows 10 o posterior | un instalador (`.exe`), para un usuario o para todos |
| macOS 13 o posterior | una imagen de disco (`.dmg`), para Apple silicon o Intel |
| Fedora | `sudo dnf copr enable nivaca/py-slowdown` y luego `sudo dnf install py-slowdown` |
| Debian 12, Ubuntu 22.04 y posteriores | el `.deb` de una versión, o mi repositorio APT firmado, [github.com/nivaca/apt](https://github.com/{{ site.github_username }}/apt) |
| Cualquier Linux | un instalador (`.run`), o un AppImage, que no necesita instalarse |
| Android 12 o posterior | la aplicación, desde sus versiones publicadas, Obtainium o F-Droid (véase arriba) |
| Desde el código fuente | Python 3.14 o posterior y la biblioteca Rubber Band: `uv run py-slowdown`, o `install/install.sh` en Linux y macOS |

Los instaladores para Windows y macOS no están firmados por Microsoft ni por Apple, así que la primera vez el sistema pregunta si se deben abrir; el README explica qué hacer.

## Documentación

- El manual de usuario, en PDF: [inglés](https://github.com/{{ site.github_username }}/py-slowdown/blob/main/docs/MANUAL_en.pdf), [español](https://github.com/{{ site.github_username }}/py-slowdown/blob/main/docs/MANUAL_es.pdf); `man py-slowdown` una vez instalado el RPM o el paquete de Debian.
- El README, con todo en detalle, los atajos de teclado y dónde se guarda cada cosa: [inglés](https://github.com/{{ site.github_username }}/py-slowdown/blob/main/README.md), [español](https://github.com/{{ site.github_username }}/py-slowdown/blob/main/README_es.md); el de la aplicación para Android: [inglés](https://github.com/{{ site.github_username }}/slowdown-android/blob/main/README.md), [español](https://github.com/{{ site.github_username }}/slowdown-android/blob/main/README_es.md).
- [Cómo se hizo py-slowdown](https://github.com/{{ site.github_username }}/py-slowdown/blob/main/docs/DESCRIPTION.md) (en inglés), su [descripción en español](https://github.com/{{ site.github_username }}/py-slowdown/blob/main/docs/DESCRIPCI%C3%93N_es.md), y los registros de cambios de [py-slowdown](https://github.com/{{ site.github_username }}/py-slowdown/blob/main/CHANGELOG_es.md) y de [la aplicación para Android](https://github.com/{{ site.github_username }}/slowdown-android/blob/main/CHANGELOG_es.md).

## Versiones

Los pasos principales, desde la primera versión hasta la actual. El [registro de cambios](https://github.com/{{ site.github_username }}/py-slowdown/blob/main/CHANGELOG_es.md) tiene todas las versiones.

<ul class="history">
  <li><span class="when">0.1.0<br>24 nov. 2026</span><span>La primera versión: la forma de onda, los mandos de siempre, la velocidad de 0,25× a 3× con Rubber Band, marcadores, la interfaz en inglés y en español; un RPM firmado, un AppImage y un paquete de Debian.</span></li>
  <li><span class="when">0.2.0</span><span>Instaladores para Windows, macOS y cualquier Linux; la repetición de una selección sin cortes; la cuenta previa.</span></li>
  <li><span class="when">1.0.0</span><span>La primera versión estable: la altura en semitonos; el tempo marcado con el pulso; el primer pulso de la grabación; reabrir el último archivo.</span></li>
  <li><span class="when">1.1.0</span><span>La exportación del audio; oír una parte de la mezcla; conservar los formantes; los bucles; atajos de teclado propios; cada archivo como se tocó; archivos leídos varias veces más rápido.</span></li>
  <li><span class="when">1.2.0</span><span>La configuración de cada grabación en un archivo propio, junto a ella; velocidades propias; la elección de la calidad de reproducción; los menús Oír y Cuenta previa.</span></li>
  <li><span class="when">1.3.0, 1.3.1</span><span>Una pausa vuelve adonde empezó a sonar; la altura en semitonos y cents, con dos perillas; el primer pulso como marcador; los archivos <code>.slx</code>, que abre el programa.</span></li>
  <li><span class="when">Android 1.0<br>25 nov.</span><span>Slowdown para Android, la ventana de py-slowdown 1.3 para el teléfono, con el mismo motor y los mismos archivos <code>.slx</code>.</span></li>
  <li><span class="when">1.4.0</span><span>Perillas para la velocidad y el volumen; un ecualizador de cinco bandas, en un panel lateral, Sonido; los bucles sobre la forma de onda; un reloj de compases y pulsos; un modo compacto; una pantalla de inicio; íconos propios del programa.</span></li>
  <li><span class="when">Android 1.1, 1.2</span><span>El idioma, elegido aparte del que tenga el teléfono; los archivos <code>.slx</code>, exportados y cargados, también en una carpeta elegida; la reproducción con la pantalla apagada; la cuenta previa, las maneras de oír y la exportación del audio, como en py-slowdown.</span></li>
  <li><span class="when">1.5.0–1.6.1<br>25–26 nov.</span><span>Seleccionar el archivo entero (Ctrl+A); los archivos de Transcribe! (<code>.xsc</code>), que se abren con sus secciones, sus bucles y su tempo, y un script que convierte muchos a la vez; el tempo, a la vista mientras se marca.</span></li>
</ul>
