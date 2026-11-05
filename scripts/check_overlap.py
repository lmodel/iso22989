#!/usr/bin/env python3
"""Report any run of words this repository shares with a copy of the standard.

ISO/IEC 22989 is copyright ISO and IEC, and this repository holds none of its
text. A person who holds a copy can test that claim: this script takes the
copy's plain text and fails on any run of four or more consecutive words that
also appears in the schema's descriptions, titles and comments, or in the
Markdown under docs/, the README or the schema's folder.

Run it by hand. It stays out of CI, since CI has no copy of the standard, and
the copy must stay outside the repository.

Usage::

    pdftotext -layout iso_iec_22989.pdf /tmp/iso22989.txt
    python scripts/check_overlap.py --source /tmp/iso22989.txt

A run may be listed in tests/overlap_allowed.yaml with the reason it is allowed.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
SCHEMA = ROOT / "src" / "iso22989" / "schema" / "iso22989.yaml"
ALLOWED = ROOT / "tests" / "overlap_allowed.yaml"
RUN = 4
# The prose this repository writes, beside the schema.
PROSE = (
    "README.md",
    "docs/about.md",
    "docs/index.md",
    "src/iso22989/schema/README.md",
    "src/iso22989/schema/OVERLAY.md",
)
TEXT_KEYS = ("description", "title", "comments", "notes")
WORD = re.compile(r"[a-z0-9]+(?:['’-][a-z0-9]+)*")


def words(text: str) -> list[str]:
    """The lowercase words of a text, with case and punctuation ignored."""
    return WORD.findall(text.lower())


def runs(text: str, size: int = RUN) -> set[tuple[str, ...]]:
    """Every run of `size` consecutive words in a text."""
    found = words(text)
    return {tuple(found[i : i + size]) for i in range(len(found) - size + 1)}


def schema_texts(node, path: str = "schema"):
    """Each (path, text) of a descriptive key anywhere in a parsed schema."""
    if isinstance(node, dict):
        for key, value in node.items():
            here = f"{path}/{key}"
            # A slot may be named description too; its entry is a mapping.
            if key in TEXT_KEYS and isinstance(value, str):
                yield here, value
            elif key in TEXT_KEYS and isinstance(value, list):
                for item in value:
                    yield here, str(item)
            else:
                yield from schema_texts(value, here)
    elif isinstance(node, list):
        for item in node:
            yield from schema_texts(item, path)


def repository_texts(root: Path = ROOT):
    """Each (where, text) this repository writes in its own words."""
    yield from schema_texts(
        yaml.safe_load((root / SCHEMA.relative_to(ROOT)).read_text(encoding="utf-8"))
    )
    for name in PROSE:
        path = root / name
        if path.is_file():
            yield name, path.read_text(encoding="utf-8")


def allowed_runs(path: Path = ALLOWED) -> dict[tuple[str, ...], str]:
    """Each allowed run with its reason. Every entry must give a reason."""
    entries = yaml.safe_load(path.read_text(encoding="utf-8")) or []
    allowed = {}
    for entry in entries:
        if not str(entry.get("reason", "")).strip():
            raise ValueError(f"{entry.get('run')!r} gives no reason")
        allowed[tuple(words(entry["run"]))] = entry["reason"]
    return allowed


def overlaps(source: str, texts, allowed) -> list[tuple[str, str]]:
    """Each (where, run) that a text shares with the source and is not allowed."""
    theirs = runs(source)
    found = []
    for where, text in texts:
        for run in sorted(runs(text) & theirs):
            if run not in allowed:
                found.append((where, " ".join(run)))
    return found


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--source", type=Path, required=True, help="The copy's plain text"
    )
    args = parser.parse_args(argv)
    source = args.source.resolve()
    if source.is_relative_to(ROOT):
        parser.error("keep the copy of the standard outside the repository")
    found = overlaps(
        source.read_text(encoding="utf-8", errors="replace"),
        repository_texts(),
        allowed_runs(),
    )
    for where, run in found:
        print(f"{where}: {run}")
    print(f"{len(found)} shared run(s) of {RUN} or more words.")
    return 1 if found else 0


if __name__ == "__main__":
    sys.exit(main())
