---
type: Playbook
id: https://w3id.org/lmodel/iso22989/knowledge/playbooks/check-against-a-copy
genre: how-to
title: Check the wording against a copy of the standard
description: How a person who holds a copy of ISO/IEC 22989 tests that the repository shares no run of four or more words with it and cites only numbers that start a line of it, using `scripts/check_overlap.py`, with the copy kept outside the repository.
references:
  - https://w3id.org/lmodel/iso22989/knowledge/references/iso-iec-22989
sources:
  - id: overlap
    resource: scripts/check_overlap.py
    title: the docstring
  - id: allowed
    resource: tests/overlap_allowed.yaml
  - id: test_overlap.py
    resource: tests/test_overlap.py
generated:
  by: process:ktl-librarian
  at: "2026-11-07T01:02:36Z"
status: draft
---

# Check the wording against a copy of the standard

The script's docstring gives the commands. The script:

- reads the copy's plain text;
- checks the schema and the prose the repository writes beside it, the bundle included;
- refuses a copy inside the repository;
- reports a term or clause number the schema cites that starts no line of the copy.[^overlap]

A run may be allowed only with a reason, in `tests/overlap_allowed.yaml`.[^allowed] Run it by hand: CI has no copy, and `tests/test_overlap.py` tests the script on text of its own.[^test_overlap.py]

[^overlap]: scripts/check_overlap.py, the docstring
[^allowed]: tests/overlap_allowed.yaml
[^test_overlap.py]: tests/test_overlap.py
