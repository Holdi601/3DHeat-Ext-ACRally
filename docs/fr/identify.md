---
title: "Quel est ce fichier : identify"
nav_order: 4
lang: "fr"
source: identify.md
source_hash: "6735d5facfac"
nav_exclude: true
search_exclude: true
---
# Quel est ce fichier : `identify` {#what-is-this-file-identify}

```bash
heat3d-acrally-maps identify <path>
```

indique si un fichier est l'un des conteneurs propres à Assetto Corsa Rally.
Le jeu livre son contenu sous forme de conteneurs IoStore d'Unreal 5, un format
de moteur que beaucoup de jeux partagent ; ce qui appartient au jeu, c'est l'endroit
où ils sont montés, leur dossier de projet `acr`. Une table des matières (`.utoc`)
montée dans `.../acr/Content/` est donc reconnue, avec les niveaux qu'elle contient :

```text
pakchunk0-Windows.utoc  (1,234 bytes)
  Assetto Corsa Rally IoStore container, mounted at ../../../acr/Content/
    files      4
    levels     ExampleStage, Menu
```

Tout le reste, y compris les conteneurs d'un autre jeu, affiche
`not an Assetto Corsa Rally file: <name>` sur la sortie d'erreur et se termine
avec le code 2 ; un fichier absent affiche `no such file` et se termine avec le code 2.
La commande `identify` de 3DHeat GameFiles décrit n'importe quel conteneur IoStore,
celui de ce jeu compris
([Unreal 5 IoStore](https://holdi601.github.io/3DHeat-GameFiles/reader-unreal-iostore.html)).
