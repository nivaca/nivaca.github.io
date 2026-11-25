---
layout: page
ref: py-slowdown
title: py-slowdown
subtitle: Play music slower or faster without changing its pitch, on the desktop and on Android
permalink: /coding/py-slowdown/
description: py-slowdown, a player by Nicolás Vaughan that changes the speed of music without changing its pitch, on Linux, Windows, macOS and Android; how to install it, and its versions.
---

py-slowdown plays audio slower or faster without changing its pitch. It is made for music: for practising a piece and learning it by ear, hearing a passage again and again at a speed one can follow. The file is shown as a waveform, the usual player controls move through it, and bookmarks keep the places one wants to come back to. What it does besides playing, such as the count-in, the tempo or the pitch in semitones, is meant for musicians; it is not a tool for transcribing speech. It runs on Linux, Windows and macOS, and Slowdown, its Android version, does most of the same on a phone.

<div class="buttons">
  <a class="button button-primary" href="https://codeberg.org/{{ site.codeberg_username }}/py-slowdown/releases"><i class="fas fa-download" aria-hidden="true"></i> Downloads</a>
  <a class="button" href="https://codeberg.org/{{ site.codeberg_username }}/slowdown-android/releases"><i class="fab fa-android" aria-hidden="true"></i> Android app</a>
</div>

<dl class="facts">
  <dt>Version</dt><dd>1.3.1 (24 November 2026); Slowdown for Android 1.0 (25 November 2026)</dd>
  <dt>Programs</dt><dd>a window for Linux, Windows and macOS; an app for Android</dd>
  <dt>Engine</dt><dd>the Rubber Band Library, with its R3 engine, the one of highest quality</dd>
  <dt>Interface</dt><dd>English and Spanish</dd>
  <dt>Needs</dt><dd>nothing else, with the installers and packages (they bring their own Python, Qt, FFmpeg and Rubber Band); from the source, Python 3.14 or later and the Rubber Band Library; on a phone, Android 12 or later on a 64-bit ARM device</dd>
  <dt>Licence</dt><dd>GNU General Public License, version 3 or later</dd>
  <dt>Code</dt><dd>py-slowdown on <a href="https://codeberg.org/{{ site.codeberg_username }}/py-slowdown">Codeberg</a> and <a href="https://github.com/{{ site.github_username }}/py-slowdown">GitHub</a>; Slowdown for Android on <a href="https://codeberg.org/{{ site.codeberg_username }}/slowdown-android">Codeberg</a> and <a href="https://github.com/{{ site.github_username }}/slowdown-android">GitHub</a></dd>
</dl>

<figure class="screenshot">
  <img src="{{ "/images/py-slowdown/main_en.webp" | relative_url }}" alt="The window of py-slowdown, with a recording at 75% and two bookmarks, Second verse and Guitar solo" loading="lazy">
  <figcaption>A recording at 75%, with two bookmarks.</figcaption>
</figure>

## What it does

It opens audio files and the sound of video files: MP3, M4A, MP4, FLAC, WAV, AIFF, Ogg, Opus, WMA and whatever else FFmpeg reads. The file appears as a waveform with a time ruler, where a click moves the position and the wheel scrolls and zooms; a long file can be played while it is still being read, and the second time its whole waveform is there at once.

The speed goes from 0.25× to 3× and can be changed while it plays, by a slider or from a list of speeds of one's own (50%, 75%, 100%…). The stretching is done by the [Rubber Band Library](https://breakfastquay.com/rubberband/), with its R3 engine, called through a small binding of py-slowdown's own; at 1× the file is played as it is, sample for sample, without going through Rubber Band. A lighter quality, which needs half the processor, or the older R2 engine, with crisper attacks, can be chosen instead. The pitch moves up or down on two knobs, in semitones (−12 to +12) and in cents (−50 to +50, to tune a recording to an instrument), without changing the speed, and a voice or an instrument can keep its formants, and so its timbre.

A pause takes the position back to where playing started, so that Space plays the same passage again. A selection repeats without end and without a gap, the end of the passage running into its start through a short fade, at any speed, and selections can be kept as loops with a name. Bookmarks, each with a label, are added at the playing position or anywhere on the waveform, listed in a side panel and exported as text.

For working on a piece it has a few more tools:

- **Hear** plays one part of the mix: one channel, the two in one, the mix without its centre (where the voice and the solo usually are), only the bass, or everything but the bass.
- **Count-in** gives a metronome's clicks before playing. Their tempo can follow the speed, and can be measured by tapping with the beat. With the recording's first beat marked, the recording comes in on the nearest beat wherever playing starts.
- **Export the audio** saves the recording, or the selection, as it sounds (at the speed and pitch chosen, and as it is heard, if asked), as WAV, FLAC, MP3 or Opus.

For each file it remembers its bookmarks, its loops, the point where it was left and how it was played, and goes on from there the next time. All that is also written in a file with the recording's name and the extension `.slx`, beside it or in a folder chosen, so that it travels with the recording; opening the `.slx` opens the recording. Everything can be done from the keyboard, and the keys can be changed, also for a foot pedal that sends keys.

## On Android

