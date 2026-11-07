---
type: Explanation
id: https://w3id.org/lmodel/iso22989/knowledge/explanations/modelling-choices
genre: explanation
title: Modelling choices
description: "Why the schema has these shapes: a vocabulary a host can describe an AI system with, records that refer by identifier, hierarchies with a designator rather than kind fields, and no class without a clause or term behind it."
references:
  - https://w3id.org/lmodel/iso22989/knowledge/datasets/iso22989-linkml-schema
sources:
  - id: about.md
    resource: docs/about.md
  - id: changelog.md
    resource: CHANGELOG.md
    title: Unreleased
generated:
  by: process:ktl-librarian
  at: "2026-11-05T09:56:09Z"
status: draft
---

# Modelling choices

The schema replaced 85 classes and 42 enums with 26 classes and 21 enums. Classes and values with no clause or term behind them were removed, and so were the classes that held a single enum.[^changelog.md]

Systems and models are hierarchies told apart by a designator, and a party has a record for each role it plays.[^about.md]

[^about.md]: docs/about.md
[^changelog.md]: CHANGELOG.md, Unreleased
