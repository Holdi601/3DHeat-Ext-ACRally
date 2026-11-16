---
title: "Trovare il gioco: stages"
nav_order: 3
lang: "it"
source: stages.md
source_hash: "742bf8ee97f7"
nav_exclude: true
search_exclude: true
---
# Trovare il gioco: `stages` {#finding-the-game-stages}

```bash
heat3d-acrally-maps stages [--install FOLDER]
```

stampa dove si trovano i contenitori di Assetto Corsa Rally e ogni tappa che contengono,
con il nome di mappa che accetta `course --level`. Eseguilo per primo: quando elenca le tappe e
termina con 0, [`course`](course-assetto-corsa-rally.md) ha il gioco di cui ha bisogno.

```text
Assetto Corsa Rally at C:\Program Files (x86)\Steam\steamapps\common\Assetto Corsa Rally\acr\Content\Paks
  ExampleStage
  ...
10 stages
```

Un livello conta come tappa quando la sua cartella di ambiente,
`Content\Environments\<Stage>\`, contiene una cartella `MeshesTrack` (le tessere di strada
della tappa); menu e altri livelli sono esclusi.

## Dove viene cercato il gioco {#where-the-game-is-looked-for}

Per prima cosa `--install`: la cartella del gioco, la sua `Content\Paks`, oppure qualsiasi cartella che contiene
file `.utoc`. Lo strumento controlla `<folder>`, poi `<folder>\acr\Content\Paks`,
poi `<folder>\Content\Paks`. Senza di esso, `steamapps\common\Assetto Corsa Rally` in
ogni libreria di Steam, controllata allo stesso modo. Anche `course` cerca nello stesso
posto.

Elencare le tappe legge solo le tabelle dei contenuti dei contenitori, quindi non serve
nessuna libreria Oodle; esportare un percorso sì
([Oodle](https://holdi601.github.io/3DHeat-GameFiles/reader-oodle.html)).

## Messaggi e stato di uscita {#messages-and-exit-status}

| Messaggio | Uscita | Significa |
|---|---|---|
| `heat3d-acrally-maps: no Assetto Corsa Rally install found in the Steam libraries. ...` | 2 | installa il gioco tramite Steam, oppure passa `--install` |
| `heat3d-acrally-maps: no Assetto Corsa Rally containers (.utoc) in <folder> ...` | 2 | `--install` punta a un posto senza i contenitori del gioco |
| `0 stages` | 2 | i contenitori si aprono ma non contengono nessuna tappa |
| `heat3d-acrally-maps: <reason>` | 1 | i contenitori non si sono potuti leggere (uno cifrato, per esempio) |
