---
title: "Was ist diese Datei: identify"
nav_order: 4
lang: "de"
source: identify.md
source_hash: "6735d5facfac"
nav_exclude: true
search_exclude: true
---
# Was ist diese Datei: `identify` {#what-is-this-file-identify}

```bash
heat3d-acrally-maps identify <path>
```

sagt, ob eine Datei einer der eigenen Container von Assetto Corsa Rally ist. Das Spiel liefert seinen
Inhalt als Unreal-5-IoStore-Container aus, einem Engine-Format, das viele Spiele teilen; was dem Spiel
selbst gehört, ist der Ort, an dem sie eingebunden sind, sein Projektordner `acr`. Eine Inhaltsverzeichnis-Datei
(`.utoc`), eingebunden unter `.../acr/Content/`, wird also erkannt, samt den Leveln, die sie enthält:

```text
pakchunk0-Windows.utoc  (1,234 bytes)
  Assetto Corsa Rally IoStore container, mounted at ../../../acr/Content/
    files      4
    levels     ExampleStage, Menu
```

Alles andere – auch Container anderer Spiele – gibt
`not an Assetto Corsa Rally file: <name>` auf der Fehlerausgabe aus und endet mit 2; eine Datei, die
nicht da ist, meldet `no such file` und endet mit 2. Das eigene `identify` von 3DHeat GameFiles
beschreibt jeden IoStore-Container, auch den dieses Spiels
([Unreal 5 IoStore](https://holdi601.github.io/3DHeat-GameFiles/de/reader-unreal-iostore.html)).
