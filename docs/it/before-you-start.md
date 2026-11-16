---
title: "Prima di iniziare"
nav_order: 1.5
lang: "it"
source: before-you-start.md
source_hash: "10b9fc801b7a"
nav_exclude: true
search_exclude: true
---
# Prima di iniziare {#before-you-start}

Non hai mai usato la riga di comando? Questa pagina ti porta da zero alla prima esecuzione.
Ci vogliono circa quindici minuti, una volta sola.

## 1. Installa Python {#install-python}

Questo strumento richiede **Python 3.10 o successivo**.

- **Windows:** scarica Python da [python.org/downloads](https://www.python.org/downloads/)
  ed esegui il programma di installazione. Nella sua prima schermata spunta **Add python.exe to PATH**,
  poi clicca **Install Now**.
- **macOS e Linux:** Python 3 spesso è già presente. Dove queste pagine dicono
  `python`, scrivi `python3`.

## 2. Ottieni questo strumento {#get-this-tool}

Apri [github.com/Holdi601/3DHeat-Ext-ACRally](https://github.com/Holdi601/3DHeat-Ext-ACRally), clicca il
pulsante verde **Code**, poi **Download ZIP**, e decomprimilo in una cartella a tua scelta. Se usi git:
`git clone https://github.com/Holdi601/3DHeat-Ext-ACRally`.

## 3. Apri un terminale in quella cartella {#open-a-terminal-in-that-folder}

Un terminale è una finestra in cui scrivi i comandi.

- **Windows:** apri la cartella in Esplora file, clicca nella barra degli indirizzi, scrivi
  `powershell` e premi Invio. Si apre una finestra blu o nera, già dentro quella cartella.
- **macOS:** apri **Terminale**, scrivi `cd ` (con uno spazio), trascina la cartella
  nella finestra e premi Invio.

`cd` vuol dire "cambia cartella": `cd C:\Strumenti\3DHeat-Ext-ACRally` va in quella cartella.

## 4. Installa lo strumento {#install-the-tool}

Scrivi questo e premi Invio:

```bash
python -m pip install -e .
```

Installa anche [3DHeat GameFiles](https://holdi601.github.io/3DHeat-GameFiles/),
la libreria su cui si basano i lettori, più numpy e Pillow.
Alla fine dovresti vedere: `Successfully installed ... heat3d-ext-acrally-...`.

Hai già una copia di GameFiles? Lo strumento la trova anche senza pip: nella cartella
indicata dalla variabile d'ambiente `HEAT3D_GAMEFILES`, dentro una copia di 3DHeat
(`exporters/gamefiles`), oppure in una cartella `3DHeat-GameFiles` accanto a questa.

## 5. Controlla che il gioco venga trovato {#check-that-the-game-is-found}

```bash
heat3d-acrally-maps stages
```

Dovresti vedere qualcosa di simile:

```text
Assetto Corsa Rally at C:\Program Files (x86)\Steam\steamapps\common\Assetto Corsa Rally\acr\Content\Paks
  ExampleStage
  ...
10 stages
```

La maggior parte dei dati del gioco è compressa con Oodle. Oodle non fa parte di questo strumento:
si cerca sul tuo computer la libreria che il gioco o un altro gioco installato include, e
`HEAT3D_OODLE` può indicarne il percorso
([Oodle](https://holdi601.github.io/3DHeat-GameFiles/reader-oodle.html)).

## 6. Registra una corsa, poi esporta il suo percorso {#record-a-run-then-export-its-course}

Registra una corsa con il registratore 3DHeat GameCapture
([Telemetria: Assetto Corsa](https://holdi601.github.io/3DHeat-GameCapture/telemetry-assetto-corsa.html),
`--game acrally`), poi:

```bash
heat3d-acrally-maps course laps\my_run.json
```

Prossimo passo: [Esportazione del percorso](course-assetto-corsa-rally.md).

## Come leggere i comandi di queste pagine {#how-to-read-the-commands-on-these-pages}

| Vedi | Significa |
|---|---|
| `<stage map name>` | un segnaposto: scrivi il tuo valore al suo posto, senza i `< >` |
| `[--install FOLDER]` | facoltativo: puoi ometterlo, oppure scriverlo come mostrato |
| `# a note` | un commento per te: non scriverlo |
| `"C:\My Files\x"` | metti tra virgolette un percorso che contiene spazi |

## Quando qualcosa va storto {#when-something-goes-wrong}

| Il messaggio | Cosa fare |
|---|---|
| `'python' is not recognized` | Python non è installato, oppure non hai spuntato la casella PATH: installalo di nuovo e spuntala (oppure scrivi `py` al posto di `python`). |
| `'heat3d-acrally-maps' is not recognized` | Ripeti il passo 4 nella cartella dello strumento, oppure scrivi `python -m heat3d_ext_acrally` al posto di `heat3d-acrally-maps`: fa lo stesso. |
| `needs 3DHeat GameFiles: ...` | Il passo 4 non ha installato GameFiles: esegui `python -m pip install git+https://github.com/Holdi601/3DHeat-GameFiles.git`, oppure imposta `HEAT3D_GAMEFILES` su una cartella di GameFiles. |
| `no Assetto Corsa Rally install found in the Steam libraries` | Indica la cartella del gioco, oppure la sua `Content\Paks`: `--install "D:\Games\Assetto Corsa Rally"`. |
| `... is a forza-... lap, not an Assetto Corsa Rally one` | Quel giro viene da un altro gioco; il messaggio indica lo strumento giusto per quello. |
| `the lap does not lie on any stage's road in any frame` | Indica la tappa: `--level <stage map name>`, come la elenca `stages`. |
| `no Oodle library found` (o simile) | Imposta `HEAT3D_OODLE` su un file `oo2core_*.dll` già presente sul tuo computer. |
| qualsiasi altra cosa | Leggi l'ultima riga del messaggio, poi apri una segnalazione su GitHub con quella riga. |

Ogni comando termina anche con uno **stato di uscita**: 0 vuol dire che ha funzionato, 2 che
non è stato trovato il gioco, GameFiles, la tappa o un file di AC Rally, 1 che la lettura o la scrittura
non è riuscita. Per vederlo, scrivi `echo $LASTEXITCODE` in PowerShell, oppure `echo $?` su
macOS e Linux.
