---
type: Service
id: https://w3id.org/lmodel/iso22989/knowledge/workflows/upstream-watch
genre: reference
title: Upstream watch (upstream-watch.yaml)
description: "The weekly check that `scripts/check_upstream_release.py` runs: a change to ISO's records of the edition or its pending amendments, or to the dataset's licence, fails the run and opens or updates an issue."
resource: .github/workflows/upstream-watch.yaml
about:
  - https://w3id.org/lmodel/iso22989/knowledge/references/iso-iec-22989
sources:
  - id: upstream-watch.yaml
    resource: .github/workflows/upstream-watch.yaml
  - id: watch
    resource: scripts/check_upstream_release.py
    title: the docstring
  - id: test_watch.py
    resource: tests/test_watch.py
    title: the docstring
  - resource: .github/scripts/report-issue.sh
    title: how the issue is opened
generated:
  by: process:ktl-librarian
  at: "2026-11-05T09:56:09Z"
status: draft
---

# Upstream watch (upstream-watch.yaml)

The workflow runs every Monday, and a failing check opens an issue or comments on the one already open.[^upstream-watch.yaml]

The script streams ISO Open Data's dataset with no token and compares each pinned record's line by its SHA-256. It also reads the dataset's licence from ISO's open data page, through the Internet Archive when iso.org refuses a script.[^watch]

`tests/test_watch.py` runs it against stubbed answers.[^test_watch.py]

[^upstream-watch.yaml]: .github/workflows/upstream-watch.yaml
[^watch]: scripts/check_upstream_release.py, the docstring
[^test_watch.py]: tests/test_watch.py, the docstring
