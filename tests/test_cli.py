"""
The command line as someone runs it - and as 3DHeat GameFiles runs it, with
the user's own arguments: `course` on another game's lap and without the game,
`stages` on containers built the way the game ships them, `identify`.
"""

from __future__ import annotations

import json

import pytest

from heat3d_ext_acrally.cli import main

from .unreal_fixtures import write_container


def run(capsys, *argv) -> tuple[int, str, str]:
    code = main([str(a) for a in argv])
    out, err = capsys.readouterr()
    return code, out, err


def lap(path, game="assetto-corsa-rally"):
    """A `heat3d-lap` document: a straight 100 m, in metres."""
    xs = [float(i) for i in range(101)]
    path.write_text(
        json.dumps(
            {
                "format": "heat3d-lap",
                "version": 1,
                "game": game,
                "track": None,
                "channels": {"time": xs, "distance": xs, "x": xs, "y": [0.0] * 101, "z": [0.0] * 101},
            }
        ),
        encoding="utf-8",
    )
    return path


def install(folder):
    """A game folder whose containers hold one stage, `Example`, laid out as the game lays it out."""
    paks = folder / "acr" / "Content" / "Paks"
    write_container(
        paks,
        "pakchunk0-Windows",
        {
            "Levels/Example.umap": b"map",
            "Levels/Example/_Generated_/Cell0.umap": b"cell",
            "Levels/Menu.umap": b"menu",
            "Environments/Example/MeshesTrack/SM_ExampleTrack0101.uasset": b"tile",
        },
    )
    return folder


class TestCourse:
    @pytest.mark.parametrize(
        "game, tool",
        [("forza-horizon-5", "heat3d-forza-maps"), ("beamng", "heat3d-beamng-maps")],
    )
    def test_another_games_lap_names_the_tool_for_it(self, capsys, tmp_path, game, tool):
        code, out, err = run(capsys, "course", lap(tmp_path / "lap.json", game))

        assert code == 2 and out == ""
        assert f"{tool} course" in err

    def test_a_game_no_tool_reads(self, capsys, tmp_path):
        code, _, err = run(capsys, "course", lap(tmp_path / "lap.json", "assetto-corsa-evo"))

        assert code == 2 and "no 3DHeat tool exports its course" in err

    def test_game_overrides_what_the_lap_says(self, capsys, tmp_path):
        code, _, err = run(capsys, "course", lap(tmp_path / "lap.json"), "--game", "beamng")

        assert code == 2 and "heat3d-beamng-maps" in err

    def test_no_install_is_one_line_and_exit_2(self, capsys, tmp_path):
        code, _, err = run(capsys, "course", lap(tmp_path / "lap.json"), "--install", tmp_path / "nowhere")

        assert code == 2
        assert len(err.strip().splitlines()) == 1 and ".utoc" in err

    def test_a_stage_that_is_not_there_lists_those_that_are(self, capsys, tmp_path):
        """GameFiles' own options, the Forza ones included, are taken as they come."""
        game = install(tmp_path / "game")

        code, out, err = run(
            capsys, "course", lap(tmp_path / "lap.json"), "--install", game, "--level", "Elsewhere",
            "--season", "winter", "--track", tmp_path, "--margin", "30", "--no-textures", "--game", "acrally",
            "--detail-budget", "100000", "--texture-size", "512", "-o", tmp_path / "out.glb",
        )

        assert code == 2 and out == ""
        assert "no stage called 'Elsewhere'; there are: Example" in err
        assert not (tmp_path / "out.glb").exists()


    def test_no_oodle_is_a_missing_dependency(self, capsys, tmp_path, monkeypatch):
        from heat3d_gamefiles.oodle import OodleUnavailable

        import heat3d_ext_acrally.acrallycourse as course

        def export(*_args, **_kwargs):
            raise OodleUnavailable("no Oodle library found. It cannot be decompressed without one.\n  more")

        monkeypatch.setattr(course, "export", export)
        game = install(tmp_path / "game")

        code, _, err = run(capsys, "course", lap(tmp_path / "lap.json"), "--install", game, "-o", tmp_path / "out.glb")

        assert code == 2
        assert err.strip().splitlines()[-1].startswith("heat3d-acrally-maps: no Oodle library found.")
        assert "HEAT3D_OODLE" in err

class TestStages:
    def test_the_install_and_its_stages(self, capsys, tmp_path):
        game = install(tmp_path / "game")

        code, out, _ = run(capsys, "stages", "--install", game)

        assert code == 0
        assert f"Assetto Corsa Rally at {game / 'acr' / 'Content' / 'Paks'}" in out
        # A level without track tiles in its environment folder is not a stage.
        assert out.splitlines()[1:] == ["  Example", "1 stages"]

    def test_the_paks_folder_itself_is_taken_too(self, capsys, tmp_path):
        game = install(tmp_path / "game")

        code, out, _ = run(capsys, "stages", "--install", game / "acr" / "Content" / "Paks")

        assert code == 0 and "  Example" in out

    def test_no_install(self, capsys, tmp_path):
        code, out, err = run(capsys, "stages", "--install", tmp_path)

        assert code == 2 and out == ""
        assert len(err.strip().splitlines()) == 1


class TestIdentify:
    def test_a_container_mounted_where_the_game_mounts_its_own(self, capsys, tmp_path):
        utoc = install(tmp_path / "game") / "acr" / "Content" / "Paks" / "pakchunk0-Windows.utoc"

        code, out, _ = run(capsys, "identify", utoc)

        assert code == 0
        assert "Assetto Corsa Rally IoStore container, mounted at ../../../acr/Content/" in out
        assert "files      4" in out and "levels     Example, Menu" in out

    def test_another_games_container_and_anything_else_are_not_this_games(self, capsys, tmp_path):
        other = write_container(tmp_path / "other", "pakchunk0-Windows", {"a.uasset": b"x"}, mount="../../../Other/Content/")
        text = tmp_path / "notes.txt"
        text.write_text("just some text\n", encoding="utf-8")
        for path in (other, text):
            code, out, err = run(capsys, "identify", path)
            assert code == 2 and out == ""
            assert err.strip() == f"not an Assetto Corsa Rally file: {path.name}"

    def test_a_missing_file(self, capsys, tmp_path):
        code, _, err = run(capsys, "identify", tmp_path / "gone.utoc")
        assert code == 2 and "no such file" in err


def test_without_gamefiles_one_line_and_exit_2(capsys, monkeypatch):
    import heat3d_ext_acrally.cli as cli

    monkeypatch.setattr(cli, "find_gamefiles", lambda: False)
    code, out, err = run(capsys, "stages")
    assert code == 2 and out == ""
    assert err.strip() == "heat3d-acrally-maps: needs 3DHeat GameFiles: pip install " \
        "git+https://github.com/Holdi601/3DHeat-GameFiles.git, or set HEAT3D_GAMEFILES to its folder"
