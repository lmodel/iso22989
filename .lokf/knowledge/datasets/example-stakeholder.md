---
type: AicStakeholder
id: https://w3id.org/lmodel/iso22989/knowledge/datasets/example-stakeholder
genre: reference
title: A bank as AI producer
description: An example written as a concept of type `AicStakeholder` in the adapt copy's keys. It shows that the domain schema admits a party as a concept, with its role and sub-role.
resource: tests/data/valid/AicStakeholder-bank.yaml
references:
  - https://w3id.org/lmodel/iso22989/knowledge/datasets/adapt-copy
sources:
  - id: readme.md
    resource: README.md
    title: the Knowledge Trust Ladder (KTL) section
  - id: example
    resource: tests/data/valid/AicStakeholder-bank.yaml
aic_stakeholder_role: ai_producer
aic_stakeholder_sub_roles:
  - ai_developer
aic_stakeholder_organization: Example Bank
generated:
  by: process:ktl-librarian
  at: "2026-11-05T09:56:09Z"
status: draft
---

# A bank as AI producer

This concept is the example in `tests/data/valid/`, written in the keys the adapt copy gives a concept.[^example] The README lists the classes a concept may name as its type.[^readme.md]

[^example]: tests/data/valid/AicStakeholder-bank.yaml
[^readme.md]: README.md, the Knowledge Trust Ladder (KTL) section
