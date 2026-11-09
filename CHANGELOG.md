# Changelog

All notable changes to this project are documented here. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

The `v0.0.0` tag is a baseline, not a release: it marks where versioning starts so the first real release is `0.1.0` rather than `1.0.0`. The schema stays below 1.0.0 until its shape settles, so a breaking change is a minor release.

## [Unreleased]

### Security

- **The sidecar copies and the skills pin are at Knowledge Trust Ladder [v0.62.0](https://github.com/noelmcloughlin/knowledge-trust-ladder/compare/v0.61.0...v0.62.0).** The release changed `.github/workflows/knowledge-registrar.yaml`, `.github/workflows/knowledge-librarian.yaml`, `.github/workflows/knowledge-release.yaml`, `.github/workflows/knowledge-sync.yaml`, `.lokf/scripts/knowledge-librarian.sh`, `.lokf/scripts/knowledge-preflight.sh`, `.lokf/scripts/knowledge-sync.sh`, `.lokf/justfile`, `website/package-lock.json`, `website/package.json` and `website/scripts/sync.mjs` here.

## [0.2.0] - 2026-11-07

### Added

- **The schema as RDF Turtle and the merged schema**, in `project/rdf/` and `project/linkml/`, from `just gen-rdf` and `just gen-merged-schema`.

### Changed

- **The bundle's schema files sit in `.lokf/schema/`**: `lokf.yaml` and the `lokf adapt` copy `iso22989.yaml`, as KTL v0.62.0 lays them out.

## [0.1.0] - 2026-11-07

### Added

- **`iso22989_term` and `iso22989_clause` annotations**, with `tests/iso22989_numbers.yaml`, which accounts for every term of Clause 3 by number.
- **`src/iso22989/schema/iso-open-data/`**, ISO Open Data's records of the edition and its two amendments in progress, with a weekly watch that reports a change. It reads only https addresses on a list of hosts and caps what it reads.
- **`scripts/check_overlap.py`**, which lets a person who holds a copy of the standard find words the repository shares with it, and any cited number that starts no line of the copy.
- **Tests** that hold the numbers, the header and each mapping, and an example per class and a counter-example per constraint, each naming where it fails.
- **Rules on `AicStakeholder`** that refuse a sub-role of another role, and a pattern that holds each of `aic_ml_hyperparameters` to `name=value`, so any validator checks both.
- **Mappings to lmodel/nist-ai-100-1** from a system, the OECD phases and the trustworthiness properties.
- **`.lokf/iso22989.yaml`, the schema's `lokf adapt` copy.** The knowledge release attaches it as `schema-<tag>-iso22989.yaml`.
- **The repository's Knowledge Trust Ladder (KTL) knowledge bundle and its sidecar automation**, from the KTL v0.61.0 templates with the lokf floor at 0.9.0, and a knowledge website that replaces the mkdocs site.
- **The governance files**: SECURITY.md, AI_COVENANT.md, NOTICE and the CONTRIBUTING checklist.

### Changed

- **The schema is rewritten** with the `Aic` prefix on classes and enums and the `aic_` prefix on slots, from 85 classes and 42 enums to 26 classes and 21 enums, each citing what it renders. A record mixes in `AicRecordMixin`, and a reference holds the `aic_id` of the record it names.
- **Systems and models become hierarchies told apart by a designator**, and the `AicEcosystem` root lists every kind of record.
- **The header** carries `version: "2022"` and ISO's page in `source`.
- **The OECD life-cycle phases are read from the OECD's own text**, with `retire_or_decommission` from the Recommendation's 2024 revision and the standard's `retirement` mapped to it.
- **The template settings** turn PyPI publishing and the docs preview off, linkml and linkml-runtime are locked at 1.12.1, and the Python project is named `iso22989-linkml`.

### Removed

- **The nine SSSOM sets**, which a matching tool wrote and no source confirmed, and most of whose targets no longer exist.
- **Classes and values with no clause or term behind them**: `Organization`, `InterestedParty`, `RiskItem`, the `Term` hierarchy and the abbreviations, and the one-off classes that held a single enum.
- **The mkdocs site**, with redirects from its addresses to the new site.
- **The overlay scaffold and its two scripts.** Each element cites its term or clause by number, and a reader with a licensed copy looks the wording up there.
