---
title: "Das Spiel finden: stages"
nav_order: 3
lang: "de"
source: stages.md
source_hash: "742bf8ee97f7"
nav_exclude: true
search_exclude: true
---
# Das Spiel finden: `stages` {#finding-the-game-stages}

```bash
heat3d-acrally-maps stages [--install FOLDER]
```

zeigt, wo die Container von Assetto Corsa Rally liegen, und jede Etappe, die sie enthalten, unter dem
Kartennamen, den `course --level` nimmt. Führe es zuerst aus: Wenn es Etappen auflistet und mit 0 endet,
hat [`course`](course-assetto-corsa-rally.md) das Spiel, das es braucht.

```text
Assetto Corsa Rally at C:\Program Files (x86)\Steam\steamapps\common\Assetto Corsa Rally\acr\Content\Paks
  ExampleStage
  ...
10 stages
```

Ein Level zählt als Etappe, wenn sein Umgebungsordner `Content\Environments\<Stage>\` einen Ordner
`MeshesTrack` hat (die Fahrbahnkacheln der Etappe); Menüs und andere Level bleiben weg.

## Wo nach dem Spiel gesucht wird {#where-the-game-is-looked-for}

Zuerst `--install`: der Ordner des Spiels, sein `Content\Paks` oder jeder Ordner mit `.utoc`-Dateien.
Das Werkzeug prüft `<folder>`, dann `<folder>\acr\Content\Paks`, dann `<folder>\Content\Paks`. Ohne
`--install` `steamapps\common\Assetto Corsa Rally` in jeder Steam-Bibliothek, mit derselben Prüfung.
`course` sucht an denselben Stellen.

Das Auflisten der Etappen liest nur die Inhaltsverzeichnisse der Container, es braucht also keine
Oodle-Bibliothek; der Export einer Strecke braucht sie
([Oodle](https://holdi601.github.io/3DHeat-GameFiles/de/reader-oodle.html)).

## Meldungen und Exitstatus {#messages-and-exit-status}

| Meldung | Exit | Bedeutung |
|---|---|---|
| `heat3d-acrally-maps: no Assetto Corsa Rally install found in the Steam libraries. ...` | 2 | installiere das Spiel über Steam, oder gib `--install` an |
| `heat3d-acrally-maps: no Assetto Corsa Rally containers (.utoc) in <folder> ...` | 2 | `--install` zeigt auf einen Ort ohne die Container des Spiels |
| `0 stages` | 2 | die Container öffnen sich, enthalten aber keine Etappe |
| `heat3d-acrally-maps: <reason>` | 1 | die Container konnten nicht gelesen werden (zum Beispiel ein verschlüsselter) |
