---
title: "¿Qué es este archivo?: identify"
nav_order: 4
lang: "es"
source: identify.md
source_hash: "6735d5facfac"
nav_exclude: true
search_exclude: true
---
# ¿Qué es este archivo?: `identify` {#what-is-this-file-identify}

```bash
heat3d-acrally-maps identify <path>
```

indica si un archivo es uno de los contenedores propios de Assetto Corsa Rally. El juego
trae su contenido en contenedores IoStore de Unreal 5, un formato del motor que
comparten muchos juegos; lo que es propio del juego es el lugar donde se montan, su
carpeta de proyecto `acr`. Así, una tabla de contenidos (`.utoc`) montada en `.../acr/Content/`
se reconoce, con los niveles que contiene:

```text
pakchunk0-Windows.utoc  (1,234 bytes)
  Assetto Corsa Rally IoStore container, mounted at ../../../acr/Content/
    files      4
    levels     ExampleStage, Menu
```

Cualquier otro archivo, incluidos los contenedores de otros juegos, muestra
`not an Assetto Corsa Rally file: <name>` en la salida de error y sale con código 2;
un archivo que no existe muestra `no such file` y sale con código 2. El propio
`identify` de 3DHeat GameFiles describe cualquier contenedor IoStore, también los de este
juego ([Unreal 5 IoStore](https://holdi601.github.io/3DHeat-GameFiles/reader-unreal-iostore.html)).
