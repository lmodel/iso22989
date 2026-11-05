---
type: Dataset
id: https://w3id.org/lmodel/iso22989/knowledge/datasets/generated-artefacts
genre: reference
title: The generated artefacts
description: "What `just gen-project` and `just gen-doc` generate from the schema: the projections in `project/`, the Python models in `src/iso22989/datamodel/`, and the merged schema in `docs/schema/`. None is edited by hand."
resource: project
references:
  - https://w3id.org/lmodel/iso22989/knowledge/datasets/iso22989-linkml-schema
sources:
  - id: contributing.md
    resource: CONTRIBUTING.md
    title: Before opening a pull request
  - id: test_data.py
    resource: tests/test_data.py
  - resource: src/iso22989/datamodel
  - resource: docs/schema
  - resource: .linkml/generators.yaml
  - resource: config.public.mk
  - resource: docs/index.md
    title: Validating data
generated:
  by: process:ktl-librarian
  at: "2026-11-05T09:56:09Z"
status: draft
---

# The generated artefacts

`just gen-project` writes the projections in `project/` and the Python models in `src/iso22989/datamodel/`, and `just gen-doc` writes the merged schema to `docs/schema/`. They are committed and never edited by hand.[^contributing.md]

`project/jsonschema/iso22989.schema.json` is what a consumer without LinkML validates with, and `tests/test_data.py` holds every valid example to it.[^test_data.py]

[^contributing.md]: CONTRIBUTING.md, Before opening a pull request
[^test_data.py]: tests/test_data.py
