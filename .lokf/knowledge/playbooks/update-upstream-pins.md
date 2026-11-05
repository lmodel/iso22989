---
type: Playbook
id: https://w3id.org/lmodel/iso22989/knowledge/playbooks/update-upstream-pins
genre: how-to
title: Move to another edition or amendment
description: "What to do when the watch reports a change: read the record, decide what the schema changes, replace the extract from one day's dataset, and move the watch's pins and the schema header together."
references:
  - https://w3id.org/lmodel/iso22989/knowledge/datasets/iso-open-data-records
  - https://w3id.org/lmodel/iso22989/knowledge/workflows/upstream-watch
sources:
  - id: watch
    resource: scripts/check_upstream_release.py
    title: the report it writes
  - id: test_upstream.py
    resource: tests/test_upstream.py
  - id: covenant
    resource: AI_COVENANT.md
    title: the note specific to this project
generated:
  by: process:ktl-librarian
  at: "2026-11-05T09:56:09Z"
status: draft
---

# Move to another edition or amendment

1. Read the watch's report, which names the record and the fields that changed.[^watch]
2. Replace the changed lines of the extract from one day's dataset, never by editing them.[^covenant]
3. Move the pins in the watch, and the header's `version` and annotations if the edition moved. `tests/test_upstream.py` holds them equal.[^test_upstream.py]
4. A person who holds the new text reads it and decides what the schema changes. No ISO text goes to an AI tool.[^covenant]

[^watch]: scripts/check_upstream_release.py, the report it writes
[^test_upstream.py]: tests/test_upstream.py
[^covenant]: AI_COVENANT.md, the note specific to this project
