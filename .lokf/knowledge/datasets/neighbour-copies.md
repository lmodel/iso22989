---
type: Dataset
id: https://w3id.org/lmodel/iso22989/knowledge/datasets/neighbour-copies
genre: reference
title: The neighbours' adapt copies
description: The adapt copies of 35 released lmodel repositories in `tests/neighbours/`, each pinned by its SHA-256, which tests hold this schema's names and mappings to.
resource: tests/neighbours
references:
  - https://w3id.org/lmodel/iso22989/knowledge/datasets/adapt-copy
sources:
  - id: test_schema_rules.py
    resource: tests/test_schema_rules.py
generated:
  by: process:ktl-librarian
  at: "2026-11-07T01:02:36Z"
status: draft
---

# The neighbours' adapt copies

Each copy is the schema asset of a release, pinned by its checksum. The tests check that this schema's copy shares no name with them, and that each mapping names a class one of them holds.[^test_schema_rules.py]

[^test_schema_rules.py]: tests/test_schema_rules.py
