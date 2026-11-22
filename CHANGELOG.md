# Changelog

## 0.3.0

- Its own icon: the 3DHeat cube with a text badge for its game (letters in 3DHeat's colours), as the
  program, window, taskbar and docs icon.
- A new window: the 3DHeat look in dark and light (follows the system, switchable), the logo and
  icon, sharp at any display scaling. Four steps: find the game (each requirement with its fix),
  choose (maps ticked when there is something to do, filters, search; jobs with their fields
  inline), work (progress, time left, cancel), done (open in 3DHeat, open the output folder, and
  for a failure what went wrong and what to do, copy details, report a problem).
- No console window on Windows: the program is a window program. From a terminal it still prints
  as before; `heat3d-acrally-cli.cmd` beside it waits for it in a terminal and passes its exit code.
- The update offer in the same look: Update now / Later / Skip this version, and "Update
  automatically" from the dialog.
- CI draws every page and dialog of the window (on Linux under a virtual display) and checks the
  Windows build is a window program.

## 0.2.0

- A standalone program for Windows and Linux (Steam/Proton, Steam Deck included; no Python needed), built by
  CI with a `SHA256SUMS` file. Without arguments it opens a window: what is found and what is missing
  (install, 3DHeat GameFiles, Oodle library, disk space), the levels folder, the course around a run you pick,
  the stage list, and updates. `--check --json` and `status --json` for scripts; a course is cut around a run,
  so `extract` has nothing to extract from the install alone and says so.
- Updates ask first (update now / later / skip this version) unless automatic updates were chosen
  (`--auto-update`, the window's checkbox, or `HEAT3D_AUTO_UPDATE=1`).
- The install is also found in Steam libraries on Linux (native and flatpak).

## 0.1.0

- First version, moved out of 3DHeat GameFiles with its history (GameFiles'
  `course` now runs this tool for an Assetto Corsa Rally lap): the stage's
  ground, split into road and terrain and coloured from the game's baked
  ground colour, with the placed models, around an AC Rally run as a 3DHeat
  course, the stage and the lap's frame found from the lap. `course` takes
  exactly GameFiles' `course` options; another game's lap, and a `--level`
  that is no stage, exit 2. `--install` takes the game's folder or its
  `Content\Paks`. New: `stages` says where the game is and lists its stages;
  `identify` recognises the game's own IoStore containers. Builds on 3DHeat
  GameFiles as a library, installed by pip or found beside a checkout.
- Installs with one pip line from the release zip, no Git needed (GameFiles comes from its own release zip); a pip install knows its version and updates itself with pip when a newer release is out.
- README: a quick start for new users.

## Docs

Where each feature is documented
([holdi601.github.io/3DHeat-Ext-ACRally](https://holdi601.github.io/3DHeat-Ext-ACRally/)):

| Feature | Page |
|---|---|
| Installing, GameFiles, Oodle, a first run | [Before you start](docs/before-you-start.md) |
| Exporting a course (`course` and its options): the install, the stage, the frame, ground, texture, models | [Course export](docs/course-assetto-corsa-rally.md) |
| Finding the install and its stages (`stages`, `--install`) | [Finding the game: stages](docs/stages.md) |
| Naming the game's containers (`identify`) | [What is this file: identify](docs/identify.md) |
| The game's content, Oodle, the formats | [Terms and licence](docs/terms.md) |
| Every option and part name, generated | [Command reference](docs/cli-reference.md) |
| Release checklist for the docs | [Maintaining these docs](docs/maintaining.md) |
