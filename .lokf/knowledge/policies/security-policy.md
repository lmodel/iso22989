---
type: Policy
id: https://w3id.org/lmodel/iso22989/knowledge/policies/security-policy
genre: reference
title: Security policy
description: How to report a vulnerability in this repository, by GitHub's private reporting, what executes here and what holds each surface. A problem in the standard belongs with its committee.
resource: SECURITY.md
sources:
  - id: security.md
    resource: SECURITY.md
generated:
  by: process:ktl-librarian
  at: "2026-11-05T09:56:09Z"
status: draft
---

# Security policy

Report through GitHub's private vulnerability reporting. Only the latest release receives fixes.[^security.md]

The watch and the two by-hand scripts send no token, and the overlay's merge writes only under `tmp/`.[^security.md] The surface table in the file says what holds each workflow.[^security.md]

[^security.md]: SECURITY.md
