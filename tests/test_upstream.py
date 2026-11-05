"""Checks that the schema models the edition ISO's records name.

ISO holds the text of ISO/IEC 22989, so src/iso22989/schema/iso-open-data/
holds ISO Open Data's records of the edition and of its pending amendments
instead, which scripts/check_upstream_release.py pins and watches. These tests
read that extract with the standard library and hold the schema header to it
and to the watch's pins.
"""

import importlib.util
import json
from functools import cache
from pathlib import Path

import yaml

ROOT = Path(__file__).parent.parent
SCHEMA = ROOT / "src" / "iso22989" / "schema" / "iso22989.yaml"
EXTRACT = (
    ROOT
    / "src"
    / "iso22989"
    / "schema"
    / "iso-open-data"
    / "iso_deliverables_metadata.jsonl"
)


@cache
def _watch():
    """The upstream watch script, loaded once as a module."""
    spec = importlib.util.spec_from_file_location(
        "watch", ROOT / "scripts" / "check_upstream_release.py"
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _records():
    lines = EXTRACT.read_text(encoding="utf-8").splitlines()
    return {r["id"]: r for r in map(json.loads, lines)}


def test_extract_matches_the_pinned_lines():
    """Each line of the extract hashes to the watch's pin, and the extract
    holds no scope, the field that summarizes the standard in ISO's words."""
    watch = _watch()
    lines = EXTRACT.read_text(encoding="utf-8").splitlines()
    hashes = {json.loads(line)["id"]: watch.digest(line) for line in lines}
    assert hashes == watch.PINNED_RECORDS
    for record in _records().values():
        assert not set(watch.LEFT_OUT) & record.keys(), record["id"]
        assert watch.line_of(record) in lines


def test_header_pins_match_the_watch():
    """The header's version, source and dates are the ones the watch pins and
    the extract records."""
    watch = _watch()
    header = yaml.safe_load(SCHEMA.read_text(encoding="utf-8"))
    notes = header["annotations"]
    edition = _records()[watch.EDITION_ID]
    assert header["version"] == watch.PINNED_VERSION == "2022"
    assert header["source"] == watch.PINNED_SOURCE
    assert header["source"].endswith(f"/{watch.EDITION_ID}.html")
    assert notes["standard"] == edition["reference"] == watch.PINNED_EDITION
    assert notes["edition"] == str(edition["edition"])
    assert notes["publication_date"] == edition["publicationDate"]
    assert notes["iso_open_data_date"] == watch.PINNED_DATE


def test_only_the_edition_is_published():
    """The edition is at the published stage and names no successor, and each
    other pinned record is a supplement ISO has not published, so the schema
    models the 2022 text alone."""
    watch = _watch()
    for record in _records().values():
        if record["id"] == watch.EDITION_ID:
            assert record["currentStage"] == watch.PUBLISHED
            assert not record["replacedBy"]
        else:
            assert record["reference"].startswith(watch.SUPPLEMENT_PREFIX)
            assert record["currentStage"] != watch.PUBLISHED
            assert record["publicationDate"] is None
