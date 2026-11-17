# 3DHeat AC Rally: Assetto Corsa Rally stages around your runs

**What is it?** This tool reads an Assetto Corsa Rally stage from your own
install and cuts out the stretch you drove: the stage's ground, split into road
and terrain and coloured from the colour the game baked for it, with the
barriers, signs, buildings and other models along your run, as one 3D course
for the [3DHeat](https://github.com/Holdi601/3DHeat) viewer.

**Why would I use it?** To analyse your AC Rally runs on the real stage -
braking points, lines and corners in 3D - instead of on a line in empty space.

**Example:** `heat3d-acrally-maps course my_run.json` -> `my_run.glb`, in the
lap's own frame: it drops into the viewer's Race tab under the lap.

**Documentation:** [holdi601.github.io/3DHeat-Ext-ACRally](https://holdi601.github.io/3DHeat-Ext-ACRally/), a page per
command with step-by-step use and example output. Part of
[3DHeat](https://github.com/Holdi601/3DHeat) ([documentation](https://holdi601.github.io/3DHeat/)).

Each game reader is its own small project with its own licence file, releases
and issue tracker, so it can be installed, updated, maintained - or withdrawn
on a rights holder's request - on its own, without affecting the viewer or the
other tools.

The courses it writes stay on your machine.

## Quick start for new users

You need: Windows, [Python](https://www.python.org/downloads/) 3.10 or later
("Add python.exe to PATH" ticked in its installer), Assetto Corsa Rally
installed through Steam, and a run recorded with
[3DHeat GameCapture](https://github.com/Holdi601/3DHeat-GameCapture)
(`python -m heat3d_capture telemetry --game acrally -o laps`, see
[Telemetry: Assetto Corsa](https://holdi601.github.io/3DHeat-GameCapture/telemetry-assetto-corsa.html)).
Most of the game's data is Oodle-compressed: the `oo2core_*_win64.dll` an
installed Unreal game ships is found by itself, or name one with
`HEAT3D_OODLE` ([Oodle](https://holdi601.github.io/3DHeat-GameFiles/reader-oodle.html)).
No Git is needed.

1. Install the tool (one line, in PowerShell or a command prompt); it brings
   [3DHeat GameFiles](https://github.com/Holdi601/3DHeat-GameFiles), the
   library it reads with:

   ```bash
   python -m pip install https://github.com/Holdi601/3DHeat-Ext-ACRally/archive/refs/tags/v0.1.0.zip
   ```

2. Check that the game is found, then export the stage around your run (the
   stage is worked out from the run; a game outside the Steam libraries needs
   `--install "<game folder>"`):

   ```bash
   heat3d-acrally-maps stages
   heat3d-acrally-maps course laps\<run>.lap.json -o my_run.glb
   ```

3. The output is `my_run.glb` in the folder you ran it in (without `-o`, it is
   named after the run). `course` ends with `wrote my_run.glb (... bytes)`.
4. Open it in the [3DHeat viewer](https://github.com/Holdi601/3DHeat#quick-start):
   download the viewer (**Code -> Download ZIP**, unpack) and double-click
   `start.bat`; it offers to install [Node.js](https://nodejs.org/) when it is
   missing and opens Chrome or Edge at `http://127.0.0.1:5273`. There,
   **Background / level -> 3D model...** and pick the `.glb`, then the
   **Race analysis** tab, **Load lap files...** and pick the run.

When a new release is out, the tool says so when it starts and offers to
update itself (`python -m heat3d_ext_acrally.update` does the same).

## Install from a checkout

New to the command line? Read [Before you start](https://holdi601.github.io/3DHeat-Ext-ACRally/before-you-start.html) first.

1. Install Python 3.10 or later, and Assetto Corsa Rally.
2. `git clone https://github.com/Holdi601/3DHeat-Ext-ACRally` (or download the
   ZIP) and open a terminal in that folder.
3. Install the command - this also installs
   [3DHeat GameFiles](https://github.com/Holdi601/3DHeat-GameFiles), the library
   with the Unreal 5 readers this tool builds on - and check that the game is
   found:

```bash
python -m pip install -e .         # installs the heat3d-acrally-maps command
heat3d-acrally-maps stages         # where the game is, and its stages
```

Without pip, a GameFiles checkout is found in `HEAT3D_GAMEFILES`, in
`../../gamefiles` (inside a 3DHeat checkout) or in `../3DHeat-GameFiles`.

Most of the game's data is Oodle-compressed. Oodle is proprietary and not
bundled: GameFiles finds a library already on your machine, or the one
`HEAT3D_OODLE` names ([Oodle](https://holdi601.github.io/3DHeat-GameFiles/reader-oodle.html)).

Runs come from the 3DHeat GameCapture recorder
([Telemetry: Assetto Corsa](https://holdi601.github.io/3DHeat-GameCapture/telemetry-assetto-corsa.html),
`--game acrally`).

## Commands

| Command | Does | Page |
|---|---|---|
| `course <lap> [-o file.glb]` | the stage's ground and models around an AC Rally run, the stage and the lap's frame found from the lap | [course](https://holdi601.github.io/3DHeat-Ext-ACRally/course-assetto-corsa-rally.html) |
| `stages [--install FOLDER]` | where the game is, and every stage it has | [stages](https://holdi601.github.io/3DHeat-Ext-ACRally/stages.html) |
| `identify <path>` | whether a `.utoc` is one of the game's own containers, and what it holds | [identify](https://holdi601.github.io/3DHeat-Ext-ACRally/identify.html) |

```bash
heat3d-acrally-maps course laps\my_run.json                       # the stage found from the run
heat3d-acrally-maps course my_run.json --level <stage map name>   # or named, as stages lists it
heat3d-acrally-maps course my_run.json --install "D:\Games\Assetto Corsa Rally" --no-textures
```

| `course` option | Does |
|---|---|
| `-o`, `--out FILE` | the `.glb` to write (default: the lap's name, in `$HEAT3D_LEVELS/acrally/courses` when that is set, else here) |
| `--level NAME` | the stage's map name, when it should not be found from the lap; a name that is no stage lists the stages and exits 2 |
| `--install FOLDER` | the game's folder or its `Content\Paks`, when it is in no Steam library |
| `--margin METRES` | ground kept either side of the driving (default 80) |
| `--texture-size {2048,1024,512}` | ground texture per 512 m square (default 2048) |
| `--no-textures` | flat colours only |
| `--no-placed` | the stage's ground only |
| `--trees` | also trees and the forests |
| `--detail-budget N` | a ceiling on placed triangles |
| `--game {forza,beamng,acrally}` | which game the lap is from (default: what the lap says, else AC Rally); another game's lap exits 2 and names its tool |
| `--track`, `--season` | Forza only: accepted, so 3DHeat GameFiles can pass its arguments on unchanged, and ignored |

Exit status: 0 done; 1 reading or writing failed; 2 nothing found - no
install, no such stage, a lap on no stage's road, not an AC Rally lap or file,
GameFiles or Oodle missing
(the message says which, and what to do). Every option, as the program prints
it: [Command reference](https://holdi601.github.io/3DHeat-Ext-ACRally/cli-reference.html).

3DHeat GameFiles' `course` runs this tool for an AC Rally lap.

## What comes out, and loading it

One glTF binary in the lap's frame (metres, Y up): the stage's ground per
512 m square (`ground:road <x>_<y>`, `ground:terrain <x>_<y>`), textured from
the game's baked ground colour, and one flat-coloured part per category of
placed model (`structure:barriers`, `ground:kerbs`, ...). Load it in the
viewer's **Background / level** panel with **3D model…** under the lap.
[The course, step by step](https://holdi601.github.io/3DHeat-Ext-ACRally/course-assetto-corsa-rally.html).

## Terms

3DHeat AC Rally is not affiliated with or endorsed by Kunos Simulazioni or 505
Games. Assetto Corsa Rally and related names and trademarks belong to their
owners. Nothing of the game is in this repository or downloaded by it - no
game assets, no game code, no DLLs; the stage comes out of your own install,
and the course it writes stays on your machine
([Terms and licence](https://holdi601.github.io/3DHeat-Ext-ACRally/terms.html)).

Rights holders: open an issue at
[github.com/Holdi601/3DHeat-Ext-ACRally/issues](https://github.com/Holdi601/3DHeat-Ext-ACRally/issues)
- we respond quickly and remove anything on request.

## Tests

```bash
python -m pip install -e .[test]
python -m pytest
```

On made-up data only: containers built the way the game ships them. The tests
on the real game run only where Assetto Corsa Rally is installed, and write
nothing into the repository.

## Licence

MIT ([`LICENSE`](LICENSE)). Third-party software it uses: [`LICENSES.md`](LICENSES.md).
