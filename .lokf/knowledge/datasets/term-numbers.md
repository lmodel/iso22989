---
type: Dataset
id: https://w3id.org/lmodel/iso22989/knowledge/datasets/term-numbers
genre: reference
title: The term and clause numbers
description: "`tests/iso22989_numbers.yaml`: every clause number of the standard's table of contents, and each term of Clause 3 with the element that renders it or why none does. It holds numbers and element names only."
resource: tests/iso22989_numbers.yaml
references:
  - https://w3id.org/lmodel/iso22989/knowledge/datasets/iso22989-linkml-schema
sources:
  - id: numbers
    resource: tests/iso22989_numbers.yaml
  - id: test_numbers.py
    resource: tests/test_numbers.py
    title: the docstring
generated:
  by: process:ktl-librarian
  at: "2026-11-05T09:56:09Z"
status: draft
---

# The term and clause numbers

The file lists each clause number and each term number, with no text of the standard.[^numbers]

`tests/test_numbers.py` holds the schema's annotations to it in both directions, so a term cannot lose its element without saying why, and a citation cannot name a clause the list does not hold.[^test_numbers.py]

[^numbers]: tests/iso22989_numbers.yaml
[^test_numbers.py]: tests/test_numbers.py, the docstring
