---
type: Dataset
id: https://w3id.org/lmodel/iso22989/knowledge/datasets/example-data
genre: reference
title: The example data
description: "`tests/data/`: a valid example per class and a counter-example per constraint, each counter-example naming on its first line where it must fail. `AicEcosystem-card-payments` is one whole ecosystem."
resource: tests/data
references:
  - https://w3id.org/lmodel/iso22989/knowledge/datasets/iso22989-linkml-schema
sources:
  - id: test_data.py
    resource: tests/test_data.py
  - id: readme
    resource: tests/data/README.md
  - resource: examples/README.md
generated:
  by: process:ktl-librarian
  at: "2026-11-07T01:17:35Z"
status: draft
---

# The example data

File names follow `ClassName-suffix.yaml`.[^readme] A counter-example's first line, `# Fails at: <pointer>`, names where it must fail, so a file that starts failing for another reason fails the test.[^test_data.py]

The same test file checks the rules no validator checks, over the examples: that references resolve within an ecosystem, that no identifier repeats, and that life-cycle work ends on or after the day it begins. It also holds the schema's sub-role rules to the role annotations.[^test_data.py]

[^readme]: tests/data/README.md
[^test_data.py]: tests/test_data.py
