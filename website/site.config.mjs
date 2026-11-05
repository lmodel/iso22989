// The site's values and options, in one place. scripts/config.mjs reads this
// file, fills in every option left out, settles each "auto" against the
// repository and checks the required values. `node scripts/config.mjs`
// prints the result. Nothing here runs code, so the pages that show the
// title import it too.
//
// The first five values are required. The rest are optional: leave one out,
// or set it to "auto", and the site shows that part of the repository when
// the repository has it. Set it to null to leave that part out.

// The repository, as owner/name, and the site's address: the owner's GitHub
// Pages domain and the path under it. A user site (the <owner>.github.io
// repository) or a custom domain sets BASE to "".
export const REPO = "lmodel/iso22989";
export const SITE = "https://lmodel.github.io";
export const BASE = "/iso22989";

// The site's title, in the header and on every social card, and its
// description, for search engines and as the home page's tagline when
// HOME.tagline is not set.
export const TITLE = "iso22989";
export const DESCRIPTION = "ISO/IEC 22989:2022 AI concepts and terminology (LinkML)";

// The branch an "Edit page" link opens.
export const BRANCH = "main";

// A custom domain, which the sync writes to public/CNAME, or null for a
// Pages address. The site leaves the domain's DNS to the repository.
export const CUSTOM_DOMAIN = null;

// The logo, as paths from the repository root: a light version, a dark one
// (the light one again when left out) and a favicon (the light logo when it
// is an SVG, else the site's own ladder mark). "auto" takes the Knowledge
// Trust Ladder logo: a knowledge-trust-ladder-logo.svg the repository
// already has, or else the copy in src/assets/. A single path is the light
// version alone. null shows the title as text.
//   export const LOGO = { light: ".assets/logo.svg", dark: ".assets/logo-dark.svg" };
export const LOGO = "auto";

// The folder of figures the README and the docs pages show, served under
// /assets/. "auto" takes .assets/ when there is one.
export const ASSETS = "auto";

// The docs pages: a folder, the sidebar groups its pages sit in (each page
// named by its path under the folder, without .md), and the paths under the
// folder that are not pages of the site, each a file or a folder. With no
// groups, every page sits in one Guides group, by title, with the folder's
// index.md first as its Overview. With groups, the sync stops with an error
// when a group names a missing page or a page has no group, so a new page
// cannot go missing from the sidebar. "auto" takes docs/ when there is one.
// null shows no docs pages.
//   export const DOCS = { dir: "docs", groups: [{ label: "Guides", pages: ["install", "usage"] }], exclude: ["templates-linkml"] };
export const DOCS = { dir: "docs", exclude: ["templates-linkml"] };

