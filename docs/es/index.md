---
title: Inicio
nav_order: 1
lang: "es"
source: index.md
source_hash: "01ac13b57f23"
nav_exclude: true
search_exclude: true
permalink: /es/
---
# 3DHeat AC Rally {#dheat-ac-rally}

**¿Qué es?** Esta herramienta lee un escenario de Assetto Corsa Rally desde **tu propia
instalación** y recorta el tramo que condujiste: el suelo del escenario, dividido en carretera y
terreno y coloreado con el color que el juego le asignó, junto con las barreras, señales, edificios y
demás modelos a lo largo de tu vuelta, todo como un recorrido 3D para el
visor [3DHeat](https://github.com/Holdi601/3DHeat)
([documentación](https://holdi601.github.io/3DHeat/)).

**¿Para qué sirve?** Para analizar tus vueltas en AC Rally sobre el escenario real: puntos de
frenada, trazadas y curvas en 3D, en lugar de sobre una línea en un espacio vacío.

**Ejemplo:** `heat3d-acrally-maps course my_run.json` -> `my_run.glb`, en el mismo sistema de
coordenadas que la vuelta: se coloca en la pestaña Análisis de carrera del visor, bajo la vuelta,
sin tener que alinearlo ni escalarlo.

## Inicio rápido {#quick-start}

¿Nunca has usado la línea de comandos? Lee primero [Antes de empezar](before-you-start.md).
Necesitas Python 3.10 o posterior, Assetto Corsa Rally, una vuelta grabada en él y
[3DHeat GameFiles](https://holdi601.github.io/3DHeat-GameFiles/) (que se instala
con esta herramienta). Ejecuta estos comandos en la carpeta donde clonaste o descomprimiste el proyecto:

```bash
python -m pip install -e .                      # installs the heat3d-acrally-maps command
heat3d-acrally-maps stages                      # where the game is, and its stages
heat3d-acrally-maps course my_run.json          # the course around that run
```

La vuelta procede del grabador 3DHeat GameCapture
([Telemetría: Assetto Corsa](https://holdi601.github.io/3DHeat-GameCapture/telemetry-assetto-corsa.html),
`--game acrally`). `course` encuentra el escenario y la orientación de los ejes de la vuelta a partir de la
propia vuelta, y termina con `wrote my_run.glb (... bytes)`. Carga el `.glb` en el panel
**Fondo / nivel** del visor con **Modelo 3D…**.

El recorrido se construye con los archivos del juego: se queda en **tu equipo**, para verlo, no para
compartirlo ni publicarlo ([Condiciones](terms.md)).

Cada lector de juego es un pequeño proyecto propio, con su propio archivo de licencia, sus propias versiones y su propio gestor de incidencias, de modo que puede instalarse, actualizarse, mantenerse - o retirarse a petición de un titular de derechos - por separado, sin afectar al visor ni a las demás herramientas.

## Páginas {#pages}

| Página | Qué cubre |
|---|---|
| [Antes de empezar](before-you-start.md) | Python, GameFiles, Oodle, una terminal, una primera ejecución |
| [Exportar el recorrido: course](course-assetto-corsa-rally.md) | cómo se convierte una vuelta en un recorrido: la instalación, el escenario, el marco, el suelo, la textura, los modelos |
| [Encontrar el juego: stages](stages.md) | dónde se encuentra Assetto Corsa Rally, qué muestra `stages` |
| [¿Qué es este archivo?: identify](identify.md) | los contenedores IoStore propios del juego |
| [Condiciones y licencia](terms.md) | el contenido del juego, los formatos, un proyecto propio |
| [Referencia de comandos](../cli-reference.md) | cada opción, generada a partir del código |
| [Mantenimiento de esta documentación](maintaining.md) | la lista de comprobaciones de cada versión |

## Relacionado {#related}

- El visor 3DHeat: [github.com/Holdi601/3DHeat](https://github.com/Holdi601/3DHeat),
  documentación en [holdi601.github.io/3DHeat](https://holdi601.github.io/3DHeat/).
- Grabar vueltas de AC Rally: el grabador GameCapture,
  [Telemetría: Assetto Corsa](https://holdi601.github.io/3DHeat-GameCapture/telemetry-assetto-corsa.html).
- La biblioteca en la que se basa esta herramienta (los lectores de IoStore, paquetes zen y texturas
  de Unreal 5, y Oodle) y su comando `course`, que entrega las vueltas de AC Rally a esta
  herramienta: [3DHeat GameFiles](https://holdi601.github.io/3DHeat-GameFiles/).

## Las herramientas de 3DHeat {#the-3dheat-tools}

| Herramienta | Qué hace | Código | Documentación |
|---|---|---|---|
| Visor 3DHeat | muestra los datos: mapas de calor, análisis de carreras, revisión de partidas | [3DHeat](https://github.com/Holdi601/3DHeat) | [docs](https://holdi601.github.io/3DHeat/) |
| GameFiles | niveles y recorridos a partir de los archivos propios de cada juego | [3DHeat-GameFiles](https://github.com/Holdi601/3DHeat-GameFiles) | [docs](https://holdi601.github.io/3DHeat-GameFiles/) |
| GameCapture | telemetría de vueltas, y niveles reconstruidos a partir de vídeo de juego | [3DHeat-GameCapture](https://github.com/Holdi601/3DHeat-GameCapture) | [docs](https://holdi601.github.io/3DHeat-GameCapture/) |
| Unreal Exporter | un plugin para el editor de Unreal: un nivel como un solo `.glb` | [3DHeat-UnrealExporter](https://github.com/Holdi601/3DHeat-UnrealExporter) | [docs](https://holdi601.github.io/3DHeat-UnrealExporter/) |
| CS2 | demos y mapas de Counter-Strike 2 | [3DHeat-CS2](https://github.com/Holdi601/3DHeat-CS2) | [docs](https://holdi601.github.io/3DHeat-CS2/) |
| Watcher | registra lo que los juegos publican mientras juegas | [3DHeat-Watcher](https://github.com/Holdi601/3DHeat-Watcher) | [docs](https://holdi601.github.io/3DHeat-Watcher/) |
| Ext-WarThunder | repeticiones de War Thunder | [3DHeat-Ext-WarThunder](https://github.com/Holdi601/3DHeat-Ext-WarThunder) | [docs](https://holdi601.github.io/3DHeat-Ext-WarThunder/) |
| Ext-WoT | repeticiones de World of Tanks | [3DHeat-Ext-WoT](https://github.com/Holdi601/3DHeat-Ext-WoT) | [docs](https://holdi601.github.io/3DHeat-Ext-WoT/) |
| Ext-WoWs | repeticiones de World of Warships | [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs) | [docs](https://holdi601.github.io/3DHeat-Ext-WoWs/) |
| Ext-Squad | demos de servidores de Squad | [3DHeat-Ext-Squad](https://github.com/Holdi601/3DHeat-Ext-Squad) | [docs](https://holdi601.github.io/3DHeat-Ext-Squad/) |
| Ext-DCS | mapas de DCS World como niveles 3D | [3DHeat-Ext-DCS](https://github.com/Holdi601/3DHeat-Ext-DCS) | [docs](https://holdi601.github.io/3DHeat-Ext-DCS/) |
| Ext-IL2 | mapas de IL-2 Sturmovik como niveles 3D | [3DHeat-Ext-IL2](https://github.com/Holdi601/3DHeat-Ext-IL2) | [docs](https://holdi601.github.io/3DHeat-Ext-IL2/) |
| Ext-Dota | el mapa de Dota 2 como nivel 3D | [3DHeat-Ext-Dota](https://github.com/Holdi601/3DHeat-Ext-Dota) | [docs](https://holdi601.github.io/3DHeat-Ext-Dota/) |
| Ext-DotaReplay | repeticiones de Dota 2 como tablas | [3DHeat-Ext-DotaReplay](https://github.com/Holdi601/3DHeat-Ext-DotaReplay) | [docs](https://holdi601.github.io/3DHeat-Ext-DotaReplay/) |
| Ext-Riot | repeticiones de League of Legends y VALORANT | [3DHeat-Ext-Riot](https://github.com/Holdi601/3DHeat-Ext-Riot) | [docs](https://holdi601.github.io/3DHeat-Ext-Riot/) |
| Ext-Forza | recorridos y coches de Forza Horizon | [3DHeat-Ext-Forza](https://github.com/Holdi601/3DHeat-Ext-Forza) | [docs](https://holdi601.github.io/3DHeat-Ext-Forza/) |
| Ext-Battlefield | niveles de Battlefield 6 como niveles 3D | [3DHeat-Ext-Battlefield](https://github.com/Holdi601/3DHeat-Ext-Battlefield) | [docs](https://holdi601.github.io/3DHeat-Ext-Battlefield/) |
| Ext-BeamNG | recorridos de BeamNG.drive alrededor de tus vueltas | [3DHeat-Ext-BeamNG](https://github.com/Holdi601/3DHeat-Ext-BeamNG) | [docs](https://holdi601.github.io/3DHeat-Ext-BeamNG/) |
| Ext-ACRally | escenarios de Assetto Corsa Rally alrededor de tus vueltas | [3DHeat-Ext-ACRally](https://github.com/Holdi601/3DHeat-Ext-ACRally) | [docs](https://holdi601.github.io/3DHeat-Ext-ACRally/) |
| Ext-Reforger | mundos de Arma Reforger como niveles 3D | [3DHeat-Ext-Reforger](https://github.com/Holdi601/3DHeat-Ext-Reforger) | [docs](https://holdi601.github.io/3DHeat-Ext-Reforger/) |
| Ext-R6 | repeticiones de partidas de Rainbow Six Siege | [3DHeat-Ext-R6](https://github.com/Holdi601/3DHeat-Ext-R6) | [docs](https://holdi601.github.io/3DHeat-Ext-R6/) |
