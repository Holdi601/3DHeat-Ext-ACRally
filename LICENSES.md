# Third-party licences

This tool is MIT licensed ([`LICENSE`](LICENSE)). What it uses, and under which
licence; each package's own source is what counts, not this file.

| Software | Licence | How it is used |
|---|---|---|
| 3DHeat GameFiles | MIT | a dependency, installed by pip: the Unreal 5 IoStore, zen package, property, mesh and texture readers, the Oodle loader, the glTF writer, lap files, corridor, surfaces, detail budget and Steam libraries |
| numpy | BSD-3-Clause | a dependency, installed by pip: meshes, transforms, the ground |
| pytest | MIT | development only: the tests |

GameFiles brings its own dependencies (lz4, Pillow), all permissive. This tool
carries no restriction of its own.

## Oodle

Most of the game's data is Oodle-compressed. Oodle (RAD Game Tools, now Epic)
is proprietary and has no redistributable build: it is **not bundled**, and
GameFiles loads a library already on the user's machine (`HEAT3D_OODLE` names
one). `oo2core_*.dll` is licensed to the product that ships it.

## The game's files

Assetto Corsa Rally belongs to Kunos Simulazioni and 505 Games. This
repository holds no file of the game and no course made from one; the tool
reads the copy the user installed, on the user's machine, and the course it
writes stays there. No other project's code was used. See
[Terms and licence](https://holdi601.github.io/3DHeat-Ext-ACRally/terms.html).
