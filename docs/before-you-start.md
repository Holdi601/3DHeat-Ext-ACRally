---
title: Before you start
nav_order: 1.5
---

# Before you start

New to the command line? This page takes you from nothing to a first run.
It takes about fifteen minutes, once.

## The standalone program (no Python needed)

Each [release](https://github.com/Holdi601/3DHeat-Ext-ACRally/releases/latest)
has a ready-to-run program for Windows (`heat3d-acrally-<version>-windows-x64.zip`)
and Linux (`heat3d-acrally-<version>-linux-x64.tar.gz`, for a Steam/Proton install,
Steam Deck included), with a `SHA256SUMS` file to check the download. Unpack it
anywhere and start `heat3d-acrally`; steps 1 to 4 below are then not needed.

Started without arguments it opens a window that:

- finds your Assetto Corsa Rally install in any Steam library, or lets you
  choose its folder;
- says what is missing: the game, the Oodle library some blocks need (it comes
  from a game or engine installed on your machine), free disk space;
- exports the course around a run you pick into the 3DHeat levels folder
  (`HEAT3D_LEVELS`, by default `%LOCALAPPDATA%\3DHeat\levels` on Windows and
  `~/.local/share/3dheat/levels` on Linux), where the viewer finds it, and
  lists the stages the game has;
- checks for updates and asks before installing one, unless you tick
  *Update automatically*.

The same program runs every command on these pages:
`heat3d-acrally heat3d-acrally-maps course my_run.json`, `heat3d-acrally stages`.
For scripts: `heat3d-acrally --check --json` reports what is found and missing,
and `heat3d-acrally status --json` the install's state. A course is cut around a
run, so there is nothing to extract from the install alone: `heat3d-acrally extract --new`
says so. The 3DHeat app's Extractors panel installs, updates and starts it for you.

## 1. Install Python

This tool needs **Python 3.10 or later**.

- **Windows:** download Python from [python.org/downloads](https://www.python.org/downloads/)
  and run the installer. On its first screen, tick **Add python.exe to PATH**,
  then click **Install Now**.
- **macOS and Linux:** Python 3 is often there already. Where these pages say
  `python`, type `python3`.

## 2. Get this tool

Open [github.com/Holdi601/3DHeat-Ext-ACRally](https://github.com/Holdi601/3DHeat-Ext-ACRally), click the
green **Code** button, then **Download ZIP**, and unzip it into a folder of your
choice. If you use git: `git clone https://github.com/Holdi601/3DHeat-Ext-ACRally`.

## 3. Open a terminal in that folder

A terminal is a window where you type commands.

- **Windows:** open the folder in Explorer, click into the address bar, type
  `powershell` and press Enter. A blue or black window opens, already in that
  folder.
- **macOS:** open **Terminal**, type `cd ` (with a space), drag the folder into
  the window and press Enter.

`cd` means "change folder": `cd C:\Tools\3DHeat-Ext-ACRally` goes to that folder.

## 4. Install the tool

Type this and press Enter:

```bash
python -m pip install -e .
```

This also installs [3DHeat GameFiles](https://holdi601.github.io/3DHeat-GameFiles/),
the library the readers build on, and numpy and Pillow.
You should see, at the end: `Successfully installed ... heat3d-ext-acrally-...`.

Already have a GameFiles checkout? The tool also finds it without pip: in the
folder the `HEAT3D_GAMEFILES` environment variable names, inside a 3DHeat
checkout (`exporters/gamefiles`), or in a `3DHeat-GameFiles` folder next to
this one.

## 5. Check that the game is found

```bash
heat3d-acrally-maps stages
```

You should see something like:

```text
Assetto Corsa Rally at C:\Program Files (x86)\Steam\steamapps\common\Assetto Corsa Rally\acr\Content\Paks
  ExampleStage
  ...
10 stages
```

Most of the game's data is Oodle-compressed. Oodle is not part of this tool:
the library the game or another installed game ships is looked for on your
machine, and `HEAT3D_OODLE` can name it
([Oodle](https://holdi601.github.io/3DHeat-GameFiles/reader-oodle.html)).

## 6. Record a run, then export its course

Record a run with the 3DHeat GameCapture recorder
([Telemetry: Assetto Corsa](https://holdi601.github.io/3DHeat-GameCapture/telemetry-assetto-corsa.html),
`--game acrally`), then:

```bash
heat3d-acrally-maps course laps\my_run.json
```

Next: [Course export](course-assetto-corsa-rally.md).

## How to read the commands on these pages

| You see | It means |
|---|---|
| `<stage map name>` | a placeholder: type your own value instead, without the `< >` |
| `[--install FOLDER]` | optional: leave it out, or type it as shown |
| `# a note` | a comment for you: do not type it |
| `"C:\My Files\x"` | put a path that has spaces in quotes |

## When something goes wrong

| The message | What to do |
|---|---|
| `'python' is not recognized` | Python is not installed, or the PATH box was not ticked: install it again and tick it (or type `py` instead of `python`). |
| `'heat3d-acrally-maps' is not recognized` | Run step 4 again in the tool's folder, or type `python -m heat3d_ext_acrally` instead of `heat3d-acrally-maps`: it does the same. |
| `needs 3DHeat GameFiles: ...` | Step 4 did not install GameFiles: run `python -m pip install https://github.com/Holdi601/3DHeat-GameFiles/archive/refs/tags/v1.1.0.zip`, or set `HEAT3D_GAMEFILES` to a GameFiles folder. |
| `no Assetto Corsa Rally install found in the Steam libraries` | Give the game's folder, or its `Content\Paks`: `--install "D:\Games\Assetto Corsa Rally"`. |
| `... is a forza-... lap, not an Assetto Corsa Rally one` | That lap is from another game; the message names the tool for it. |
| `the lap does not lie on any stage's road in any frame` | Name the stage: `--level <stage map name>`, as `stages` lists it. |
| `no Oodle library found` (or similar) | Set `HEAT3D_OODLE` to an `oo2core_*.dll` already on your machine. |
| anything else | Read the last line of the message, then open an issue on GitHub with it. |

Every command also ends with an **exit status**: 0 means it worked, 2 that
the game, GameFiles, the stage or an AC Rally file was not found, 1 that reading or writing
failed. To see it, type `echo $LASTEXITCODE` in PowerShell or `echo $?` on
macOS and Linux.
