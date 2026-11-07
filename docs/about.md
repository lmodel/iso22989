# About iso22989

This page is for anyone reading the [LinkML](https://linkml.io) schema's elements: it says how they are named, how records refer to one another, and what the model leaves out.

## Names

Classes and enums carry the `Aic` prefix, for AI concepts, and slots the `aic_` prefix, so they can be imported beside the Linked Open Knowledge Format (LOKF) and other vocabularies without a clash. Enums are singular, and enum values are snake_case. Every element is in the `iso22989:` namespace (`https://w3id.org/lmodel/iso22989/`).

An element cites what it renders by number: `iso22989_term` for a term of Clause 3, and `iso22989_clause` for a clause. [`tests/iso22989_numbers.yaml`](https://github.com/lmodel/iso22989/blob/main/tests/iso22989_numbers.yaml) lists every term with the element that renders it, or why none does, and every clause number. A concept keeps its own name where that name is the term. Descriptions are this project's own words. A reader with a licensed copy looks the standard's wording up there, by those numbers.

## Records and references

Every record mixes in `AicRecordMixin`, so it has an `aic_id`, a `title` and a `description`. A record that refers to another holds the other's `aic_id`, and `AicEcosystem` holds each kind of record in a list of its own, so every identifier a reference names can be found there.

Two kinds of record come in variants, told apart by a type designator:

- A system is an `AicSystem`, or one of its kinds: `AicAgent`, `AicExpertSystem` or `AicRobot`. `aic_system_type` names which.
- A model is an `AicModel`, or an `AicMachineLearningModel`, or an `AicNeuralNetworkModel`. `aic_model_type` names which.

A party has an `AicStakeholder` record for each role it plays. Each sub-role sits under one role, and the schema's rules refuse a sub-role of another role. The list of sub-roles is open: lmodel/iso42001 names nine more parts under the AI producer role, and only a copy of each standard can settle which parts each one names.

A prediction, the decision it informs and the action that follows are records that point back along that chain.

## What is left out

The schema holds no text of ISO/IEC 22989. It does not list the standard's abbreviations, since the schema spells each name out. Its `AicOecdLifecycleStage` values are the OECD's phases, read from the OECD's own text. The `related_mappings` that pair them with the standard's stages are this project's reading, and have not been checked against Annex A.

The schema models the 2022 text alone. ISO lists two amendments in progress, and `scripts/check_upstream_release.py` reports when ISO publishes one.

## Reference

- [ISO/IEC 22989:2022 on ISO's site](https://www.iso.org/standard/74296.html)
- [ISO Open Data](https://www.iso.org/open-data.html), whose records of it the repository keeps
