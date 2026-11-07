"""Checks the script that tests the repository's text against a copy of the
standard. The copy itself stays outside the repository, so these tests give the
script text of their own."""

import importlib.util
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).parent.parent
SCHEMA = ROOT / "src" / "iso22989" / "schema" / "iso22989.yaml"


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
    """Its texts cover a class description, a comment, the Markdown pages,
    NOTICE, the bundle's concepts, the example data and the numbers file."""
    texts = list(overlap.repository_texts())
    places = {where for where, _ in texts}
    assert "schema/classes/AicSystem/description" in places
    assert "schema/classes/AicSystem/comments" in places
    assert {"README.md", "CHANGELOG.md", "NOTICE", "llms.txt"} <= places
    assert {"docs/about.md", "docs/rights.md"} <= places
    assert ".lokf/knowledge/explanations/scope.md" in places
    assert "tests/iso22989_numbers.yaml" in places
    assert any(where.startswith("tests/data/valid/") for where in places)


def test_a_copy_inside_the_repository_is_refused(overlap, tmp_path, capsys):
    """The copy of the standard must stay outside the repository."""
    inside = ROOT / "tests" / "data" / "README.md"
    with pytest.raises(SystemExit):
        overlap.main(["--source", str(inside)])
    assert "outside the repository" in capsys.readouterr().err


def test_the_script_reads_every_cited_number(overlap):
    """Its numbers cover a class's term, an attribute's term and a value's clause."""
    schema = yaml.safe_load(SCHEMA.read_text(encoding="utf-8"))
    numbers = set(overlap.schema_numbers(schema))
    assert {"3.1.4", "3.3.4", "6.2.2", "Annex A"} <= numbers
    assert all(n == n.strip() and "," not in n for n in numbers)


def test_a_cited_number_that_starts_no_line_is_reported(overlap):
    """A number found only inside a line, or not at all, is reported; one at
    the start of a line, with any indent, is not."""
    source = "  3.1.4\nsome text about 5.2 here\n6.2.2 heading\n3.1.40 other\n"
    assert overlap.missing_numbers(["3.1.4", "5.2", "6.2.2", "3.1.4"], source) == [
        "5.2"
    ]
    assert overlap.missing_numbers(["3.1.4", "3.1.41"], source) == ["3.1.41"]


def test_a_clean_run_exits_zero(overlap, tmp_path):
    """A source that shares no words and starts a line with every cited number
    passes. The numbers come from the schema, so the source holds no text."""
    schema = yaml.safe_load(SCHEMA.read_text(encoding="utf-8"))
    lines = [f"{n} zzz" for n in sorted(set(overlap.schema_numbers(schema)))]
    source = tmp_path / "source.txt"
    source.write_text("\n".join(lines) + "\nyyy xxx www vvv uuu\n", encoding="utf-8")
    assert overlap.main(["--source", str(source)]) == 0


def test_a_missing_number_fails_the_run(overlap, tmp_path, capsys):
    """A source that starts no line with a cited number fails, and the output
    names the number."""
    source = tmp_path / "source.txt"
    source.write_text("zzz yyy xxx www vvv uuu\n", encoding="utf-8")
    assert overlap.main(["--source", str(source)]) == 1
    assert (
        "schema cites 3.1.4, which starts no line of the copy"
        in capsys.readouterr().out
    )
