---
title: "Startseite"
nav_order: 1
lang: "de"
source: index.md
source_hash: "5942fc0278fa"
nav_exclude: true
search_exclude: true
permalink: /de/
---
# 3DHeat AC Rally {#dheat-ac-rally}

**Was ist das?** Dieses Werkzeug liest eine Etappe von Assetto Corsa Rally aus **deiner eigenen
Installation** und schneidet den Abschnitt heraus, den du gefahren bist: den Boden der Etappe, aufgeteilt in
Fahrbahn und Gelände und in der Farbe eingefärbt, die das Spiel dafür eingebacken hat, dazu die Leitplanken,
Schilder, Gebäude und anderen Modelle entlang deiner Runde, als ein 3D-Streckenmodell für den
[3DHeat](https://github.com/Holdi601/3DHeat)-Viewer ([Dokumentation](https://holdi601.github.io/3DHeat/)).

**Wozu braucht man das?** Um deine AC-Rally-Fahrten auf der echten Etappe zu analysieren – Bremspunkte,
Linien und Kurven in 3D – statt auf einer Linie im leeren Raum.

**Beispiel:** `heat3d-acrally-maps course my_run.json` -> `my_run.glb`, im selben Rahmen wie die Runde:
es fügt sich in die Rennanalyse des Viewers unter der Runde ein, ohne Platzieren oder Skalieren.

## Schnellstart {#quick-start}

Noch nie in der Kommandozeile gearbeitet? Lies zuerst [Bevor du anfängst](before-you-start.md).
Du brauchst Python 3.10 oder neuer, Assetto Corsa Rally, eine darin aufgezeichnete Fahrt und
[3DHeat GameFiles](https://holdi601.github.io/3DHeat-GameFiles/) (wird mit diesem Werkzeug installiert).
Führe diese Befehle in dem Ordner aus, in den du das Werkzeug geklont oder entpackt hast:

```bash
python -m pip install -e .                      # installiert den Befehl heat3d-acrally-maps
heat3d-acrally-maps stages                      # wo das Spiel liegt, und seine Etappen
heat3d-acrally-maps course my_run.json          # die Strecke um diese Fahrt
```

Die Fahrt kommt vom 3DHeat-GameCapture-Recorder
([Telemetrie: Assetto Corsa](https://holdi601.github.io/3DHeat-GameCapture/telemetry-assetto-corsa.html),
`--game acrally`). `course` findet die Etappe und die Lage der Achsen der Runde aus der Runde selbst
und endet mit `wrote my_run.glb (... bytes)`. Lade die `.glb` im Panel **Hintergrund / Level** des
Viewers mit **3D-Modell…**.

Die Strecke wird aus den Dateien des Spiels gebaut: sie bleibt **auf deinem Rechner**, zum Ansehen,
nicht zum Teilen oder Veröffentlichen ([Bedingungen](terms.md)).

## Seiten {#pages}

| Seite | Was sie behandelt |
|---|---|
| [Bevor du anfängst](before-you-start.md) | Python, GameFiles, Oodle, ein Terminal, ein erster Lauf |
| [Streckenexport: course](course-assetto-corsa-rally.md) | wie aus einer Fahrt eine Strecke wird: die Installation, die Etappe, der Rahmen, Boden, Textur, Modelle |
| [Das Spiel finden: stages](stages.md) | wo Assetto Corsa Rally gefunden wird, was `stages` ausgibt |
| [Was ist diese Datei: identify](identify.md) | die eigenen IoStore-Container des Spiels |
| [Bedingungen und Lizenz](terms.md) | die Inhalte des Spiels, die Formate, warum dies ein eigenes Paket ist |
| [Befehlsreferenz](../cli-reference.md) | jede Option, aus dem Code erzeugt |
| [Diese Doku pflegen](maintaining.md) | die Checkliste für jedes Release |

## Verwandt {#related}

- Der 3DHeat-Viewer: [github.com/Holdi601/3DHeat](https://github.com/Holdi601/3DHeat),
  Dokumentation unter [holdi601.github.io/3DHeat](https://holdi601.github.io/3DHeat/).
- Aufnahme von AC-Rally-Fahrten: der GameCapture-Recorder,
  [Telemetrie: Assetto Corsa](https://holdi601.github.io/3DHeat-GameCapture/telemetry-assetto-corsa.html).
- Die Bibliothek, auf der dieses Werkzeug aufbaut – die Leser für Unreal-5-IoStore, Zen-Pakete und
  Texturen sowie Oodle – und ihr Befehl `course`, der AC-Rally-Runden an dieses Werkzeug übergibt:
  [3DHeat GameFiles](https://holdi601.github.io/3DHeat-GameFiles/).

## Die 3DHeat-Werkzeuge {#the-3dheat-tools}

| Werkzeug | Was es tut | Code | Doku |
|---|---|---|---|
| 3DHeat viewer | zeigt die Daten: Heatmaps, Rennanalyse, Match-Auswertung | [3DHeat](https://github.com/Holdi601/3DHeat) | [Doku](https://holdi601.github.io/3DHeat/) |
| GameFiles | Level und Strecken aus den eigenen Dateien eines Spiels | [3DHeat-GameFiles](https://github.com/Holdi601/3DHeat-GameFiles) | [Doku](https://holdi601.github.io/3DHeat-GameFiles/) |
| GameCapture | Rundentelemetrie und Level, aus Gameplay-Video rekonstruiert | [3DHeat-GameCapture](https://github.com/Holdi601/3DHeat-GameCapture) | [Doku](https://holdi601.github.io/3DHeat-GameCapture/) |
| Unreal Exporter | ein Plugin für den Unreal Editor: ein Level als eine `.glb` | [3DHeat-UnrealExporter](https://github.com/Holdi601/3DHeat-UnrealExporter) | [Doku](https://holdi601.github.io/3DHeat-UnrealExporter/) |
| CS2 | Counter-Strike-2-Demos und -Karten | [3DHeat-CS2](https://github.com/Holdi601/3DHeat-CS2) | [Doku](https://holdi601.github.io/3DHeat-CS2/) |
| Watcher | zeichnet auf, was Spiele veröffentlichen, während du spielst | [3DHeat-Watcher](https://github.com/Holdi601/3DHeat-Watcher) | [Doku](https://holdi601.github.io/3DHeat-Watcher/) |
| Ext-WarThunder | War-Thunder-Replays | [3DHeat-Ext-WarThunder](https://github.com/Holdi601/3DHeat-Ext-WarThunder) | [Doku](https://holdi601.github.io/3DHeat-Ext-WarThunder/) |
| Ext-WoT | World-of-Tanks-Replays | [3DHeat-Ext-WoT](https://github.com/Holdi601/3DHeat-Ext-WoT) | [Doku](https://holdi601.github.io/3DHeat-Ext-WoT/) |
| Ext-WoWs | World-of-Warships-Replays | [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs) | [Doku](https://holdi601.github.io/3DHeat-Ext-WoWs/) |
| Ext-Squad | Squad-Serverdemos | [3DHeat-Ext-Squad](https://github.com/Holdi601/3DHeat-Ext-Squad) | [Doku](https://holdi601.github.io/3DHeat-Ext-Squad/) |
| Ext-DCS | DCS-World-Karten als 3D-Level | [3DHeat-Ext-DCS](https://github.com/Holdi601/3DHeat-Ext-DCS) | [Doku](https://holdi601.github.io/3DHeat-Ext-DCS/) |
| Ext-IL2 | IL-2-Sturmovik-Karten als 3D-Level | [3DHeat-Ext-IL2](https://github.com/Holdi601/3DHeat-Ext-IL2) | [Doku](https://holdi601.github.io/3DHeat-Ext-IL2/) |
| Ext-Dota | die Dota-2-Karte als 3D-Level | [3DHeat-Ext-Dota](https://github.com/Holdi601/3DHeat-Ext-Dota) | [Doku](https://holdi601.github.io/3DHeat-Ext-Dota/) |
| Ext-DotaReplay | Dota-2-Replays als Tabellen | [3DHeat-Ext-DotaReplay](https://github.com/Holdi601/3DHeat-Ext-DotaReplay) | [Doku](https://holdi601.github.io/3DHeat-Ext-DotaReplay/) |
| Ext-Riot | League-of-Legends- und VALORANT-Replays | [3DHeat-Ext-Riot](https://github.com/Holdi601/3DHeat-Ext-Riot) | [Doku](https://holdi601.github.io/3DHeat-Ext-Riot/) |
| Ext-Forza | Forza-Horizon-Strecken und -Autos | [3DHeat-Ext-Forza](https://github.com/Holdi601/3DHeat-Ext-Forza) | [Doku](https://holdi601.github.io/3DHeat-Ext-Forza/) |
| Ext-Battlefield | Battlefield-6-Level als 3D-Level | [3DHeat-Ext-Battlefield](https://github.com/Holdi601/3DHeat-Ext-Battlefield) | [Doku](https://holdi601.github.io/3DHeat-Ext-Battlefield/) |
| Ext-BeamNG | BeamNG.drive-Strecken um deine Runden | [3DHeat-Ext-BeamNG](https://github.com/Holdi601/3DHeat-Ext-BeamNG) | [Doku](https://holdi601.github.io/3DHeat-Ext-BeamNG/) |
| Ext-ACRally | Assetto-Corsa-Rally-Etappen um deine Runden | [3DHeat-Ext-ACRally](https://github.com/Holdi601/3DHeat-Ext-ACRally) | [Doku](https://holdi601.github.io/3DHeat-Ext-ACRally/) |
| Ext-Reforger | Arma-Reforger-Welten als 3D-Level | [3DHeat-Ext-Reforger](https://github.com/Holdi601/3DHeat-Ext-Reforger) | [Doku](https://holdi601.github.io/3DHeat-Ext-Reforger/) |
| Ext-R6 | Rainbow-Six-Siege-Match-Replays | [3DHeat-Ext-R6](https://github.com/Holdi601/3DHeat-Ext-R6) | [Doku](https://holdi601.github.io/3DHeat-Ext-R6/) |
