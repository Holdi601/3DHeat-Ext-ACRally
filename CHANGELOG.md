# Changelog

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
