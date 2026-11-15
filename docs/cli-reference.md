---
title: Command reference
nav_order: 90
---

# Command reference

Generated from the code by `tools/gen_docs_reference.py`: do not edit by hand.
The other pages explain each command step by step.

## `heat3d-acrally-maps`

```text
usage: heat3d-acrally-maps [-h] [--version] {course,stages,identify} ...

Assetto Corsa Rally stages from your own install as 3DHeat courses

positional arguments:
  {course,stages,identify}
    course              export the stage around an Assetto Corsa Rally lap, working
                        out the stage
    stages              where Assetto Corsa Rally is, and every stage it has
    identify            say whether a file is one of Assetto Corsa Rally's containers

options:
  -h, --help            show this help message and exit
  --version             show program's version number and exit

What you point it at is the game publisher's, under the game's own licence; the
courses stay on your machine. Oodle-compressed blocks need the Oodle library already
on your machine (HEAT3D_OODLE).
```

## `course`

```text
usage: heat3d-acrally-maps course [-h] [--texture-size {2048,1024,512}]
                                  [--no-textures]
                                  [--season {summer,autumn,winter,spring}]
                                  [--no-placed] [--trees]
                                  [--detail-budget DETAIL_BUDGET] [-o OUT]
                                  [--track TRACK] [--margin MARGIN]
                                  [--game {forza,beamng,acrally}] [--level LEVEL]
                                  [--install INSTALL]
                                  lap

positional arguments:
  lap                   a lap: a file written by heat3d_capture, a lap folder, or a
                        .csv with the lap's positions

options:
  -h, --help            show this help message and exit
  --texture-size {2048,1024,512}
                        ground texture per 512 m tile, in pixels (2048 = 25 cm a
                        pixel)
  --no-textures         flat colours only: a far smaller file, and no ground detail
  --season {summer,autumn,winter,spring}
                        Forza only; accepted and ignored here
  --no-placed           the stage's ground only: leave out kerbs, barriers, signs,
                        rocks and buildings
  --trees               also place trees and bushes, the forests included (many
                        triangles, and they hide the road)
  --detail-budget DETAIL_BUDGET
                        a ceiling on triangles for everything placed; the costliest
                        models drop to coarser levels of detail until it fits, and
                        past that the furthest copies are left out (default: enough to
                        keep every copy, and at least 1,500,000; kerbs always stay at
                        full detail)
  -o, --out OUT         where to write the .glb (default: the lap's name, in
                        $HEAT3D_LEVELS/acrally/courses when that is set, else here)
  --track TRACK         Forza only; accepted and ignored here
  --margin MARGIN       metres of ground to keep either side of the driving (default
                        80)
  --game {forza,beamng,acrally}
                        which game the lap is from (default: what the lap file says,
                        else AC Rally); another game's lap exits 2
  --level LEVEL         the stage's map name, as `stages` lists it, if it should not
                        be found from the lap
  --install INSTALL     the game's folder, or its Content\Paks, if it is not in a
                        Steam library
```

## `stages`

```text
usage: heat3d-acrally-maps stages [-h] [--install INSTALL]

options:
  -h, --help         show this help message and exit
  --install INSTALL  the game's folder, or its Content\Paks, if it is not in a Steam
                     library
```

## `identify`

```text
usage: heat3d-acrally-maps identify [-h] path

positional arguments:
  path        an IoStore table of contents (.utoc)

options:
  -h, --help  show this help message and exit
```

## Output

### `.glb` parts

The stage's ground, per 512 m square in Unreal space: `ground:road <x>_<y>` and `ground:terrain <x>_<y>`.

Placed models, one flat-coloured part per category: `structure:barriers` (barriers), `structure:signs` (signs), `structure:buildings` (buildings), `structure:infrastructure` (infrastructure), `structure:rocks` (rocks), `structure:props` (props), `structure:trees` (trees), `ground:kerbs` (kerbs).

Categories placed by default: `barriers`, `signs`, `buildings`, `infrastructure`, `rocks`, `props`, `kerbs`; `--trees` adds `trees`.
