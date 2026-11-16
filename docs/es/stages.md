---
title: "Encontrar el juego: stages"
nav_order: 3
lang: "es"
source: stages.md
source_hash: "742bf8ee97f7"
nav_exclude: true
search_exclude: true
---
# Encontrar el juego: `stages` {#finding-the-game-stages}

```bash
heat3d-acrally-maps stages [--install FOLDER]
```

muestra dónde están los contenedores de Assetto Corsa Rally y cada escenario que contienen,
con el nombre de mapa que acepta `course --level`. Ejecútalo primero: cuando lista escenarios y
sale con código 0, [`course`](course-assetto-corsa-rally.md) ya tiene el juego que necesita.

```text
Assetto Corsa Rally at C:\Program Files (x86)\Steam\steamapps\common\Assetto Corsa Rally\acr\Content\Paks
  ExampleStage
  ...
10 stages
```

Un nivel cuenta como escenario cuando su carpeta de entorno,
`Content\Environments\<Stage>\`, tiene una carpeta `MeshesTrack` (las piezas de carretera del
escenario); los menús y otros niveles se dejan fuera.

## Dónde se busca el juego {#where-the-game-is-looked-for}

Primero `--install`: la carpeta del juego, su `Content\Paks`, o cualquier carpeta que contenga
archivos `.utoc`. La herramienta revisa `<folder>`, luego `<folder>\acr\Content\Paks`,
y luego `<folder>\Content\Paks`. Sin esta opción, busca `steamapps\common\Assetto Corsa Rally`
en cada biblioteca de Steam, comprobando lo mismo. `course` busca en los mismos
lugares.

Listar los escenarios solo lee las tablas de contenido de los contenedores, así que no
necesita una biblioteca Oodle; exportar un recorrido sí
([Oodle](https://holdi601.github.io/3DHeat-GameFiles/reader-oodle.html)).

## Mensajes y código de salida {#messages-and-exit-status}

| Mensaje | Salida | Significa |
|---|---|---|
| `heat3d-acrally-maps: no Assetto Corsa Rally install found in the Steam libraries. ...` | 2 | instala el juego a través de Steam, o indica `--install` |
| `heat3d-acrally-maps: no Assetto Corsa Rally containers (.utoc) in <folder> ...` | 2 | `--install` apunta a un lugar sin los contenedores del juego |
| `0 stages` | 2 | los contenedores se abren pero no contienen ningún escenario |
| `heat3d-acrally-maps: <reason>` | 1 | no se pudieron leer los contenedores (uno cifrado, por ejemplo) |
