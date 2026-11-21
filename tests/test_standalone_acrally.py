"""The standalone app on a synthetic Assetto Corsa Rally install (tiny fake files, no game data)."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from heat3d_ext_acrally import standalone_spec
from heat3d_ext_acrally.app import entry, update


@pytest.fixture(autouse=True)
def _isolated(tmp_path, monkeypatch):
    monkeypatch.setenv("LOCALAPPDATA", str(tmp_path / "appdata"))
    monkeypatch.setenv("XDG_DATA_HOME", str(tmp_path / "appdata"))
    monkeypatch.setenv("HEAT3D_LEVELS", str(tmp_path / "levels"))
    monkeypatch.setenv("HEAT3D_NO_UPDATE", "1")
    update.AUTO_THIS_RUN = False


def _install(tmp_path: Path) -> Path:
    paks = tmp_path / "Assetto Corsa Rally" / "acr" / "Content" / "Paks"
    paks.mkdir(parents=True)
    (paks / "global.utoc").write_bytes(b"not a real table of contents")
    return paks


def test_find_from_a_chosen_folder(tmp_path):
    paks = _install(tmp_path)
    find = standalone_spec.SPEC.games[0].find
    assert find(str(tmp_path / "Assetto Corsa Rally")) == paks
    assert find(str(paks)) == paks
    assert find(str(tmp_path / "elsewhere")) is None


def test_tasks_take_the_chosen_install(tmp_path, monkeypatch, capsys):
    paks = _install(tmp_path)
    spec = standalone_spec.SPEC
    monkeypatch.setattr(standalone_spec, "game_folders", lambda s, given=None: {"acrally": paks})
    tasks = {t.id: t for t in spec.tasks}
    argv = tasks["course"].argv({"lap": "run.csv"}, tmp_path / "levels")
    assert argv == ["heat3d-acrally-maps", "course", "run.csv", "--install", str(paks)]
    assert tasks["stages"].argv({}, tmp_path / "levels")[:2] == ["heat3d-acrally-maps", "stages"]
    for t in spec.tasks:
        assert t.argv({i.key: "x" for i in t.inputs}, tmp_path)[0] in spec.tools


def test_status_has_no_maps_and_extract_says_so(capsys):
    spec = standalone_spec.SPEC
    assert not spec.has_maps()
    assert entry.main(spec, ["status", "--json"]) == 0
    doc = json.loads(capsys.readouterr().out)
    assert doc["id"] == "heat3d-acrally" and doc["games"][0]["maps"] == []
    assert entry.main(spec, ["extract", "--new", "--progress-json"]) == 0
    lines = [json.loads(l) for l in capsys.readouterr().out.splitlines() if l.startswith("{")]
    assert lines[-1] == {"event": "done", "ok": 0, "failed": 0}
