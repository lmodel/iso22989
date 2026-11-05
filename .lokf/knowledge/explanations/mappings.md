---
type: Explanation
id: https://w3id.org/lmodel/iso22989/knowledge/explanations/mappings
genre: explanation
title: Mappings and the SSSOM sets
description: "Where the schema crosses to other vocabularies: inline mappings to released gist, SPDX and UCO classes, each tested. The nine SSSOM sets are gone, since a matching tool wrote them and most targets no longer exist."
references:
  - https://w3id.org/lmodel/iso22989/knowledge/datasets/neighbour-copies
sources:
  - id: readme.md
    resource: README.md
    title: Mappings
  - id: test_schema_rules.py
    resource: tests/test_schema_rules.py
generated:
  by: process:ktl-librarian
  at: "2026-11-05T09:56:09Z"
status: draft
---

# Mappings and the SSSOM sets

The README lists each mapping, and the schema is their one home.[^readme.md] `tests/test_schema_rules.py` holds each to a class of a released copy.[^test_schema_rules.py]

The SSSOM sets are gone, since a matching tool wrote them, no source confirmed their rows, and most named terms that no longer exist.[^readme.md]

[^readme.md]: README.md, Mappings
[^test_schema_rules.py]: tests/test_schema_rules.py