// Old addresses under BASE, each redirected to a page of the site, such as
// the addresses a retired mkdocs site gave its pages and a w3id rule still
// names. An entry whose key and value both end in /[...slug] stands for one
// redirect per schema page.
//   export const REDIRECTS = { "/elements": "/schema/", "/elements/[...slug]": "/schema/[...slug]", "/about": "/docs/about/" };
export const REDIRECTS = {
  "/about": "/docs/about/",
  "/elements": "/schema/",
  "/rights": "/docs/rights/",
  "/elements/AbbreviatedTerm": "/schema/",
  "/elements/abbreviation_code": "/schema/",
  "/elements/AbbreviationCode": "/schema/",
  "/elements/AbbreviationEntry": "/schema/",
  "/elements/abbreviations": "/schema/",
  "/elements/Action": "/schema/AicAction/",
  "/elements/action_target": "/schema/aic_action_target/",
  "/elements/activation_function": "/schema/",
  "/elements/ActivationFunctionType": "/schema/aic_network_activation_functions/",
  "/elements/actuating_capabilities": "/schema/",
  "/elements/affected_dataset": "/schema/",
  "/elements/affected_model": "/schema/",
  "/elements/affected_stakeholders": "/schema/",
  "/elements/agent_architecture": "/schema/",
  "/elements/AgentArchitectureType": "/schema/",
  "/elements/ai_applications": "/schema/aic_ecosystem_applications/",
  "/elements/ai_applications_domain": "/schema/",
  "/elements/ai_components": "/schema/",
  "/elements/ai_concepts": "/schema/",
  "/elements/ai_datasets": "/schema/aic_ecosystem_datasets/",
  "/elements/ai_ecosystem": "/schema/",
  "/elements/ai_field": "/schema/aic_system_fields/",
  "/elements/ai_fields": "/schema/",
  "/elements/ai_functional_view": "/schema/",
  "/elements/ai_lifecycle": "/schema/",
  "/elements/ai_lifecycle_processes": "/schema/aic_ecosystem_lifecycle_processes/",
  "/elements/ai_models": "/schema/aic_ecosystem_models/",
  "/elements/ai_stakeholder_roles": "/schema/aic_ecosystem_stakeholders/",
  "/elements/ai_stakeholders": "/schema/",
  "/elements/ai_system_type": "/schema/aic_system_scope/",
  "/elements/ai_systems": "/schema/aic_ecosystem_systems/",
  "/elements/ai_systems_involved": "/schema/",
  "/elements/AIAgent": "/schema/AicAgent/",
  "/elements/AIApplication": "/schema/AicApplication/",
  "/elements/AIApplicationDomain": "/schema/AicApplicationDomain/",
  "/elements/AIAuditor": "/schema/AicStakeholder/",
  "/elements/AIComponent": "/schema/AicComponent/",
  "/elements/AIConcept": "/schema/",
  "/elements/AIConceptsCollection": "/schema/AicEcosystem/",
  "/elements/AICustomer": "/schema/AicStakeholder/",
  "/elements/AIEcosystem": "/schema/AicEcosystem/",
  "/elements/AIEvaluator": "/schema/AicStakeholder/",
  "/elements/AIField": "/schema/AicField/",
  "/elements/AIFunctionalComponent": "/schema/AicFunctionalStep/",
  "/elements/AILifecycleProcess": "/schema/AicLifecycleProcess/",
  "/elements/AILifecycleStage": "/schema/AicLifecycleStage/",
  "/elements/AIModel": "/schema/AicModel/",
  "/elements/AIPartner": "/schema/AicStakeholder/",
  "/elements/AIPlatformProvider": "/schema/AicStakeholderSubRole/",
  "/elements/AIProducer": "/schema/AicStakeholder/",
  "/elements/AIProvider": "/schema/AicStakeholder/",
  "/elements/AIServiceProductProvider": "/schema/AicStakeholderSubRole/",
  "/elements/AIStakeholderRole": "/schema/AicStakeholder/",
  "/elements/AIStakeholderRoleType": "/schema/AicStakeholderRole/",
  "/elements/AISubject": "/schema/AicStakeholder/",
  "/elements/AISystem": "/schema/AicSystem/",
  "/elements/AISystemCharacteristic": "/schema/",
  "/elements/AISystemIntegrator": "/schema/AicStakeholderSubRole/",
  "/elements/AISystemType": "/schema/AicSystemScope/",
  "/elements/AITerm": "/schema/",
  "/elements/AIUser": "/schema/AicStakeholderSubRole/",
  "/elements/algorithm_family": "/schema/aic_ml_algorithm/",
  "/elements/aliases": "/schema/",
  "/elements/annotator": "/schema/",
  "/elements/applicable_biases": "/schema/",
  "/elements/application_domain": "/schema/aic_application_domain/",
  "/elements/applies_to_metric": "/schema/",
  "/elements/approval_criteria": "/schema/",
  "/elements/augmented_capability": "/schema/",
  "/elements/autonomy_criterion_scores": "/schema/",
  "/elements/autonomy_level": "/schema/aic_system_autonomy/",
  "/elements/AutonomyAssessment": "/schema/AicAutonomy/",
  "/elements/AutonomyCriterion": "/schema/",
  "/elements/AutonomyLevel": "/schema/AicAutonomy/",
  "/elements/based_on_predictions": "/schema/",
  "/elements/BiasType": "/schema/",
  "/elements/big_data_characteristics": "/schema/",
  "/elements/BigDataCharacteristic": "/schema/",
  "/elements/capacity_units": "/schema/",
  "/elements/catastrophic_forgetting_risk": "/schema/",
  "/elements/CatastrophicForgetting": "/schema/",
  "/elements/clause_reference": "/schema/",
  "/elements/cognitive_capabilities": "/schema/",
  "/elements/CognitiveComputingSystem": "/schema/AicTechnique/",
  "/elements/collection_date_range": "/schema/",
  "/elements/component_function": "/schema/",
  "/elements/components": "/schema/aic_system_components/",
  "/elements/ComputationVerifier": "/schema/AicStakeholder/",
  "/elements/ComputerVisionFunction": "/schema/AicTaskKind/",
  "/elements/ComputerVisionTask": "/schema/AicTaskKind/",
  "/elements/ComputerVisionTerm": "/schema/",
  "/elements/computing_resources": "/schema/",
  "/elements/ComputingResourceType": "/schema/AicResourceKind/",
  "/elements/confidence": "/schema/aic_prediction_confidence/",
  "/elements/confidence_score": "/schema/",
  "/elements/ConfidenceScore": "/schema/",
  "/elements/consequence": "/schema/",
  "/elements/consumed_by": "/schema/",
  "/elements/contact": "/schema/aic_stakeholder_contact/",
  "/elements/contains_personal_data": "/schema/",
  "/elements/controlled_by": "/schema/",
  "/elements/ConvolutionOperation": "/schema/AicNeuralNetworkModel/",
  "/elements/coverage_scope": "/schema/",
  "/elements/cv_task": "/schema/",
  "/elements/cyber_components": "/schema/",
  "/elements/cyber_physical_systems": "/schema/",
  "/elements/CyberPhysicalSystem": "/schema/AicCyberPhysicalSystem/",
  "/elements/data_collection_method": "/schema/",
  "/elements/data_modality": "/schema/",
  "/elements/data_processes": "/schema/",
  "/elements/data_processes_applied": "/schema/",
  "/elements/data_provenance": "/schema/",
  "/elements/data_quality_notes": "/schema/",
  "/elements/data_source_type": "/schema/",
  "/elements/data_sources": "/schema/",
  "/elements/data_version": "/schema/",
  "/elements/DataCollectionMethod": "/schema/",
  "/elements/DataDrift": "/schema/",
  "/elements/DataLabel": "/schema/aic_dataset_labels/",
  "/elements/DataLabelType": "/schema/aic_dataset_labels/",
  "/elements/DataModality": "/schema/",
  "/elements/DataProcess": "/schema/AicDataProcess/",
  "/elements/DataProcessType": "/schema/AicDataProcessKind/",
  "/elements/DataProvider": "/schema/AicStakeholderSubRole/",
  "/elements/DataSample": "/schema/aic_dataset_sample_count/",
  "/elements/Dataset": "/schema/AicDataset/",
  "/elements/dataset_role": "/schema/aic_dataset_roles/",
  "/elements/DatasetRole": "/schema/AicDatasetRole/",
  "/elements/datasets": "/schema/aic_system_datasets/",
  "/elements/DataSourceType": "/schema/",
  "/elements/DataSubject": "/schema/AicStakeholderSubRole/",
  "/elements/DataTerm": "/schema/",
  "/elements/Decision": "/schema/AicDecision/",
  "/elements/decision_outcome": "/schema/aic_decision_outcome/",
  "/elements/decision_policy": "/schema/aic_decision_criteria/",
  "/elements/depends_on": "/schema/",
  "/elements/detected_at": "/schema/",
  "/elements/device_role": "/schema/",
  "/elements/devices": "/schema/",
  "/elements/drift_type": "/schema/",
  "/elements/DurationType": "/schema/",
  "/elements/ecosystem_components": "/schema/",
  "/elements/edge_count": "/schema/",
  "/elements/embodiment": "/schema/",
  "/elements/end_date": "/schema/aic_lifecycle_end/",
  "/elements/engineering_approach": "/schema/",
  "/elements/EngineeringApproach": "/schema/AicTechnique/",
  "/elements/EvaluationMetric": "/schema/aic_task_performance_measures/",
  "/elements/executed_by": "/schema/",
  "/elements/execution_status": "/schema/",
  "/elements/ExecutionStatus": "/schema/",
  "/elements/expansion": "/schema/",
  "/elements/expert_systems": "/schema/",
  "/elements/ExpertSystem": "/schema/AicExpertSystem/",
  "/elements/FaultToleranceMechanism": "/schema/AicTrustworthinessProperty/",
  "/elements/feature_count": "/schema/",
  "/elements/functional_components": "/schema/aic_system_steps/",
  "/elements/goal_set": "/schema/",
  "/elements/ground_truth_available": "/schema/",
  "/elements/ground_truth_value": "/schema/",
  "/elements/GroundTruthRecord": "/schema/aic_dataset_ground_truth/",
  "/elements/hosting_system": "/schema/",
  "/elements/human_roles": "/schema/",
  "/elements/HumanMachineTeam": "/schema/aic_system_human_teaming/",
  "/elements/hyperparameters": "/schema/aic_ml_hyperparameters/",
  "/elements/id": "/schema/aic_id/",
  "/elements/Inference": "/schema/aic_expert_inference/",
  "/elements/inference_engine": "/schema/",
  "/elements/inference_latency_ms": "/schema/",
  "/elements/inference_strategy": "/schema/",
  "/elements/InferenceEngine": "/schema/aic_expert_inference/",
  "/elements/input_arity": "/schema/",
  "/elements/input_dataset": "/schema/",
  "/elements/input_modalities": "/schema/",
  "/elements/InputData": "/schema/AicDatasetRole/",
  "/elements/IntelligenceAugmentation": "/schema/",
  "/elements/intended_purpose": "/schema/aic_system_purpose/",
  "/elements/InterestedParty": "/schema/",
  "/elements/iot_integration": "/schema/",
  "/elements/iot_subsystem": "/schema/",
  "/elements/iot_systems": "/schema/",
  "/elements/IoTDevice": "/schema/AicIotDevice/",
  "/elements/IoTDeviceRole": "/schema/",
  "/elements/IoTSystem": "/schema/AicIotSystem/",
  "/elements/iso_stage": "/schema/",
  "/elements/jurisdictional_issues": "/schema/aic_system_jurisdictional_issues/",
  "/elements/JurisdictionalIssueType": "/schema/",
  "/elements/kernel_size": "/schema/",
  "/elements/knowledge_graphs": "/schema/",
  "/elements/knowledge_type": "/schema/",
  "/elements/KnowledgeGraph": "/schema/AicKnowledge/",
  "/elements/KnowledgeRepresentation": "/schema/AicKnowledge/",
  "/elements/KnowledgeType": "/schema/AicKnowledgeKind/",
  "/elements/label_type": "/schema/",
  "/elements/label_value": "/schema/aic_dataset_labels/",
  "/elements/language_code": "/schema/",
  "/elements/lifecycle_stage": "/schema/aic_system_stage/",
  "/elements/likelihood": "/schema/",
  "/elements/MachineLearningParadigm": "/schema/AicLearningParadigm/",
  "/elements/MachineLearningTerm": "/schema/",
  "/elements/mapping_notes": "/schema/",
  "/elements/measurement_method": "/schema/aic_claim_measure/",
  "/elements/mechanism_type": "/schema/",
  "/elements/metric_name": "/schema/",
  "/elements/metric_unit": "/schema/",
  "/elements/metric_value": "/schema/",
  "/elements/mitigation_strategy": "/schema/",
  "/elements/MLAlgorithmFamily": "/schema/AicAlgorithmFamily/",
  "/elements/modality": "/schema/",
  "/elements/model_compression_applied": "/schema/",
  "/elements/model_paradigm": "/schema/aic_ml_paradigm/",
  "/elements/model_version": "/schema/aic_model_version/",
  "/elements/ModelDesigner": "/schema/AicStakeholder/",
  "/elements/ModelImplementer": "/schema/AicStakeholder/",
  "/elements/models": "/schema/aic_system_models/",
  "/elements/ModelVerifier": "/schema/AicStakeholder/",
  "/elements/name": "/schema/title/",
  "/elements/NamedEntity": "/schema/AicRecordMixin/",
  "/elements/NaturalLanguage": "/schema/aic_task_languages/",
  "/elements/neural_network_architecture": "/schema/",
  "/elements/NeuralNetworkArchitecture": "/schema/AicNetworkArchitecture/",
  "/elements/NeuralNetworkModel": "/schema/AicNeuralNetworkModel/",
  "/elements/NeuralNetworkPhenomenon": "/schema/",
  "/elements/NeuralNetworkTerm": "/schema/",
  "/elements/Neuron": "/schema/AicNeuralNetworkModel/",
  "/elements/NeuroSymbolicApproach": "/schema/",
  "/elements/nlp_component_type": "/schema/",
  "/elements/NLPComponent": "/schema/AicTaskKind/",
  "/elements/NLPComponentType": "/schema/AicTaskKind/",
  "/elements/NLPTerm": "/schema/",
  "/elements/node_count": "/schema/",
  "/elements/number_of_layers": "/schema/",
  "/elements/number_of_parameters": "/schema/",
  "/elements/oecd_stage": "/schema/",
  "/elements/OECDLifecycleMapping": "/schema/AicOecdLifecycleStage/",
  "/elements/OECDLifecycleStage": "/schema/AicOecdLifecycleStage/",
  "/elements/ontology_reference": "/schema/",
  "/elements/Organization": "/schema/",
  "/elements/organization_name": "/schema/aic_stakeholder_organization/",
  "/elements/output_dataset": "/schema/",
  "/elements/output_label_type": "/schema/",
  "/elements/over_model": "/schema/",
  "/elements/padding": "/schema/",
  "/elements/parameter_count": "/schema/aic_ml_parameter_count/",
  "/elements/parameters": "/schema/",
  "/elements/performance_metric": "/schema/",
  "/elements/performed_by": "/schema/",
  "/elements/physical_processes": "/schema/",
  "/elements/PolicyMaker": "/schema/AicStakeholderSubRole/",
  "/elements/potential_event": "/schema/",
  "/elements/predicted_value": "/schema/aic_prediction_value/",
  "/elements/Prediction": "/schema/AicPrediction/",
  "/elements/preferred_label": "/schema/",
  "/elements/process_inputs": "/schema/aic_lifecycle_inputs/",
  "/elements/process_outputs": "/schema/aic_lifecycle_outputs/",
  "/elements/process_stage": "/schema/aic_lifecycle_stage/",
  "/elements/process_sub_type": "/schema/",
  "/elements/process_type": "/schema/",
  "/elements/produced_by": "/schema/",
  "/elements/produced_output": "/schema/",
  "/elements/property_evidence": "/schema/aic_claim_evidence/",
  "/elements/provenance_statement": "/schema/",
  "/elements/Recommendation": "/schema/AicPrediction/",
  "/elements/recommendation_outcome_type": "/schema/",
  "/elements/RecommendationOutcomeType": "/schema/",
  "/elements/recommended_items": "/schema/",
  "/elements/record_count": "/schema/",
  "/elements/reference_dataset": "/schema/",
  "/elements/Regulator": "/schema/AicStakeholderSubRole/",
  "/elements/RelevantAuthority": "/schema/AicStakeholder/",
  "/elements/representation_form": "/schema/",
  "/elements/resource_type": "/schema/aic_pool_kind/",
  "/elements/ResourcePool": "/schema/AicResourcePool/",
  "/elements/responsibilities": "/schema/aic_stakeholder_responsibilities/",
  "/elements/responsible_role": "/schema/aic_lifecycle_responsible/",
  "/elements/risk_items": "/schema/",
  "/elements/risk_source": "/schema/",
  "/elements/RiskItem": "/schema/",
  "/elements/Robot": "/schema/AicRobot/",
  "/elements/rule_count": "/schema/",
  "/elements/sample_label": "/schema/",
  "/elements/sample_payload": "/schema/",
  "/elements/script": "/schema/",
  "/elements/see_also_uri": "/schema/",
  "/elements/semantic_model": "/schema/",
  "/elements/SemanticComputingSystem": "/schema/AicTechnique/",
  "/elements/sensing_capabilities": "/schema/",
  "/elements/severity": "/schema/",
  "/elements/societal_impacts": "/schema/aic_system_societal_impacts/",
  "/elements/SocietalImpactCategory": "/schema/",
  "/elements/soft_computing_techniques": "/schema/",
  "/elements/SoftComputingSystem": "/schema/AicTechnique/",
  "/elements/SoftComputingTechnique": "/schema/AicTechnique/",
  "/elements/stakeholder_role_type": "/schema/aic_stakeholder_role/",
  "/elements/stakeholders": "/schema/aic_system_stakeholders/",
  "/elements/start_date": "/schema/aic_lifecycle_start/",
  "/elements/stride": "/schema/",
  "/elements/supports_continuous_learning": "/schema/aic_ml_continuous_learning/",
  "/elements/symbolic_approach": "/schema/aic_system_approaches/",
  "/elements/SymbolicApproach": "/schema/AicApproach/",
  "/elements/system_characteristics": "/schema/",
  "/elements/Task": "/schema/AicTask/",
  "/elements/task_allocation": "/schema/",
  "/elements/task_categories": "/schema/",
  "/elements/task_category": "/schema/",
  "/elements/TaskCategory": "/schema/AicTaskKind/",
  "/elements/tasks": "/schema/",
  "/elements/Term": "/schema/",
  "/elements/terminology": "/schema/",
  "/elements/test_dataset": "/schema/",
  "/elements/Threshold": "/schema/aic_decision_criteria/",
  "/elements/threshold_policy": "/schema/",
  "/elements/threshold_value": "/schema/",
  "/elements/trained_on": "/schema/",
  "/elements/training_dataset": "/schema/",
  "/elements/training_duration": "/schema/",
  "/elements/training_phenomena": "/schema/",
  "/elements/triggered_by": "/schema/",
  "/elements/trustworthiness": "/schema/",
  "/elements/trustworthiness_properties": "/schema/",
  "/elements/trustworthiness_property_type": "/schema/aic_claim_property/",
  "/elements/trustworthiness_records": "/schema/aic_ecosystem_claims/",
  "/elements/TrustworthinessProperty": "/schema/AicTrustworthinessClaim/",
  "/elements/TrustworthinessPropertyType": "/schema/AicTrustworthinessProperty/",
  "/elements/TrustworthinessTerm": "/schema/",
  "/elements/uses_model": "/schema/",
  "/elements/validation_dataset": "/schema/",
  "/elements/validation_methods": "/schema/",
  "/elements/validation_strategy": "/schema/",
  "/elements/ValidationStrategy": "/schema/",
  "/elements/verification_methods": "/schema/",
  "/elements/verification_validation_level": "/schema/",
  "/elements/VerificationValidationFramework": "/schema/AicAssessment/",
  "/elements/VerificationValidationLevel": "/schema/",
  "/elements/[...slug]": "/schema/[...slug]",
};

