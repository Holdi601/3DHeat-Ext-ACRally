"""
The standalone app's description of this tool (app/spec.py): the Assetto
Corsa Rally install it reads, the checks before a course can be exported, and
the course export as a task. A course is cut around a recorded run, and the
stage and its frame are found from the run, so there are no maps to extract
from the install alone: the window lists what is found and runs `course` and
`stages`. `python -m heat3d_ext_acrally.standalone_spec` runs the app from a
checkout; the release executables run the same.
"""

from __future__ import annotations

import sys
from pathlib import Path

from . import __version__
from .app.spec import Check, GameSpec, Input, Spec, Task, game_folders

TOOL = "heat3d-acrally-maps"


def _find(given: str | None) -> Path | None:
    from .acrally import find_paks

    if given:
        return find_paks((given,), defaults=False)
    return find_paks()


def _install_args() -> list[str]:
    """`--install <Paks>` when the install is known (chosen in the window, or found)."""
    paks = game_folders(SPEC).get("acrally")
    return ["--install", str(paks)] if paks else []


def _checks(found: dict, levels: Path) -> list[Check]:
    from ._gamefiles import NEEDED, find_gamefiles

    checks = [Check("gamefiles", "3DHeat GameFiles (the readers this tool builds on)", find_gamefiles(),
                    "found" if find_gamefiles() else NEEDED)]
    if not checks[0].ok:
        return checks
    from heat3d_gamefiles.oodle import find_oodle

    paks = found.get("acrally")
    lib = None
    if paks is not None:
        game = paks.parent.parent.parent if paks.name.lower() == "paks" else paks
        for where in (game, game / "Engine" / "Binaries" / "ThirdParty" / "Oodle" / "Win64",
                      game / "Engine" / "Binaries" / "Win64", game / "acr" / "Binaries" / "Win64"):
            lib = find_oodle(where) if where.is_dir() else None
            if lib:
                break
    lib = lib or find_oodle()
    if sys.platform != "win32":
        detail = "the Oodle library is a Windows DLL; a course whose blocks are Oodle-compressed is exported on Windows"
        checks.append(Check("oodle", "Oodle library (from your own install)", False, detail))
    else:
        checks.append(Check(
            "oodle", "Oodle library (from your own install)", lib is not None,
            str(lib) if lib else "not found; Oodle-compressed blocks need it. Set HEAT3D_OODLE to an "
            "oo2core_*_win64.dll from a game or engine installed on this machine.",
        ))
    return checks


SPEC = Spec(
    id="heat3d-acrally",
    name="3DHeat AC Rally",
    repo="Holdi601/3DHeat-Ext-ACRally",
    version=__version__,
    tools={TOOL: "heat3d_ext_acrally.cli:main"},
    default_tool=TOOL,
    description="Assetto Corsa Rally stages around your runs, as 3DHeat courses",
    module="heat3d_ext_acrally.standalone_spec",
    games=[GameSpec(
        key="acrally", label="Assetto Corsa Rally", find=_find, subdir="acrally",
        platforms=("windows-x64", "linux-x64"),
    )],
    checks=_checks,
    tasks=[
        Task(
            "course", "Course around a run",
            [Input("lap", "A recorded run (a lap file, or a .csv with its positions)", "file")],
            lambda v, levels: [TOOL, "course", v["lap"], *_install_args()],
            help="the stage's ground and what stands on it along the run, into <levels>/acrally/courses",
        ),
        Task(
            "stages", "List the stages",
            [],
            lambda v, levels: [TOOL, "stages", *_install_args()],
            help="where the game is, and every stage it has",
        ),
    ],
    min_free_gb=2.0,
    notice="Not affiliated with or endorsed by the makers or publishers of Assetto Corsa Rally.",
)

if __name__ == "__main__":
    from .app.entry import main
    from .update import apply

    raise SystemExit(main(SPEC, apply_source=apply))
