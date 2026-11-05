---
type: Dataset
id: https://w3id.org/lmodel/iso22989/knowledge/datasets/overlay
genre: reference
title: The overlay scaffold
description: "`src/iso22989/schema/iso22989-overlay.template.yaml`: an empty scaffold of every element, which a licence holder copies and fills privately, and merges into a private schema under `tmp/`."
resource: src/iso22989/schema/iso22989-overlay.template.yaml
references:
  - https://w3id.org/lmodel/iso22989/knowledge/datasets/iso22989-linkml-schema
sources:
  - id: overlay.md
    resource: src/iso22989/schema/OVERLAY.md
  - id: test_overlay.py
    resource: tests/test_overlay.py
    title: the docstring
  - resource: scripts/create_overlay_template.py
  - resource: scripts/overlay_populated_text.py
generated:
  by: process:ktl-librarian
  at: "2026-11-05T09:56:09Z"
status: draft
---

# The overlay scaffold

The scaffold holds no text. A licence holder fills a private copy, which git ignores, and `just overlay-licensed-text` merges it under `tmp/`. The merge takes only descriptive keys.[^overlay.md]

`tests/test_overlay.py` checks that the scaffold is what the script writes, that it is empty, and that git ignores the private files.[^test_overlay.py]

[^overlay.md]: src/iso22989/schema/OVERLAY.md
[^test_overlay.py]: tests/test_overlay.py, the docstring
