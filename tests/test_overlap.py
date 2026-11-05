"""Checks the script that tests the repository's text against a copy of the
standard. The copy itself stays outside the repository, so these tests give the
script text of their own."""

import importlib.util
from pathlib import Path

import pytest

ROOT = Path(__file__).parent.parent


@pytest.fixture
def overlap():
    spec = importlib.util.spec_from_file_location(
        "check_overlap", ROOT / "scripts" / "check_overlap.py"
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_a_shared_run_of_four_words_is_found(overlap):
    """Four words in a row are found, whatever their case and punctuation."""
    source = "The quick brown fox, jumps over the lazy dog."
    found = overlap.overlaps(source, [("here", "a QUICK brown FOX jumps")], {})
    assert ("here", "quick brown fox jumps") in found


def test_three_shared_words_are_not_a_run(overlap):
    """Three words in a row pass."""
    source = "The quick brown fox jumps."
    assert not overlap.overlaps(source, [("here", "a quick brown cat")], {})


def test_an_allowed_run_passes(overlap):
    """A run on the allow-list is not reported."""
    allowed = {("quick", "brown", "fox", "jumps"): "A test."}
    found = overlap.overlaps(
        "The quick brown fox jumps.", [("here", "quick brown fox jumps")], allowed
    )
    assert not found


def test_every_allowed_run_gives_a_reason(overlap):
    """The committed allow-list loads, and an entry with no reason is refused."""
    assert all(overlap.allowed_runs().values())


def test_an_entry_without_a_reason_is_refused(overlap, tmp_path):
    """An allow-list entry must say why."""
    path = tmp_path / "allowed.yaml"
    path.write_text("- run: a b c d\n  reason: ''\n", encoding="utf-8")
    with pytest.raises(ValueError, match="gives no reason"):
        overlap.allowed_runs(path)


def test_the_script_reads_the_schema_text_and_the_prose(overlap):
    """Its texts cover a class description, a comment, and the README."""
    texts = list(overlap.repository_texts())
    places = {where for where, _ in texts}
    assert "schema/classes/AicSystem/description" in places
    assert "schema/classes/AicSystem/comments" in places
    assert "README.md" in places


def test_a_copy_inside_the_repository_is_refused(overlap, tmp_path, capsys):
    """The copy of the standard must stay outside the repository."""
    inside = ROOT / "tests" / "data" / "README.md"
    with pytest.raises(SystemExit):
        overlap.main(["--source", str(inside)])
    assert "outside the repository" in capsys.readouterr().err


def test_a_clean_run_exits_zero(overlap, tmp_path):
    """A source that shares nothing passes."""
    source = tmp_path / "source.txt"
    source.write_text("zzz yyy xxx www vvv uuu", encoding="utf-8")
    assert overlap.main(["--source", str(source)]) == 0
