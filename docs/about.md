# About iso22989

A LinkML schema for ISO/IEC 22989:2022 (Information technology — Artificial
intelligence — Artificial intelligence concepts and terminology), with a
curated suite of SSSOM mappings to neighbouring AI, security, privacy and
upper-ontology schemas.

The public schema ships with **paraphrased** descriptions only. The normative
text of ISO/IEC 22989:2022 is © ISO/IEC and is not reproduced anywhere in this
repository. License holders may maintain a private verbatim-text overlay — see
[OVERLAY.md](../src/iso22989/schema/OVERLAY.md).

## Schema

| Element | Count |
|---|---|
| Classes | 85 |
| Slots | 105 |
| Enums | 42 |
| Custom types | 2 |
| Subsets | 9 |

Coverage spans the full ISO/IEC 22989:2022 vocabulary:

- **Core AI concepts** — `AISystem`, `AIModel`, `AIComponent`, `Dataset`,
  `InferenceEngine`, `AIApplication`, `AILifecycleProcess`, `Task`,
  `Prediction`, `Decision`, `Action`.
- **Stakeholders** — `AIStakeholderRole` plus specialised roles
  (`AIProvider`, `AIProducer`, `AICustomer`, `AIPartner`, `AISubject`,
  `RelevantAuthority`, `AIPlatformProvider`, `AIServiceProductProvider`,
  `ModelDesigner`, `ModelImplementer`, `ComputationVerifier`, `ModelVerifier`,
  `AIUser`, `AISystemIntegrator`, `DataProvider`, `AIAuditor`, `AIEvaluator`,
  `DataSubject`, `PolicyMaker`, `Regulator`).
- **Trustworthiness** — `TrustworthinessProperty` with the full
  `TrustworthinessPropertyType` enumeration (robustness, reliability,
  resilience, controllability, explainability, predictability, transparency,
  fairness, bias mitigation, accountability, privacy, safety) and supporting
  `BiasType`, `SocietalImpactCategory`, `JurisdictionalIssueType`.
- **Lifecycle** — `AILifecycleStage`, `OECDLifecycleStage`,
  `OECDLifecycleMapping`, `VerificationValidationFramework`,
  `AutonomyAssessment`, `EvaluationMetric`.
- **AI ecosystem** — `KnowledgeGraph`, `ExpertSystem`,
  `CognitiveComputingSystem`, `SemanticComputingSystem`, `NLPComponent`,
  `ComputerVisionFunction`, `Robot`, `IoTSystem`, `IoTDevice`,
  `CyberPhysicalSystem`, `HumanMachineTeam`.
- **Data** — `InputData`, `DataProcess`, `DataSample`, `DataLabel`,
  `GroundTruthRecord`.
- **Terminology** — `AbbreviatedTerm` plus seven `Term` specialisations
  (`AITerm`, `DataTerm`, `MachineLearningTerm`, `NeuralNetworkTerm`,
  `TrustworthinessTerm`, `NLPTerm`, `ComputerVisionTerm`) anchoring every
  ISO/IEC 22989:2022 Clause 3 sub-clause.
- **Annex SL anchors** — `Organization`, `InterestedParty` for
  cross-management-system reuse.
- **Risk** — `RiskItem` for AI-risk records carried into ISO/IEC 23894 /
  ISO/IEC 42001 risk programmes.

`AIConceptsCollection` is the containment root for serialising full inventories.

## Cross-framework mappings (SSSOM)

Nine SSSOM/TSV mapping sets are published under `src/iso22989/mappings/`.
All follow the 10-column SSSOM convention with embedded YAML metadata,
PascalCase class CURIEs and `<EnumName>#pv_snake_case` PV CURIEs.
Mapping justification is `semapv:LLMBasedMatching` pending expert review.

### NIST AI Risk Management Framework

