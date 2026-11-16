---
title: Home
nav_order: 1
lang: "it"
source: index.md
source_hash: "5942fc0278fa"
nav_exclude: true
search_exclude: true
permalink: /it/
---
# 3DHeat AC Rally {#dheat-ac-rally}

**Che cos'è?** Questo strumento legge una tappa di Assetto Corsa Rally dalla **tua installazione**
e ritaglia il tratto che hai percorso: il terreno della tappa, diviso in strada e terreno e colorato
con il colore che il gioco ha impresso per essa, insieme a barriere, cartelli, edifici e altri
modelli lungo il tuo giro, come un unico percorso 3D per il visualizzatore
[3DHeat](https://github.com/Holdi601/3DHeat) ([documentazione](https://holdi601.github.io/3DHeat/)).

**Perché usarlo?** Per analizzare le tue corse in AC Rally sulla tappa vera - punti di frenata, traiettorie e
curve in 3D - invece che su una linea nel vuoto.

**Esempio:** `heat3d-acrally-maps course my_run.json` -> `my_run.glb`, nello stesso sistema di riferimento del giro:
entra nella scheda Analisi di gara del visualizzatore sotto il giro, senza dover posizionarlo né ridimensionarlo.

## Avvio rapido {#quick-start}

Non hai mai usato la riga di comando? Leggi prima [Prima di iniziare](before-you-start.md).
Ti servono Python 3.10 o successivo, Assetto Corsa Rally, una corsa registrata con quel gioco e
[3DHeat GameFiles](https://holdi601.github.io/3DHeat-GameFiles/) (installato
con questo strumento). Esegui questi comandi nella cartella in cui hai clonato o decompresso lo strumento:

```bash
python -m pip install -e .                      # installa il comando heat3d-acrally-maps
heat3d-acrally-maps stages                      # dove si trova il gioco, e le sue tappe
heat3d-acrally-maps course my_run.json          # il percorso intorno a quella corsa
```

La corsa viene dal registratore 3DHeat GameCapture
([Telemetria: Assetto Corsa](https://holdi601.github.io/3DHeat-GameCapture/telemetry-assetto-corsa.html),
`--game acrally`). `course` trova la tappa e l'orientamento degli assi a partire
dal giro stesso, e termina con `wrote my_run.glb (... bytes)`. Carica il file `.glb`
nel pannello **Sfondo / livello** del visualizzatore con **Modello 3D…**.

Il percorso è costruito a partire dai file del gioco: resta **sul tuo computer**, per
guardarlo, non per condividerlo o pubblicarlo ([Termini](terms.md)).

## Pagine {#pages}

| Pagina | Cosa contiene |
|---|---|
| [Prima di iniziare](before-you-start.md) | Python, GameFiles, Oodle, un terminale, una prima esecuzione |
| [Esportazione del percorso: course](course-assetto-corsa-rally.md) | come una corsa diventa un percorso: l'installazione, la tappa, il sistema di riferimento, il terreno, le texture, i modelli |
| [Trovare il gioco: stages](stages.md) | dove viene trovato Assetto Corsa Rally, cosa stampa `stages` |
| [Che file è questo: identify](identify.md) | i contenitori IoStore propri del gioco |
| [Termini e licenza](terms.md) | i contenuti del gioco, i formati, perché questo è un pacchetto separato |
| [Riferimento dei comandi](../cli-reference.md) | ogni opzione, generata dal codice |
| [Manutenzione di questa documentazione](maintaining.md) | la lista di controllo per ogni rilascio |

## Collegamenti {#related}

- Il visualizzatore 3DHeat: [github.com/Holdi601/3DHeat](https://github.com/Holdi601/3DHeat),
  documentazione su [holdi601.github.io/3DHeat](https://holdi601.github.io/3DHeat/).
- Registrare le corse di AC Rally: il registratore GameCapture,
  [Telemetria: Assetto Corsa](https://holdi601.github.io/3DHeat-GameCapture/telemetry-assetto-corsa.html).
- La libreria su cui si basa questo strumento - i lettori IoStore, pacchetti zen e
  texture di Unreal 5, e Oodle - e il suo comando `course`, che passa a questo strumento
  le corse di AC Rally: [3DHeat GameFiles](https://holdi601.github.io/3DHeat-GameFiles/).

## Gli strumenti 3DHeat {#the-3dheat-tools}

| Strumento | Cosa fa | Codice | Documentazione |
|---|---|---|---|
| Visualizzatore 3DHeat | mostra i dati: mappe di calore, analisi di gara, revisione delle partite | [3DHeat](https://github.com/Holdi601/3DHeat) | [docs](https://holdi601.github.io/3DHeat/) |
| GameFiles | livelli e percorsi dai file propri di un gioco | [3DHeat-GameFiles](https://github.com/Holdi601/3DHeat-GameFiles) | [docs](https://holdi601.github.io/3DHeat-GameFiles/) |
| GameCapture | telemetria dei giri, e livelli ricostruiti dai video di gioco | [3DHeat-GameCapture](https://github.com/Holdi601/3DHeat-GameCapture) | [docs](https://holdi601.github.io/3DHeat-GameCapture/) |
| Unreal Exporter | un plugin per l'Editor di Unreal: un livello come un unico `.glb` | [3DHeat-UnrealExporter](https://github.com/Holdi601/3DHeat-UnrealExporter) | [docs](https://holdi601.github.io/3DHeat-UnrealExporter/) |
| CS2 | demo e mappe di Counter-Strike 2 | [3DHeat-CS2](https://github.com/Holdi601/3DHeat-CS2) | [docs](https://holdi601.github.io/3DHeat-CS2/) |
| Watcher | registra ciò che i giochi pubblicano mentre giochi | [3DHeat-Watcher](https://github.com/Holdi601/3DHeat-Watcher) | [docs](https://holdi601.github.io/3DHeat-Watcher/) |
| Ext-WarThunder | replay di War Thunder | [3DHeat-Ext-WarThunder](https://github.com/Holdi601/3DHeat-Ext-WarThunder) | [docs](https://holdi601.github.io/3DHeat-Ext-WarThunder/) |
| Ext-WoT | replay di World of Tanks | [3DHeat-Ext-WoT](https://github.com/Holdi601/3DHeat-Ext-WoT) | [docs](https://holdi601.github.io/3DHeat-Ext-WoT/) |
| Ext-WoWs | replay di World of Warships | [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs) | [docs](https://holdi601.github.io/3DHeat-Ext-WoWs/) |
| Ext-Squad | demo dei server di Squad | [3DHeat-Ext-Squad](https://github.com/Holdi601/3DHeat-Ext-Squad) | [docs](https://holdi601.github.io/3DHeat-Ext-Squad/) |
| Ext-DCS | mappe di DCS World come livelli 3D | [3DHeat-Ext-DCS](https://github.com/Holdi601/3DHeat-Ext-DCS) | [docs](https://holdi601.github.io/3DHeat-Ext-DCS/) |
| Ext-IL2 | mappe di IL-2 Sturmovik come livelli 3D | [3DHeat-Ext-IL2](https://github.com/Holdi601/3DHeat-Ext-IL2) | [docs](https://holdi601.github.io/3DHeat-Ext-IL2/) |
| Ext-Dota | la mappa di Dota 2 come livello 3D | [3DHeat-Ext-Dota](https://github.com/Holdi601/3DHeat-Ext-Dota) | [docs](https://holdi601.github.io/3DHeat-Ext-Dota/) |
| Ext-DotaReplay | replay di Dota 2 come tabelle | [3DHeat-Ext-DotaReplay](https://github.com/Holdi601/3DHeat-Ext-DotaReplay) | [docs](https://holdi601.github.io/3DHeat-Ext-DotaReplay/) |
| Ext-Riot | replay di League of Legends e VALORANT | [3DHeat-Ext-Riot](https://github.com/Holdi601/3DHeat-Ext-Riot) | [docs](https://holdi601.github.io/3DHeat-Ext-Riot/) |
| Ext-Forza | percorsi e auto di Forza Horizon | [3DHeat-Ext-Forza](https://github.com/Holdi601/3DHeat-Ext-Forza) | [docs](https://holdi601.github.io/3DHeat-Ext-Forza/) |
| Ext-Battlefield | livelli di Battlefield 6 come livelli 3D | [3DHeat-Ext-Battlefield](https://github.com/Holdi601/3DHeat-Ext-Battlefield) | [docs](https://holdi601.github.io/3DHeat-Ext-Battlefield/) |
| Ext-BeamNG | percorsi di BeamNG.drive intorno ai tuoi giri | [3DHeat-Ext-BeamNG](https://github.com/Holdi601/3DHeat-Ext-BeamNG) | [docs](https://holdi601.github.io/3DHeat-Ext-BeamNG/) |
| Ext-ACRally | tappe di Assetto Corsa Rally intorno ai tuoi giri | [3DHeat-Ext-ACRally](https://github.com/Holdi601/3DHeat-Ext-ACRally) | [docs](https://holdi601.github.io/3DHeat-Ext-ACRally/) |
| Ext-Reforger | mondi di Arma Reforger come livelli 3D | [3DHeat-Ext-Reforger](https://github.com/Holdi601/3DHeat-Ext-Reforger) | [docs](https://holdi601.github.io/3DHeat-Ext-Reforger/) |
| Ext-R6 | replay di partite di Rainbow Six Siege | [3DHeat-Ext-R6](https://github.com/Holdi601/3DHeat-Ext-R6) | [docs](https://holdi601.github.io/3DHeat-Ext-R6/) |