[Slowdown for Android](https://github.com/{{ site.github_username }}/slowdown-android) (version 1.0) is the same program for a phone. It has the same engine, reads and writes the same `.slx` files, and its window is laid out and coloured like that of py-slowdown: the waveform, the player's buttons, the knobs of the speed, the volume and the pitch, and the panel of the bookmarks and the loops. A tap on the waveform moves the position, dragging scrolls, and pinching zooms around the fingers. It changes the speed and the pitch as the desktop program does, repeats a selection or the whole file without a gap, keeps loops and bookmarks with names, and remembers how each file was played. MP3, FLAC, WAV and AIFF are decoded by the app itself, a five-minute song in half a second; other formats by the codecs of Android, more slowly. A keyboard or a foot pedal works with the keys of py-slowdown, and the play button of headphones plays and pauses.

The count-in, the ways of hearing, exporting the audio and playing with the screen off are not in the app yet. It is written in Kotlin, with the sound engine in C++, and needs Android 12 or later on a 64-bit ARM device. It can be installed from its releases ([Codeberg](https://codeberg.org/{{ site.codeberg_username }}/slowdown-android/releases), [GitHub](https://github.com/{{ site.github_username }}/slowdown-android/releases)), with [Obtainium](https://github.com/ImranR98/Obtainium), or from my own F-Droid repository, [nivaca.codeberg.page/fdroid](https://nivaca.codeberg.page/fdroid/); all three use the same signed APK, so any one of them updates the others.

## Installing it

Every release is signed, and is on [Codeberg](https://codeberg.org/{{ site.codeberg_username }}/py-slowdown/releases) and [GitHub](https://github.com/{{ site.github_username }}/py-slowdown/releases). The installers carry all the program needs, so nothing else has to be installed.

| System | How |
|---|---|
| Windows 10 or later | an installer (`.exe`), for one user or for everyone |
| macOS 13 or later | a disk image (`.dmg`), for Apple silicon or Intel |
| Fedora | `sudo dnf copr enable nivaca/py-slowdown`, then `sudo dnf install py-slowdown` |
| Debian 12, Ubuntu 22.04 and later | the `.deb` of a release, or my signed APT repository, [github.com/nivaca/apt](https://github.com/{{ site.github_username }}/apt) |
| Any Linux | an installer (`.run`), or an AppImage, which needs no installing |
| Android 12 or later | the app, from its releases, Obtainium or F-Droid (see above) |
| From the source | Python 3.14 or later and the Rubber Band Library: `uv run py-slowdown`, or `install/install.sh` on Linux and macOS |

The installers for Windows and macOS are not signed by Microsoft or Apple, so the first time the system asks whether to open them; the README says how.

## Documentation

- The user manual, in PDF: [English](https://github.com/{{ site.github_username }}/py-slowdown/blob/main/docs/MANUAL_en.pdf), [Spanish](https://github.com/{{ site.github_username }}/py-slowdown/blob/main/docs/MANUAL_es.pdf); `man py-slowdown` once the RPM or the Debian package is installed.
- The README, with everything at length, the keyboard shortcuts and where each thing is kept: [English](https://github.com/{{ site.github_username }}/py-slowdown/blob/main/README.md), [Spanish](https://github.com/{{ site.github_username }}/py-slowdown/blob/main/README_es.md); that of the Android app: [English](https://github.com/{{ site.github_username }}/slowdown-android/blob/main/README.md), [Spanish](https://github.com/{{ site.github_username }}/slowdown-android/blob/main/README_es.md).
- [How py-slowdown was made](https://github.com/{{ site.github_username }}/py-slowdown/blob/main/docs/DESCRIPTION.md), and the changelogs of [py-slowdown](https://github.com/{{ site.github_username }}/py-slowdown/blob/main/CHANGELOG.md) and of [the Android app](https://github.com/{{ site.github_username }}/slowdown-android/blob/main/CHANGELOG.md).

## Versions

The main steps, from the first version to the present one. The [changelog](https://github.com/{{ site.github_username }}/py-slowdown/blob/main/CHANGELOG.md) has every version.

<ul class="history">
  <li><span class="when">0.1.0<br>24 Nov. 2026</span><span>The first version: the waveform, the usual controls, the speed from 0.25× to 3× by Rubber Band, bookmarks, an interface in English and Spanish; a signed RPM, an AppImage and a Debian package.</span></li>
  <li><span class="when">0.2.0</span><span>Installers for Windows, macOS and any Linux; repeating a selection without a gap; the count-in.</span></li>
  <li><span class="when">1.0.0</span><span>The first stable version: the pitch in semitones; tapping the tempo; the recording's first beat; reopening the last file.</span></li>
  <li><span class="when">1.1.0</span><span>Exporting the audio; hearing one part of the mix; keeping the formants; loops; keyboard shortcuts of one's own; each file as it was played; files read several times faster.</span></li>
  <li><span class="when">1.2.0</span><span>The settings of each recording in a file of its own, beside it; speeds of one's own; a choice of playback quality; menus Hear and Count-in.</span></li>
  <li><span class="when">1.3.0, 1.3.1</span><span>A pause goes back to where playing started; the pitch in semitones and cents, on two knobs; the first beat as a bookmark; the <code>.slx</code> files, opened by the program.</span></li>
  <li><span class="when">Android 1.0<br>25 Nov.</span><span>Slowdown for Android, the window of py-slowdown 1.3 for a phone, with the same engine and the same <code>.slx</code> files.</span></li>
</ul>
