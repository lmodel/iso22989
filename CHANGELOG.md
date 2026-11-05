# Changelog

All notable changes to this project are documented here. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

The `v0.0.0` tag is a baseline, not a release: it marks where versioning starts so the first real release is `0.1.0` rather than `1.0.0`. The schema stays below 1.0.0 until its shape settles, so a breaking change is a minor release.

## [Unreleased]

### Added

- **`iso22989_term` and `iso22989_clause` annotations**, with `tests/iso22989_numbers.yaml`, which accounts for every term of Clause 3 by number.
- **`src/iso22989/schema/iso-open-data/`**, ISO Open Data's records of the edition and its two amendments in progress, with a weekly watch that reports a change.
- **`scripts/check_overlap.py`**, which lets a person who holds a copy of the standard find words the repository shares with it.
- **Tests** that hold the numbers, the header and each mapping, and an example per class and a counter-example per constraint, each naming where it fails.
- **`.lokf/iso22989.yaml`, the schema's `lokf adapt` copy.** The knowledge release attaches it as `schema-<tag>-iso22989.yaml`.
- **The repository's Knowledge Trust Ladder (KTL) knowledge bundle and its sidecar automation**, from the KTL v0.61.0 templates with the lokf floor at 0.9.0, and a knowledge website that replaces the mkdocs site.
- **The governance files**: SECURITY.md, AI_COVENANT.md, NOTICE and the CONTRIBUTING checklist.

### Changed

- **The schema is rewritten** with the `Aic` prefix on classes and enums and the `aic_` prefix on slots, from 85 classes and 42 enums to 26 classes and 21 enums, each citing what it renders. A record mixes in `AicRecordMixin`, and a reference holds the `aic_id` of the record it names.
- **Systems and models become hierarchies told apart by a designator**, and the `AicEcosystem` root lists every kind of record.
- **The header** carries `version: "2022"` and ISO's page in `source`.
- **The overlay** covers attributes and writes only under `tmp/`, and `OVERLAY.md` and `docs/about.md` are compacted.
- **The template settings** turn PyPI publishing and the docs preview off, linkml and linkml-runtime are locked at 1.12.1, and the Python project is named `iso22989-linkml`.

### Removed

- **The nine SSSOM sets**, which a matching tool wrote and no source confirmed, and most of whose targets no longer exist.
- **Classes and values with no clause or term behind them**: `Organization`, `InterestedParty`, `RiskItem`, the `Term` hierarchy and the abbreviations, and the one-off classes that held a single enum.
- **The mkdocs site**, with redirects from its addresses to the new site.
