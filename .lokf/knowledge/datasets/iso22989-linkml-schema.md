---
type: Dataset
id: https://w3id.org/lmodel/iso22989/knowledge/datasets/iso22989-linkml-schema
genre: reference
title: The iso22989 LinkML schema
description: "`src/iso22989/schema/iso22989.yaml`: the vocabulary for describing an AI system in ISO/IEC 22989's terms, with the `Aic` class prefix, the `aic_` slot prefix and `AicEcosystem` as its root."
resource: src/iso22989/schema/iso22989.yaml
about:
  - https://w3id.org/lmodel/iso22989/knowledge/references/iso-iec-22989
sources:
  - id: schema
    resource: src/iso22989/schema/iso22989.yaml
  - id: about.md
    resource: docs/about.md
generated:
  by: process:ktl-librarian
  at: "2026-11-05T09:56:09Z"
status: draft
---

# The iso22989 LinkML schema

Every record mixes in `AicRecordMixin`, so it has an `aic_id`, a `title` and a `description`. A record refers to another by that identifier, and `AicEcosystem` holds each kind of record in a list of its own.[^about.md]

A system is an `AicSystem`, `AicAgent`, `AicExpertSystem` or `AicRobot`, and a model is an `AicModel`, `AicMachineLearningModel` or `AicNeuralNetworkModel`. A designator names which.[^about.md]

An element cites what it renders by number, in the `iso22989_term` or `iso22989_clause` annotation.[^schema]

[^schema]: src/iso22989/schema/iso22989.yaml
[^about.md]: docs/about.md
