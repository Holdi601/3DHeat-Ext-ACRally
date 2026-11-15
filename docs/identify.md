---
title: "What is this file: identify"
nav_order: 4
---

# What is this file: `identify`

```bash
heat3d-acrally-maps identify <path>
```

says whether a file is one of Assetto Corsa Rally's own containers. The game
ships its content as Unreal 5 IoStore containers, an engine format many games
share; what is the game's own is where they are mounted, its project folder
`acr`. So a table of contents (`.utoc`) mounted at `.../acr/Content/` is
recognised, with the levels it holds:

```text
pakchunk0-Windows.utoc  (1,234 bytes)
  Assetto Corsa Rally IoStore container, mounted at ../../../acr/Content/
    files      4
    levels     ExampleStage, Menu
```

Anything else - another game's containers included - prints
`not an Assetto Corsa Rally file: <name>` on the error output and exits
with 2; a file that is not there says `no such file` and exits with 2. 3DHeat
GameFiles' own `identify` describes any IoStore container, this game's
included ([Unreal 5 IoStore](https://holdi601.github.io/3DHeat-GameFiles/reader-unreal-iostore.html)).
