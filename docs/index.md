---
title: Home
nav_order: 1
---

# 3DHeat AC Rally

**What is it?** This tool reads an Assetto Corsa Rally stage from **your own
install** and cuts out the stretch you drove: the stage's ground, split into
road and terrain and coloured from the colour the game baked for it, with the
barriers, signs, buildings and other models along your lap, as one 3D course
for the [3DHeat](https://github.com/Holdi601/3DHeat) viewer
([documentation](https://holdi601.github.io/3DHeat/)).

**Why would I use it?** To analyse your AC Rally runs on the real stage -
braking points, lines and corners in 3D - instead of on a line in empty space.

**Example:** `heat3d-acrally-maps course my_run.json` -> `my_run.glb`, in the
same frame as the lap: it drops into the viewer's Race tab under the lap with
no placing or scaling.

## Quick start

You need Windows, Python 3.10 or later ("Add python.exe to PATH" ticked in its
installer), Assetto Corsa Rally installed through Steam and a run recorded with
[3DHeat GameCapture](https://github.com/Holdi601/3DHeat-GameCapture); no Git.
New to the command line? Read [Before you start](before-you-start.md) first.

```bash
python -m pip install https://github.com/Holdi601/3DHeat-Ext-ACRally/archive/refs/tags/v0.1.0.zip
heat3d-acrally-maps stages                                     # where the game is, and its stages
heat3d-acrally-maps course laps\<run>.lap.json -o my_run.glb   # the stage around that run
```

The install brings [3DHeat GameFiles](https://holdi601.github.io/3DHeat-GameFiles/),
the library it reads with. The run comes from
`python -m heat3d_capture telemetry --game acrally -o laps`
([Telemetry: Assetto Corsa](https://holdi601.github.io/3DHeat-GameCapture/telemetry-assetto-corsa.html)).
`course` finds the stage and the way the run's axes lie from the run itself
and ends with `wrote my_run.glb (... bytes)`; the file lands in the folder you
ran it in. A game outside the Steam libraries needs `--install "<game folder>"`.
Most of the game's data is Oodle-compressed: an `oo2core_*_win64.dll` that an
installed Unreal game ships is found by itself, or `HEAT3D_OODLE` names one
([Oodle](https://holdi601.github.io/3DHeat-GameFiles/reader-oodle.html)).

Then open the `.glb` in the [3DHeat viewer](https://github.com/Holdi601/3DHeat#quick-start):
download it (**Code -> Download ZIP**, unpack), double-click `start.bat` (it
offers to install Node.js when it is missing and opens `http://127.0.0.1:5273`),
then **Background / level -> 3D model...** and pick the file, and in the
**Race analysis** tab **Load lap files...** and pick the run. The course stays
on your machine.

When a new release is out, the tool says so when it starts and offers to
update itself.

Each game reader is its own small project with its own licence file, releases
and issue tracker, so it can be installed, updated, maintained - or withdrawn
on a rights holder's request - on its own, without affecting the viewer or the
other tools.

## Pages

| Page | What it covers |
|---|---|
| [Before you start](before-you-start.md) | Python, GameFiles, Oodle, a terminal, a first run |
| [Course export: course](course-assetto-corsa-rally.md) | how a run becomes a course: the install, the stage, the frame, ground, texture, models |
| [Finding the game: stages](stages.md) | where Assetto Corsa Rally is found, what `stages` prints |
| [What is this file: identify](identify.md) | the game's own IoStore containers |
| [Terms and licence](terms.md) | the game's content, the formats, a project of its own |
| [Command reference](cli-reference.md) | every option, generated from the code |
| [Maintaining these docs](maintaining.md) | the release checklist |

## Related

- The 3DHeat viewer: [github.com/Holdi601/3DHeat](https://github.com/Holdi601/3DHeat),
  documentation at [holdi601.github.io/3DHeat](https://holdi601.github.io/3DHeat/).
- Recording AC Rally runs: the GameCapture recorder,
  [Telemetry: Assetto Corsa](https://holdi601.github.io/3DHeat-GameCapture/telemetry-assetto-corsa.html).
- The library this tool builds on - the Unreal 5 IoStore, zen package and
  texture readers, and Oodle - and its `course` command, which hands AC Rally
  laps to this tool: [3DHeat GameFiles](https://holdi601.github.io/3DHeat-GameFiles/).

## The 3DHeat tools

| Tool | What it does | Code | Docs |
|---|---|---|---|
| 3DHeat viewer | shows the data: heatmaps, race analysis, match review | [3DHeat](https://github.com/Holdi601/3DHeat) | [docs](https://holdi601.github.io/3DHeat/) |
| GameFiles | levels and courses from a game's own files | [3DHeat-GameFiles](https://github.com/Holdi601/3DHeat-GameFiles) | [docs](https://holdi601.github.io/3DHeat-GameFiles/) |
| GameCapture | lap telemetry, and levels rebuilt from gameplay video | [3DHeat-GameCapture](https://github.com/Holdi601/3DHeat-GameCapture) | [docs](https://holdi601.github.io/3DHeat-GameCapture/) |
| Unreal Exporter | an Unreal Editor plugin: a level as one `.glb` | [3DHeat-UnrealExporter](https://github.com/Holdi601/3DHeat-UnrealExporter) | [docs](https://holdi601.github.io/3DHeat-UnrealExporter/) |
| CS2 | Counter-Strike 2 demos and maps | [3DHeat-CS2](https://github.com/Holdi601/3DHeat-CS2) | [docs](https://holdi601.github.io/3DHeat-CS2/) |
| Watcher | records what games publish while you play | [3DHeat-Watcher](https://github.com/Holdi601/3DHeat-Watcher) | [docs](https://holdi601.github.io/3DHeat-Watcher/) |
| Ext-WarThunder | War Thunder replays | [3DHeat-Ext-WarThunder](https://github.com/Holdi601/3DHeat-Ext-WarThunder) | [docs](https://holdi601.github.io/3DHeat-Ext-WarThunder/) |
| Ext-WoT | World of Tanks replays | [3DHeat-Ext-WoT](https://github.com/Holdi601/3DHeat-Ext-WoT) | [docs](https://holdi601.github.io/3DHeat-Ext-WoT/) |
| Ext-WoWs | World of Warships replays | [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs) | [docs](https://holdi601.github.io/3DHeat-Ext-WoWs/) |
| Ext-Squad | Squad server demos | [3DHeat-Ext-Squad](https://github.com/Holdi601/3DHeat-Ext-Squad) | [docs](https://holdi601.github.io/3DHeat-Ext-Squad/) |
| Ext-DCS | DCS World maps as 3D levels | [3DHeat-Ext-DCS](https://github.com/Holdi601/3DHeat-Ext-DCS) | [docs](https://holdi601.github.io/3DHeat-Ext-DCS/) |
| Ext-IL2 | IL-2 Sturmovik maps as 3D levels | [3DHeat-Ext-IL2](https://github.com/Holdi601/3DHeat-Ext-IL2) | [docs](https://holdi601.github.io/3DHeat-Ext-IL2/) |
| Ext-Dota | the Dota 2 map as a 3D level | [3DHeat-Ext-Dota](https://github.com/Holdi601/3DHeat-Ext-Dota) | [docs](https://holdi601.github.io/3DHeat-Ext-Dota/) |
| Ext-DotaReplay | Dota 2 replays as tables | [3DHeat-Ext-DotaReplay](https://github.com/Holdi601/3DHeat-Ext-DotaReplay) | [docs](https://holdi601.github.io/3DHeat-Ext-DotaReplay/) |
| Ext-Riot | League of Legends and VALORANT replays | [3DHeat-Ext-Riot](https://github.com/Holdi601/3DHeat-Ext-Riot) | [docs](https://holdi601.github.io/3DHeat-Ext-Riot/) |
| Ext-Forza | Forza Horizon courses and cars | [3DHeat-Ext-Forza](https://github.com/Holdi601/3DHeat-Ext-Forza) | [docs](https://holdi601.github.io/3DHeat-Ext-Forza/) |
| Ext-Battlefield | Battlefield 6 levels as 3D levels | [3DHeat-Ext-Battlefield](https://github.com/Holdi601/3DHeat-Ext-Battlefield) | [docs](https://holdi601.github.io/3DHeat-Ext-Battlefield/) |
| Ext-BeamNG | BeamNG.drive courses around your laps | [3DHeat-Ext-BeamNG](https://github.com/Holdi601/3DHeat-Ext-BeamNG) | [docs](https://holdi601.github.io/3DHeat-Ext-BeamNG/) |
| Ext-ACRally | Assetto Corsa Rally stages around your laps | [3DHeat-Ext-ACRally](https://github.com/Holdi601/3DHeat-Ext-ACRally) | [docs](https://holdi601.github.io/3DHeat-Ext-ACRally/) |
| Ext-Reforger | Arma Reforger worlds as 3D levels | [3DHeat-Ext-Reforger](https://github.com/Holdi601/3DHeat-Ext-Reforger) | [docs](https://holdi601.github.io/3DHeat-Ext-Reforger/) |
| Ext-R6 | Rainbow Six Siege match replays | [3DHeat-Ext-R6](https://github.com/Holdi601/3DHeat-Ext-R6) | [docs](https://holdi601.github.io/3DHeat-Ext-R6/) |
