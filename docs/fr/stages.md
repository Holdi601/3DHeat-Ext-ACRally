---
title: "Trouver le jeu : stages"
nav_order: 3
lang: "fr"
source: stages.md
source_hash: "742bf8ee97f7"
nav_exclude: true
search_exclude: true
---
# Trouver le jeu : `stages` {#finding-the-game-stages}

```bash
heat3d-acrally-maps stages [--install FOLDER]
```

affiche où se trouvent les conteneurs d'Assetto Corsa Rally et chaque étape qu'ils
contiennent, sous le nom de carte que prend `course --level`. Lancez-la en premier : quand
elle liste des étapes et se termine avec le code 0, [`course`](course-assetto-corsa-rally.md)
dispose du jeu dont il a besoin.

```text
Assetto Corsa Rally at C:\Program Files (x86)\Steam\steamapps\common\Assetto Corsa Rally\acr\Content\Paks
  ExampleStage
  ...
10 stages
```

Un niveau compte comme étape quand son dossier d'environnement,
`Content\Environments\<Stage>\`, contient un dossier `MeshesTrack` (les tuiles de route
de l'étape) ; les menus et les autres niveaux sont laissés de côté.

## Où le jeu est cherché {#where-the-game-is-looked-for}

D'abord `--install` : le dossier du jeu, son `Content\Paks`, ou tout dossier contenant des
fichiers `.utoc`. L'outil vérifie `<dossier>`, puis `<dossier>\acr\Content\Paks`, puis
`<dossier>\Content\Paks`. Sans cette option, il cherche `steamapps\common\Assetto Corsa Rally`
dans chaque bibliothèque Steam, en vérifiant de la même façon. `course` cherche aux mêmes
endroits.

Lister les étapes ne lit que les tables des matières des conteneurs : aucune bibliothèque
Oodle n'est nécessaire ; l'export d'un parcours, lui, en a besoin
([Oodle](https://holdi601.github.io/3DHeat-GameFiles/reader-oodle.html)).

## Messages et code de sortie {#messages-and-exit-status}

| Message | Sortie | Signification |
|---|---|---|
| `heat3d-acrally-maps: no Assetto Corsa Rally install found in the Steam libraries. ...` | 2 | installez le jeu via Steam, ou passez `--install` |
| `heat3d-acrally-maps: no Assetto Corsa Rally containers (.utoc) in <folder> ...` | 2 | `--install` pointe vers un endroit sans les conteneurs du jeu |
| `0 stages` | 2 | les conteneurs s'ouvrent mais ne contiennent aucune étape |
| `heat3d-acrally-maps: <reason>` | 1 | les conteneurs n'ont pas pu être lus (un conteneur chiffré, par exemple) |
