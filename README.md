<a href="https://github.com/linkml/linkml-project-copier"><img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-teal.json" alt="Copier Badge" style="max-width:100%;"/></a>

# iso22989

ISO/IEC 22989:2022 AI concepts and terminology (LinkML)

> **Only want to ask?** Install `ktl-docent` into any agent you use, by a route from [the install page](https://w3id.org/ktl/docs/install/), and ask it about this project. It answers from the bundle and says how far each answer has been checked.
>
> **Agents:** if `.lokf/knowledge/index.md` exists, read it first. `llms.txt` says how to weigh it.

## Documentation Website

[https://lmodel.github.io/iso22989](https://lmodel.github.io/iso22989)

## What it models

The schema is a vocabulary for describing an AI system in the terms of [ISO/IEC 22989:2022](https://www.iso.org/standard/74296.html), first edition: the system and its kinds, its models, data and tasks, its stage of life, the parties around it, the trustworthiness claims made for it, and the fields and applications it belongs to. It holds no text of the standard. Each element cites its clause or term by number, and [tests/iso22989_numbers.yaml](tests/iso22989_numbers.yaml) accounts for every term of Clause 3.

`src/iso22989/schema/iso-open-data/` holds ISO Open Data's records of the edition and its two amendments in progress, and a weekly workflow opens an issue when ISO changes them.

## Mappings

* **[lmodel/gist](https://github.com/lmodel/gist)**: `broad_mappings` from a system and a robot, and `related_mappings` from a task. `tests/test_schema_rules.py` checks them against the released copy.
* **[lmodel/spdx](https://github.com/lmodel/spdx)**: `related_mappings` from a system to `AIPackage` and from a dataset to `DatasetPackage`. `tests/test_schema_rules.py` checks them.
* **[lmodel/uco](https://github.com/lmodel/uco)**: `broad_mappings` and `narrow_mappings` from a connected device, and `related_mappings` from a stakeholder. `tests/test_schema_rules.py` checks them.

The schema is the one home for mappings. The SSSOM sets are gone, since a matching tool wrote them, no source confirmed their rows, and most named terms that no longer exist.

## Repository Structure

* [docs/](docs/): the website's own pages
* [project/](project/): generated project files (do not edit them)
* [scripts/](scripts/): the upstream watch and the overlap check
* [src/iso22989/schema/](src/iso22989/schema): the LinkML schema (edit it) and ISO's records
* [src/iso22989/datamodel/](src/iso22989/datamodel): the generated Python datamodel
* [tests/](tests/): Python tests, with example data in [data/](tests/data) and the neighbours' adapt copies in [neighbours/](tests/neighbours)
* [website/](website/): the Astro Starlight site built from the README, `docs/`, the schema's pages and the knowledge bundle

## Developer Tools

Run `just` to list the project's [just](https://github.com/casey/just/) recipes.

## Knowledge Trust Ladder (KTL)

`.lokf/` holds this project's [KTL](https://w3id.org/ktl/) knowledge bundle. Its domain schema, `.lokf/iso22989.yaml`, is the copy `just lokf-adapt` writes from `src/iso22989/schema/iso22989.yaml`, and `just lokf-adapt-check` says when it is stale. Edit the source, never the copy. A release carries the copy as `schema-<tag>-iso22989.yaml`, on the terms [CONTRIBUTING.md](CONTRIBUTING.md#releasing-maintainers) gives.

The copy roots `AicSystem`, `AicComponent`, `AicKnowledge`, `AicTask`, `AicModel`, `AicDataset`, `AicStakeholder`, `AicLifecycleProcess`, `AicTrustworthinessClaim`, `AicAssessment`, `AicApplication`, `AicResourcePool`, `AicIotDevice`, `AicIotSystem` and `AicCyberPhysicalSystem` on `Concept`. In Obsidian, add these to the *Known LOKF types* setting of the KTL Registrar and KTL Curator plugins:

```text
AicSystem, AicAgent, AicExpertSystem, AicRobot, AicComponent, AicKnowledge, AicTask, AicModel, AicMachineLearningModel, AicNeuralNetworkModel, AicDataset, AicStakeholder, AicLifecycleProcess, AicTrustworthinessClaim, AicAssessment, AicApplication, AicResourcePool, AicIotDevice, AicIotSystem, AicCyberPhysicalSystem
```

The copy drops `aic_id` for LOKF's `id`, folds `title` and `description` into LOKF's, and demotes the two designators, since a concept's `type` already names its class. Every other key starts with `aic_`, and `tests/test_schema_rules.py` holds the copy apart from LOKF and the released neighbours.

## License

The schema and the code are under the Apache License 2.0 ([LICENSE](LICENSE)), and the knowledge bundle in [.lokf/knowledge/](.lokf/knowledge) is under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

ISO/IEC 22989 is copyright ISO and IEC, and this repository holds none of its text: [NOTICE](./NOTICE) gives the position, and [docs/rights.md](docs/rights.md) what it means for reuse. This is not an ISO or IEC project, and its use implies no endorsement by either.

## Contributing and security

[CONTRIBUTING.md](CONTRIBUTING.md) is the checklist for pull requests and
releases, [AI_COVENANT.md](AI_COVENANT.md) sets the rules for AI-assisted work,
[SECURITY.md](SECURITY.md) says how to report a vulnerability, and
[CHANGELOG.md](CHANGELOG.md) records the changes.

## Credits

Built from the [linkml-project-copier](https://github.com/linkml/linkml-project-copier) template ([doi:10.5281/zenodo.15163584](https://doi.org/10.5281/zenodo.15163584)).