| File | Target | Rows |
|---|---|---|
| `iso22989-to-nist-ai-rmf-common.sssom.tsv` | NIST AI RMF common module (trustworthiness characteristics) | 14 |
| `iso22989-to-nist-ai-100-1.sssom.tsv` | NIST AI 100-1 (RMF 1.0 core) | 24 |
| `iso22989-to-nist-ai-600-1.sssom.tsv` | NIST AI 600-1 (Generative AI Profile) | 21 |
| `iso22989-to-merged-nist-ai-rmf.sssom.tsv` | Consolidated NIST AI RMF rollup | 13 |

### ISO sibling standards

| File | Target | Rows |
|---|---|---|
| `iso22989-to-iso42001.sssom.tsv` | ISO/IEC 42001:2023 AI management system | 4 |
| `iso22989-to-iso27001.sssom.tsv` | ISO/IEC 27001:2022 ISMS (Annex SL + risk + privacy) | 8 |
| `iso22989-to-iso29100.sssom.tsv` | ISO/IEC 29100:2011 privacy framework | 13 |

### Upper ontologies

| File | Target | Rows |
|---|---|---|
| `iso22989-to-gist.sssom.tsv` | gist minimal upper ontology (Semantic Arts) | 10 |
| `iso22989-to-uco-core.sssom.tsv` | Unified Cyber Ontology (UCO) Core | 4 |

**Total: 111 mapping rows across 9 mapping sets.**

## Verbatim-text overlay

License-holders of ISO/IEC 22989:2022 may locally swap the public paraphrased
descriptions for the verbatim normative wording using a deep-merge overlay
pipeline; the overlay file is git-ignored and never published. See
[OVERLAY.md](../src/iso22989/schema/OVERLAY.md).

Pipeline:

- `just create-empty-overlay` — regenerate the empty scaffold
  `iso22989-overlay.template.yaml` (committed; contains no copyrighted text).
- `just overlay-licensed-text` — merge the populated overlay into
  `tmp/iso22989-merged.yaml` for local use by downstream generators.

## Testing

The full gate — `just test` (schema generation → `pytest` → example generation)
— is green: **90 passing tests, 0 failures**.

- `tests/data/valid/` contains **34** example fixtures. Every fixture is loaded
  through the generated Python data model *and* validated against the schema.
  Coverage spans all major classes plus the constraint-bearing ones —
  required-slot classes (`ResourcePool`, `IoTDevice`, `DataProcess`,
  `GroundTruthRecord`, `DataLabel`, `SoftComputingSystem`, `EvaluationMetric`,
  `Threshold`, `OECDLifecycleMapping`, `VerificationValidationFramework`,
  `AbbreviationEntry`), an `ifabsent` sub-role (`AIProvider`), inlined-list
  containment (`IoTSystem`, `AIConceptsCollection`) and object references
  (`Robot`, `KnowledgeGraph`).
- `tests/data/invalid/` contains **10** counter-examples, each failing for a
  single documented reason and together exercising every enforced constraint
  type: invalid enum value, missing required slot, `minimum_value`,
  `maximum_value` (custom type), `pattern`, and wrong scalar type. Each file
  carries a header comment naming the violation it triggers.
- The harness (`tests/test_data.py`) adds structural guards so the data-driven
  tests can never pass vacuously: the schema must parse via `SchemaView`, both
  corpora must be non-empty, and every fixture's file-name stem must name a
  concrete (non-abstract) schema class.

### Schema fixes landed alongside the tests

- Removed a duplicate `tree_root` (only `AIConceptsCollection` is the
  serialisation root; `AISystem` is no longer a competing root).
- Gave the `ConfidenceScore` custom type an explicit `base: float` /
  `uri: xsd:float`, clearing `shaclgen`/`sqltablegen` "unknown range base"
  errors while preserving its `[0.0, 1.0]` bounds.

### Known upstream limitation

`ifabsent` defaults are applied by the Python loader but **not** by JSON-Schema
validation, so a `required` slot with an `ifabsent` default must still be stated
explicitly in validated fixtures (e.g. `AIProvider`). This issue was raised updstream.

## Reference

- [ISO/IEC 22989:2022(E)](https://www.iso.org/standard/74296.html)
- [SSSOM specification](https://mapping-commons.github.io/sssom/)
- [LinkML](https://linkml.io/)
