---
title: "Che file è questo: identify"
nav_order: 4
lang: "it"
source: identify.md
source_hash: "6735d5facfac"
nav_exclude: true
search_exclude: true
---
# Che file è questo: `identify` {#what-is-this-file-identify}

```bash
heat3d-acrally-maps identify <path>
```

dice se un file è uno dei contenitori propri di Assetto Corsa Rally. Il gioco distribuisce i suoi
contenuti come contenitori IoStore di Unreal 5, un formato del motore che molti giochi
condividono; ciò che è del gioco è dove vengono montati, nella sua cartella di progetto
`acr`. Quindi un indice (`.utoc`) montato in `.../acr/Content/` viene riconosciuto, con i livelli che contiene:

```text
pakchunk0-Windows.utoc  (1,234 bytes)
  Assetto Corsa Rally IoStore container, mounted at ../../../acr/Content/
    files      4
    levels     ExampleStage, Menu
```

Qualsiasi altra cosa, compresi i contenitori di altri giochi, stampa
`not an Assetto Corsa Rally file: <name>` sull'uscita degli errori e termina con 2; un file che non
esiste risponde `no such file` e termina con 2. Lo strumento `identify` di 3DHeat
GameFiles descrive qualsiasi contenitore IoStore, anche quelli di questo gioco
([Unreal 5 IoStore](https://holdi601.github.io/3DHeat-GameFiles/reader-unreal-iostore.html)).
