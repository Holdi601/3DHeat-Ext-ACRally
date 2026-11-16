---
title: Terms and licence
nav_order: 9
---

# Terms and licence

## The game's content

Assetto Corsa Rally and its stages belong to its developer, Kunos Simulazioni,
and its publisher, 505 Games. 3DHeat AC Rally is not affiliated with or
endorsed by Kunos Simulazioni or 505 Games. Assetto Corsa Rally and related
names and trademarks belong to their owners.

This tool ships nothing of the game and downloads nothing: no game assets, no
game code, no DLLs. It reads the files of the copy **you** installed, on your
machine, outside the game. It changes nothing in the game and talks to no
server. A course it writes is cut from the game's stage and stays on your
machine, for analysing your own runs; please do not share or publish it.

Each game reader is its own small project with its own licence file, releases
and issue tracker, so it can be installed, updated, maintained - or withdrawn
on a rights holder's request - on its own, without affecting the viewer or the
other tools.

Rights holders: open an issue at
[github.com/Holdi601/3DHeat-Ext-ACRally/issues](https://github.com/Holdi601/3DHeat-Ext-ACRally/issues)
- we respond quickly and remove anything on request.

The rules of 3DHeat GameFiles apply here unchanged
([Rules and licences](https://holdi601.github.io/3DHeat-GameFiles/rules-and-licences.html)):

- **No keys: none shipped, none recovered.** None of the game's containers is
  encrypted; an encrypted IoStore container is refused outright.
- **Your own files.** The tool reads the game files
  installed on your machine. It never downloads game content.
- **Output is not for redistribution.** Keep exported `.glb` files, and the
  textures inside them, for your own analysis. Do not publish, share or sell
  exported courses, levels, models or textures. The repository's `.gitignore`
  keeps game files, exports and laps out of version control.

## Oodle is found, not bundled

Oodle (RAD Game Tools, now Epic) is proprietary and has no redistributable
build. `oo2core_*.dll` is licensed to the product that ships it. 3DHeat
GameFiles therefore loads a library already on the machine rather than
carrying one, and this tool carries none either
([Oodle](https://holdi601.github.io/3DHeat-GameFiles/reader-oodle.html)).

## The formats

The game is Unreal Engine 5. Its containers and packages are read by 3DHeat
GameFiles' Unreal readers. Unreal 5's cooked property data needs each class's
property list. The lists in GameFiles' `unversioned.py` are **names and types
only**. They were derived from the Unreal Engine headers Epic makes available
to anyone with a linked account, and checked against the shipped data. No
engine source is included or required. What this tool adds - where a stage is,
how its components place their meshes, which way a lap's axes lie - was
worked out from the installed game ([Course export](course-assetto-corsa-rally.md)).

## Licence and sources

MIT ([`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-ACRally/blob/main/LICENSE)).
Needs 3DHeat GameFiles (MIT) and numpy (BSD-3-Clause); the tests need pytest
(MIT). See
[`LICENSES.md`](https://github.com/Holdi601/3DHeat-Ext-ACRally/blob/main/LICENSES.md).
Written for this project; no code was taken from any other project.
