"""
heat3d-acrally-maps course <lap> [-o file.glb]   the stage around an Assetto Corsa Rally lap, as a 3DHeat course
heat3d-acrally-maps stages [--install FOLDER]    where the game is, and the stages it has
heat3d-acrally-maps identify <path>              an Assetto Corsa Rally IoStore container

`course` takes exactly the options of 3DHeat GameFiles' `course`, so GameFiles
can hand an AC Rally lap over unchanged; the ones that only mean something for
another game (`--track`, `--season`) are accepted and ignored.

Exit status: 0 done, 1 failed, 2 nothing found (no Assetto Corsa Rally install,
no such stage, not an AC Rally lap or file, 3DHeat GameFiles missing).
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from . import __version__
from ._gamefiles import NEEDED, find_gamefiles

PROG = "heat3d-acrally-maps"

#: The names a lap gives this game.
GAMES = ("acrally", "assetto-corsa-rally")

#: The tool that exports a course for each other game a lap can be from.
_OTHER_TOOLS = {"beamng": "heat3d-beamng-maps"}

#: What `stages` and `course` say when the game is not found.
_NO_INSTALL = (
    "no Assetto Corsa Rally install found in the Steam libraries. Name its "
    "folder with --install (the game's folder, or its Content\\Paks)."
)


def _slug(name: str) -> str:
    """A course name as a file name: `Example Stage` -> `example_stage`."""
    return re.sub(r"[^a-z0-9]+", "_", name.lower()).strip("_") or "course"


def _paks(given: Path | None) -> Path | None:
    """The game's `Content/Paks`: from the folder given, if it leads to one, else the Steam libraries'."""
    from .acrally import find_paks

    if given is not None:
        return find_paks((given,), defaults=False)
    return find_paks()


def _no_install(given: Path | None) -> str:
    if given is not None:
        return f"{PROG}: no Assetto Corsa Rally containers (.utoc) in {given}, its acr\\Content\\Paks or its Content\\Paks"
    return f"{PROG}: {_NO_INSTALL}"


def _not_rally(name: str, game: str) -> str:
    tool = "heat3d-forza-maps" if game.startswith("forza") else _OTHER_TOOLS.get(game)
    if tool:
        return f"{PROG}: {name} is a {game} lap, not an Assetto Corsa Rally one: export its course with `{tool} course`."
    return (
        f"{PROG}: {name} is a {game} lap, not an Assetto Corsa Rally one, and no 3DHeat tool exports its course; "
        "`heat3d-gamefiles course` says why."
    )


def _stage_names(paks: Path) -> tuple[list[str] | None, str | None]:
    """
    The stages the containers hold, or a one-line reason they do not open.

    Which levels are stages is a matter of paths alone, so only the tables of
    contents are read: no package, and so no Oodle library, is needed for it.
    """
    from types import SimpleNamespace

    from heat3d_gamefiles.iostore import IoStoreError, Store

    from .acrally import list_stages

    try:
        store = Store(paks)
    except IoStoreError as exc:
        return None, str(exc)
    # `list_stages` reads nothing but `packages.store`'s paths.
    return list_stages(SimpleNamespace(store=store)), None


def _course(args) -> int:
    """An AC Rally lap in, the stage around it out: the stage and the frame are found from the lap."""
    from heat3d_gamefiles import levelshome
    from heat3d_gamefiles.lapinput import UnreadableLap, read

    try:
        driven = read(args.lap)
    except UnreadableLap as exc:
        print(exc, file=sys.stderr)
        return 1
    # A lap that does not say which game it is from is taken as AC Rally's: that
    # is the game this tool reads.
    game = (args.game or driven.game or "acrally").lower()
    if game not in GAMES:
        print(_not_rally(driven.name, game), file=sys.stderr)
        return 2
    paks = _paks(args.install)
    if paks is None:
        print(_no_install(args.install), file=sys.stderr)
        return 2
    if args.level:
        # A stage that is not there is "nothing found": said, with the stages
        # there are, before anything is read.
        stages, reason = _stage_names(paks)
        if stages is None:
            print(f"{PROG}: {reason}", file=sys.stderr)
            return 1
        if not any(s.lower() == args.level.lower() for s in stages):
            print(f"{PROG}: no stage called {args.level!r}; there are: {', '.join(stages)}", file=sys.stderr)
            return 2
    target = args.out or levelshome.default(_slug(driven.name) + ".glb", "acrally", "courses")
    target.parent.mkdir(parents=True, exist_ok=True)
    from heat3d_gamefiles.oodle import OodleUnavailable

    from .acrallycourse import export

    if len(driven) < 2:
        print(f"{driven.name} holds no driving", file=sys.stderr)
        return 1
    print(f"{driven.name}: {len(driven):,} samples, {driven.metres:,.0f} m driven (Assetto Corsa Rally)")
    try:
        return export(driven, target, args, paks=paks)
    except OodleUnavailable as exc:
        # A missing dependency: nothing was read, so nothing was found.
        print(f"{PROG}: {str(exc).splitlines()[0]} Set HEAT3D_OODLE to an oo2core_*.dll on this machine.", file=sys.stderr)
        return 2


def _stages(args) -> int:
    """Where the game's containers are, and every stage they hold."""
    paks = _paks(args.install)
    if paks is None:
        print(_no_install(args.install), file=sys.stderr)
        return 2
    print(f"Assetto Corsa Rally at {paks}")
    stages, reason = _stage_names(paks)
    if stages is None:
        print(f"{PROG}: {reason}", file=sys.stderr)
        return 1
    for name in stages:
        print(f"  {name}")
    print(f"{len(stages)} stages")
    return 0 if stages else 2


# --------------------------------------------------------------------- identify


