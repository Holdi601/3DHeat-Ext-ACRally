---
title: "Bevor du anfängst"
nav_order: 1.5
lang: "de"
source: before-you-start.md
source_hash: "aa8ae8477336"
nav_exclude: true
search_exclude: true
---
# Bevor du anfängst {#before-you-start}

Noch nie in der Kommandozeile gearbeitet? Diese Seite führt dich von null bis zu einem ersten Lauf.
Es dauert einmal etwa fünfzehn Minuten.

## 1. Python installieren {#install-python}

Dieses Werkzeug braucht **Python 3.10 oder neuer**.

- **Windows:** Lade Python von [python.org/downloads](https://www.python.org/downloads/) herunter
  und starte das Installationsprogramm. Setze auf dem ersten Bildschirm den Haken bei **Add python.exe to PATH**
  und klicke dann auf **Install Now**.
- **macOS und Linux:** Python 3 ist oft schon vorhanden. Wo diese Seiten
  `python` schreiben, tippe `python3`.

## 2. Dieses Werkzeug holen {#get-this-tool}

Öffne [github.com/Holdi601/3DHeat-Ext-ACRally](https://github.com/Holdi601/3DHeat-Ext-ACRally), klicke auf den
grünen Knopf **Code** und dann auf **Download ZIP**, und entpacke es in einen Ordner deiner Wahl. Wenn du git
benutzt: `git clone https://github.com/Holdi601/3DHeat-Ext-ACRally`.

## 3. Ein Terminal in diesem Ordner öffnen {#open-a-terminal-in-that-folder}

Ein Terminal ist ein Fenster, in das du Befehle tippst.

- **Windows:** Öffne den Ordner im Explorer, klicke in die Adresszeile, tippe
  `powershell` und drücke Enter. Ein blau-schwarzes Fenster öffnet sich, schon in
  diesem Ordner.
- **macOS:** Öffne **Terminal**, tippe `cd ` (mit einem Leerzeichen), zieh den Ordner in
  das Fenster und drücke Enter.

`cd` heißt „Ordner wechseln“: `cd C:\Tools\3DHeat-Ext-ACRally` geht in diesen Ordner.

## 4. Das Werkzeug installieren {#install-the-tool}

Tippe das und drücke Enter:

```bash
python -m pip install -e .
```

Dabei wird auch [3DHeat GameFiles](https://holdi601.github.io/3DHeat-GameFiles/) installiert,
die Bibliothek, auf der die Leser aufbauen, sowie numpy und Pillow.
Am Ende solltest du sehen: `Successfully installed ... heat3d-ext-acrally-...`.

Du hast schon eine Kopie von GameFiles? Das Werkzeug findet sie auch ohne pip: in dem
Ordner, den die Umgebungsvariable `HEAT3D_GAMEFILES` nennt, in einer 3DHeat-Kopie
(`exporters/gamefiles`) oder in einem Ordner `3DHeat-GameFiles` neben diesem.

## 5. Prüfen, ob das Spiel gefunden wird {#check-that-the-game-is-found}

```bash
heat3d-acrally-maps stages
```

Du solltest etwa so etwas sehen:

```text
Assetto Corsa Rally at C:\Program Files (x86)\Steam\steamapps\common\Assetto Corsa Rally\acr\Content\Paks
  ExampleStage
  ...
10 stages
```

Der größte Teil der Daten des Spiels ist mit Oodle komprimiert. Oodle ist nicht Teil dieses
Werkzeugs: Gesucht wird die Bibliothek, die das Spiel oder ein anderes installiertes Spiel mitbringt,
auf deinem Rechner, und `HEAT3D_OODLE` kann sie benennen
([Oodle](https://holdi601.github.io/3DHeat-GameFiles/de/reader-oodle.html)).

## 6. Eine Fahrt aufzeichnen, dann ihre Strecke exportieren {#record-a-run-then-export-its-course}

Zeichne eine Fahrt mit dem 3DHeat-GameCapture-Recorder auf
([Telemetrie: Assetto Corsa](https://holdi601.github.io/3DHeat-GameCapture/telemetry-assetto-corsa.html),
`--game acrally`), dann:

```bash
heat3d-acrally-maps course laps\my_run.json
```

Weiter: [Streckenexport](course-assetto-corsa-rally.md).

## So liest du die Befehle auf diesen Seiten {#how-to-read-the-commands-on-these-pages}

| Du siehst | Es bedeutet |
|---|---|
| `<stage map name>` | ein Platzhalter: tippe stattdessen deinen eigenen Wert, ohne die `< >` |
| `[--install FOLDER]` | optional: lass es weg, oder tippe es wie gezeigt |
| `# a note` | ein Kommentar für dich: nicht eintippen |
| `"C:\My Files\x"` | setze einen Pfad mit Leerzeichen in Anführungszeichen |

## Wenn etwas schiefgeht {#when-something-goes-wrong}

| Die Meldung | Was zu tun ist |
|---|---|
| `'python' is not recognized` | Python ist nicht installiert, oder der Haken bei PATH war nicht gesetzt: installiere es erneut und setze den Haken (oder tippe `py` statt `python`). |
| `'heat3d-acrally-maps' is not recognized` | Führe Schritt 4 im Ordner des Werkzeugs noch einmal aus, oder tippe `python -m heat3d_ext_acrally` statt `heat3d-acrally-maps`: es tut dasselbe. |
| `needs 3DHeat GameFiles: ...` | Schritt 4 hat GameFiles nicht installiert: führe `python -m pip install https://github.com/Holdi601/3DHeat-GameFiles/archive/refs/tags/v1.1.0.zip` aus, oder setze `HEAT3D_GAMEFILES` auf einen GameFiles-Ordner. |
| `no Assetto Corsa Rally install found in the Steam libraries` | Gib den Ordner des Spiels an, oder seinen `Content\Paks`: `--install "D:\Games\Assetto Corsa Rally"`. |
| `... is a forza-... lap, not an Assetto Corsa Rally one` | Diese Runde stammt aus einem anderen Spiel; die Meldung nennt das passende Werkzeug dafür. |
| `the lap does not lie on any stage's road in any frame` | Nenne die Etappe: `--level <stage map name>`, so wie `stages` sie auflistet. |
| `no Oodle library found` (oder ähnlich) | Setze `HEAT3D_OODLE` auf eine `oo2core_*.dll`, die schon auf deinem Rechner liegt. |
| alles andere | Lies die letzte Zeile der Meldung und eröffne damit ein Issue auf GitHub. |

Jeder Befehl endet außerdem mit einem **Exitstatus**: 0 heißt, es hat funktioniert; 2, dass das
Spiel, GameFiles, die Etappe oder eine Datei von AC Rally nicht gefunden wurde; 1, dass Lesen oder
Schreiben fehlschlug. Um ihn zu sehen, tippe `echo $LASTEXITCODE` in PowerShell oder `echo $?` unter
macOS und Linux.
