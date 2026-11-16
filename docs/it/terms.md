---
title: "Termini e licenza"
nav_order: 9
lang: "it"
source: terms.md
source_hash: "d94bf4eca099"
nav_exclude: true
search_exclude: true
---
# Termini e licenza {#terms-and-licence}

## I contenuti del gioco {#the-games-content}

Assetto Corsa Rally e le sue tappe appartengono al suo sviluppatore, Kunos Simulazioni,
e al suo editore, 505 Games, che non approvano questo progetto. Questo strumento non include
nulla del gioco e non scarica nulla: legge i file della copia **che hai** installato, sul tuo computer,
al di fuori del gioco. Non modifica nulla nel gioco e non comunica con nessun server. Un percorso
che scrive è una derivazione della tappa del gioco: è tuo per analizzare le tue corse,
non per condividerlo o pubblicarlo. Usare lo strumento è una tua decisione, secondo i termini che
hai accettato per il gioco.

Per questo è un pacchetto separato: se i proprietari del gioco dovessero chiederne la rimozione, va via da solo,
e il visualizzatore, GameFiles e gli altri strumenti restano.

Si applicano qui, invariate, le regole di 3DHeat GameFiles
([Regole e licenze](https://holdi601.github.io/3DHeat-GameFiles/rules-and-licences.html)):

- **Nessuna chiave: nessuna fornita, nessuna recuperata.** Nessuno dei contenitori del gioco è cifrato;
  un contenitore IoStore cifrato viene rifiutato senza eccezioni.
- **I tuoi file, la tua responsabilità.** Lo strumento legge i file di gioco installati sul tuo
  computer. Non scarica mai contenuti di gioco.
- **L'output non è da ridistribuire.** Conserva i file `.glb` esportati, e le texture al loro interno,
  per la tua analisi. Non pubblicare, condividere né vendere percorsi, livelli, modelli o texture esportati. Il
  file `.gitignore` del repository tiene fuori dal controllo di versione i file di gioco, le esportazioni e i giri.

## Oodle si trova, non è incluso {#oodle-is-found-not-bundled}

Oodle (RAD Game Tools, ora Epic) è proprietario e non esiste una build ridistribuibile.
`oo2core_*.dll` è concesso in licenza al prodotto che lo distribuisce. Per questo
3DHeat GameFiles carica una libreria già presente sulla macchina invece di includerne una, e
anche questo strumento non ne include nessuna
([Oodle](https://holdi601.github.io/3DHeat-GameFiles/reader-oodle.html)).

## I formati {#the-formats}

Il gioco è Unreal Engine 5. I suoi contenitori e pacchetti sono letti dai lettori Unreal di
3DHeat GameFiles. I dati di proprietà compilati di Unreal 5 richiedono l'elenco delle proprietà di ogni
classe. Gli elenchi in `unversioned.py` di GameFiles contengono **solo nomi e tipi**, fatti sul formato
come quelli di un file di mappatura di interoperabilità. Sono stati ricavati dalle intestazioni del motore Unreal che
Epic mette a disposizione di chiunque abbia un account collegato, e verificati sui dati distribuiti.
Nessun codice sorgente del motore è incluso o richiesto. Ciò che lo strumento aggiunge - dove si trova una tappa,
come i suoi componenti posizionano le mesh, come sono orientati gli assi di un giro - è stato ricavato dal
gioco installato ([Esportazione del percorso](course-assetto-corsa-rally.md)).

## Licenza e fonti {#licence-and-sources}

MIT ([`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-ACRally/blob/main/LICENSE)).
Richiede 3DHeat GameFiles (MIT) e numpy (BSD-3-Clause); i test richiedono pytest
(MIT). Vedi
[`LICENSES.md`](https://github.com/Holdi601/3DHeat-Ext-ACRally/blob/main/LICENSES.md).
Scritto per questo progetto; non è stato preso codice da nessun altro progetto.