#: Where the game mounts its containers: its project folder is `acr`.
_MOUNT = re.compile(r"(^|/)acr/content/?$", re.I)


def _identify(args) -> int:
    """
    An IoStore table of contents mounted where AC Rally mounts its own, and
    what it holds. Everything else - other games' containers included - is
    left to 3DHeat GameFiles' own `identify`.
    """
    import struct

    from heat3d_gamefiles.iostore import MAGIC, Container, IoStoreError

    path = args.path
    if not path.is_file():
        print(f"{PROG}: no such file: {path}", file=sys.stderr)
        return 2
    container = None
    with path.open("rb") as handle:
        head = handle.read(len(MAGIC))
    if head == MAGIC:
        try:
            container = Container.open(path)
        except (IoStoreError, OSError, struct.error):
            container = None
    if container is None or not _MOUNT.search(container.mount.rstrip("/") + "/"):
        print(f"not an Assetto Corsa Rally file: {path.name}", file=sys.stderr)
        return 2
    files = list(container.files)
    levels = sorted(
        (
            f.rsplit("/", 1)[-1][:-5]
            for f in files
            if f.lower().endswith(".umap") and "/content/levels/" in f.lower() and "/_generated_/" not in f.lower()
        ),
        key=str.lower,
    )
    lines = [
        f"{path.name}  ({path.stat().st_size:,} bytes)",
        f"  Assetto Corsa Rally IoStore container, mounted at {container.mount}",
        f"    files      {len(files):,}",
    ]
    if levels:
        lines.append(f"    levels     {', '.join(levels[:6])}" + (f" and {len(levels) - 6} more" if len(levels) > 6 else ""))
    print("\n".join(lines))
    return 0


# --------------------------------------------------------------------- the command line


def _export_options(p) -> None:
    """The options GameFiles' `course` takes for what goes into the file, with its defaults."""
    from heat3d_gamefiles.detail import DEFAULT_BUDGET

    p.add_argument(
        "--texture-size",
        type=int,
        choices=(2048, 1024, 512),
        default=2048,
        help="ground texture per 512 m tile, in pixels (2048 = 25 cm a pixel)",
    )
    p.add_argument(
        "--no-textures",
        action="store_true",
        help="flat colours only: a far smaller file, and no ground detail",
    )
    p.add_argument(
        "--season",
        choices=("summer", "autumn", "winter", "spring"),
        default="summer",
        help="Forza only; accepted and ignored here",
    )
    p.add_argument(
        "--no-placed",
        action="store_true",
        help="the stage's ground only: leave out kerbs, barriers, signs, rocks and buildings",
    )
    p.add_argument(
        "--trees",
        action="store_true",
        help="also place trees and bushes, the forests included (many triangles, and they hide the road)",
    )
    p.add_argument(
        "--detail-budget",
        type=int,
        default=None,
        help=(
            "a ceiling on triangles for everything placed; the costliest models drop "
            "to coarser levels of detail until it fits, and past that the furthest "
            "copies are left out (default: enough to keep every copy, and at least "
            f"{DEFAULT_BUDGET:,}; kerbs always stay at full detail)"
        ),
    )


def main(argv: list[str] | None = None) -> int:
    if not find_gamefiles():
        print(f"{PROG}: {NEEDED}", file=sys.stderr)
        return 2
    try:
        from . import update

        update.startup("heat3d_ext_acrally")
    except Exception:  # an update check never stops an export
        pass
    ap = argparse.ArgumentParser(
        prog=PROG,
        description="Assetto Corsa Rally stages from your own install as 3DHeat courses",
        epilog=(
            "What you point it at is the game publisher's, under the game's own licence; "
            "the courses stay on your machine. Oodle-compressed blocks need the Oodle library "
            "already on your machine (HEAT3D_OODLE)."
        ),
    )
    ap.add_argument("--version", action="version", version=__version__)
    sub = ap.add_subparsers(dest="verb", required=True)

    p = sub.add_parser("course", help="export the stage around an Assetto Corsa Rally lap, working out the stage")
    _export_options(p)
    p.add_argument(
        "lap",
        help="a lap: a file written by heat3d_capture, a lap folder, or a .csv with the lap's positions",
    )
    p.add_argument(
        "-o",
        "--out",
        type=Path,
        default=None,
        help=(
            "where to write the .glb (default: the lap's name, in "
            "$HEAT3D_LEVELS/acrally/courses when that is set, else here)"
        ),
    )
    p.add_argument("--track", type=Path, default=None, help="Forza only; accepted and ignored here")
    p.add_argument(
        "--margin",
        type=float,
        default=80.0,
        help="metres of ground to keep either side of the driving (default 80)",
    )
    p.add_argument(
        "--game",
        choices=("forza", "beamng", "acrally"),
        default=None,
        help="which game the lap is from (default: what the lap file says, else AC Rally); another game's lap exits 2",
    )
    p.add_argument(
        "--level",
        default=None,
        help="the stage's map name, as `stages` lists it, if it should not be found from the lap",
    )
    p.add_argument(
        "--install",
        type=Path,
        default=None,
        help="the game's folder, or its Content\\Paks, if it is not in a Steam library",
    )
    p.set_defaults(run=_course)

    p = sub.add_parser("stages", help="where Assetto Corsa Rally is, and every stage it has")
    p.add_argument("--install", type=Path, default=None, help="the game's folder, or its Content\\Paks, if it is not in a Steam library")
    p.set_defaults(run=_stages)

    p = sub.add_parser("identify", help="say whether a file is one of Assetto Corsa Rally's containers")
    p.add_argument("path", type=Path, help="an IoStore table of contents (.utoc)")
    p.set_defaults(run=_identify)

    args = ap.parse_args(argv)
    return args.run(args)


if __name__ == "__main__":
    sys.exit(main())
