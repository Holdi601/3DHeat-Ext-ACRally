---
title: "Finding the game: stages"
nav_order: 3
---

# Finding the game: `stages`

```bash
heat3d-acrally-maps stages [--install FOLDER]
```

prints where Assetto Corsa Rally's containers are and every stage they hold,
by the map name `course --level` takes. Run it first: when it lists stages and
exits with 0, [`course`](course-assetto-corsa-rally.md) has the game it needs.

```text
Assetto Corsa Rally at C:\Program Files (x86)\Steam\steamapps\common\Assetto Corsa Rally\acr\Content\Paks
  ExampleStage
  ...
10 stages
```

A level counts as a stage when its environment folder,
`Content\Environments\<Stage>\`, has a `MeshesTrack` folder (the stage's road
tiles); menus and other levels are left out.

## Where the game is looked for

`--install` first: the game's folder, its `Content\Paks`, or any folder holding
`.utoc` files. The tool checks `<folder>`, then `<folder>\acr\Content\Paks`,
then `<folder>\Content\Paks`. Without it, `steamapps\common\Assetto Corsa Rally`
in every Steam library, checked the same way. `course` looks in the same
places.

Listing the stages reads only the containers' tables of contents, so it needs
no Oodle library; exporting a course does
([Oodle](https://holdi601.github.io/3DHeat-GameFiles/reader-oodle.html)).

## Messages and exit status

| Message | Exit | Means |
|---|---|---|
| `heat3d-acrally-maps: no Assetto Corsa Rally install found in the Steam libraries. ...` | 2 | install the game through Steam, or pass `--install` |
| `heat3d-acrally-maps: no Assetto Corsa Rally containers (.utoc) in <folder> ...` | 2 | `--install` points somewhere without the game's containers |
| `0 stages` | 2 | the containers open but hold no stage |
| `heat3d-acrally-maps: <reason>` | 1 | the containers could not be read (an encrypted one, say) |