// A Keep a Changelog file, read as a page per release. "auto" takes
// CHANGELOG.md when it holds a released version.
export const CHANGELOG = "auto";

// The tag a release carries, with {version} for its number. A release page
// links the repository, the docs and the bundle at that tag, and the release
// itself, when git has the tag. A repository whose tags carry no "v" sets
// "{version}". null links nothing.
export const RELEASE_TAG = "v{version}";

// Pages from files outside the docs folder, each at /<slug>/, listed in the
// Guide sidebar after Home under its label. An entry's `retells` names the
// file whose page it retells, and `level` the words for its reading level
// (the label when left out): both pages then offer each other under their
// titles.
//   export const PAGES = [{ slug: "simple", source: "docs/overview.en-simple.md", label: "In short", retells: "docs/overview.md" }];
export const PAGES = [];

// The LinkML schema's pages, which gen-doc writes, under a Schema topic: a
// folder, and the command that writes it, which the sync runs when the
// folder is missing. "auto" takes the first of the root, a linkmo project
// and .linkml/ whose justfile has a gen-doc recipe, else the sidecar's
// domain schema. null shows no schema.
//   export const SCHEMA = { dir: "docs/elements", build: "just gen-doc" };
export const SCHEMA = "auto";

// The data: a folder of SQLite databases and their Datasette metadata, served
// under /browse/ with a page that opens each in Datasette Lite, and the
// command that writes it. The databases go on the public site, so it is null
// until set. "auto" takes a linkmo project's browse/ folder.
//   export const BROWSE = { dir: "browse", build: "just build-browse" };
export const BROWSE = null;

// The workspace of a domain host, which the knowledge-federation workflow
// serves at workspace/ under the site, and which the graph page offers to
// draw beside the bundle's own graph. "auto" offers it when the repository
// has that workflow; true offers it always, and null never.
export const WORKSPACE = "auto";

// The home page: its source, from the file's `# ` title down ("auto" takes
// the README when it has one, else the bundle's own introduction); the
// tagline under the title (a string, { boldLineOf: <file> } for the first
// line of that file that is bold throughout, or DESCRIPTION when null); and
// the buttons, with site-relative links (Browse the bundle, Architecture when
// the docs have an architecture page, Schema when the site shows the schema,
// Bundle health and Knowledge graph when null).
export const HOME = { source: "auto", tagline: null, actions: null };
