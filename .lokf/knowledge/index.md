---
lokf_version: "0.2"
okf_version: "0.2"
base_iri: https://w3id.org/lmodel/iso22989/knowledge/
context: https://w3id.org/lokf/context.jsonld
title: iso22989 Knowledge Bundle
description: ISO/IEC 22989:2022 AI concepts and terminology (LinkML)
license: https://creativecommons.org/licenses/by/4.0/
publisher:
  type: Person
  id: https://w3id.org/lmodel/iso22989/knowledge/person/noel-mcloughlin
  name: Noel McLoughlin
---

# iso22989 Knowledge Bundle

A [LOKF](https://lokf.nolan-nichols.com) knowledge base for iso22989. Every Markdown file under `knowledge/` is one concept; together they form a queryable knowledge graph, derived from this repository's code and docs.

# Services

* [Documentation site](services/documentation-site.md) - The knowledge website in `website/`, an Astro Starlight site that the Knowledge website workflow publishes to GitHub Pages at `https://lmodel.github.io/iso22989`, built from the README, `docs/`, the schema's pages and the bundle. It replaces the mkdocs site.

# Workflows

* [Knowledge librarian (knowledge-librarian.yaml)](workflows/knowledge-librarian.md) - The sidecar's scheduled agent run that keeps the bundle in step with the repository and opens a pull request for a person to review. It is inert until `KNOWLEDGE_LIBRARIAN_ENABLED` is `true`.
* [Knowledge registrar (knowledge-registrar.yaml)](workflows/knowledge-registrar.md) - The gate on the bundle: it validates the bundle on each pull request that touches it and weekly, and checks that each new `human:` event in a pull request is backed by an approval or a signature. It never judges whether content is true.
* [Knowledge release (knowledge-release.yaml)](workflows/knowledge-release.md) - The workflow that attaches the bundle, a Copilot skill and the schema's adapt copy to a GitHub release, each with a checksum. It starts by hand or, once `KNOWLEDGE_RELEASE_ENABLED` is `true`, on each published release.
* [Knowledge sync (knowledge-sync.yaml)](workflows/knowledge-sync.md) - The weekly workflow that keeps the sidecar's copies and the skills pin at the newest release of Knowledge Trust Ladder, by one pull request that a person merges.
* [Knowledge website (knowledge-website.yaml)](workflows/knowledge-website.md) - The workflow that builds `website/` on each pull request that touches its inputs, and deploys the default branch's build to GitHub Pages once `KNOWLEDGE_WEBSITE_ENABLED` is `true`.
* [Lint and docs (lint-and-docs.yaml)](workflows/lint-and-docs.md) - The static checks on pull requests, on `main` and every Monday: ShellCheck, actionlint, the word budgets of CONTRIBUTING.md and SECURITY.md, markdownlint, lychee and codespell.
* [Build and test (main.yaml)](workflows/main.md) - The Build and test workflow: on every pull request and push to `main`, it runs `just test` on Python 3.10 to 3.14, and lints the schema and checks the adapt copy on 3.13.
* [Semantic release (semantic-release.yml)](workflows/semantic-release.md) - The workflow that computes the next version from Conventional Commits on `main`, promotes the changelog, tags and publishes a GitHub Release, and dispatches the knowledge release once `KNOWLEDGE_RELEASE_ENABLED` is `true`.
* [Upstream watch (upstream-watch.yaml)](workflows/upstream-watch.md) - The weekly check that `scripts/check_upstream_release.py` runs: a change to ISO's records of the edition or its pending amendments, or to the dataset's licence, fails the run and opens or updates an issue.

# Playbooks

* [Release](playbooks/release.md) - How a release happens: `semantic-release.yml` reads Conventional Commits on `main`, promotes the `## [Unreleased]` section, tags and publishes. The first release needs the `v0.0.0` baseline tag on `main`, and PyPI publishing stays off.
* [Regenerate and test](playbooks/regenerate-and-test.md) - How to change the schema: edit `src/iso22989/schema/iso22989.yaml`, run `just lint`, `just gen-project`, `just gen-doc`, `just lokf-adapt`, `just create-empty-overlay` and `just test`, and commit what they write.
* [Move to another edition or amendment](playbooks/update-upstream-pins.md) - What to do when the watch reports a change: read the record, decide what the schema changes, replace the extract from one day's dataset, and move the watch's pins and the schema header together.
* [Check the wording against a copy of the standard](playbooks/check-against-a-copy.md) - How a person who holds a copy of ISO/IEC 22989 tests that the repository shares no run of four or more words with it, using `scripts/check_overlap.py`, with the copy kept outside the repository.
* [Knowledge sources map](playbooks/knowledge-sources.md) - The librarian's scrape map: every repository location this bundle derives concepts from, how to re-check each, and the tracked paths left out with their reasons.

# Glossary

* [Adapt copy](glossary/adapt-copy.md) - An adapt copy: the copy of a published LinkML schema that `lokf adapt` writes so that it can sit beside LOKF's `lokf.yaml` in a domain schema, with its chosen roots on `Concept`.

# Datasets

* [The schema's adapt copy](datasets/adapt-copy.md) - `.lokf/iso22989.yaml`, the copy `just lokf-adapt` writes from the schema so that it sits beside LOKF's `lokf.yaml`: fifteen classes rooted on `Concept`, `ai_rmf_id` dropped for LOKF's `id`, `title` and `description` folded into LOKF's, and two designators demoted.
* [The iso22989 LinkML schema](datasets/iso22989-linkml-schema.md) - `src/iso22989/schema/iso22989.yaml`: the vocabulary for describing an AI system in ISO/IEC 22989's terms, with the `Aic` class prefix, the `aic_` slot prefix and `AicEcosystem` as its root.
* [The term and clause numbers](datasets/term-numbers.md) - `tests/iso22989_numbers.yaml`: every clause number of the standard's table of contents, and each term of Clause 3 with the element that renders it or why none does. It holds numbers and element names only.
* [ISO Open Data's records](datasets/iso-open-data-records.md) - `src/iso22989/schema/iso-open-data/`: ISO's records of the edition and its two pending amendments as of 2026-11-05, under ODC-By v1.0, each without its scope and pinned by hash.
* [The overlay scaffold](datasets/overlay.md) - `src/iso22989/schema/iso22989-overlay.template.yaml`: an empty scaffold of every element, which a licence holder copies and fills privately, and merges into a private schema under `tmp/`.
* [The generated artefacts](datasets/generated-artefacts.md) - What `just gen-project` and `just gen-doc` generate from the schema: the projections in `project/`, the Python models in `src/iso22989/datamodel/`, and the merged schema in `docs/schema/`. None is edited by hand.
* [The example data](datasets/example-data.md) - `tests/data/`: a valid example per class and a counter-example per constraint, each counter-example naming on its first line where it must fail. `AicEcosystem-card-payments` is one whole ecosystem.
* [A bank as AI producer](datasets/example-stakeholder.md) - An example written as a concept of type `AicStakeholder` in the adapt copy's keys. It shows that the domain schema admits a party as a concept, with its role and sub-role.
* [The neighbours' adapt copies](datasets/neighbour-copies.md) - The adapt copies of 19 released lmodel repositories in `tests/neighbours/`, each pinned by its SHA-256, which tests hold this schema's names and mappings to.

# References

* [ISO/IEC 22989:2022](references/iso-iec-22989.md) - The edition the schema renders: ISO's record 74296, first edition, published 2022-07-19. Two amendments are in progress and unpublished, and this bundle holds none of the standard's text.

# Policies

* [AI covenant](policies/ai-covenant.md) - The rules for AI-assisted work here: whoever submits owns the contribution, an element cites its clause or term and quotes none of it, no ISO text goes anywhere in the repository or to an AI tool.
* [Security policy](policies/security-policy.md) - How to report a vulnerability in this repository, by GitHub's private reporting, what executes here and what holds each surface. A problem in the standard belongs with its committee.
* [Licence and attribution](policies/license-and-attribution.md) - Whose work each part is: the code and schema under Apache-2.0, the bundle under CC BY 4.0, ISO's metadata records under ODC-By, and the standard's text, which the repository does not hold.

# Explanations

* [Modelling choices](explanations/modelling-choices.md) - Why the schema has these shapes: a vocabulary a host can describe an AI system with, records that refer by identifier, hierarchies with a designator rather than kind fields, and no class without a clause or term behind it.
* [Mappings and the SSSOM sets](explanations/mappings.md) - Where the schema crosses to other vocabularies: inline mappings to released gist, SPDX and UCO classes, each tested. The nine SSSOM sets are gone, since a matching tool wrote them and most targets no longer exist.
* [Scope](explanations/scope.md) - What the schema leaves out: the standard's text, its abbreviations and its pending amendments. Its OECD pairings are this project's reading of Annex A, not checked against its text.
