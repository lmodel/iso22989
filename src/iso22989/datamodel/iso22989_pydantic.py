from __future__ import annotations

import re
import sys
from datetime import (
    date,
    datetime,
    time
)
from decimal import Decimal
from enum import Enum
from typing import (
    Any,
    ClassVar,
    Literal,
    Optional,
    Union
)

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    RootModel,
    SerializationInfo,
    SerializerFunctionWrapHandler,
    field_validator,
    model_serializer
)


metamodel_version = "1.11.0"
version = "0.1.0"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        serialize_by_alias = True,
        validate_by_name = True,
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )





class LinkMLMeta(RootModel):
    root: dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key:str):
        return getattr(self.root, key)

    def __getitem__(self, key:str):
        return self.root[key]

    def __setitem__(self, key:str, value):
        self.root[key] = value

    def __contains__(self, key:str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta({'annotations': {'developing_committee': {'tag': 'developing_committee',
                                              'value': 'ISO/IEC JTC 1/SC 42 '
                                                       '(Artificial Intelligence)'},
                     'related_standards': {'tag': 'related_standards',
                                           'value': 'ISO/IEC 42001 (AI management '
                                                    'system); ISO/IEC 23894 (AI '
                                                    'risk management guidance); '
                                                    'ISO/IEC 38507 (Governance '
                                                    'implications of AI); ISO/IEC '
                                                    '5338 (AI system life cycle '
                                                    'process); ISO/IEC 5259 (Data '
                                                    'quality for analytics and '
                                                    'ML); ISO/IEC TR 24028 '
                                                    '(Overview of trustworthiness '
                                                    'in AI); ISO/IEC TR 24027 '
                                                    '(Bias in AI systems and AI '
                                                    'aided decision making); OECD '
                                                    'AI Principles; NIST AI Risk '
                                                    'Management Framework (AI RMF '
                                                    '1.0)'},
                     'rights_notice': {'tag': 'rights_notice',
                                       'value': 'This project is licensed under '
                                                'Apache-2.0 for original schema '
                                                'structure and descriptions. '
                                                'ISO/IEC standards text is owned '
                                                'by ISO/IEC and is not reproduced '
                                                'verbatim by this project. '
                                                'Verbatim term definitions, where '
                                                'required by downstream consumers, '
                                                'must be supplied through a '
                                                'private overlay file under their '
                                                'own ISO licence.'},
                     'schema_status': {'tag': 'schema_status', 'value': 'draft'},
                     'standard_date': {'tag': 'standard_date', 'value': '2022-07'},
                     'standard_edition': {'tag': 'standard_edition',
                                          'value': 'First edition'},
                     'standard_reference': {'tag': 'standard_reference',
                                            'value': 'ISO/IEC 22989:2022(E)'},
                     'standard_title': {'tag': 'standard_title',
                                        'value': 'Information technology — '
                                                 'Artificial intelligence — '
                                                 'Artificial intelligence concepts '
                                                 'and terminology'}},
     'default_prefix': 'iso22989',
     'default_range': 'string',
     'description': 'A LinkML schema modelling the artificial-intelligence '
                    'concepts, terminology, life-cycle stages, stakeholder roles, '
                    'ecosystem components and application domains defined in '
                    'ISO/IEC 22989:2022. The schema supplies the controlled '
                    'vocabulary referenced by sibling lmodel schemas (iso42001 '
                    'AIMS, iso23894 AI risk management) and supports SSSOM '
                    'mappings to adjacent AI taxonomies.',
     'id': 'https://w3id.org/lmodel/iso22989',
     'imports': ['linkml:types'],
     'license': 'https://www.apache.org/licenses/LICENSE-2.0',
     'name': 'iso22989',
     'prefixes': {'dcterms': {'prefix_prefix': 'dcterms',
                              'prefix_reference': 'http://purl.org/dc/terms/'},
                  'eu_ai_act': {'prefix_prefix': 'eu_ai_act',
                                'prefix_reference': 'https://w3id.org/lmodel/eu-ai-act/'},
                  'gist_linkml': {'prefix_prefix': 'gist_linkml',
                                  'prefix_reference': 'https://w3id.org/lmodel/gist/'},
                  'iso22989': {'prefix_prefix': 'iso22989',
                               'prefix_reference': 'https://w3id.org/lmodel/iso22989/'},
                  'iso23894': {'prefix_prefix': 'iso23894',
                               'prefix_reference': 'https://w3id.org/lmodel/iso23894/'},
                  'iso27001': {'prefix_prefix': 'iso27001',
                               'prefix_reference': 'https://w3id.org/lmodel/iso27001/'},
                  'iso29100': {'prefix_prefix': 'iso29100',
                               'prefix_reference': 'https://w3id.org/lmodel/iso29100/'},
                  'iso42001': {'prefix_prefix': 'iso42001',
                               'prefix_reference': 'https://w3id.org/lmodel/iso42001/'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'nist_ai_100_1': {'prefix_prefix': 'nist_ai_100_1',
                                    'prefix_reference': 'https://w3id.org/lmodel/nist-ai-100-1/'},
                  'nist_ai_600_1': {'prefix_prefix': 'nist_ai_600_1',
                                    'prefix_reference': 'https://w3id.org/lmodel/nist-ai-600-1/'},
                  'nist_ai_rmf': {'prefix_prefix': 'nist_ai_rmf',
                                  'prefix_reference': 'https://w3id.org/lmodel/nist-ai-100-1/'},
                  'nist_ai_rmf_common': {'prefix_prefix': 'nist_ai_rmf_common',
                                         'prefix_reference': 'https://w3id.org/lmodel/nist-ai-100-1/schema/nist_ai_rmf_common/'},
                  'oecd_ai': {'prefix_prefix': 'oecd_ai',
                              'prefix_reference': 'https://oecd.ai/en/ai-principles#'},
                  'prov': {'prefix_prefix': 'prov',
                           'prefix_reference': 'http://www.w3.org/ns/prov#'},
                  'rdfs': {'prefix_prefix': 'rdfs',
                           'prefix_reference': 'http://www.w3.org/2000/01/rdf-schema#'},
                  'schema': {'prefix_prefix': 'schema',
                             'prefix_reference': 'http://schema.org/'},
                  'semapv': {'prefix_prefix': 'semapv',
                             'prefix_reference': 'https://w3id.org/semapv/vocab/'},
                  'skos': {'prefix_prefix': 'skos',
                           'prefix_reference': 'http://www.w3.org/2004/02/skos/core#'},
                  'uco_core': {'prefix_prefix': 'uco_core',
                               'prefix_reference': 'https://w3id.org/lmodel/uco-core/'}},
     'see_also': ['https://lmodel.github.io/iso22989',
                  'https://www.iso.org/standard/74296.html'],
     'source_file': 'src/iso22989/schema/iso22989.yaml',
     'subsets': {'ai_applications_domain': {'description': 'Application domains '
                                                           'presented in Clause 10 '
                                                           '(fraud detection, '
                                                           'automated vehicles, '
                                                           'predictive maintenance '
                                                           'and similar).',
                                            'from_schema': 'https://w3id.org/lmodel/iso22989',
                                            'name': 'ai_applications_domain'},
                 'ai_concepts': {'description': 'Conceptual elements introduced in '
                                                'Clause 5 (AI concepts), including '
                                                'agent, knowledge, cognition, '
                                                'autonomy, IoT/CPS, '
                                                'trustworthiness, jurisdictional '
                                                'and societal-impact concepts.',
                                 'from_schema': 'https://w3id.org/lmodel/iso22989',
                                 'name': 'ai_concepts'},
                 'ai_ecosystem': {'description': 'Ecosystem-level classes in '
                                                 'Clause 8 (AI systems, AI '
                                                 'functions, ML, engineering '
                                                 'approaches, data sources, '
                                                 'cloud/edge computing and '
                                                 'resource pools).',
                                  'from_schema': 'https://w3id.org/lmodel/iso22989',
                                  'name': 'ai_ecosystem'},
                 'ai_fields': {'description': 'Sub-fields of AI introduced in '
                                              'Clause 9 (computer vision, NLP, '
                                              'data mining, planning).',
                               'from_schema': 'https://w3id.org/lmodel/iso22989',
                               'name': 'ai_fields'},
                 'ai_functional_view': {'description': 'Classes representing the '
                                                       'functional view of an AI '
                                                       'system in Clause 7 (data '
                                                       'and information, knowledge '
                                                       'and learning, '
                                                       'prediction/decision/ '
                                                       'action chain).',
                                        'from_schema': 'https://w3id.org/lmodel/iso22989',
                                        'name': 'ai_functional_view'},
                 'ai_lifecycle': {'description': 'Classes and enums representing '
                                                 'the AI system life-cycle model '
                                                 'and its stages in Clause 6.',
                                  'from_schema': 'https://w3id.org/lmodel/iso22989',
                                  'name': 'ai_lifecycle'},
                 'ai_stakeholders': {'description': 'AI stakeholder roles '
                                                    'enumerated in Clause 5.19 '
                                                    '(provider, producer, '
                                                    'customer, partner, subject, '
                                                    'relevant authorities) '
                                                    'together with the sub-role '
                                                    'refinements used by the '
                                                    'standard.',
                                     'from_schema': 'https://w3id.org/lmodel/iso22989',
                                     'name': 'ai_stakeholders'},
                 'terminology': {'description': 'Classes and enums representing '
                                                'terms and definitions in Clause 3 '
                                                'of ISO/IEC 22989:2022 (Terms '
                                                'related to AI, data, machine '
                                                'learning, neural networks, '
                                                'trustworthiness, natural-language '
                                                'processing and computer vision).',
                                 'from_schema': 'https://w3id.org/lmodel/iso22989',
                                 'name': 'terminology'},
                 'trustworthiness': {'description': 'Trustworthiness properties of '
                                                    'AI systems as listed in '
                                                    'Clause 5.15 (robustness, '
                                                    'reliability, resilience, '
                                                    'controllability, '
                                                    'explainability, '
                                                    'predictability, transparency, '
                                                    'fairness, bias mitigation).',
                                     'from_schema': 'https://w3id.org/lmodel/iso22989',
                                     'name': 'trustworthiness'}},
     'title': 'ISO/IEC 22989:2022: AI Concepts and Terminology — LinkML Schema',
     'types': {'ConfidenceScore': {'base': 'float',
                                   'description': 'Numeric confidence score '
                                                  'expressed as a value in the '
                                                  'closed interval [0.0, 1.0]. '
                                                  'Used for model prediction '
                                                  'confidence, trust scores and '
                                                  'similar normalised quality '
                                                  'indicators.',
                                   'from_schema': 'https://w3id.org/lmodel/iso22989',
                                   'maximum_value': 1.0,
                                   'minimum_value': 0.0,
                                   'name': 'ConfidenceScore',
                                   'typeof': 'float',
                                   'uri': 'xsd:float'},
               'DurationType': {'base': 'str',
                                'description': 'ISO 8601 duration value such as '
                                               'P1Y, P30D or PT4H.',
                                'from_schema': 'https://w3id.org/lmodel/iso22989',
                                'name': 'DurationType',
                                'uri': 'xsd:duration'}}} )

class AISystemType(str, Enum):
    """
    High-level capability classification of an AI system, from narrow (single-task) through general (broad cross-domain) systems and the historical strong/weak AI distinction in Clause 5.2.
    """
    narrow_ai = "narrow_ai"
    """
    AI system designed and deployed for a single, well-bounded task.
    """
    general_ai = "general_ai"
    """
    Hypothetical AI system able to perform any cognitive task a human can perform.
    """
    weak_ai = "weak_ai"
    """
    Historical term largely overlapping with narrow AI; emphasises tool-like behaviour.
    """
    strong_ai = "strong_ai"
    """
    Historical term largely overlapping with general AI; emphasises human-equivalent cognition.
    """


class SymbolicApproach(str, Enum):
    """
    The symbolic vs subsymbolic axis used in Clause 5.9 to classify AI reasoning techniques.
    """
    symbolic = "symbolic"
    """
    Approaches that manipulate explicit symbolic representations (rules, logic, knowledge graphs).
    """
    subsymbolic = "subsymbolic"
    """
    Approaches that operate on distributed numeric representations (neural networks, statistical models).
    """
    hybrid = "hybrid"
    """
    Approaches that combine symbolic and subsymbolic techniques (neuro-symbolic AI).
    """


class MachineLearningParadigm(str, Enum):
    """
    Top-level machine-learning paradigms enumerated in Clause 5.11.
    """
    supervised = "supervised"
    """
    Learning from labelled input-output examples.
    """
    unsupervised = "unsupervised"
    """
    Learning structure from unlabelled data (clustering, density estimation, dimensionality reduction).
    """
    semi_supervised = "semi_supervised"
    """
    Learning from a mixture of labelled and unlabelled data.
    """
    reinforcement = "reinforcement"
    """
    Learning policies by interaction with an environment that issues rewards.
    """
    transfer = "transfer"
    """
    Reusing knowledge learned on one task to accelerate learning on a related task.
    """
    self_supervised = "self_supervised"
    """
    Learning representations from data using auxiliary tasks derived from the data itself.
    """


class MLAlgorithmFamily(str, Enum):
    """
    Example machine-learning algorithm families enumerated in Clause 5.12.
    """
    neural_network = "neural_network"
    """
    Networks of interconnected processing units (artificial neurons) trained by gradient methods.
    """
    bayesian_network = "bayesian_network"
    """
    Probabilistic graphical models encoding conditional dependencies between variables.
    """
    decision_tree = "decision_tree"
    """
    Tree-structured models splitting the input space on feature thresholds.
    """
    support_vector_machine = "support_vector_machine"
    """
    Margin-maximising classifiers operating in (possibly kernelised) feature spaces.
    """
    genetic_algorithm = "genetic_algorithm"
    """
    Population-based optimisation inspired by biological evolution (Clause 5.8).
    """


class AutonomyLevel(str, Enum):
    """
    Degree of system autonomy as discussed in Clause 5.13 (autonomy, heteronomy and automation). Encodes both the qualitative axis (autonomous / heteronomous / automated) and the six-level operational autonomy gradient widely used by ISO/IEC JTC 1/SC 42 work products.
    """
    automated = "automated"
    """
    System executes a fixed predefined behaviour without runtime adaptation.
    """
    heteronomous = "heteronomous"
    """
    System operates under external direction or supervision.
    """
    autonomous = "autonomous"
    """
    System pursues goals using its own decision-making within a defined operating envelope.
    """
    level_0_no_automation = "level_0_no_automation"
    """
    Human performs all tasks; no autonomous functionality (Clause 5.13).
    """
    level_1_assistance = "level_1_assistance"
    """
    System assists the operator with one or more specific tasks.
    """
    level_2_partial_automation = "level_2_partial_automation"
    """
    System performs some sub-functions; operator retains overall control.
    """
    level_3_conditional_automation = "level_3_conditional_automation"
    """
    System handles defined tasks but expects the operator to intervene when requested.
    """
    level_4_high_automation = "level_4_high_automation"
    """
    System performs the mission within a defined operating envelope without operator intervention.
    """
    level_5_full_automation = "level_5_full_automation"
    """
    System performs the entire mission autonomously across all conditions.
    """


class TrustworthinessPropertyType(str, Enum):
    """
    Properties contributing to AI trustworthiness, enumerated in Clause 5.15 (robustness, reliability, resilience, controllability, explainability, predictability, transparency, fairness and bias-related properties).
    """
    robustness = "robustness"
    """
    Ability to maintain performance under varied or adversarial conditions.
    """
    reliability = "reliability"
    """
    Consistent intended behaviour over time under stated conditions.
    """
    resilience = "resilience"
    """
    Ability to recover acceptable behaviour after disruption or failure.
    """
    controllability = "controllability"
    """
    Property of allowing authorised humans to intervene in system behaviour.
    """
    explainability = "explainability"
    """
    Property of producing explanations of system behaviour that are intelligible to relevant audiences.
    """
    predictability = "predictability"
    """
    Property of behaviour being anticipatable given known inputs and state.
    """
    transparency = "transparency"
    """
    Property of disclosing meaningful information about the system to interested parties.
    """
    fairness = "fairness"
    """
    Property of avoiding inappropriate or harmful discrimination across groups.
    """
    bias_mitigation = "bias_mitigation"
    """
    Property of identifying and reducing unwanted bias in data, models or outcomes.
    """
    accountability = "accountability"
    """
    Property of having identifiable parties answerable for system behaviour and outcomes.
    """
    privacy = "privacy"
    """
    Property of respecting personal data and individual privacy expectations.
    """
    safety = "safety"
    """
    Property of not causing unacceptable risk of harm to people, property or environment.
    """
    availability = "availability"
    """
    Property of being accessible and usable on demand by authorised entities (Clause 5.15.3 context).
    """
    integrity = "integrity"
    """
    Property of safeguarding accuracy and completeness of data, models and outputs (Clause 5.15 Note).
    """
    authenticity = "authenticity"
    """
    Property of being able to verify the origin and identity of inputs, models and outputs (Clause 5.15 Note).
    """
    security = "security"
    """
    Property of preserving confidentiality, integrity and availability of the AI system and its data (Clause 5.15 context).
    """
    usability = "usability"
    """
    Property of being effectively, efficiently and satisfactorily usable by the intended users (Clause 5.15 Note).
    """
    quality = "quality"
    """
    Aggregate property reflecting how well the AI system meets stated and implied needs (Clause 5.15 Note).
    """
    fault_tolerance = "fault_tolerance"
    """
    Property of continuing to operate correctly in the presence of component faults (Clause 5.15.4 context).
    """


class BiasType(str, Enum):
    """
    Categories of bias relevant to AI systems as discussed in Clause 5.15.9 and ISO/IEC TR 24027.
    """
    data_bias = "data_bias"
    """
    Bias introduced through sampling, labelling or representation of training data.
    """
    algorithmic_bias = "algorithmic_bias"
    """
    Bias introduced through model or algorithm choice and parameterisation.
    """
    societal_bias = "societal_bias"
    """
    Bias reflecting structural inequalities in the data-generating environment.
    """
    cognitive_bias = "cognitive_bias"
    """
    Bias introduced through human cognition during design, labelling or interpretation.
    """
    automation_bias = "automation_bias"
    """
    Tendency of users to over-rely on automated outputs.
    """


class AILifecycleStage(str, Enum):
    """
    AI system life-cycle stages identified in Clause 6.2.
    """
    inception = "inception"
    """
    Identification of need, opportunity and high-level objectives for the AI system.
    """
    design_and_development = "design_and_development"
    """
    Architecture, model selection, data preparation, training and integration activities.
    """
    verification_and_validation = "verification_and_validation"
    """
    Evidence-gathering activities establishing that the system meets specified requirements.
    """
    deployment = "deployment"
    """
    Release of the AI system into its operational environment.
    """
    operation_and_monitoring = "operation_and_monitoring"
    """
    Routine use of the AI system with ongoing observation of behaviour and performance.
    """
    continuous_validation = "continuous_validation"
    """
    Ongoing checks that the system continues to meet validation criteria during operation.
    """
    re_evaluation = "re_evaluation"
    """
    Periodic or event-triggered reassessment of the system, often leading to retraining or redesign.
    """
    retirement = "retirement"
    """
    Decommissioning of the AI system and management of residual data and artefacts.
    """


class AIFunctionalComponent(str, Enum):
    """
    Functional building blocks of an AI system as introduced in Clause 7.
    """
    data_and_information = "data_and_information"
    """
    Data acquisition, storage and information management functions.
    """
    knowledge_and_learning = "knowledge_and_learning"
    """
    Functions producing or maintaining knowledge representations and learned models.
    """
    prediction = "prediction"
    """
    Functions producing predictions from inputs using a trained model or knowledge base.
    """
    decision = "decision"
    """
    Functions selecting a course of action based on predictions and constraints.
    """
    action = "action"
    """
    Functions enacting decisions on the environment or downstream systems.
    """


class AIStakeholderRoleType(str, Enum):
    """
    AI stakeholder roles enumerated in Clause 5.19.
    """
    ai_provider = "ai_provider"
    """
    Party that makes an AI system available to AI customers.
    """
    ai_producer = "ai_producer"
    """
    Party that designs, develops or assembles AI systems or components.
    """
    ai_customer = "ai_customer"
    """
    Party that uses an AI system or a service backed by an AI system.
    """
    ai_partner = "ai_partner"
    """
    Party providing services that support the AI life cycle (data brokers, integrators, evaluators).
    """
    ai_subject = "ai_subject"
    """
    Person or group whose data is used by, or who is otherwise affected by, the AI system.
    """
    relevant_authority = "relevant_authority"
    """
    Body with regulatory, supervisory or standards-setting responsibility for AI.
    """


class EngineeringApproach(str, Enum):
    """
    Non-learning engineering approaches contributing to AI, from Clause 8.5.
    """
    expert_system = "expert_system"
    """
    Rule-based system encoding domain expertise (Clause 8.5.2).
    """
    logic_programming = "logic_programming"
    """
    Programming paradigm based on formal logic (Clause 8.5.3).
    """
    knowledge_graph = "knowledge_graph"
    """
    Graph-structured knowledge representation used for reasoning and retrieval.
    """
    constraint_satisfaction = "constraint_satisfaction"
    """
    Solving problems by satisfying a set of declared constraints.
    """


class ComputingResourceType(str, Enum):
    """
    Categories of computing resource used by AI systems, drawn from Clauses 8.6 (cloud and edge computing) and 8.7 (resource pools).
    """
    cloud = "cloud"
    """
    Centralised, elastically provisioned computing resources accessed over a network.
    """
    edge = "edge"
    """
    Computing resources located close to data sources or end users.
    """
    on_premises = "on_premises"
    """
    Computing resources owned and operated within the organisation's own facilities.
    """
    cpu = "cpu"
    """
    General-purpose central-processing-unit compute capacity.
    """
    gpu = "gpu"
    """
    Graphics-processing-unit compute capacity, commonly used for neural network training and inference.
    """
    tpu = "tpu"
    """
    Tensor-processing-unit or similar accelerator specialised for ML workloads.
    """
    asic = "asic"
    """
    Application-specific integrated circuit designed for a fixed AI workload (Clause 8.7.2).
    """
    fpga = "fpga"
    """
    Field-programmable gate array offering reconfigurable hardware acceleration.
    """
    npu = "npu"
    """
    Neural-network processing unit specialised for neural-network inference and training.
    """
    dsp = "dsp"
    """
    Digital signal processor used to accelerate signal-processing workloads.
    """


class DataModality(str, Enum):
    """
    Modalities of input data handled by AI systems, drawn from the data, NLP and CV terminology sections (Clauses 3.2, 3.6, 3.7).
    """
    structured = "structured"
    """
    Tabular or relational data with an explicit schema.
    """
    semi_structured = "semi_structured"
    """
    Data with self-describing structure such as JSON, XML or graph formats.
    """
    unstructured = "unstructured"
    """
    Data without an explicit schema (free text, images, audio, video).
    """
    text = "text"
    """
    Natural-language text data.
    """
    image = "image"
    """
    Two-dimensional visual data.
    """
    video = "video"
    """
    Temporal sequences of visual frames.
    """
    audio = "audio"
    """
    Acoustic signal data.
    """
    sensor = "sensor"
    """
    Telemetry or measurement data from physical sensors.
    """
    time_series = "time_series"
    """
    Ordered observations indexed by time.
    """
    graph = "graph"
    """
    Data represented as nodes and edges.
    """


class DatasetRole(str, Enum):
    """
    Role a dataset plays in a machine-learning workflow, drawn from Clauses 5.11.6–5.11.8.
    """
    training = "training"
    """
    Dataset used to fit model parameters.
    """
    validation = "validation"
    """
    Dataset used to tune hyperparameters and select among candidate models.
    """
    test = "test"
    """
    Dataset used for a final unbiased estimate of model performance.
    """
    production = "production"
    """
    Live data observed during operational deployment.
    """
    reference = "reference"
    """
    Curated dataset used as a benchmark across experiments.
    """


class NLPComponentType(str, Enum):
    """
    Components of a natural-language-processing pipeline as enumerated in Clauses 3.6 and 9.2.
    """
    tokenisation = "tokenisation"
    """
    Segmenting text into tokens such as words or subwords.
    """
    lemmatisation = "lemmatisation"
    """
    Reducing tokens to their canonical dictionary form.
    """
    part_of_speech_tagging = "part_of_speech_tagging"
    """
    Assigning grammatical category labels to tokens.
    """
    syntactic_parsing = "syntactic_parsing"
    """
    Producing syntactic structure for sentences.
    """
    semantic_analysis = "semantic_analysis"
    """
    Deriving meaning representations from text.
    """
    named_entity_recognition = "named_entity_recognition"
    """
    Identifying and classifying named entities in text.
    """
    sentiment_analysis = "sentiment_analysis"
    """
    Estimating subjective polarity or affect in text.
    """
    machine_translation = "machine_translation"
    """
    Automatically translating text between natural languages.
    """
    speech_recognition = "speech_recognition"
    """
    Converting acoustic speech signals into text.
    """
    speech_synthesis = "speech_synthesis"
    """
    Generating speech audio from text.
    """
    natural_language_understanding = "natural_language_understanding"
    """
    Deriving structured meaning, intent or entities from natural-language input (Clause 9.2).
    """
    natural_language_generation = "natural_language_generation"
    """
    Producing natural-language output from structured inputs (Clause 9.2).
    """
    automatic_summarization = "automatic_summarization"
    """
    Producing condensed summaries of longer text (Clause 3.6.1).
    """
    dialogue_management = "dialogue_management"
    """
    Controlling multi-turn conversational interaction (Clause 9.2.2).
    """
    information_retrieval = "information_retrieval"
    """
    Finding relevant documents or passages in a collection in response to a query.
    """
    question_answering = "question_answering"
    """
    Producing direct answers to natural-language questions.
    """
    relationship_extraction = "relationship_extraction"
    """
    Identifying typed relationships between entities mentioned in text.
    """
    emotion_recognition = "emotion_recognition"
    """
    Detecting affective or emotional state expressed in text or speech.
    """
    optical_character_recognition = "optical_character_recognition"
    """
    Converting images of printed or handwritten text into machine-readable text (Clause 3.6.12).
    """
    coreference_resolution = "coreference_resolution"
    """
    Linking mentions in text that refer to the same entity.
    """


class ComputerVisionTask(str, Enum):
    """
    Computer-vision tasks drawn from Clauses 3.7 and 9.1.
    """
    image_classification = "image_classification"
    """
    Assigning a class label to an image.
    """
    object_detection = "object_detection"
    """
    Localising and classifying objects within an image.
    """
    semantic_segmentation = "semantic_segmentation"
    """
    Assigning a class label to each pixel in an image.
    """
    instance_segmentation = "instance_segmentation"
    """
    Assigning labels to pixels grouped by individual object instance.
    """
    image_recognition = "image_recognition"
    """
    General recognition of image content, including faces and scenes.
    """
    pose_estimation = "pose_estimation"
    """
    Estimating the spatial pose of objects or persons.
    """
    optical_character_recognition = "optical_character_recognition"
    """
    Extracting machine-readable text from images of printed or handwritten content.
    """
    face_recognition = "face_recognition"
    """
    Identifying or verifying persons from facial images (Clause 3.7.2).
    """
    scene_recognition = "scene_recognition"
    """
    Classifying the type of scene or environment depicted in an image.
    """
    motion_tracking = "motion_tracking"
    """
    Following the position of objects across successive frames in video.
    """
    visual_anomaly_detection = "visual_anomaly_detection"
    """
    Identifying visual patterns that deviate from expected behaviour.
    """
    three_d_reconstruction = "three_d_reconstruction"
    """
    Recovering three-dimensional structure from one or more images.
    """
    action_recognition = "action_recognition"
    """
    Recognising discrete actions performed in video.
    """
    activity_recognition = "activity_recognition"
    """
    Recognising higher-level activities composed of multiple actions in video.
    """


class AIField(str, Enum):
    """
    Sub-fields of AI referenced in Clause 9.
    """
    computer_vision = "computer_vision"
    """
    AI sub-field concerned with interpreting visual information.
    """
    natural_language_processing = "natural_language_processing"
    """
    AI sub-field concerned with processing and generating human language.
    """
    data_mining = "data_mining"
    """
    Extraction of patterns and knowledge from large data sets.
    """
    planning = "planning"
    """
    AI sub-field concerned with sequencing actions to achieve goals.
    """
    robotics = "robotics"
    """
    AI sub-field concerned with embodied autonomous systems.
    """
    knowledge_representation_and_reasoning = "knowledge_representation_and_reasoning"
    """
    AI sub-field concerned with explicit representation and inference over knowledge.
    """
    speech_processing = "speech_processing"
    """
    AI sub-field concerned with processing and producing speech signals.
    """
    multi_agent_systems = "multi_agent_systems"
    """
    AI sub-field concerned with coordination and interaction among multiple agents.
    """


class AIApplicationDomain(str, Enum):
    """
    Example AI application domains presented in Clause 10.
    """
    fraud_detection = "fraud_detection"
    """
    Identification of fraudulent transactions or behaviours (Clause 10.2).
    """
    automated_vehicles = "automated_vehicles"
    """
    AI capabilities used in self-driving or driver-assistance systems (Clause 10.3).
    """
    predictive_maintenance = "predictive_maintenance"
    """
    Anticipating equipment failures from sensor data (Clause 10.4).
    """
    recommendation = "recommendation"
    """
    Personalised recommendation of items or actions.
    """
    medical_diagnosis = "medical_diagnosis"
    """
    AI-assisted diagnostic decision support in healthcare.
    """
    content_generation = "content_generation"
    """
    AI-generated text, images, audio or other media.
    """
    agriculture = "agriculture"
    """
    AI applications in farming, crop and livestock management (Clause 10.1).
    """
    automotive = "automotive"
    """
    AI applications in vehicle design, manufacture and in-vehicle services (Clause 10.1).
    """
    banking_and_finance = "banking_and_finance"
    """
    AI applications in banking, finance and capital markets (Clause 10.1).
    """
    defense_and_security = "defense_and_security"
    """
    AI applications in defence and physical security (Clause 10.1).
    """
    education = "education"
    """
    AI applications in learning, teaching and assessment (Clause 10.1).
    """
    energy_and_utilities = "energy_and_utilities"
    """
    AI applications in energy generation, distribution and consumption (Clause 10.1).
    """
    healthcare = "healthcare"
    """
    AI applications in clinical care and health management (Clause 10.1).
    """
    legal_services = "legal_services"
    """
    AI applications in legal research, contracting and compliance (Clause 10.1).
    """
    manufacturing = "manufacturing"
    """
    AI applications in industrial production (Clause 10.1).
    """
    media_and_entertainment = "media_and_entertainment"
    """
    AI applications in media production, distribution and recommendation (Clause 10.1).
    """
    mixed_reality = "mixed_reality"
    """
    AI applications in virtual, augmented and mixed reality (Clause 10.1).
    """
    public_sector = "public_sector"
    """
    AI applications in government and public administration (Clause 10.1).
    """
    retail = "retail"
    """
    AI applications in retail and e-commerce (Clause 10.1).
    """
    space = "space"
    """
    AI applications in space exploration and operations (Clause 10.1).
    """
    telecommunications = "telecommunications"
    """
    AI applications in telecommunications networks and services (Clause 10.1).
    """


class OECDLifecycleStage(str, Enum):
    """
    OECD AI system life-cycle stages used in the informative mapping of Annex A.
    """
    plan_and_design = "plan_and_design"
    """
    OECD stage covering planning and design activities.
    """
    collect_and_process_data = "collect_and_process_data"
    """
    OECD stage covering data collection and processing.
    """
    build_and_use_model = "build_and_use_model"
    """
    OECD stage covering model building and inference.
    """
    verify_and_validate = "verify_and_validate"
    """
    OECD stage covering verification and validation.
    """
    deploy = "deploy"
    """
    OECD stage covering deployment of the AI system.
    """
    operate_and_monitor = "operate_and_monitor"
    """
    OECD stage covering operation and monitoring of the AI system.
    """


class JurisdictionalIssueType(str, Enum):
    """
    Categories of jurisdictional issue surfaced in Clause 5.17.
    """
    data_residency = "data_residency"
    """
    Constraints on the geographical location of stored or processed data.
    """
    cross_border_transfer = "cross_border_transfer"
    """
    Constraints on movement of data or AI outputs across legal jurisdictions.
    """
    liability = "liability"
    """
    Allocation of legal responsibility for AI-system actions and outcomes.
    """
    regulatory_compliance = "regulatory_compliance"
    """
    Conformity with applicable AI-specific or sector-specific regulations.
    """
    intellectual_property = "intellectual_property"
    """
    Ownership and licensing of training data, models and outputs.
    """


class SocietalImpactCategory(str, Enum):
    """
    Categories of societal impact discussed in Clause 5.18.
    """
    employment = "employment"
    """
    Effects on labour markets and the nature of work.
    """
    human_rights = "human_rights"
    """
    Effects on the exercise of fundamental human rights.
    """
    environment = "environment"
    """
    Environmental footprint of AI development and deployment.
    """
    democratic_processes = "democratic_processes"
    """
    Effects on political discourse, elections and civic participation.
    """
    digital_divide = "digital_divide"
    """
    Differential access to and impact of AI systems across populations.
    """


class NeuralNetworkArchitecture(str, Enum):
    """
    Architectural families of neural networks enumerated across Clause 3.4 and Clause 5.12.1.
    """
    feed_forward = "feed_forward"
    """
    Feed-forward neural network with unidirectional information flow (Clause 3.4.6).
    """
    recurrent = "recurrent"
    """
    Recurrent neural network with feedback connections (Clause 3.4.10).
    """
    long_short_term_memory = "long_short_term_memory"
    """
    LSTM recurrent architecture mitigating short memory in plain RNNs (Clause 3.4.7).
    """
    gated_recurrent_unit = "gated_recurrent_unit"
    """
    GRU recurrent architecture, a simplified gating variant of LSTM.
    """
    convolutional = "convolutional"
    """
    Convolutional neural network using local receptive fields (Clause 3.4.2).
    """
    transformer = "transformer"
    """
    Attention-based architecture used for sequence modelling.
    """
    autoencoder = "autoencoder"
    """
    Encoder-decoder architecture trained to reconstruct inputs for representation learning.
    """
    generative_adversarial = "generative_adversarial"
    """
    Adversarial pairing of generator and discriminator networks.
    """
    deep = "deep"
    """
    Neural network with many hidden layers (deep learning, Clause 3.4.4).
    """


class NeuralNetworkPhenomenon(str, Enum):
    """
    Training-time phenomena that affect neural-network learning, drawn from Clause 3.4.
    """
    vanishing_gradient = "vanishing_gradient"
    """
    Gradient signal shrinks across layers during back-propagation, slowing learning.
    """
    exploding_gradient = "exploding_gradient"
    """
    Gradient signal grows without bound across layers during back-propagation (Clause 3.4.5).
    """
    catastrophic_forgetting = "catastrophic_forgetting"
    """
    Previously learned knowledge is lost when the network is retrained on new data.
    """
    overfitting = "overfitting"
    """
    Model fits training data idiosyncrasies and fails to generalise.
    """
    underfitting = "underfitting"
    """
    Model lacks capacity or training to capture the underlying signal.
    """


class ActivationFunctionType(str, Enum):
    """
    Common activation functions used in neural networks (Clause 3.4.1).
    """
    sigmoid = "sigmoid"
    """
    Logistic sigmoid activation.
    """
    tanh = "tanh"
    """
    Hyperbolic tangent activation.
    """
    relu = "relu"
    """
    Rectified linear unit activation.
    """
    leaky_relu = "leaky_relu"
    """
    Rectified linear unit with non-zero gradient below zero.
    """
    softmax = "softmax"
    """
    Softmax activation producing a probability distribution.
    """
    linear = "linear"
    """
    Identity / linear activation.
    """
    other = "other"
    """
    Activation function not enumerated explicitly.
    """


class AgentArchitectureType(str, Enum):
    """
    Agent architectures discussed in Clause 5.3 (agent paradigm).
    """
    reflex_agent = "reflex_agent"
    """
    Agent that maps current percepts directly to actions.
    """
    model_based_agent = "model_based_agent"
    """
    Agent that maintains an internal model of the environment to guide action.
    """
    goal_based_agent = "goal_based_agent"
    """
    Agent that selects actions to achieve explicit goals.
    """
    utility_based_agent = "utility_based_agent"
    """
    Agent that selects actions to maximise an expected utility function.
    """
    learning_agent = "learning_agent"
    """
    Agent that improves its behaviour through experience.
    """
    multi_agent = "multi_agent"
    """
    Agent operating jointly with other agents in a shared environment.
    """


class KnowledgeType(str, Enum):
    """
    Types of knowledge distinguished in Clause 3.1 and Clause 5.4 (declarative versus procedural knowledge, etc.).
    """
    declarative = "declarative"
    """
    Knowledge of facts and relationships (Clause 3.1.12).
    """
    procedural = "procedural"
    """
    Knowledge of how to perform tasks (Clause 3.1.28).
    """
    tacit = "tacit"
    """
    Implicit, experience-based knowledge that is hard to articulate.
    """
    common_sense = "common_sense"
    """
    Background knowledge expected to be shared by typical humans.
    """
    domain_specific = "domain_specific"
    """
    Knowledge specific to a particular application domain.
    """


class DataProcessType(str, Enum):
    """
    Data-handling processes enumerated in Clause 5.10 and Clause 3.2 (data acquisition, annotation, preparation, quality checking, sampling, augmentation, drift and poisoning handling, etc.).
    """
    data_acquisition = "data_acquisition"
    """
    Collecting data from one or more sources.
    """
    exploratory_data_analysis = "exploratory_data_analysis"
    """
    Initial profiling of a dataset to understand its characteristics (Clause 3.2.6).
    """
    data_annotation = "data_annotation"
    """
    Adding labels or other metadata to data items (Clause 3.2.1).
    """
    data_labeling = "data_labeling"
    """
    Assigning target labels to records for supervised learning.
    """
    data_preparation = "data_preparation"
    """
    Transforming raw data into a form suitable for analysis or training.
    """
    data_cleaning = "data_cleaning"
    """
    Detecting and correcting errors and inconsistencies in data.
    """
    filtering = "filtering"
    """
    Removing data items that do not match selection criteria.
    """
    normalisation = "normalisation"
    """
    Rescaling features to a common range or distribution.
    """
    de_identification = "de_identification"
    """
    Removing or transforming personally identifiable information.
    """
    data_quality_checking = "data_quality_checking"
    """
    Assessing completeness, accuracy, representativeness and bias of data (Clause 3.2.2).
    """
    data_sampling = "data_sampling"
    """
    Selecting a subset of records from a larger population (Clause 3.2.4).
    """
    data_augmentation = "data_augmentation"
    """
    Creating additional training examples via transformation of existing data (Clause 3.2.3).
    """
    feature_engineering = "feature_engineering"
    """
    Constructing or selecting features used as model inputs.
    """
    imputation = "imputation"
    """
    Replacing missing values with substituted estimates (Clause 3.2.8).
    """
    data_drift_detection = "data_drift_detection"
    """
    Detecting changes in the statistical distribution of operational data.
    """
    data_poisoning_detection = "data_poisoning_detection"
    """
    Identifying adversarial contamination of training data.
    """
    concept_drift_handling = "concept_drift_handling"
    """
    Detecting and responding to changes in the relationship between inputs and target labels (Clause 5.11.9.1).
    """
    catastrophic_forgetting_mitigation = "catastrophic_forgetting_mitigation"
    """
    Strategies to prevent loss of previously learned knowledge during retraining (Clause 5.11.9.1).
    """
    retraining = "retraining"
    """
    Updating an existing trained model on new or revised data (Clause 5.11.9).
    """


class DataLabelType(str, Enum):
    """
    Categories of target label produced or consumed by ML workflows.
    """
    categorical = "categorical"
    """
    Discrete unordered class labels.
    """
    binary = "binary"
    """
    Two-class label (typically positive / negative).
    """
    ordinal = "ordinal"
    """
    Discrete ordered labels.
    """
    numeric = "numeric"
    """
    Continuous numeric target value.
    """
    structured = "structured"
    """
    Composite or graph-structured label.
    """
    sequence = "sequence"
    """
    Ordered sequence of label tokens (e.g. sequence labelling, structured prediction).
    """
    graph = "graph"
    """
    Graph-structured label such as a parse tree or relational structure.
    """
    none = "none"
    """
    No explicit label (unsupervised or self-supervised setting).
    """


class TaskCategory(str, Enum):
    """
    Categories of AI task addressed by AI systems, derived from the\n      machine-learning, NLP and computer-vision terminology in Clause 3.
    """
    classification = "classification"
    """
    Assigning a class label to an input.
    """
    regression = "regression"
    """
    Predicting a continuous numeric value.
    """
    clustering = "clustering"
    """
    Grouping items by similarity without supervision.
    """
    ranking = "ranking"
    """
    Ordering items by relevance or preference.
    """
    recommendation = "recommendation"
    """
    Suggesting items to a user given context.
    """
    anomaly_detection = "anomaly_detection"
    """
    Identifying inputs that deviate from expected behaviour.
    """
    dimensionality_reduction = "dimensionality_reduction"
    """
    Producing a lower-dimensional representation of the data.
    """
    generation = "generation"
    """
    Producing new content (text, images, audio, etc.).
    """
    planning = "planning"
    """
    Producing a sequence of actions that achieve a goal.
    """
    control = "control"
    """
    Selecting actions to influence a dynamical system.
    """
    decision_support = "decision_support"
    """
    Producing recommendations or explanations to support human decisions.
    """


class AISystemCharacteristic(str, Enum):
    """
    Distinguishing characteristics of AI systems summarised in Clause 5.1.
    """
    interactive = "interactive"
    """
    Engages in interaction with users or other systems.
    """
    contextual = "contextual"
    """
    Adapts behaviour to its operational context.
    """
    adaptive = "adaptive"
    """
    Adjusts behaviour over time in response to new data or feedback.
    """
    oversight_enabled = "oversight_enabled"
    """
    Provides mechanisms for human oversight and intervention.
    """
    data_dependent = "data_dependent"
    """
    Performance depends materially on the data used to build or operate the system.
    """


class SoftComputingTechnique(str, Enum):
    """
    Techniques grouped under soft computing in Clause 5.7.
    """
    fuzzy_logic = "fuzzy_logic"
    """
    Reasoning with degrees of truth rather than crisp Boolean values.
    """
    evolutionary_computing = "evolutionary_computing"
    """
    Optimisation inspired by biological evolution (including genetic algorithms).
    """
    swarm_intelligence = "swarm_intelligence"
    """
    Optimisation inspired by collective behaviour of decentralised agents.
    """
    probabilistic_reasoning = "probabilistic_reasoning"
    """
    Reasoning under uncertainty using probability theory.
    """
    neural_computing = "neural_computing"
    """
    Computation realised by networks of artificial neurons.
    """


class BigDataCharacteristic(str, Enum):
    """
    Characteristics commonly used to describe big data sources in Clause 8.6.1.
    """
    volume = "volume"
    """
    Total amount of data managed.
    """
    velocity = "velocity"
    """
    Rate at which data is generated or processed.
    """
    variety = "variety"
    """
    Range of data types and sources.
    """
    veracity = "veracity"
    """
    Trustworthiness and accuracy of the data.
    """
    value = "value"
    """
    Usefulness of the data for the intended purpose.
    """
    variability = "variability"
    """
    Degree to which data characteristics change over time.
    """


class IoTDeviceRole(str, Enum):
    """
    Roles played by devices in IoT and cyber-physical systems (Clause 5.14).
    """
    sensor = "sensor"
    """
    Device that observes the physical environment.
    """
    actuator = "actuator"
    """
    Device that effects changes in the physical environment.
    """
    gateway = "gateway"
    """
    Device that connects local IoT subnets to wider networks.
    """
    edge_compute = "edge_compute"
    """
    Device providing local computation at the network edge.
    """
    controller = "controller"
    """
    Device that supervises or coordinates other IoT devices.
    """


class AbbreviationCode(str, Enum):
    """
    Acronyms and abbreviations listed in Clause 4.
    """
    AI = "AI"
    """
    Artificial intelligence.
    """
    API = "API"
    """
    Application programming interface.
    """
    ASIC = "ASIC"
    """
    Application-specific integrated circuit.
    """
    CNN = "CNN"
    """
    Convolutional neural network.
    """
    CPS = "CPS"
    """
    Cyber-physical system.
    """
    CPU = "CPU"
    """
    Central processing unit.
    """
    CRISP_DM = "CRISP_DM"
    """
    Cross-industry standard process for data mining.
    """
    DNN = "DNN"
    """
    Deep neural network.
    """
    DSP = "DSP"
    """
    Digital signal processor.
    """
    FFNN = "FFNN"
    """
    Feed-forward neural network.
    """
    FPGA = "FPGA"
    """
    Field-programmable gate array.
    """
    GA = "GA"
    """
    Genetic algorithm.
    """
    GPU = "GPU"
    """
    Graphics processing unit.
    """
    HMM = "HMM"
    """
    Hidden Markov model.
    """
    IoT = "IoT"
    """
    Internet of Things.
    """
    IR = "IR"
    """
    Information retrieval.
    """
    IT = "IT"
    """
    Information technology.
    """
    KDD = "KDD"
    """
    Knowledge discovery in data.
    """
    LSTM = "LSTM"
    """
    Long short-term memory.
    """
    ML = "ML"
    """
    Machine learning.
    """
    MT = "MT"
    """
    Machine translation.
    """
    NER = "NER"
    """
    Named entity recognition.
    """
    NLG = "NLG"
    """
    Natural language generation.
    """
    NLP = "NLP"
    """
    Natural language processing.
    """
    NLU = "NLU"
    """
    Natural language understanding.
    """
    NN = "NN"
    """
    Neural network.
    """
    NPU = "NPU"
    """
    Neural-network processing unit.
    """
    OCR = "OCR"
    """
    Optical character recognition.
    """
    OECD = "OECD"
    """
    Organisation for Economic Co-operation and Development.
    """
    PII = "PII"
    """
    Personally identifiable information.
    """
    POS = "POS"
    """
    Part of speech.
    """
    RL = "RL"
    """
    Reinforcement learning.
    """
    RNN = "RNN"
    """
    Recurrent neural network.
    """
    SVM = "SVM"
    """
    Support vector machine.
    """


class ValidationStrategy(str, Enum):
    """
    Strategies for partitioning data and assessing generalisation, drawn from Clause 5.11.8 and Clause 5.16.
    """
    holdout = "holdout"
    """
    Single train / validation / test split.
    """
    two_way_split = "two_way_split"
    """
    Two-way split (train / test) used when data is limited (Clause 5.11.8).
    """
    cross_validation = "cross_validation"
    """
    K-fold cross-validation.
    """
    stratified_cross_validation = "stratified_cross_validation"
    """
    Cross-validation that preserves class distribution in each fold.
    """
    bootstrap = "bootstrap"
    """
    Resampling-with-replacement estimation of generalisation error.
    """
    time_series_split = "time_series_split"
    """
    Forward-chaining split that respects temporal order.
    """


class VerificationValidationLevel(str, Enum):
    """
    Levels of verifiability and validatability used to characterise an AI system in Clause 5.16.
    """
    completely_verifiable = "completely_verifiable"
    """
    System behaviour is fully verifiable against specifications.
    """
    partially_verifiable_validatable = "partially_verifiable_validatable"
    """
    System is partially verifiable and validatable against specifications.
    """
    unverifiable_validatable = "unverifiable_validatable"
    """
    System is not verifiable but its behaviour can be validated empirically.
    """
    unverifiable_partially_validatable = "unverifiable_partially_validatable"
    """
    System is not verifiable and only partially validatable.
    """
    unverifiable_unvalidatable = "unverifiable_unvalidatable"
    """
    System is neither verifiable nor validatable with available techniques.
    """


class DataSourceType(str, Enum):
    """
    Classification of data sources discussed in Clause 8.6.1.
    """
    first_party = "first_party"
    """
    Data collected directly by the organisation operating the AI system.
    """
    second_party = "second_party"
    """
    Data shared by a partner organisation under agreement.
    """
    third_party = "third_party"
    """
    Data acquired from an external data provider.
    """
    open_data = "open_data"
    """
    Publicly available data released under an open licence.
    """
    synthetic = "synthetic"
    """
    Data generated by simulation, sampling or generative models.
    """
    queried_union = "queried_union"
    """
    Data assembled on demand from a union of underlying sources.
    """


class DataCollectionMethod(str, Enum):
    """
    Methods of data collection enumerated in Clause 8.6.1.
    """
    point_of_sale = "point_of_sale"
    """
    Captured at the point of a commercial transaction.
    """
    survey = "survey"
    """
    Collected through structured questionnaires.
    """
    research_study = "research_study"
    """
    Collected as part of a designed research study.
    """
    sensor_capture = "sensor_capture"
    """
    Captured by a physical sensor.
    """
    image_capture = "image_capture"
    """
    Captured by an imaging device.
    """
    audio_capture = "audio_capture"
    """
    Captured by an audio recording device.
    """
    document_extraction = "document_extraction"
    """
    Extracted from text or document corpora.
    """
    web_scraping = "web_scraping"
    """
    Harvested from publicly accessible web resources.
    """
    interaction_log = "interaction_log"
    """
    Recorded from interactions with software or services.
    """
    transactional_log = "transactional_log"
    """
    Recorded as a side effect of transactional systems.
    """


class AutonomyCriterion(str, Enum):
    """
    Criteria contributing to the assessment of autonomy in Clause 5.13.\n      Each criterion is graded independently when assigning an\n      `AutonomyLevel`.
    """
    external_supervision = "external_supervision"
    """
    Degree to which an external operator supervises the system.
    """
    situated_understanding = "situated_understanding"
    """
    Degree to which the system understands its operational context.
    """
    reactivity = "reactivity"
    """
    Degree to which the system reacts to environmental changes.
    """
    persistence = "persistence"
    """
    Span over which the system continues operating without intervention.
    """
    adaptability = "adaptability"
    """
    Degree to which the system adapts behaviour to new conditions.
    """
    performance_evaluation = "performance_evaluation"
    """
    Ability of the system to evaluate its own performance.
    """
    proactive_planning = "proactive_planning"
    """
    Ability of the system to plan future actions proactively.
    """


class NeuroSymbolicApproach(str, Enum):
    """
    Sub-categorisation of hybrid neuro-symbolic approaches mentioned in\n      Clause 5.9.
    """
    symbolic_in_neural = "symbolic_in_neural"
    """
    Symbolic reasoning embedded within a primarily subsymbolic architecture.
    """
    neural_in_symbolic = "neural_in_symbolic"
    """
    Subsymbolic components invoked inside a symbolic reasoning framework.
    """
    tightly_coupled = "tightly_coupled"
    """
    Symbolic and subsymbolic components share representations end-to-end.
    """
    loosely_coupled = "loosely_coupled"
    """
    Symbolic and subsymbolic components exchange information at well-defined interfaces.
    """


class RecommendationOutcomeType(str, Enum):
    """
    High-level categorisation of recommendations produced by an AI system\n      (Clauses 7.4, 10).
    """
    content_recommendation = "content_recommendation"
    """
    Suggestion of content items.
    """
    action_recommendation = "action_recommendation"
    """
    Suggestion of an action to take.
    """
    ranking_recommendation = "ranking_recommendation"
    """
    Recommendation expressed as a ranked list.
    """
    next_best_action = "next_best_action"
    """
    Recommendation of the single most appropriate next action.
    """


class ExecutionStatus(str, Enum):
    """
    Execution status values for actions and processes.
    """
    planned = "planned"
    """
    Execution has been planned but not yet started.
    """
    in_progress = "in_progress"
    """
    Execution is currently in progress.
    """
    completed = "completed"
    """
    Execution has completed successfully.
    """
    failed = "failed"
    """
    Execution has terminated unsuccessfully.
    """
    cancelled = "cancelled"
    """
    Execution was cancelled before completion.
    """



class NamedEntity(ConfiguredBaseModel):
    """
    Abstract base class for any addressable entity in the schema, carrying identity, label and clause-reference metadata.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'schema:Thing',
         'close_mappings': ['nist_ai_rmf_common:NamedThing', 'uco_core:UcoThing'],
         'exact_mappings': ['iso29100:NamedEntity'],
         'from_schema': 'https://w3id.org/lmodel/iso22989'})

    id: str = Field(default=..., description="""Unique CURIE or URI identifying the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:identifier'} })
    name: str = Field(default=..., description="""Human-readable label for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['dcterms:title', 'schema:name'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Free-text description of the entity (paraphrased; verbatim ISO text excluded).""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:description'} })
    clause_reference: Optional[str] = Field(default=None, description="""ISO/IEC 22989:2022 clause identifier (e.g. \"5.11.4\") the element corresponds to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'AutonomyAssessment',
                       'VerificationValidationFramework']} })
    aliases: Optional[list[str]] = Field(default=None, description="""Alternative names or synonyms for the term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:altLabel'} })
    preferred_label: Optional[str] = Field(default=None, description="""Preferred natural-language label.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:prefLabel'} })
    see_also_uri: Optional[list[str]] = Field(default=None, description="""Pointers to related external resources or term records.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:seeAlso'} })

    @field_validator('clause_reference')
    def pattern_clause_reference(cls, v):
        pattern=re.compile(r"^[0-9]+(\.[0-9]+){0,3}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid clause_reference format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid clause_reference format: {v}"
            raise ValueError(err_msg)
        return v


class Term(NamedEntity):
    """
    Abstract base class for a glossary term defined in Clause 3. Concrete subclasses partition the terminology along Clauses 3.1–3.7.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'exact_mappings': ['skos:Concept'],
         'from_schema': 'https://w3id.org/lmodel/iso22989',
         'in_subset': ['terminology']})

    id: str = Field(default=..., description="""Unique CURIE or URI identifying the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:identifier'} })
    name: str = Field(default=..., description="""Human-readable label for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['dcterms:title', 'schema:name'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Free-text description of the entity (paraphrased; verbatim ISO text excluded).""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:description'} })
    clause_reference: Optional[str] = Field(default=None, description="""ISO/IEC 22989:2022 clause identifier (e.g. \"5.11.4\") the element corresponds to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'AutonomyAssessment',
                       'VerificationValidationFramework']} })
    aliases: Optional[list[str]] = Field(default=None, description="""Alternative names or synonyms for the term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:altLabel'} })
    preferred_label: Optional[str] = Field(default=None, description="""Preferred natural-language label.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:prefLabel'} })
    see_also_uri: Optional[list[str]] = Field(default=None, description="""Pointers to related external resources or term records.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:seeAlso'} })

    @field_validator('clause_reference')
    def pattern_clause_reference(cls, v):
        pattern=re.compile(r"^[0-9]+(\.[0-9]+){0,3}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid clause_reference format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid clause_reference format: {v}"
            raise ValueError(err_msg)
        return v


class AITerm(Term):
    """
    Term defined in Clause 3.1 (terms related to AI).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'clause_section': {'tag': 'clause_section', 'value': '3.1'}},
         'from_schema': 'https://w3id.org/lmodel/iso22989'})

    id: str = Field(default=..., description="""Unique CURIE or URI identifying the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:identifier'} })
    name: str = Field(default=..., description="""Human-readable label for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['dcterms:title', 'schema:name'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Free-text description of the entity (paraphrased; verbatim ISO text excluded).""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:description'} })
    clause_reference: Optional[str] = Field(default=None, description="""ISO/IEC 22989:2022 clause identifier (e.g. \"5.11.4\") the element corresponds to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'AutonomyAssessment',
                       'VerificationValidationFramework']} })
    aliases: Optional[list[str]] = Field(default=None, description="""Alternative names or synonyms for the term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:altLabel'} })
    preferred_label: Optional[str] = Field(default=None, description="""Preferred natural-language label.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:prefLabel'} })
    see_also_uri: Optional[list[str]] = Field(default=None, description="""Pointers to related external resources or term records.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:seeAlso'} })

    @field_validator('clause_reference')
    def pattern_clause_reference(cls, v):
        pattern=re.compile(r"^[0-9]+(\.[0-9]+){0,3}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid clause_reference format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid clause_reference format: {v}"
            raise ValueError(err_msg)
        return v


class DataTerm(Term):
    """
    Term defined in Clause 3.2 (terms related to data).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'clause_section': {'tag': 'clause_section', 'value': '3.2'}},
         'from_schema': 'https://w3id.org/lmodel/iso22989'})

    id: str = Field(default=..., description="""Unique CURIE or URI identifying the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:identifier'} })
    name: str = Field(default=..., description="""Human-readable label for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['dcterms:title', 'schema:name'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Free-text description of the entity (paraphrased; verbatim ISO text excluded).""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:description'} })
    clause_reference: Optional[str] = Field(default=None, description="""ISO/IEC 22989:2022 clause identifier (e.g. \"5.11.4\") the element corresponds to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'AutonomyAssessment',
                       'VerificationValidationFramework']} })
    aliases: Optional[list[str]] = Field(default=None, description="""Alternative names or synonyms for the term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:altLabel'} })
    preferred_label: Optional[str] = Field(default=None, description="""Preferred natural-language label.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:prefLabel'} })
    see_also_uri: Optional[list[str]] = Field(default=None, description="""Pointers to related external resources or term records.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:seeAlso'} })

    @field_validator('clause_reference')
    def pattern_clause_reference(cls, v):
        pattern=re.compile(r"^[0-9]+(\.[0-9]+){0,3}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid clause_reference format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid clause_reference format: {v}"
            raise ValueError(err_msg)
        return v


class MachineLearningTerm(Term):
    """
    Term defined in Clause 3.3 (terms related to machine learning).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'clause_section': {'tag': 'clause_section', 'value': '3.3'}},
         'from_schema': 'https://w3id.org/lmodel/iso22989'})

    id: str = Field(default=..., description="""Unique CURIE or URI identifying the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:identifier'} })
    name: str = Field(default=..., description="""Human-readable label for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['dcterms:title', 'schema:name'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Free-text description of the entity (paraphrased; verbatim ISO text excluded).""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:description'} })
    clause_reference: Optional[str] = Field(default=None, description="""ISO/IEC 22989:2022 clause identifier (e.g. \"5.11.4\") the element corresponds to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'AutonomyAssessment',
                       'VerificationValidationFramework']} })
    aliases: Optional[list[str]] = Field(default=None, description="""Alternative names or synonyms for the term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:altLabel'} })
    preferred_label: Optional[str] = Field(default=None, description="""Preferred natural-language label.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:prefLabel'} })
    see_also_uri: Optional[list[str]] = Field(default=None, description="""Pointers to related external resources or term records.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:seeAlso'} })

    @field_validator('clause_reference')
    def pattern_clause_reference(cls, v):
        pattern=re.compile(r"^[0-9]+(\.[0-9]+){0,3}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid clause_reference format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid clause_reference format: {v}"
            raise ValueError(err_msg)
        return v


class NeuralNetworkTerm(Term):
    """
    Term defined in Clause 3.4 (terms related to neural networks).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'clause_section': {'tag': 'clause_section', 'value': '3.4'}},
         'from_schema': 'https://w3id.org/lmodel/iso22989'})

    id: str = Field(default=..., description="""Unique CURIE or URI identifying the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:identifier'} })
    name: str = Field(default=..., description="""Human-readable label for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['dcterms:title', 'schema:name'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Free-text description of the entity (paraphrased; verbatim ISO text excluded).""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:description'} })
    clause_reference: Optional[str] = Field(default=None, description="""ISO/IEC 22989:2022 clause identifier (e.g. \"5.11.4\") the element corresponds to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'AutonomyAssessment',
                       'VerificationValidationFramework']} })
    aliases: Optional[list[str]] = Field(default=None, description="""Alternative names or synonyms for the term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:altLabel'} })
    preferred_label: Optional[str] = Field(default=None, description="""Preferred natural-language label.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:prefLabel'} })
    see_also_uri: Optional[list[str]] = Field(default=None, description="""Pointers to related external resources or term records.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:seeAlso'} })

    @field_validator('clause_reference')
    def pattern_clause_reference(cls, v):
        pattern=re.compile(r"^[0-9]+(\.[0-9]+){0,3}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid clause_reference format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid clause_reference format: {v}"
            raise ValueError(err_msg)
        return v


class TrustworthinessTerm(Term):
    """
    Term defined in Clause 3.5 (terms related to trustworthiness).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'clause_section': {'tag': 'clause_section', 'value': '3.5'}},
         'from_schema': 'https://w3id.org/lmodel/iso22989',
         'in_subset': ['terminology', 'trustworthiness']})

    id: str = Field(default=..., description="""Unique CURIE or URI identifying the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:identifier'} })
    name: str = Field(default=..., description="""Human-readable label for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['dcterms:title', 'schema:name'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Free-text description of the entity (paraphrased; verbatim ISO text excluded).""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:description'} })
    clause_reference: Optional[str] = Field(default=None, description="""ISO/IEC 22989:2022 clause identifier (e.g. \"5.11.4\") the element corresponds to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'AutonomyAssessment',
                       'VerificationValidationFramework']} })
    aliases: Optional[list[str]] = Field(default=None, description="""Alternative names or synonyms for the term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:altLabel'} })
    preferred_label: Optional[str] = Field(default=None, description="""Preferred natural-language label.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:prefLabel'} })
    see_also_uri: Optional[list[str]] = Field(default=None, description="""Pointers to related external resources or term records.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:seeAlso'} })

    @field_validator('clause_reference')
    def pattern_clause_reference(cls, v):
        pattern=re.compile(r"^[0-9]+(\.[0-9]+){0,3}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid clause_reference format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid clause_reference format: {v}"
            raise ValueError(err_msg)
        return v


class NLPTerm(Term):
    """
    Term defined in Clause 3.6 (terms related to natural-language processing).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'clause_section': {'tag': 'clause_section', 'value': '3.6'}},
         'from_schema': 'https://w3id.org/lmodel/iso22989'})

    id: str = Field(default=..., description="""Unique CURIE or URI identifying the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:identifier'} })
    name: str = Field(default=..., description="""Human-readable label for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['dcterms:title', 'schema:name'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Free-text description of the entity (paraphrased; verbatim ISO text excluded).""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:description'} })
    clause_reference: Optional[str] = Field(default=None, description="""ISO/IEC 22989:2022 clause identifier (e.g. \"5.11.4\") the element corresponds to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'AutonomyAssessment',
                       'VerificationValidationFramework']} })
    aliases: Optional[list[str]] = Field(default=None, description="""Alternative names or synonyms for the term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:altLabel'} })
    preferred_label: Optional[str] = Field(default=None, description="""Preferred natural-language label.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:prefLabel'} })
    see_also_uri: Optional[list[str]] = Field(default=None, description="""Pointers to related external resources or term records.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:seeAlso'} })

    @field_validator('clause_reference')
    def pattern_clause_reference(cls, v):
        pattern=re.compile(r"^[0-9]+(\.[0-9]+){0,3}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid clause_reference format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid clause_reference format: {v}"
            raise ValueError(err_msg)
        return v


class ComputerVisionTerm(Term):
    """
    Term defined in Clause 3.7 (terms related to computer vision).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'clause_section': {'tag': 'clause_section', 'value': '3.7'}},
         'from_schema': 'https://w3id.org/lmodel/iso22989'})

    id: str = Field(default=..., description="""Unique CURIE or URI identifying the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:identifier'} })
    name: str = Field(default=..., description="""Human-readable label for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['dcterms:title', 'schema:name'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Free-text description of the entity (paraphrased; verbatim ISO text excluded).""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:description'} })
    clause_reference: Optional[str] = Field(default=None, description="""ISO/IEC 22989:2022 clause identifier (e.g. \"5.11.4\") the element corresponds to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'AutonomyAssessment',
                       'VerificationValidationFramework']} })
    aliases: Optional[list[str]] = Field(default=None, description="""Alternative names or synonyms for the term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:altLabel'} })
    preferred_label: Optional[str] = Field(default=None, description="""Preferred natural-language label.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:prefLabel'} })
    see_also_uri: Optional[list[str]] = Field(default=None, description="""Pointers to related external resources or term records.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:seeAlso'} })

    @field_validator('clause_reference')
    def pattern_clause_reference(cls, v):
        pattern=re.compile(r"^[0-9]+(\.[0-9]+){0,3}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid clause_reference format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid clause_reference format: {v}"
            raise ValueError(err_msg)
        return v


class AbbreviatedTerm(NamedEntity):
    """
    Abbreviation or acronym listed in Clause 4 with its expansion and optional definition reference.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/iso22989',
         'in_subset': ['terminology'],
         'slot_usage': {'expansion': {'description': 'Expanded form of the '
                                                     'abbreviation.',
                                      'name': 'expansion',
                                      'required': True}}})

    expansion: str = Field(default=..., description="""Expanded form of the abbreviation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AbbreviatedTerm', 'AbbreviationEntry']} })
    id: str = Field(default=..., description="""Unique CURIE or URI identifying the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:identifier'} })
    name: str = Field(default=..., description="""Human-readable label for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['dcterms:title', 'schema:name'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Free-text description of the entity (paraphrased; verbatim ISO text excluded).""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:description'} })
    clause_reference: Optional[str] = Field(default=None, description="""ISO/IEC 22989:2022 clause identifier (e.g. \"5.11.4\") the element corresponds to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'AutonomyAssessment',
                       'VerificationValidationFramework']} })
    aliases: Optional[list[str]] = Field(default=None, description="""Alternative names or synonyms for the term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:altLabel'} })
    preferred_label: Optional[str] = Field(default=None, description="""Preferred natural-language label.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:prefLabel'} })
    see_also_uri: Optional[list[str]] = Field(default=None, description="""Pointers to related external resources or term records.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:seeAlso'} })

    @field_validator('clause_reference')
    def pattern_clause_reference(cls, v):
        pattern=re.compile(r"^[0-9]+(\.[0-9]+){0,3}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid clause_reference format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid clause_reference format: {v}"
            raise ValueError(err_msg)
        return v


class AIConcept(NamedEntity):
    """
    Abstract base for Clause 5 conceptual entities (agent, knowledge, cognition, autonomy, etc.).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'from_schema': 'https://w3id.org/lmodel/iso22989',
         'in_subset': ['ai_concepts']})

    id: str = Field(default=..., description="""Unique CURIE or URI identifying the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:identifier'} })
    name: str = Field(default=..., description="""Human-readable label for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['dcterms:title', 'schema:name'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Free-text description of the entity (paraphrased; verbatim ISO text excluded).""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:description'} })
    clause_reference: Optional[str] = Field(default=None, description="""ISO/IEC 22989:2022 clause identifier (e.g. \"5.11.4\") the element corresponds to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'AutonomyAssessment',
                       'VerificationValidationFramework']} })
    aliases: Optional[list[str]] = Field(default=None, description="""Alternative names or synonyms for the term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:altLabel'} })
    preferred_label: Optional[str] = Field(default=None, description="""Preferred natural-language label.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:prefLabel'} })
    see_also_uri: Optional[list[str]] = Field(default=None, description="""Pointers to related external resources or term records.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:seeAlso'} })

    @field_validator('clause_reference')
    def pattern_clause_reference(cls, v):
        pattern=re.compile(r"^[0-9]+(\.[0-9]+){0,3}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid clause_reference format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid clause_reference format: {v}"
            raise ValueError(err_msg)
        return v


class AIAgent(AIConcept):
    """
    Entity that perceives its environment and acts upon it to achieve goals (Clause 5.3).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/iso22989'})

    autonomy_level: Optional[AutonomyLevel] = Field(default=None, description="""Operational autonomy level of the AI system.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIAgent', 'AISystem', 'AutonomyAssessment']} })
    symbolic_approach: Optional[SymbolicApproach] = Field(default=None, description="""Predominant symbolic vs subsymbolic approach used by the system.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIAgent', 'KnowledgeRepresentation', 'AISystem']} })
    agent_architecture: Optional[AgentArchitectureType] = Field(default=None, description="""Agent architecture realised by the entity (Clause 5.3).""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIAgent', 'AISystem']} })
    goal_set: Optional[list[str]] = Field(default=None, description="""Goals the agent is configured to pursue.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIAgent']} })
    id: str = Field(default=..., description="""Unique CURIE or URI identifying the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:identifier'} })
    name: str = Field(default=..., description="""Human-readable label for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['dcterms:title', 'schema:name'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Free-text description of the entity (paraphrased; verbatim ISO text excluded).""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:description'} })
    clause_reference: Optional[str] = Field(default=None, description="""ISO/IEC 22989:2022 clause identifier (e.g. \"5.11.4\") the element corresponds to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'AutonomyAssessment',
                       'VerificationValidationFramework']} })
    aliases: Optional[list[str]] = Field(default=None, description="""Alternative names or synonyms for the term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:altLabel'} })
    preferred_label: Optional[str] = Field(default=None, description="""Preferred natural-language label.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:prefLabel'} })
    see_also_uri: Optional[list[str]] = Field(default=None, description="""Pointers to related external resources or term records.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:seeAlso'} })

    @field_validator('clause_reference')
    def pattern_clause_reference(cls, v):
        pattern=re.compile(r"^[0-9]+(\.[0-9]+){0,3}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid clause_reference format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid clause_reference format: {v}"
            raise ValueError(err_msg)
        return v


class KnowledgeRepresentation(AIConcept):
    """
    Representation of knowledge usable by an AI system (Clause 5.4), including knowledge graphs, ontologies and rule bases.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/iso22989'})

    symbolic_approach: Optional[SymbolicApproach] = Field(default=None, description="""Predominant symbolic vs subsymbolic approach used by the system.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIAgent', 'KnowledgeRepresentation', 'AISystem']} })
    knowledge_type: Optional[KnowledgeType] = Field(default=None, description="""Type of knowledge captured (Clause 3.1.12, 3.1.28).""", json_schema_extra = { "linkml_meta": {'domain_of': ['KnowledgeRepresentation']} })
    representation_form: Optional[str] = Field(default=None, description="""Concrete form of representation (rules, frames, ontology, graph, vectors).""", json_schema_extra = { "linkml_meta": {'domain_of': ['KnowledgeRepresentation']} })
    id: str = Field(default=..., description="""Unique CURIE or URI identifying the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:identifier'} })
    name: str = Field(default=..., description="""Human-readable label for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['dcterms:title', 'schema:name'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Free-text description of the entity (paraphrased; verbatim ISO text excluded).""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:description'} })
    clause_reference: Optional[str] = Field(default=None, description="""ISO/IEC 22989:2022 clause identifier (e.g. \"5.11.4\") the element corresponds to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'AutonomyAssessment',
                       'VerificationValidationFramework']} })
    aliases: Optional[list[str]] = Field(default=None, description="""Alternative names or synonyms for the term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:altLabel'} })
    preferred_label: Optional[str] = Field(default=None, description="""Preferred natural-language label.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:prefLabel'} })
    see_also_uri: Optional[list[str]] = Field(default=None, description="""Pointers to related external resources or term records.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:seeAlso'} })

    @field_validator('clause_reference')
    def pattern_clause_reference(cls, v):
        pattern=re.compile(r"^[0-9]+(\.[0-9]+){0,3}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid clause_reference format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid clause_reference format: {v}"
            raise ValueError(err_msg)
        return v


class AISystem(NamedEntity):
    """
    Engineered system that uses AI techniques to perform tasks delegated to it. Aggregates lifecycle, functional, model and stakeholder data.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['iso42001:AISystem', 'nist_ai_100_1:AiSystem'],
         'from_schema': 'https://w3id.org/lmodel/iso22989',
         'in_subset': ['ai_concepts', 'ai_lifecycle', 'ai_functional_view'],
         'related_mappings': ['nist_ai_rmf:AISystem',
                              'iso27001:Asset',
                              'uco_core:UcoObject']})

    ai_system_type: Optional[AISystemType] = Field(default=None, description="""Capability classification of the AI system.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AISystem']} })
    symbolic_approach: Optional[SymbolicApproach] = Field(default=None, description="""Predominant symbolic vs subsymbolic approach used by the system.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIAgent', 'KnowledgeRepresentation', 'AISystem']} })
    autonomy_level: Optional[AutonomyLevel] = Field(default=None, description="""Operational autonomy level of the AI system.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIAgent', 'AISystem', 'AutonomyAssessment']} })
    intended_purpose: Optional[str] = Field(default=None, description="""Stated intended purpose of the AI system.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AISystem', 'AIApplication']} })
    application_domain: Optional[list[AIApplicationDomain]] = Field(default=None, description="""Application domain(s) the AI system targets.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AISystem', 'AIApplication']} })
    ai_field: Optional[list[AIField]] = Field(default=None, description="""AI sub-field(s) the system draws on.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AISystem']} })
    functional_components: Optional[list[AIFunctionalComponent]] = Field(default=None, description="""Functional components exhibited by the system (Clause 7).""", json_schema_extra = { "linkml_meta": {'domain_of': ['AISystem']} })
    lifecycle_stage: Optional[AILifecycleStage] = Field(default=None, description="""Current life-cycle stage of the AI system.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AISystem']} })
    stakeholders: Optional[list[AIStakeholderRole]] = Field(default=None, description="""Stakeholder roles associated with the AI system.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AISystem']} })
    components: Optional[list[AIComponent]] = Field(default=None, description="""Constituent components of the AI system.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AISystem']} })
    models: Optional[list[AIModel]] = Field(default=None, description="""Trained or knowledge-based models embedded in the AI system.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AISystem']} })
    datasets: Optional[list[Dataset]] = Field(default=None, description="""Datasets used by, or produced by, the AI system.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AISystem']} })
    trustworthiness_properties: Optional[list[TrustworthinessProperty]] = Field(default=None, description="""Trustworthiness properties claimed for the AI system.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AISystem']} })
    jurisdictional_issues: Optional[list[JurisdictionalIssueType]] = Field(default=None, description="""Jurisdictional issues considered in scope for the application.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AISystem', 'AIApplication']} })
    societal_impacts: Optional[list[SocietalImpactCategory]] = Field(default=None, description="""Societal impact categories considered in scope.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AISystem', 'AIApplication']} })
    system_characteristics: Optional[list[AISystemCharacteristic]] = Field(default=None, description="""Distinguishing characteristics from Clause 5.1.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AISystem']} })
    task_categories: Optional[list[TaskCategory]] = Field(default=None, description="""Task categories the AI system addresses.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AISystem']} })
    agent_architecture: Optional[AgentArchitectureType] = Field(default=None, description="""Agent architecture, if the AI system is structured as an agent (Clause 5.3).""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIAgent', 'AISystem']} })
    data_processes: Optional[list[DataProcess]] = Field(default=None, description="""Data-handling processes applied within the AI system (Clause 5.10).""", json_schema_extra = { "linkml_meta": {'domain_of': ['AISystem', 'AIConceptsCollection']} })
    iot_integration: Optional[str] = Field(default=None, description="""IoT/CPS system this AI system is integrated with, if any (Clause 5.14).""", json_schema_extra = { "linkml_meta": {'domain_of': ['AISystem']} })
    id: str = Field(default=..., description="""Unique CURIE or URI identifying the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:identifier'} })
    name: str = Field(default=..., description="""Human-readable label for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['dcterms:title', 'schema:name'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Free-text description of the entity (paraphrased; verbatim ISO text excluded).""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:description'} })
    clause_reference: Optional[str] = Field(default=None, description="""ISO/IEC 22989:2022 clause identifier (e.g. \"5.11.4\") the element corresponds to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'AutonomyAssessment',
                       'VerificationValidationFramework']} })
    aliases: Optional[list[str]] = Field(default=None, description="""Alternative names or synonyms for the term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:altLabel'} })
    preferred_label: Optional[str] = Field(default=None, description="""Preferred natural-language label.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:prefLabel'} })
    see_also_uri: Optional[list[str]] = Field(default=None, description="""Pointers to related external resources or term records.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:seeAlso'} })

    @field_validator('clause_reference')
    def pattern_clause_reference(cls, v):
        pattern=re.compile(r"^[0-9]+(\.[0-9]+){0,3}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid clause_reference format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid clause_reference format: {v}"
            raise ValueError(err_msg)
        return v


class AIComponent(NamedEntity):
    """
    Functional component of an AI system, such as a data pipeline, preprocessor, model server, or post-processing module.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/iso22989',
         'in_subset': ['ai_functional_view']})

    component_function: Optional[AIFunctionalComponent] = Field(default=None, description="""Functional view component implemented by an AI component (Clause 7).""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIComponent']} })
    depends_on: Optional[list[str]] = Field(default=None, description="""Other components this component depends on at runtime.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIComponent']} })
    id: str = Field(default=..., description="""Unique CURIE or URI identifying the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:identifier'} })
    name: str = Field(default=..., description="""Human-readable label for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['dcterms:title', 'schema:name'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Free-text description of the entity (paraphrased; verbatim ISO text excluded).""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:description'} })
    clause_reference: Optional[str] = Field(default=None, description="""ISO/IEC 22989:2022 clause identifier (e.g. \"5.11.4\") the element corresponds to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'AutonomyAssessment',
                       'VerificationValidationFramework']} })
    aliases: Optional[list[str]] = Field(default=None, description="""Alternative names or synonyms for the term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:altLabel'} })
    preferred_label: Optional[str] = Field(default=None, description="""Preferred natural-language label.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:prefLabel'} })
    see_also_uri: Optional[list[str]] = Field(default=None, description="""Pointers to related external resources or term records.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:seeAlso'} })

    @field_validator('clause_reference')
    def pattern_clause_reference(cls, v):
        pattern=re.compile(r"^[0-9]+(\.[0-9]+){0,3}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid clause_reference format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid clause_reference format: {v}"
            raise ValueError(err_msg)
        return v


class AIModel(NamedEntity):
    """
    Trained or rule-based model embedded in an AI system. Carries paradigm, algorithm family, dataset references and version metadata.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'close_mappings': ['nist_ai_100_1:AiSystemDimensionEnum#AI_MODEL'],
         'from_schema': 'https://w3id.org/lmodel/iso22989',
         'in_subset': ['terminology', 'ai_concepts'],
         'related_mappings': ['nist_ai_rmf:Model']})

    model_paradigm: Optional[MachineLearningParadigm] = Field(default=None, description="""Machine-learning paradigm under which the model was trained.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIModel']} })
    algorithm_family: Optional[MLAlgorithmFamily] = Field(default=None, description="""Algorithm family the model belongs to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIModel']} })
    engineering_approach: Optional[EngineeringApproach] = Field(default=None, description="""Non-learning engineering approach used (for symbolic/knowledge-based models).""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIModel']} })
    training_dataset: Optional[str] = Field(default=None, description="""Dataset used to fit the model.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIModel']} })
    validation_dataset: Optional[str] = Field(default=None, description="""Dataset used for hyperparameter tuning and model selection.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIModel']} })
    test_dataset: Optional[str] = Field(default=None, description="""Dataset used to estimate generalisation performance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIModel']} })
    hyperparameters: Optional[list[str]] = Field(default=None, description="""Free-form record of model hyperparameter settings.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIModel']} })
    model_version: Optional[str] = Field(default=None, description="""Version identifier of the trained model artefact.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIModel']} })
    trained_on: Optional[str] = Field(default=None, description="""Date or version reference for when the model was last trained.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIModel']} })
    supports_continuous_learning: Optional[bool] = Field(default=None, description="""Whether a model supports continuous or online learning (Clause 3.1.9, 5.11.9.2).""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIModel']} })
    catastrophic_forgetting_risk: Optional[float] = Field(default=None, description="""Estimated risk of catastrophic forgetting on retraining (Clause 5.11.9.1).""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIModel']} })
    parameter_count: Optional[int] = Field(default=None, description="""Approximate count of trainable model parameters.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['AIModel']} })
    training_duration: Optional[str] = Field(default=None, description="""Wall-clock duration of model training, expressed as an ISO 8601 duration.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIModel']} })
    inference_latency_ms: Optional[float] = Field(default=None, description="""Typical end-to-end inference latency in milliseconds.""", ge=0.0, json_schema_extra = { "linkml_meta": {'domain_of': ['AIModel']} })
    model_compression_applied: Optional[bool] = Field(default=None, description="""Whether the model has had compression or distillation applied for deployment (Clause 8.6.2).""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIModel']} })
    neural_network_architecture: Optional[NeuralNetworkArchitecture] = Field(default=None, description="""Neural-network architecture, when algorithm_family is neural_network (Clauses 3.4, 5.12.1).""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIModel']} })
    activation_function: Optional[ActivationFunctionType] = Field(default=None, description="""Predominant activation function used in the network (Clause 3.4.1).""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIModel', 'Neuron']} })
    training_phenomena: Optional[list[NeuralNetworkPhenomenon]] = Field(default=None, description="""Training-time phenomena observed for the model (Clause 3.4).""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIModel']} })
    id: str = Field(default=..., description="""Unique CURIE or URI identifying the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:identifier'} })
    name: str = Field(default=..., description="""Human-readable label for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['dcterms:title', 'schema:name'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Free-text description of the entity (paraphrased; verbatim ISO text excluded).""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:description'} })
    clause_reference: Optional[str] = Field(default=None, description="""ISO/IEC 22989:2022 clause identifier (e.g. \"5.11.4\") the element corresponds to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'AutonomyAssessment',
                       'VerificationValidationFramework']} })
    aliases: Optional[list[str]] = Field(default=None, description="""Alternative names or synonyms for the term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:altLabel'} })
    preferred_label: Optional[str] = Field(default=None, description="""Preferred natural-language label.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:prefLabel'} })
    see_also_uri: Optional[list[str]] = Field(default=None, description="""Pointers to related external resources or term records.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:seeAlso'} })

    @field_validator('clause_reference')
    def pattern_clause_reference(cls, v):
        pattern=re.compile(r"^[0-9]+(\.[0-9]+){0,3}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid clause_reference format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid clause_reference format: {v}"
            raise ValueError(err_msg)
        return v


class NeuralNetworkModel(AIModel):
    """
    AIModel realised as a neural network (Clause 5.12.1, Clause 3.4 terms).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/iso22989',
         'in_subset': ['terminology'],
         'slot_usage': {'algorithm_family': {'ifabsent': 'MLAlgorithmFamily(neural_network)',
                                             'name': 'algorithm_family'}}})

    number_of_layers: Optional[int] = Field(default=None, description="""Number of layers in the network.""", ge=1, json_schema_extra = { "linkml_meta": {'domain_of': ['NeuralNetworkModel']} })
    number_of_parameters: Optional[int] = Field(default=None, description="""Approximate number of trainable parameters.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['NeuralNetworkModel']} })
    model_paradigm: Optional[MachineLearningParadigm] = Field(default=None, description="""Machine-learning paradigm under which the model was trained.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIModel']} })
    algorithm_family: Optional[MLAlgorithmFamily] = Field(default=MLAlgorithmFamily.neural_network, description="""Algorithm family the model belongs to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIModel'], 'ifabsent': 'MLAlgorithmFamily(neural_network)'} })
    engineering_approach: Optional[EngineeringApproach] = Field(default=None, description="""Non-learning engineering approach used (for symbolic/knowledge-based models).""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIModel']} })
    training_dataset: Optional[str] = Field(default=None, description="""Dataset used to fit the model.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIModel']} })
    validation_dataset: Optional[str] = Field(default=None, description="""Dataset used for hyperparameter tuning and model selection.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIModel']} })
    test_dataset: Optional[str] = Field(default=None, description="""Dataset used to estimate generalisation performance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIModel']} })
    hyperparameters: Optional[list[str]] = Field(default=None, description="""Free-form record of model hyperparameter settings.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIModel']} })
    model_version: Optional[str] = Field(default=None, description="""Version identifier of the trained model artefact.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIModel']} })
    trained_on: Optional[str] = Field(default=None, description="""Date or version reference for when the model was last trained.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIModel']} })
    supports_continuous_learning: Optional[bool] = Field(default=None, description="""Whether a model supports continuous or online learning (Clause 3.1.9, 5.11.9.2).""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIModel']} })
    catastrophic_forgetting_risk: Optional[float] = Field(default=None, description="""Estimated risk of catastrophic forgetting on retraining (Clause 5.11.9.1).""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIModel']} })
    parameter_count: Optional[int] = Field(default=None, description="""Approximate count of trainable model parameters.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['AIModel']} })
    training_duration: Optional[str] = Field(default=None, description="""Wall-clock duration of model training, expressed as an ISO 8601 duration.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIModel']} })
    inference_latency_ms: Optional[float] = Field(default=None, description="""Typical end-to-end inference latency in milliseconds.""", ge=0.0, json_schema_extra = { "linkml_meta": {'domain_of': ['AIModel']} })
    model_compression_applied: Optional[bool] = Field(default=None, description="""Whether the model has had compression or distillation applied for deployment (Clause 8.6.2).""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIModel']} })
    neural_network_architecture: Optional[NeuralNetworkArchitecture] = Field(default=None, description="""Neural-network architecture, when algorithm_family is neural_network (Clauses 3.4, 5.12.1).""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIModel']} })
    activation_function: Optional[ActivationFunctionType] = Field(default=None, description="""Predominant activation function used in the network (Clause 3.4.1).""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIModel', 'Neuron']} })
    training_phenomena: Optional[list[NeuralNetworkPhenomenon]] = Field(default=None, description="""Training-time phenomena observed for the model (Clause 3.4).""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIModel']} })
    id: str = Field(default=..., description="""Unique CURIE or URI identifying the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:identifier'} })
    name: str = Field(default=..., description="""Human-readable label for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['dcterms:title', 'schema:name'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Free-text description of the entity (paraphrased; verbatim ISO text excluded).""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:description'} })
    clause_reference: Optional[str] = Field(default=None, description="""ISO/IEC 22989:2022 clause identifier (e.g. \"5.11.4\") the element corresponds to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'AutonomyAssessment',
                       'VerificationValidationFramework']} })
    aliases: Optional[list[str]] = Field(default=None, description="""Alternative names or synonyms for the term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:altLabel'} })
    preferred_label: Optional[str] = Field(default=None, description="""Preferred natural-language label.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:prefLabel'} })
    see_also_uri: Optional[list[str]] = Field(default=None, description="""Pointers to related external resources or term records.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:seeAlso'} })

    @field_validator('clause_reference')
    def pattern_clause_reference(cls, v):
        pattern=re.compile(r"^[0-9]+(\.[0-9]+){0,3}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid clause_reference format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid clause_reference format: {v}"
            raise ValueError(err_msg)
        return v


class Dataset(NamedEntity):
    """
    Collection of data items used by an AI system in a training, validation, test, reference or production role.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/iso22989',
         'in_subset': ['terminology'],
         'related_mappings': ['schema:Dataset',
                              'iso27001:Asset',
                              'iso29100:PersonallyIdentifiableInformation',
                              'uco_core:UcoObject']})

    data_modality: Optional[list[DataModality]] = Field(default=None, description="""Modalities present in the dataset.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset']} })
    dataset_role: Optional[DatasetRole] = Field(default=None, description="""Role the dataset plays in the ML workflow.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset']} })
    data_provenance: Optional[str] = Field(default=None, description="""Provenance statement for the dataset (origin, collection method, licensing).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset'], 'slot_uri': 'prov:wasDerivedFrom'} })
    record_count: Optional[int] = Field(default=None, description="""Number of records or examples in the dataset.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset']} })
    data_quality_notes: Optional[str] = Field(default=None, description="""Notes on data quality, completeness or representativeness.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset']} })
    contains_personal_data: Optional[bool] = Field(default=None, description="""Whether the dataset contains personal or personally identifiable information.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset']} })
    label_type: Optional[DataLabelType] = Field(default=None, description="""Type of target label associated with the dataset (Clause 3.2.10).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset', 'DataLabel']} })
    ground_truth_available: Optional[bool] = Field(default=None, description="""Whether trusted ground-truth labels are available (Clause 3.2.7).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset']} })
    feature_count: Optional[int] = Field(default=None, description="""Number of features per record.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset']} })
    data_processes_applied: Optional[list[DataProcess]] = Field(default=None, description="""Data-handling processes applied to the dataset (Clause 5.10).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset']} })
    id: str = Field(default=..., description="""Unique CURIE or URI identifying the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:identifier'} })
    name: str = Field(default=..., description="""Human-readable label for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['dcterms:title', 'schema:name'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Free-text description of the entity (paraphrased; verbatim ISO text excluded).""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:description'} })
    clause_reference: Optional[str] = Field(default=None, description="""ISO/IEC 22989:2022 clause identifier (e.g. \"5.11.4\") the element corresponds to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'AutonomyAssessment',
                       'VerificationValidationFramework']} })
    aliases: Optional[list[str]] = Field(default=None, description="""Alternative names or synonyms for the term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:altLabel'} })
    preferred_label: Optional[str] = Field(default=None, description="""Preferred natural-language label.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:prefLabel'} })
    see_also_uri: Optional[list[str]] = Field(default=None, description="""Pointers to related external resources or term records.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:seeAlso'} })

    @field_validator('clause_reference')
    def pattern_clause_reference(cls, v):
        pattern=re.compile(r"^[0-9]+(\.[0-9]+){0,3}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid clause_reference format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid clause_reference format: {v}"
            raise ValueError(err_msg)
        return v


class TrustworthinessProperty(NamedEntity):
    """
    Claim about a trustworthiness property of an AI system or model, with evidence and measurement metadata.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'close_mappings': ['nist_ai_rmf_common:TrustworthinessCharacteristicEnum'],
         'from_schema': 'https://w3id.org/lmodel/iso22989',
         'in_subset': ['trustworthiness'],
         'related_mappings': ['nist_ai_rmf:TrustworthinessCharacteristic',
                              'iso29100:PrivacyFramework']})

    trustworthiness_property_type: TrustworthinessPropertyType = Field(default=..., description="""Which trustworthiness property is being characterised.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TrustworthinessProperty']} })
    property_evidence: Optional[list[str]] = Field(default=None, description="""References to evidence supporting the property claim.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TrustworthinessProperty']} })
    measurement_method: Optional[str] = Field(default=None, description="""How the property was assessed or measured.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TrustworthinessProperty']} })
    applicable_biases: Optional[list[BiasType]] = Field(default=None, description="""Bias categories considered relevant to this property assessment.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TrustworthinessProperty']} })
    confidence_score: Optional[float] = Field(default=None, description="""Normalised confidence in the property claim.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TrustworthinessProperty']} })
    id: str = Field(default=..., description="""Unique CURIE or URI identifying the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:identifier'} })
    name: str = Field(default=..., description="""Human-readable label for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['dcterms:title', 'schema:name'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Free-text description of the entity (paraphrased; verbatim ISO text excluded).""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:description'} })
    clause_reference: Optional[str] = Field(default=None, description="""ISO/IEC 22989:2022 clause identifier (e.g. \"5.11.4\") the element corresponds to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'AutonomyAssessment',
                       'VerificationValidationFramework']} })
    aliases: Optional[list[str]] = Field(default=None, description="""Alternative names or synonyms for the term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:altLabel'} })
    preferred_label: Optional[str] = Field(default=None, description="""Preferred natural-language label.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:prefLabel'} })
    see_also_uri: Optional[list[str]] = Field(default=None, description="""Pointers to related external resources or term records.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:seeAlso'} })

    @field_validator('clause_reference')
    def pattern_clause_reference(cls, v):
        pattern=re.compile(r"^[0-9]+(\.[0-9]+){0,3}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid clause_reference format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid clause_reference format: {v}"
            raise ValueError(err_msg)
        return v


class AILifecycleProcess(NamedEntity):
    """
    Process or activity associated with a stage of the AI system life cycle (Clause 6).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['gist_linkml:Event'],
         'close_mappings': ['nist_ai_100_1:AiLifecycleStage'],
         'from_schema': 'https://w3id.org/lmodel/iso22989',
         'in_subset': ['ai_lifecycle'],
         'related_mappings': ['nist_ai_600_1:SuggestedAction']})

    process_stage: AILifecycleStage = Field(default=..., description="""Life-cycle stage the process belongs to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AILifecycleProcess']} })
    process_inputs: Optional[list[str]] = Field(default=None, description="""Inputs consumed by the process.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AILifecycleProcess']} })
    process_outputs: Optional[list[str]] = Field(default=None, description="""Outputs produced by the process.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AILifecycleProcess']} })
    responsible_role: Optional[AIStakeholderRoleType] = Field(default=None, description="""Stakeholder role responsible for executing the process.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AILifecycleProcess']} })
    start_date: Optional[date] = Field(default=None, description="""Date the process started.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AILifecycleProcess']} })
    end_date: Optional[date] = Field(default=None, description="""Date the process completed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AILifecycleProcess']} })
    risk_items: Optional[list[str]] = Field(default=None, description="""Risks identified or addressed by a process or assessment.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AILifecycleProcess']} })
    approval_criteria: Optional[list[str]] = Field(default=None, description="""Criteria that must be met for an output or process to be approved.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AILifecycleProcess']} })
    process_sub_type: Optional[str] = Field(default=None, description="""Free-text refinement of the process within its life-cycle stage (e.g. \"objectives\", \"requirements\").""", json_schema_extra = { "linkml_meta": {'domain_of': ['AILifecycleProcess']} })
    id: str = Field(default=..., description="""Unique CURIE or URI identifying the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:identifier'} })
    name: str = Field(default=..., description="""Human-readable label for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['dcterms:title', 'schema:name'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Free-text description of the entity (paraphrased; verbatim ISO text excluded).""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:description'} })
    clause_reference: Optional[str] = Field(default=None, description="""ISO/IEC 22989:2022 clause identifier (e.g. \"5.11.4\") the element corresponds to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'AutonomyAssessment',
                       'VerificationValidationFramework']} })
    aliases: Optional[list[str]] = Field(default=None, description="""Alternative names or synonyms for the term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:altLabel'} })
    preferred_label: Optional[str] = Field(default=None, description="""Preferred natural-language label.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:prefLabel'} })
    see_also_uri: Optional[list[str]] = Field(default=None, description="""Pointers to related external resources or term records.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:seeAlso'} })

    @field_validator('clause_reference')
    def pattern_clause_reference(cls, v):
        pattern=re.compile(r"^[0-9]+(\.[0-9]+){0,3}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid clause_reference format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid clause_reference format: {v}"
            raise ValueError(err_msg)
        return v


class AIStakeholderRole(NamedEntity):
    """
    Stakeholder role enacted by an organisation or individual in relation to an AI system (Clause 5.19).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'close_mappings': ['nist_ai_100_1:AiActor'],
         'from_schema': 'https://w3id.org/lmodel/iso22989',
         'in_subset': ['ai_stakeholders']})

    stakeholder_role_type: AIStakeholderRoleType = Field(default=..., description="""Canonical stakeholder role type as defined in Clause 5.19.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIStakeholderRole']} })
    organization_name: Optional[str] = Field(default=None, description="""Name of the organisation acting in the stakeholder role.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIStakeholderRole']} })
    contact: Optional[str] = Field(default=None, description="""Contact identifier (e.g. email) for the stakeholder.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIStakeholderRole']} })
    responsibilities: Optional[list[str]] = Field(default=None, description="""Free-text statements of responsibility.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIStakeholderRole']} })
    id: str = Field(default=..., description="""Unique CURIE or URI identifying the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:identifier'} })
    name: str = Field(default=..., description="""Human-readable label for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['dcterms:title', 'schema:name'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Free-text description of the entity (paraphrased; verbatim ISO text excluded).""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:description'} })
    clause_reference: Optional[str] = Field(default=None, description="""ISO/IEC 22989:2022 clause identifier (e.g. \"5.11.4\") the element corresponds to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'AutonomyAssessment',
                       'VerificationValidationFramework']} })
    aliases: Optional[list[str]] = Field(default=None, description="""Alternative names or synonyms for the term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:altLabel'} })
    preferred_label: Optional[str] = Field(default=None, description="""Preferred natural-language label.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:prefLabel'} })
    see_also_uri: Optional[list[str]] = Field(default=None, description="""Pointers to related external resources or term records.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:seeAlso'} })

    @field_validator('clause_reference')
    def pattern_clause_reference(cls, v):
        pattern=re.compile(r"^[0-9]+(\.[0-9]+){0,3}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid clause_reference format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid clause_reference format: {v}"
            raise ValueError(err_msg)
        return v


class AIProvider(AIStakeholderRole):
    """
    Stakeholder making an AI system available to customers (Clause 5.19.2).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/iso22989',
         'slot_usage': {'stakeholder_role_type': {'ifabsent': 'AIStakeholderRoleType(ai_provider)',
                                                  'name': 'stakeholder_role_type'}}})

    stakeholder_role_type: AIStakeholderRoleType = Field(default=AIStakeholderRoleType.ai_provider, description="""Canonical stakeholder role type as defined in Clause 5.19.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIStakeholderRole'],
         'ifabsent': 'AIStakeholderRoleType(ai_provider)'} })
    organization_name: Optional[str] = Field(default=None, description="""Name of the organisation acting in the stakeholder role.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIStakeholderRole']} })
    contact: Optional[str] = Field(default=None, description="""Contact identifier (e.g. email) for the stakeholder.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIStakeholderRole']} })
    responsibilities: Optional[list[str]] = Field(default=None, description="""Free-text statements of responsibility.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIStakeholderRole']} })
    id: str = Field(default=..., description="""Unique CURIE or URI identifying the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:identifier'} })
    name: str = Field(default=..., description="""Human-readable label for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['dcterms:title', 'schema:name'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Free-text description of the entity (paraphrased; verbatim ISO text excluded).""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:description'} })
    clause_reference: Optional[str] = Field(default=None, description="""ISO/IEC 22989:2022 clause identifier (e.g. \"5.11.4\") the element corresponds to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'AutonomyAssessment',
                       'VerificationValidationFramework']} })
    aliases: Optional[list[str]] = Field(default=None, description="""Alternative names or synonyms for the term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:altLabel'} })
    preferred_label: Optional[str] = Field(default=None, description="""Preferred natural-language label.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:prefLabel'} })
    see_also_uri: Optional[list[str]] = Field(default=None, description="""Pointers to related external resources or term records.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:seeAlso'} })

    @field_validator('clause_reference')
    def pattern_clause_reference(cls, v):
        pattern=re.compile(r"^[0-9]+(\.[0-9]+){0,3}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid clause_reference format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid clause_reference format: {v}"
            raise ValueError(err_msg)
        return v


class AIProducer(AIStakeholderRole):
    """
    Stakeholder designing, developing or assembling AI systems (Clause 5.19.3).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'close_mappings': ['iso29100:PIIProcessor'],
         'from_schema': 'https://w3id.org/lmodel/iso22989',
         'slot_usage': {'stakeholder_role_type': {'ifabsent': 'AIStakeholderRoleType(ai_producer)',
                                                  'name': 'stakeholder_role_type'}}})

    stakeholder_role_type: AIStakeholderRoleType = Field(default=AIStakeholderRoleType.ai_producer, description="""Canonical stakeholder role type as defined in Clause 5.19.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIStakeholderRole'],
         'ifabsent': 'AIStakeholderRoleType(ai_producer)'} })
    organization_name: Optional[str] = Field(default=None, description="""Name of the organisation acting in the stakeholder role.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIStakeholderRole']} })
    contact: Optional[str] = Field(default=None, description="""Contact identifier (e.g. email) for the stakeholder.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIStakeholderRole']} })
    responsibilities: Optional[list[str]] = Field(default=None, description="""Free-text statements of responsibility.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIStakeholderRole']} })
    id: str = Field(default=..., description="""Unique CURIE or URI identifying the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:identifier'} })
    name: str = Field(default=..., description="""Human-readable label for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['dcterms:title', 'schema:name'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Free-text description of the entity (paraphrased; verbatim ISO text excluded).""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:description'} })
    clause_reference: Optional[str] = Field(default=None, description="""ISO/IEC 22989:2022 clause identifier (e.g. \"5.11.4\") the element corresponds to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'AutonomyAssessment',
                       'VerificationValidationFramework']} })
    aliases: Optional[list[str]] = Field(default=None, description="""Alternative names or synonyms for the term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:altLabel'} })
    preferred_label: Optional[str] = Field(default=None, description="""Preferred natural-language label.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:prefLabel'} })
    see_also_uri: Optional[list[str]] = Field(default=None, description="""Pointers to related external resources or term records.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:seeAlso'} })

    @field_validator('clause_reference')
    def pattern_clause_reference(cls, v):
        pattern=re.compile(r"^[0-9]+(\.[0-9]+){0,3}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid clause_reference format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid clause_reference format: {v}"
            raise ValueError(err_msg)
        return v


class AICustomer(AIStakeholderRole):
    """
    Stakeholder using an AI system or AI-backed service (Clause 5.19.4).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/iso22989',
         'slot_usage': {'stakeholder_role_type': {'ifabsent': 'AIStakeholderRoleType(ai_customer)',
                                                  'name': 'stakeholder_role_type'}}})

    stakeholder_role_type: AIStakeholderRoleType = Field(default=AIStakeholderRoleType.ai_customer, description="""Canonical stakeholder role type as defined in Clause 5.19.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIStakeholderRole'],
         'ifabsent': 'AIStakeholderRoleType(ai_customer)'} })
    organization_name: Optional[str] = Field(default=None, description="""Name of the organisation acting in the stakeholder role.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIStakeholderRole']} })
    contact: Optional[str] = Field(default=None, description="""Contact identifier (e.g. email) for the stakeholder.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIStakeholderRole']} })
    responsibilities: Optional[list[str]] = Field(default=None, description="""Free-text statements of responsibility.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIStakeholderRole']} })
    id: str = Field(default=..., description="""Unique CURIE or URI identifying the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:identifier'} })
    name: str = Field(default=..., description="""Human-readable label for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['dcterms:title', 'schema:name'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Free-text description of the entity (paraphrased; verbatim ISO text excluded).""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:description'} })
    clause_reference: Optional[str] = Field(default=None, description="""ISO/IEC 22989:2022 clause identifier (e.g. \"5.11.4\") the element corresponds to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'AutonomyAssessment',
                       'VerificationValidationFramework']} })
    aliases: Optional[list[str]] = Field(default=None, description="""Alternative names or synonyms for the term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:altLabel'} })
    preferred_label: Optional[str] = Field(default=None, description="""Preferred natural-language label.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:prefLabel'} })
    see_also_uri: Optional[list[str]] = Field(default=None, description="""Pointers to related external resources or term records.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:seeAlso'} })

    @field_validator('clause_reference')
    def pattern_clause_reference(cls, v):
        pattern=re.compile(r"^[0-9]+(\.[0-9]+){0,3}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid clause_reference format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid clause_reference format: {v}"
            raise ValueError(err_msg)
        return v


class AIPartner(AIStakeholderRole):
    """
    Stakeholder providing supporting services across the AI life cycle (Clause 5.19.5).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'close_mappings': ['iso29100:ThirdParty',
                            'nist_ai_100_1:AiActorTaskEnum#THIRD_PARTY_ENTITIES',
                            'nist_ai_600_1:GaiActorTaskEnum#THIRD_PARTY_ENTITIES'],
         'from_schema': 'https://w3id.org/lmodel/iso22989',
         'slot_usage': {'stakeholder_role_type': {'ifabsent': 'AIStakeholderRoleType(ai_partner)',
                                                  'name': 'stakeholder_role_type'}}})

    stakeholder_role_type: AIStakeholderRoleType = Field(default=AIStakeholderRoleType.ai_partner, description="""Canonical stakeholder role type as defined in Clause 5.19.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIStakeholderRole'],
         'ifabsent': 'AIStakeholderRoleType(ai_partner)'} })
    organization_name: Optional[str] = Field(default=None, description="""Name of the organisation acting in the stakeholder role.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIStakeholderRole']} })
    contact: Optional[str] = Field(default=None, description="""Contact identifier (e.g. email) for the stakeholder.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIStakeholderRole']} })
    responsibilities: Optional[list[str]] = Field(default=None, description="""Free-text statements of responsibility.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIStakeholderRole']} })
    id: str = Field(default=..., description="""Unique CURIE or URI identifying the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:identifier'} })
    name: str = Field(default=..., description="""Human-readable label for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['dcterms:title', 'schema:name'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Free-text description of the entity (paraphrased; verbatim ISO text excluded).""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:description'} })
    clause_reference: Optional[str] = Field(default=None, description="""ISO/IEC 22989:2022 clause identifier (e.g. \"5.11.4\") the element corresponds to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'AutonomyAssessment',
                       'VerificationValidationFramework']} })
    aliases: Optional[list[str]] = Field(default=None, description="""Alternative names or synonyms for the term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:altLabel'} })
    preferred_label: Optional[str] = Field(default=None, description="""Preferred natural-language label.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:prefLabel'} })
    see_also_uri: Optional[list[str]] = Field(default=None, description="""Pointers to related external resources or term records.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:seeAlso'} })

    @field_validator('clause_reference')
    def pattern_clause_reference(cls, v):
        pattern=re.compile(r"^[0-9]+(\.[0-9]+){0,3}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid clause_reference format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid clause_reference format: {v}"
            raise ValueError(err_msg)
        return v


class AISubject(AIStakeholderRole):
    """
    Person or group affected by an AI system (Clause 5.19.6).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'close_mappings': ['nist_ai_100_1:AiActorTaskEnum#AFFECTED_INDIVIDUALS_OR_COMMUNITIES',
                            'nist_ai_600_1:GaiActorTaskEnum#AFFECTED_INDIVIDUALS_AND_COMMUNITIES'],
         'from_schema': 'https://w3id.org/lmodel/iso22989',
         'slot_usage': {'stakeholder_role_type': {'ifabsent': 'AIStakeholderRoleType(ai_subject)',
                                                  'name': 'stakeholder_role_type'}}})

    stakeholder_role_type: AIStakeholderRoleType = Field(default=AIStakeholderRoleType.ai_subject, description="""Canonical stakeholder role type as defined in Clause 5.19.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIStakeholderRole'],
         'ifabsent': 'AIStakeholderRoleType(ai_subject)'} })
    organization_name: Optional[str] = Field(default=None, description="""Name of the organisation acting in the stakeholder role.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIStakeholderRole']} })
    contact: Optional[str] = Field(default=None, description="""Contact identifier (e.g. email) for the stakeholder.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIStakeholderRole']} })
    responsibilities: Optional[list[str]] = Field(default=None, description="""Free-text statements of responsibility.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIStakeholderRole']} })
    id: str = Field(default=..., description="""Unique CURIE or URI identifying the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:identifier'} })
    name: str = Field(default=..., description="""Human-readable label for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['dcterms:title', 'schema:name'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Free-text description of the entity (paraphrased; verbatim ISO text excluded).""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:description'} })
    clause_reference: Optional[str] = Field(default=None, description="""ISO/IEC 22989:2022 clause identifier (e.g. \"5.11.4\") the element corresponds to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'AutonomyAssessment',
                       'VerificationValidationFramework']} })
    aliases: Optional[list[str]] = Field(default=None, description="""Alternative names or synonyms for the term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:altLabel'} })
    preferred_label: Optional[str] = Field(default=None, description="""Preferred natural-language label.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:prefLabel'} })
    see_also_uri: Optional[list[str]] = Field(default=None, description="""Pointers to related external resources or term records.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:seeAlso'} })

    @field_validator('clause_reference')
    def pattern_clause_reference(cls, v):
        pattern=re.compile(r"^[0-9]+(\.[0-9]+){0,3}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid clause_reference format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid clause_reference format: {v}"
            raise ValueError(err_msg)
        return v


class RelevantAuthority(AIStakeholderRole):
    """
    Regulator or standards-setting body with oversight responsibilities (Clause 5.19.7).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'close_mappings': ['nist_ai_100_1:AiActorTaskEnum#GOVERNANCE_AND_OVERSIGHT',
                            'nist_ai_600_1:GaiActorTaskEnum#GOVERNANCE_AND_OVERSIGHT'],
         'from_schema': 'https://w3id.org/lmodel/iso22989',
         'slot_usage': {'stakeholder_role_type': {'ifabsent': 'AIStakeholderRoleType(relevant_authority)',
                                                  'name': 'stakeholder_role_type'}}})

    stakeholder_role_type: AIStakeholderRoleType = Field(default=AIStakeholderRoleType.relevant_authority, description="""Canonical stakeholder role type as defined in Clause 5.19.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIStakeholderRole'],
         'ifabsent': 'AIStakeholderRoleType(relevant_authority)'} })
    organization_name: Optional[str] = Field(default=None, description="""Name of the organisation acting in the stakeholder role.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIStakeholderRole']} })
    contact: Optional[str] = Field(default=None, description="""Contact identifier (e.g. email) for the stakeholder.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIStakeholderRole']} })
    responsibilities: Optional[list[str]] = Field(default=None, description="""Free-text statements of responsibility.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIStakeholderRole']} })
    id: str = Field(default=..., description="""Unique CURIE or URI identifying the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:identifier'} })
    name: str = Field(default=..., description="""Human-readable label for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['dcterms:title', 'schema:name'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Free-text description of the entity (paraphrased; verbatim ISO text excluded).""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:description'} })
    clause_reference: Optional[str] = Field(default=None, description="""ISO/IEC 22989:2022 clause identifier (e.g. \"5.11.4\") the element corresponds to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'AutonomyAssessment',
                       'VerificationValidationFramework']} })
    aliases: Optional[list[str]] = Field(default=None, description="""Alternative names or synonyms for the term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:altLabel'} })
    preferred_label: Optional[str] = Field(default=None, description="""Preferred natural-language label.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:prefLabel'} })
    see_also_uri: Optional[list[str]] = Field(default=None, description="""Pointers to related external resources or term records.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:seeAlso'} })

    @field_validator('clause_reference')
    def pattern_clause_reference(cls, v):
        pattern=re.compile(r"^[0-9]+(\.[0-9]+){0,3}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid clause_reference format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid clause_reference format: {v}"
            raise ValueError(err_msg)
        return v


class AIEcosystem(NamedEntity):
    """
    Aggregation of the AI systems, data sources, computing resources and stakeholder roles that surround a deployment context (Clause 8).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/iso22989',
         'in_subset': ['ai_ecosystem']})

    computing_resources: Optional[list[ComputingResourceType]] = Field(default=None, description="""Computing resource types relied upon.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIEcosystem']} })
    data_sources: Optional[list[str]] = Field(default=None, description="""Identifiers or descriptions of data sources feeding the ecosystem.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIEcosystem']} })
    ecosystem_components: Optional[list[str]] = Field(default=None, description="""Free-text or CURIE references to ecosystem components.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIEcosystem']} })
    ai_systems: Optional[list[AISystem]] = Field(default=None, description="""AI systems documented in the collection.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIEcosystem', 'AIConceptsCollection']} })
    ai_stakeholder_roles: Optional[list[AIStakeholderRole]] = Field(default=None, description="""Stakeholder role records in the collection.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIEcosystem', 'AIConceptsCollection']} })
    big_data_characteristics: Optional[list[BigDataCharacteristic]] = Field(default=None, description="""Big-data characteristics that the ecosystem exhibits (Clause 8.6.1).""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIEcosystem']} })
    id: str = Field(default=..., description="""Unique CURIE or URI identifying the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:identifier'} })
    name: str = Field(default=..., description="""Human-readable label for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['dcterms:title', 'schema:name'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Free-text description of the entity (paraphrased; verbatim ISO text excluded).""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:description'} })
    clause_reference: Optional[str] = Field(default=None, description="""ISO/IEC 22989:2022 clause identifier (e.g. \"5.11.4\") the element corresponds to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'AutonomyAssessment',
                       'VerificationValidationFramework']} })
    aliases: Optional[list[str]] = Field(default=None, description="""Alternative names or synonyms for the term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:altLabel'} })
    preferred_label: Optional[str] = Field(default=None, description="""Preferred natural-language label.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:prefLabel'} })
    see_also_uri: Optional[list[str]] = Field(default=None, description="""Pointers to related external resources or term records.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:seeAlso'} })

    @field_validator('clause_reference')
    def pattern_clause_reference(cls, v):
        pattern=re.compile(r"^[0-9]+(\.[0-9]+){0,3}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid clause_reference format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid clause_reference format: {v}"
            raise ValueError(err_msg)
        return v


class ResourcePool(NamedEntity):
    """
    Pool of computing resources (CPU/GPU/TPU/ASIC/FPGA) available to AI workloads (Clause 8.7).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/iso22989',
         'in_subset': ['ai_ecosystem'],
         'slot_usage': {'resource_type': {'name': 'resource_type', 'required': True}}})

    resource_type: ComputingResourceType = Field(default=..., description="""Category of computing resource (Clause 8.7).""", json_schema_extra = { "linkml_meta": {'domain_of': ['ResourcePool']} })
    capacity_units: Optional[str] = Field(default=None, description="""Capacity expressed in units appropriate to the resource type.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ResourcePool']} })
    id: str = Field(default=..., description="""Unique CURIE or URI identifying the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:identifier'} })
    name: str = Field(default=..., description="""Human-readable label for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['dcterms:title', 'schema:name'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Free-text description of the entity (paraphrased; verbatim ISO text excluded).""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:description'} })
    clause_reference: Optional[str] = Field(default=None, description="""ISO/IEC 22989:2022 clause identifier (e.g. \"5.11.4\") the element corresponds to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'AutonomyAssessment',
                       'VerificationValidationFramework']} })
    aliases: Optional[list[str]] = Field(default=None, description="""Alternative names or synonyms for the term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:altLabel'} })
    preferred_label: Optional[str] = Field(default=None, description="""Preferred natural-language label.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:prefLabel'} })
    see_also_uri: Optional[list[str]] = Field(default=None, description="""Pointers to related external resources or term records.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:seeAlso'} })

    @field_validator('clause_reference')
    def pattern_clause_reference(cls, v):
        pattern=re.compile(r"^[0-9]+(\.[0-9]+){0,3}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid clause_reference format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid clause_reference format: {v}"
            raise ValueError(err_msg)
        return v


class NLPComponent(NamedEntity):
    """
    Component of a natural-language-processing pipeline (Clause 9.2).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/iso22989',
         'in_subset': ['ai_fields'],
         'slot_usage': {'nlp_component_type': {'name': 'nlp_component_type',
                                               'required': True}}})

    nlp_component_type: NLPComponentType = Field(default=..., description="""Type of NLP pipeline component (Clause 9.2.2).""", json_schema_extra = { "linkml_meta": {'domain_of': ['NLPComponent']} })
    id: str = Field(default=..., description="""Unique CURIE or URI identifying the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:identifier'} })
    name: str = Field(default=..., description="""Human-readable label for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['dcterms:title', 'schema:name'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Free-text description of the entity (paraphrased; verbatim ISO text excluded).""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:description'} })
    clause_reference: Optional[str] = Field(default=None, description="""ISO/IEC 22989:2022 clause identifier (e.g. \"5.11.4\") the element corresponds to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'AutonomyAssessment',
                       'VerificationValidationFramework']} })
    aliases: Optional[list[str]] = Field(default=None, description="""Alternative names or synonyms for the term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:altLabel'} })
    preferred_label: Optional[str] = Field(default=None, description="""Preferred natural-language label.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:prefLabel'} })
    see_also_uri: Optional[list[str]] = Field(default=None, description="""Pointers to related external resources or term records.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:seeAlso'} })

    @field_validator('clause_reference')
    def pattern_clause_reference(cls, v):
        pattern=re.compile(r"^[0-9]+(\.[0-9]+){0,3}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid clause_reference format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid clause_reference format: {v}"
            raise ValueError(err_msg)
        return v


class ComputerVisionFunction(NamedEntity):
    """
    Computer-vision capability provided by an AI system (Clause 9.1).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/iso22989',
         'in_subset': ['ai_fields'],
         'slot_usage': {'cv_task': {'name': 'cv_task', 'required': True}}})

    cv_task: ComputerVisionTask = Field(default=..., description="""Type of computer-vision task (Clause 9.1).""", json_schema_extra = { "linkml_meta": {'domain_of': ['ComputerVisionFunction']} })
    id: str = Field(default=..., description="""Unique CURIE or URI identifying the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:identifier'} })
    name: str = Field(default=..., description="""Human-readable label for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['dcterms:title', 'schema:name'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Free-text description of the entity (paraphrased; verbatim ISO text excluded).""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:description'} })
    clause_reference: Optional[str] = Field(default=None, description="""ISO/IEC 22989:2022 clause identifier (e.g. \"5.11.4\") the element corresponds to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'AutonomyAssessment',
                       'VerificationValidationFramework']} })
    aliases: Optional[list[str]] = Field(default=None, description="""Alternative names or synonyms for the term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:altLabel'} })
    preferred_label: Optional[str] = Field(default=None, description="""Preferred natural-language label.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:prefLabel'} })
    see_also_uri: Optional[list[str]] = Field(default=None, description="""Pointers to related external resources or term records.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:seeAlso'} })

    @field_validator('clause_reference')
    def pattern_clause_reference(cls, v):
        pattern=re.compile(r"^[0-9]+(\.[0-9]+){0,3}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid clause_reference format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid clause_reference format: {v}"
            raise ValueError(err_msg)
        return v


class AIApplication(NamedEntity):
    """
    Description of an AI application instance situated in a domain (Clause 10).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/iso22989',
         'in_subset': ['ai_applications_domain']})

    application_domain: Optional[list[AIApplicationDomain]] = Field(default=None, description="""Application domain(s) the AI system targets.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AISystem', 'AIApplication']} })
    intended_purpose: Optional[str] = Field(default=None, description="""Stated intended purpose of the AI system.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AISystem', 'AIApplication']} })
    jurisdictional_issues: Optional[list[JurisdictionalIssueType]] = Field(default=None, description="""Jurisdictional issues considered in scope for the application.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AISystem', 'AIApplication']} })
    societal_impacts: Optional[list[SocietalImpactCategory]] = Field(default=None, description="""Societal impact categories considered in scope.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AISystem', 'AIApplication']} })
    hosting_system: Optional[str] = Field(default=None, description="""AI system that provides the application.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIApplication']} })
    id: str = Field(default=..., description="""Unique CURIE or URI identifying the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:identifier'} })
    name: str = Field(default=..., description="""Human-readable label for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['dcterms:title', 'schema:name'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Free-text description of the entity (paraphrased; verbatim ISO text excluded).""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:description'} })
    clause_reference: Optional[str] = Field(default=None, description="""ISO/IEC 22989:2022 clause identifier (e.g. \"5.11.4\") the element corresponds to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'AutonomyAssessment',
                       'VerificationValidationFramework']} })
    aliases: Optional[list[str]] = Field(default=None, description="""Alternative names or synonyms for the term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:altLabel'} })
    preferred_label: Optional[str] = Field(default=None, description="""Preferred natural-language label.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:prefLabel'} })
    see_also_uri: Optional[list[str]] = Field(default=None, description="""Pointers to related external resources or term records.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:seeAlso'} })

    @field_validator('clause_reference')
    def pattern_clause_reference(cls, v):
        pattern=re.compile(r"^[0-9]+(\.[0-9]+){0,3}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid clause_reference format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid clause_reference format: {v}"
            raise ValueError(err_msg)
        return v


class Task(NamedEntity):
    """
    AI task addressed by a model or system (e.g. classification, regression, planning). Provides a first-class entity for the task categories enumerated across Clause 3 terminology.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'close_mappings': ['gist_linkml:Task',
                            'nist_ai_100_1:AiSystemDimensionEnum#TASK_AND_OUTPUT'],
         'from_schema': 'https://w3id.org/lmodel/iso22989',
         'in_subset': ['ai_functional_view'],
         'slot_usage': {'task_category': {'name': 'task_category', 'required': True}}})

    task_category: TaskCategory = Field(default=..., description="""Category of AI task being addressed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Task']} })
    input_modalities: Optional[list[DataModality]] = Field(default=None, description="""Modalities of input accepted by a task or component.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Task']} })
    output_label_type: Optional[DataLabelType] = Field(default=None, description="""Type of output label produced by a task, when applicable.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Task']} })
    performance_metric: Optional[list[str]] = Field(default=None, description="""Metrics used to evaluate performance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Task']} })
    id: str = Field(default=..., description="""Unique CURIE or URI identifying the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:identifier'} })
    name: str = Field(default=..., description="""Human-readable label for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['dcterms:title', 'schema:name'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Free-text description of the entity (paraphrased; verbatim ISO text excluded).""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:description'} })
    clause_reference: Optional[str] = Field(default=None, description="""ISO/IEC 22989:2022 clause identifier (e.g. \"5.11.4\") the element corresponds to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'AutonomyAssessment',
                       'VerificationValidationFramework']} })
    aliases: Optional[list[str]] = Field(default=None, description="""Alternative names or synonyms for the term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:altLabel'} })
    preferred_label: Optional[str] = Field(default=None, description="""Preferred natural-language label.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:prefLabel'} })
    see_also_uri: Optional[list[str]] = Field(default=None, description="""Pointers to related external resources or term records.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:seeAlso'} })

    @field_validator('clause_reference')
    def pattern_clause_reference(cls, v):
        pattern=re.compile(r"^[0-9]+(\.[0-9]+){0,3}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid clause_reference format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid clause_reference format: {v}"
            raise ValueError(err_msg)
        return v


class Prediction(NamedEntity):
    """
    Prediction produced by an AI model (Clause 7.4.2).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/iso22989',
         'in_subset': ['ai_functional_view']})

    predicted_value: Optional[str] = Field(default=None, description="""Serialised representation of a predicted value (Clause 7.4.2).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Prediction']} })
    confidence: Optional[float] = Field(default=None, description="""Normalised confidence value associated with an output or claim.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Prediction', 'Recommendation']} })
    produced_by: Optional[str] = Field(default=None, description="""Model that produced the prediction.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Prediction']} })
    id: str = Field(default=..., description="""Unique CURIE or URI identifying the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:identifier'} })
    name: str = Field(default=..., description="""Human-readable label for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['dcterms:title', 'schema:name'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Free-text description of the entity (paraphrased; verbatim ISO text excluded).""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:description'} })
    clause_reference: Optional[str] = Field(default=None, description="""ISO/IEC 22989:2022 clause identifier (e.g. \"5.11.4\") the element corresponds to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'AutonomyAssessment',
                       'VerificationValidationFramework']} })
    aliases: Optional[list[str]] = Field(default=None, description="""Alternative names or synonyms for the term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:altLabel'} })
    preferred_label: Optional[str] = Field(default=None, description="""Preferred natural-language label.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:prefLabel'} })
    see_also_uri: Optional[list[str]] = Field(default=None, description="""Pointers to related external resources or term records.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:seeAlso'} })

    @field_validator('clause_reference')
    def pattern_clause_reference(cls, v):
        pattern=re.compile(r"^[0-9]+(\.[0-9]+){0,3}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid clause_reference format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid clause_reference format: {v}"
            raise ValueError(err_msg)
        return v


class Decision(NamedEntity):
    """
    Decision produced by an AI system on the basis of one or more predictions (Clause 7.4.3).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'close_mappings': ['gist_linkml:Determination'],
         'from_schema': 'https://w3id.org/lmodel/iso22989',
         'in_subset': ['ai_functional_view']})

    decision_outcome: Optional[str] = Field(default=None, description="""Chosen course of action resulting from a decision (Clause 7.4.3).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Decision']} })
    decision_policy: Optional[str] = Field(default=None, description="""Policy or rule used to translate predictions into a decision.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Decision']} })
    based_on_predictions: Optional[list[str]] = Field(default=None, description="""Predictions that supported the decision.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Decision', 'Recommendation']} })
    id: str = Field(default=..., description="""Unique CURIE or URI identifying the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:identifier'} })
    name: str = Field(default=..., description="""Human-readable label for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['dcterms:title', 'schema:name'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Free-text description of the entity (paraphrased; verbatim ISO text excluded).""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:description'} })
    clause_reference: Optional[str] = Field(default=None, description="""ISO/IEC 22989:2022 clause identifier (e.g. \"5.11.4\") the element corresponds to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'AutonomyAssessment',
                       'VerificationValidationFramework']} })
    aliases: Optional[list[str]] = Field(default=None, description="""Alternative names or synonyms for the term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:altLabel'} })
    preferred_label: Optional[str] = Field(default=None, description="""Preferred natural-language label.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:prefLabel'} })
    see_also_uri: Optional[list[str]] = Field(default=None, description="""Pointers to related external resources or term records.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:seeAlso'} })

    @field_validator('clause_reference')
    def pattern_clause_reference(cls, v):
        pattern=re.compile(r"^[0-9]+(\.[0-9]+){0,3}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid clause_reference format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid clause_reference format: {v}"
            raise ValueError(err_msg)
        return v


class Action(NamedEntity):
    """
    Action carried out as a result of an AI-system decision (Clause 7.4.4).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'close_mappings': ['gist_linkml:Event'],
         'from_schema': 'https://w3id.org/lmodel/iso22989',
         'in_subset': ['ai_functional_view']})

    action_target: Optional[str] = Field(default=None, description="""Entity or system on which an action is performed (Clause 7.4.4).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Action']} })
    execution_status: Optional[ExecutionStatus] = Field(default=None, description="""Execution status of an action or process.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Action']} })
    triggered_by: Optional[str] = Field(default=None, description="""Decision that triggered the action.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Action']} })
    id: str = Field(default=..., description="""Unique CURIE or URI identifying the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:identifier'} })
    name: str = Field(default=..., description="""Human-readable label for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['dcterms:title', 'schema:name'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Free-text description of the entity (paraphrased; verbatim ISO text excluded).""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:description'} })
    clause_reference: Optional[str] = Field(default=None, description="""ISO/IEC 22989:2022 clause identifier (e.g. \"5.11.4\") the element corresponds to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'AutonomyAssessment',
                       'VerificationValidationFramework']} })
    aliases: Optional[list[str]] = Field(default=None, description="""Alternative names or synonyms for the term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:altLabel'} })
    preferred_label: Optional[str] = Field(default=None, description="""Preferred natural-language label.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:prefLabel'} })
    see_also_uri: Optional[list[str]] = Field(default=None, description="""Pointers to related external resources or term records.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:seeAlso'} })

    @field_validator('clause_reference')
    def pattern_clause_reference(cls, v):
        pattern=re.compile(r"^[0-9]+(\.[0-9]+){0,3}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid clause_reference format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid clause_reference format: {v}"
            raise ValueError(err_msg)
        return v


class InferenceEngine(NamedEntity):
    """
    Component performing inference over a model or knowledge base (Clause 3.1.17).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/iso22989',
         'in_subset': ['ai_functional_view']})

    inference_strategy: Optional[str] = Field(default=None, description="""Inference strategy used (e.g. forward_chaining, backward_chaining, probabilistic).""", json_schema_extra = { "linkml_meta": {'domain_of': ['InferenceEngine', 'Inference']} })
    uses_model: Optional[str] = Field(default=None, description="""Model the inference engine evaluates.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InferenceEngine']} })
    id: str = Field(default=..., description="""Unique CURIE or URI identifying the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:identifier'} })
    name: str = Field(default=..., description="""Human-readable label for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['dcterms:title', 'schema:name'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Free-text description of the entity (paraphrased; verbatim ISO text excluded).""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:description'} })
    clause_reference: Optional[str] = Field(default=None, description="""ISO/IEC 22989:2022 clause identifier (e.g. \"5.11.4\") the element corresponds to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'AutonomyAssessment',
                       'VerificationValidationFramework']} })
    aliases: Optional[list[str]] = Field(default=None, description="""Alternative names or synonyms for the term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:altLabel'} })
    preferred_label: Optional[str] = Field(default=None, description="""Preferred natural-language label.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:prefLabel'} })
    see_also_uri: Optional[list[str]] = Field(default=None, description="""Pointers to related external resources or term records.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:seeAlso'} })

    @field_validator('clause_reference')
    def pattern_clause_reference(cls, v):
        pattern=re.compile(r"^[0-9]+(\.[0-9]+){0,3}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid clause_reference format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid clause_reference format: {v}"
            raise ValueError(err_msg)
        return v


class KnowledgeGraph(KnowledgeRepresentation):
    """
    Graph-structured knowledge representation, often used for reasoning and retrieval (Clause 8.5).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/iso22989',
         'in_subset': ['ai_ecosystem'],
         'related_mappings': ['gist_linkml:KnowledgeConcept']})

    node_count: Optional[int] = Field(default=None, description="""Approximate number of nodes in a graph-structured artefact.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['KnowledgeGraph']} })
    edge_count: Optional[int] = Field(default=None, description="""Approximate number of edges in a graph-structured artefact.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['KnowledgeGraph']} })
    ontology_reference: Optional[list[str]] = Field(default=None, description="""Ontologies referenced by a knowledge artefact.""", json_schema_extra = { "linkml_meta": {'domain_of': ['KnowledgeGraph']} })
    symbolic_approach: Optional[SymbolicApproach] = Field(default=None, description="""Predominant symbolic vs subsymbolic approach used by the system.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIAgent', 'KnowledgeRepresentation', 'AISystem']} })
    knowledge_type: Optional[KnowledgeType] = Field(default=None, description="""Type of knowledge captured (Clause 3.1.12, 3.1.28).""", json_schema_extra = { "linkml_meta": {'domain_of': ['KnowledgeRepresentation']} })
    representation_form: Optional[str] = Field(default=None, description="""Concrete form of representation (rules, frames, ontology, graph, vectors).""", json_schema_extra = { "linkml_meta": {'domain_of': ['KnowledgeRepresentation']} })
    id: str = Field(default=..., description="""Unique CURIE or URI identifying the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:identifier'} })
    name: str = Field(default=..., description="""Human-readable label for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['dcterms:title', 'schema:name'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Free-text description of the entity (paraphrased; verbatim ISO text excluded).""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:description'} })
    clause_reference: Optional[str] = Field(default=None, description="""ISO/IEC 22989:2022 clause identifier (e.g. \"5.11.4\") the element corresponds to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'AutonomyAssessment',
                       'VerificationValidationFramework']} })
    aliases: Optional[list[str]] = Field(default=None, description="""Alternative names or synonyms for the term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:altLabel'} })
    preferred_label: Optional[str] = Field(default=None, description="""Preferred natural-language label.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:prefLabel'} })
    see_also_uri: Optional[list[str]] = Field(default=None, description="""Pointers to related external resources or term records.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:seeAlso'} })

    @field_validator('clause_reference')
    def pattern_clause_reference(cls, v):
        pattern=re.compile(r"^[0-9]+(\.[0-9]+){0,3}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid clause_reference format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid clause_reference format: {v}"
            raise ValueError(err_msg)
        return v


class ExpertSystem(NamedEntity):
    """
    Rule-based system encoding domain expertise (Clause 8.5.2).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/iso22989',
         'in_subset': ['ai_ecosystem']})

    rule_count: Optional[int] = Field(default=None, description="""Approximate count of rules in a rule-based knowledge base.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['ExpertSystem']} })
    inference_engine: Optional[InferenceEngine] = Field(default=None, description="""Inference engine used by the expert system.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExpertSystem']} })
    id: str = Field(default=..., description="""Unique CURIE or URI identifying the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:identifier'} })
    name: str = Field(default=..., description="""Human-readable label for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['dcterms:title', 'schema:name'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Free-text description of the entity (paraphrased; verbatim ISO text excluded).""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:description'} })
    clause_reference: Optional[str] = Field(default=None, description="""ISO/IEC 22989:2022 clause identifier (e.g. \"5.11.4\") the element corresponds to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'AutonomyAssessment',
                       'VerificationValidationFramework']} })
    aliases: Optional[list[str]] = Field(default=None, description="""Alternative names or synonyms for the term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:altLabel'} })
    preferred_label: Optional[str] = Field(default=None, description="""Preferred natural-language label.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:prefLabel'} })
    see_also_uri: Optional[list[str]] = Field(default=None, description="""Pointers to related external resources or term records.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:seeAlso'} })

    @field_validator('clause_reference')
    def pattern_clause_reference(cls, v):
        pattern=re.compile(r"^[0-9]+(\.[0-9]+){0,3}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid clause_reference format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid clause_reference format: {v}"
            raise ValueError(err_msg)
        return v


class CognitiveComputingSystem(AIConcept):
    """
    System combining AI techniques to emulate human cognitive functions (Clause 5.5).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/iso22989'})

    cognitive_capabilities: Optional[list[str]] = Field(default=None, description="""Cognitive capabilities the system provides (e.g. perception, reasoning, learning).""", json_schema_extra = { "linkml_meta": {'domain_of': ['CognitiveComputingSystem']} })
    id: str = Field(default=..., description="""Unique CURIE or URI identifying the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:identifier'} })
    name: str = Field(default=..., description="""Human-readable label for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['dcterms:title', 'schema:name'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Free-text description of the entity (paraphrased; verbatim ISO text excluded).""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:description'} })
    clause_reference: Optional[str] = Field(default=None, description="""ISO/IEC 22989:2022 clause identifier (e.g. \"5.11.4\") the element corresponds to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'AutonomyAssessment',
                       'VerificationValidationFramework']} })
    aliases: Optional[list[str]] = Field(default=None, description="""Alternative names or synonyms for the term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:altLabel'} })
    preferred_label: Optional[str] = Field(default=None, description="""Preferred natural-language label.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:prefLabel'} })
    see_also_uri: Optional[list[str]] = Field(default=None, description="""Pointers to related external resources or term records.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:seeAlso'} })

    @field_validator('clause_reference')
    def pattern_clause_reference(cls, v):
        pattern=re.compile(r"^[0-9]+(\.[0-9]+){0,3}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid clause_reference format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid clause_reference format: {v}"
            raise ValueError(err_msg)
        return v


class SemanticComputingSystem(AIConcept):
    """
    System whose behaviour is driven by the explicit semantics of its inputs and knowledge sources (Clause 5.6).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/iso22989'})

    semantic_model: Optional[str] = Field(default=None, description="""Reference to the semantic model or ontology used.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SemanticComputingSystem']} })
    id: str = Field(default=..., description="""Unique CURIE or URI identifying the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:identifier'} })
    name: str = Field(default=..., description="""Human-readable label for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['dcterms:title', 'schema:name'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Free-text description of the entity (paraphrased; verbatim ISO text excluded).""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:description'} })
    clause_reference: Optional[str] = Field(default=None, description="""ISO/IEC 22989:2022 clause identifier (e.g. \"5.11.4\") the element corresponds to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'AutonomyAssessment',
                       'VerificationValidationFramework']} })
    aliases: Optional[list[str]] = Field(default=None, description="""Alternative names or synonyms for the term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:altLabel'} })
    preferred_label: Optional[str] = Field(default=None, description="""Preferred natural-language label.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:prefLabel'} })
    see_also_uri: Optional[list[str]] = Field(default=None, description="""Pointers to related external resources or term records.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:seeAlso'} })

    @field_validator('clause_reference')
    def pattern_clause_reference(cls, v):
        pattern=re.compile(r"^[0-9]+(\.[0-9]+){0,3}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid clause_reference format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid clause_reference format: {v}"
            raise ValueError(err_msg)
        return v


class SoftComputingSystem(AIConcept):
    """
    System employing soft computing techniques tolerant of imprecision and uncertainty (Clause 5.7).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/iso22989'})

    soft_computing_techniques: list[SoftComputingTechnique] = Field(default=..., description="""Soft-computing techniques the system employs.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SoftComputingSystem']} })
    id: str = Field(default=..., description="""Unique CURIE or URI identifying the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:identifier'} })
    name: str = Field(default=..., description="""Human-readable label for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['dcterms:title', 'schema:name'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Free-text description of the entity (paraphrased; verbatim ISO text excluded).""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:description'} })
    clause_reference: Optional[str] = Field(default=None, description="""ISO/IEC 22989:2022 clause identifier (e.g. \"5.11.4\") the element corresponds to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'AutonomyAssessment',
                       'VerificationValidationFramework']} })
    aliases: Optional[list[str]] = Field(default=None, description="""Alternative names or synonyms for the term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:altLabel'} })
    preferred_label: Optional[str] = Field(default=None, description="""Preferred natural-language label.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:prefLabel'} })
    see_also_uri: Optional[list[str]] = Field(default=None, description="""Pointers to related external resources or term records.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:seeAlso'} })

    @field_validator('clause_reference')
    def pattern_clause_reference(cls, v):
        pattern=re.compile(r"^[0-9]+(\.[0-9]+){0,3}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid clause_reference format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid clause_reference format: {v}"
            raise ValueError(err_msg)
        return v


class DataProcess(NamedEntity):
    """
    Discrete data-handling process applied to a dataset during AI system development or operation (Clause 5.10).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['gist_linkml:Event'],
         'close_mappings': ['nist_ai_100_1:AiSystemDimensionEnum#DATA_AND_INPUT'],
         'from_schema': 'https://w3id.org/lmodel/iso22989',
         'in_subset': ['ai_functional_view'],
         'related_mappings': ['iso29100:PIIProcessingActivity']})

    process_type: DataProcessType = Field(default=..., description="""Type of data-handling process performed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DataProcess']} })
    input_dataset: Optional[str] = Field(default=None, description="""Dataset consumed by the process.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DataProcess']} })
    output_dataset: Optional[str] = Field(default=None, description="""Dataset produced by the process.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DataProcess']} })
    parameters: Optional[list[str]] = Field(default=None, description="""Free-form parameters configuring the process.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DataProcess']} })
    executed_by: Optional[str] = Field(default=None, description="""Stakeholder role that executed the process.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DataProcess']} })
    id: str = Field(default=..., description="""Unique CURIE or URI identifying the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:identifier'} })
    name: str = Field(default=..., description="""Human-readable label for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['dcterms:title', 'schema:name'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Free-text description of the entity (paraphrased; verbatim ISO text excluded).""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:description'} })
    clause_reference: Optional[str] = Field(default=None, description="""ISO/IEC 22989:2022 clause identifier (e.g. \"5.11.4\") the element corresponds to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'AutonomyAssessment',
                       'VerificationValidationFramework']} })
    aliases: Optional[list[str]] = Field(default=None, description="""Alternative names or synonyms for the term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:altLabel'} })
    preferred_label: Optional[str] = Field(default=None, description="""Preferred natural-language label.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:prefLabel'} })
    see_also_uri: Optional[list[str]] = Field(default=None, description="""Pointers to related external resources or term records.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:seeAlso'} })

    @field_validator('clause_reference')
    def pattern_clause_reference(cls, v):
        pattern=re.compile(r"^[0-9]+(\.[0-9]+){0,3}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid clause_reference format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid clause_reference format: {v}"
            raise ValueError(err_msg)
        return v


class DataSample(NamedEntity):
    """
    Individual data record within a dataset (Clause 3.2.13).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/iso22989',
         'in_subset': ['terminology']})

    sample_payload: Optional[str] = Field(default=None, description="""Serialised representation of the sample contents.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DataSample']} })
    sample_label: Optional[str] = Field(default=None, description="""Label or target value associated with the sample.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DataSample']} })
    id: str = Field(default=..., description="""Unique CURIE or URI identifying the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:identifier'} })
    name: str = Field(default=..., description="""Human-readable label for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['dcterms:title', 'schema:name'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Free-text description of the entity (paraphrased; verbatim ISO text excluded).""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:description'} })
    clause_reference: Optional[str] = Field(default=None, description="""ISO/IEC 22989:2022 clause identifier (e.g. \"5.11.4\") the element corresponds to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'AutonomyAssessment',
                       'VerificationValidationFramework']} })
    aliases: Optional[list[str]] = Field(default=None, description="""Alternative names or synonyms for the term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:altLabel'} })
    preferred_label: Optional[str] = Field(default=None, description="""Preferred natural-language label.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:prefLabel'} })
    see_also_uri: Optional[list[str]] = Field(default=None, description="""Pointers to related external resources or term records.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:seeAlso'} })

    @field_validator('clause_reference')
    def pattern_clause_reference(cls, v):
        pattern=re.compile(r"^[0-9]+(\.[0-9]+){0,3}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid clause_reference format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid clause_reference format: {v}"
            raise ValueError(err_msg)
        return v


class DataLabel(NamedEntity):
    """
    Label or annotation attached to one or more data samples (Clause 3.2.10).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/iso22989',
         'in_subset': ['terminology'],
         'slot_usage': {'label_value': {'name': 'label_value', 'required': True}}})

    label_value: str = Field(default=..., description="""Concrete label value.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DataLabel']} })
    label_type: Optional[DataLabelType] = Field(default=None, description="""Type of target label associated with a dataset, sample or annotation (Clause 3.2.10).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset', 'DataLabel']} })
    annotator: Optional[str] = Field(default=None, description="""Role of the party that produced the label.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DataLabel']} })
    id: str = Field(default=..., description="""Unique CURIE or URI identifying the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:identifier'} })
    name: str = Field(default=..., description="""Human-readable label for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['dcterms:title', 'schema:name'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Free-text description of the entity (paraphrased; verbatim ISO text excluded).""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:description'} })
    clause_reference: Optional[str] = Field(default=None, description="""ISO/IEC 22989:2022 clause identifier (e.g. \"5.11.4\") the element corresponds to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'AutonomyAssessment',
                       'VerificationValidationFramework']} })
    aliases: Optional[list[str]] = Field(default=None, description="""Alternative names or synonyms for the term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:altLabel'} })
    preferred_label: Optional[str] = Field(default=None, description="""Preferred natural-language label.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:prefLabel'} })
    see_also_uri: Optional[list[str]] = Field(default=None, description="""Pointers to related external resources or term records.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:seeAlso'} })

    @field_validator('clause_reference')
    def pattern_clause_reference(cls, v):
        pattern=re.compile(r"^[0-9]+(\.[0-9]+){0,3}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid clause_reference format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid clause_reference format: {v}"
            raise ValueError(err_msg)
        return v


class GroundTruthRecord(NamedEntity):
    """
    Trusted reference record used to evaluate or train an AI model (Clause 3.2.7).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/iso22989',
         'in_subset': ['terminology'],
         'slot_usage': {'ground_truth_value': {'name': 'ground_truth_value',
                                               'required': True}}})

    ground_truth_value: str = Field(default=..., description="""Trusted reference value (Clause 3.2.7).""", json_schema_extra = { "linkml_meta": {'domain_of': ['GroundTruthRecord']} })
    provenance_statement: Optional[str] = Field(default=None, description="""Provenance description for an artefact.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GroundTruthRecord'], 'slot_uri': 'prov:wasDerivedFrom'} })
    id: str = Field(default=..., description="""Unique CURIE or URI identifying the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:identifier'} })
    name: str = Field(default=..., description="""Human-readable label for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['dcterms:title', 'schema:name'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Free-text description of the entity (paraphrased; verbatim ISO text excluded).""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:description'} })
    clause_reference: Optional[str] = Field(default=None, description="""ISO/IEC 22989:2022 clause identifier (e.g. \"5.11.4\") the element corresponds to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'AutonomyAssessment',
                       'VerificationValidationFramework']} })
    aliases: Optional[list[str]] = Field(default=None, description="""Alternative names or synonyms for the term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:altLabel'} })
    preferred_label: Optional[str] = Field(default=None, description="""Preferred natural-language label.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:prefLabel'} })
    see_also_uri: Optional[list[str]] = Field(default=None, description="""Pointers to related external resources or term records.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:seeAlso'} })

    @field_validator('clause_reference')
    def pattern_clause_reference(cls, v):
        pattern=re.compile(r"^[0-9]+(\.[0-9]+){0,3}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid clause_reference format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid clause_reference format: {v}"
            raise ValueError(err_msg)
        return v


class Robot(NamedEntity):
    """
    Embodied agent able to perceive its environment and act in the physical world (Clause 5.3 / Clause 9.5 robotics field).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/iso22989',
         'in_subset': ['ai_concepts']})

    embodiment: Optional[str] = Field(default=None, description="""Free-text description of the physical embodiment.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Robot']} })
    controlled_by: Optional[str] = Field(default=None, description="""AI system that controls the robot.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Robot']} })
    id: str = Field(default=..., description="""Unique CURIE or URI identifying the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:identifier'} })
    name: str = Field(default=..., description="""Human-readable label for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['dcterms:title', 'schema:name'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Free-text description of the entity (paraphrased; verbatim ISO text excluded).""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:description'} })
    clause_reference: Optional[str] = Field(default=None, description="""ISO/IEC 22989:2022 clause identifier (e.g. \"5.11.4\") the element corresponds to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'AutonomyAssessment',
                       'VerificationValidationFramework']} })
    aliases: Optional[list[str]] = Field(default=None, description="""Alternative names or synonyms for the term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:altLabel'} })
    preferred_label: Optional[str] = Field(default=None, description="""Preferred natural-language label.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:prefLabel'} })
    see_also_uri: Optional[list[str]] = Field(default=None, description="""Pointers to related external resources or term records.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:seeAlso'} })

    @field_validator('clause_reference')
    def pattern_clause_reference(cls, v):
        pattern=re.compile(r"^[0-9]+(\.[0-9]+){0,3}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid clause_reference format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid clause_reference format: {v}"
            raise ValueError(err_msg)
        return v


class IoTDevice(NamedEntity):
    """
    Device participating in an Internet-of-Things deployment (Clause 5.14.2).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/iso22989',
         'in_subset': ['ai_ecosystem'],
         'slot_usage': {'device_role': {'name': 'device_role', 'required': True}}})

    device_role: IoTDeviceRole = Field(default=..., description="""Role played by a device in an IoT or cyber-physical system (Clause 5.14.2).""", json_schema_extra = { "linkml_meta": {'domain_of': ['IoTDevice']} })
    sensing_capabilities: Optional[list[str]] = Field(default=None, description="""Sensing capabilities of the device.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IoTDevice']} })
    actuating_capabilities: Optional[list[str]] = Field(default=None, description="""Actuating capabilities of the device.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IoTDevice']} })
    id: str = Field(default=..., description="""Unique CURIE or URI identifying the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:identifier'} })
    name: str = Field(default=..., description="""Human-readable label for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['dcterms:title', 'schema:name'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Free-text description of the entity (paraphrased; verbatim ISO text excluded).""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:description'} })
    clause_reference: Optional[str] = Field(default=None, description="""ISO/IEC 22989:2022 clause identifier (e.g. \"5.11.4\") the element corresponds to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'AutonomyAssessment',
                       'VerificationValidationFramework']} })
    aliases: Optional[list[str]] = Field(default=None, description="""Alternative names or synonyms for the term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:altLabel'} })
    preferred_label: Optional[str] = Field(default=None, description="""Preferred natural-language label.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:prefLabel'} })
    see_also_uri: Optional[list[str]] = Field(default=None, description="""Pointers to related external resources or term records.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:seeAlso'} })

    @field_validator('clause_reference')
    def pattern_clause_reference(cls, v):
        pattern=re.compile(r"^[0-9]+(\.[0-9]+){0,3}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid clause_reference format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid clause_reference format: {v}"
            raise ValueError(err_msg)
        return v


class IoTSystem(NamedEntity):
    """
    Networked system composed of IoT devices, possibly enhanced with AI capabilities (Clause 5.14.2).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/iso22989',
         'in_subset': ['ai_ecosystem']})

    devices: Optional[list[IoTDevice]] = Field(default=None, description="""Devices that make up the IoT system.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IoTSystem']} })
    ai_components: Optional[list[str]] = Field(default=None, description="""AI components that operate within the IoT system.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IoTSystem']} })
    id: str = Field(default=..., description="""Unique CURIE or URI identifying the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:identifier'} })
    name: str = Field(default=..., description="""Human-readable label for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['dcterms:title', 'schema:name'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Free-text description of the entity (paraphrased; verbatim ISO text excluded).""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:description'} })
    clause_reference: Optional[str] = Field(default=None, description="""ISO/IEC 22989:2022 clause identifier (e.g. \"5.11.4\") the element corresponds to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'AutonomyAssessment',
                       'VerificationValidationFramework']} })
    aliases: Optional[list[str]] = Field(default=None, description="""Alternative names or synonyms for the term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:altLabel'} })
    preferred_label: Optional[str] = Field(default=None, description="""Preferred natural-language label.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:prefLabel'} })
    see_also_uri: Optional[list[str]] = Field(default=None, description="""Pointers to related external resources or term records.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:seeAlso'} })

    @field_validator('clause_reference')
    def pattern_clause_reference(cls, v):
        pattern=re.compile(r"^[0-9]+(\.[0-9]+){0,3}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid clause_reference format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid clause_reference format: {v}"
            raise ValueError(err_msg)
        return v


class CyberPhysicalSystem(NamedEntity):
    """
    System that tightly integrates computational and physical components, typically with feedback loops between sensing and actuation (Clause 5.14.3).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/iso22989',
         'in_subset': ['ai_ecosystem']})

    physical_processes: Optional[list[str]] = Field(default=None, description="""Physical processes the system monitors or controls.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CyberPhysicalSystem']} })
    cyber_components: Optional[list[str]] = Field(default=None, description="""Computational components participating in the system.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CyberPhysicalSystem']} })
    iot_subsystem: Optional[str] = Field(default=None, description="""IoT subsystem the CPS relies on, if any.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CyberPhysicalSystem']} })
    id: str = Field(default=..., description="""Unique CURIE or URI identifying the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:identifier'} })
    name: str = Field(default=..., description="""Human-readable label for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['dcterms:title', 'schema:name'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Free-text description of the entity (paraphrased; verbatim ISO text excluded).""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:description'} })
    clause_reference: Optional[str] = Field(default=None, description="""ISO/IEC 22989:2022 clause identifier (e.g. \"5.11.4\") the element corresponds to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'AutonomyAssessment',
                       'VerificationValidationFramework']} })
    aliases: Optional[list[str]] = Field(default=None, description="""Alternative names or synonyms for the term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:altLabel'} })
    preferred_label: Optional[str] = Field(default=None, description="""Preferred natural-language label.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:prefLabel'} })
    see_also_uri: Optional[list[str]] = Field(default=None, description="""Pointers to related external resources or term records.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:seeAlso'} })

    @field_validator('clause_reference')
    def pattern_clause_reference(cls, v):
        pattern=re.compile(r"^[0-9]+(\.[0-9]+){0,3}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid clause_reference format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid clause_reference format: {v}"
            raise ValueError(err_msg)
        return v


class AbbreviationEntry(NamedEntity):
    """
    Record of a single abbreviation listed in Clause 4 of the standard.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/iso22989',
         'in_subset': ['terminology'],
         'slot_usage': {'abbreviation_code': {'name': 'abbreviation_code',
                                              'required': True},
                        'expansion': {'name': 'expansion', 'required': True}}})

    abbreviation_code: AbbreviationCode = Field(default=..., description="""Acronym or abbreviation code (Clause 4).""", json_schema_extra = { "linkml_meta": {'domain_of': ['AbbreviationEntry']} })
    expansion: str = Field(default=..., description="""Expanded form of an abbreviation (Clause 4).""", json_schema_extra = { "linkml_meta": {'domain_of': ['AbbreviatedTerm', 'AbbreviationEntry']} })
    id: str = Field(default=..., description="""Unique CURIE or URI identifying the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:identifier'} })
    name: str = Field(default=..., description="""Human-readable label for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['dcterms:title', 'schema:name'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Free-text description of the entity (paraphrased; verbatim ISO text excluded).""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:description'} })
    clause_reference: Optional[str] = Field(default=None, description="""ISO/IEC 22989:2022 clause identifier (e.g. \"5.11.4\") the element corresponds to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'AutonomyAssessment',
                       'VerificationValidationFramework']} })
    aliases: Optional[list[str]] = Field(default=None, description="""Alternative names or synonyms for the term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:altLabel'} })
    preferred_label: Optional[str] = Field(default=None, description="""Preferred natural-language label.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:prefLabel'} })
    see_also_uri: Optional[list[str]] = Field(default=None, description="""Pointers to related external resources or term records.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:seeAlso'} })

    @field_validator('clause_reference')
    def pattern_clause_reference(cls, v):
        pattern=re.compile(r"^[0-9]+(\.[0-9]+){0,3}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid clause_reference format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid clause_reference format: {v}"
            raise ValueError(err_msg)
        return v


class AIConceptsCollection(ConfiguredBaseModel):
    """
    Top-level container aggregating AI systems, models, datasets, lifecycle processes, stakeholder roles, applications and trustworthiness records for serialisation as a single artefact.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/iso22989', 'tree_root': True})

    ai_systems: Optional[list[AISystem]] = Field(default=None, description="""AI systems documented in the collection.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIEcosystem', 'AIConceptsCollection']} })
    ai_models: Optional[list[AIModel]] = Field(default=None, description="""Trained or knowledge-based models in the collection.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIConceptsCollection']} })
    ai_datasets: Optional[list[Dataset]] = Field(default=None, description="""Datasets referenced by entities in the collection.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIConceptsCollection']} })
    ai_lifecycle_processes: Optional[list[AILifecycleProcess]] = Field(default=None, description="""Life-cycle process records in the collection.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIConceptsCollection']} })
    ai_stakeholder_roles: Optional[list[AIStakeholderRole]] = Field(default=None, description="""Stakeholder role records in the collection.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIEcosystem', 'AIConceptsCollection']} })
    ai_applications: Optional[list[AIApplication]] = Field(default=None, description="""AI application records in the collection.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIConceptsCollection']} })
    trustworthiness_records: Optional[list[TrustworthinessProperty]] = Field(default=None, description="""Trustworthiness property claims documented in the collection.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIConceptsCollection']} })
    tasks: Optional[list[Task]] = Field(default=None, description="""Task records in the collection.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIConceptsCollection']} })
    data_processes: Optional[list[DataProcess]] = Field(default=None, description="""Data-handling process records in the collection.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AISystem', 'AIConceptsCollection']} })
    iot_systems: Optional[list[IoTSystem]] = Field(default=None, description="""IoT system records in the collection.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIConceptsCollection']} })
    cyber_physical_systems: Optional[list[CyberPhysicalSystem]] = Field(default=None, description="""Cyber-physical system records in the collection.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIConceptsCollection']} })
    knowledge_graphs: Optional[list[KnowledgeGraph]] = Field(default=None, description="""Knowledge-graph records in the collection.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIConceptsCollection']} })
    expert_systems: Optional[list[ExpertSystem]] = Field(default=None, description="""Expert-system records in the collection.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIConceptsCollection']} })
    abbreviations: Optional[list[AbbreviationEntry]] = Field(default=None, description="""Clause 4 abbreviation records.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIConceptsCollection']} })


class AIPlatformProvider(AIProvider):
    """
    Provider of platform infrastructure on which AI services are operated (Clause 5.19.2).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/iso22989'})

    stakeholder_role_type: AIStakeholderRoleType = Field(default=AIStakeholderRoleType.ai_provider, description="""Canonical stakeholder role type as defined in Clause 5.19.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIStakeholderRole'],
         'ifabsent': 'AIStakeholderRoleType(ai_provider)'} })
    organization_name: Optional[str] = Field(default=None, description="""Name of the organisation acting in the stakeholder role.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIStakeholderRole']} })
    contact: Optional[str] = Field(default=None, description="""Contact identifier (e.g. email) for the stakeholder.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIStakeholderRole']} })
    responsibilities: Optional[list[str]] = Field(default=None, description="""Free-text statements of responsibility.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIStakeholderRole']} })
    id: str = Field(default=..., description="""Unique CURIE or URI identifying the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:identifier'} })
    name: str = Field(default=..., description="""Human-readable label for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['dcterms:title', 'schema:name'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Free-text description of the entity (paraphrased; verbatim ISO text excluded).""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:description'} })
    clause_reference: Optional[str] = Field(default=None, description="""ISO/IEC 22989:2022 clause identifier (e.g. \"5.11.4\") the element corresponds to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'AutonomyAssessment',
                       'VerificationValidationFramework']} })
    aliases: Optional[list[str]] = Field(default=None, description="""Alternative names or synonyms for the term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:altLabel'} })
    preferred_label: Optional[str] = Field(default=None, description="""Preferred natural-language label.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:prefLabel'} })
    see_also_uri: Optional[list[str]] = Field(default=None, description="""Pointers to related external resources or term records.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:seeAlso'} })

    @field_validator('clause_reference')
    def pattern_clause_reference(cls, v):
        pattern=re.compile(r"^[0-9]+(\.[0-9]+){0,3}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid clause_reference format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid clause_reference format: {v}"
            raise ValueError(err_msg)
        return v


class AIServiceProductProvider(AIProvider):
    """
    Provider of an AI-enabled service or product to customers (Clause 5.19.2).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/iso22989'})

    stakeholder_role_type: AIStakeholderRoleType = Field(default=AIStakeholderRoleType.ai_provider, description="""Canonical stakeholder role type as defined in Clause 5.19.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIStakeholderRole'],
         'ifabsent': 'AIStakeholderRoleType(ai_provider)'} })
    organization_name: Optional[str] = Field(default=None, description="""Name of the organisation acting in the stakeholder role.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIStakeholderRole']} })
    contact: Optional[str] = Field(default=None, description="""Contact identifier (e.g. email) for the stakeholder.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIStakeholderRole']} })
    responsibilities: Optional[list[str]] = Field(default=None, description="""Free-text statements of responsibility.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIStakeholderRole']} })
    id: str = Field(default=..., description="""Unique CURIE or URI identifying the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:identifier'} })
    name: str = Field(default=..., description="""Human-readable label for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['dcterms:title', 'schema:name'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Free-text description of the entity (paraphrased; verbatim ISO text excluded).""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:description'} })
    clause_reference: Optional[str] = Field(default=None, description="""ISO/IEC 22989:2022 clause identifier (e.g. \"5.11.4\") the element corresponds to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'AutonomyAssessment',
                       'VerificationValidationFramework']} })
    aliases: Optional[list[str]] = Field(default=None, description="""Alternative names or synonyms for the term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:altLabel'} })
    preferred_label: Optional[str] = Field(default=None, description="""Preferred natural-language label.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:prefLabel'} })
    see_also_uri: Optional[list[str]] = Field(default=None, description="""Pointers to related external resources or term records.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:seeAlso'} })

    @field_validator('clause_reference')
    def pattern_clause_reference(cls, v):
        pattern=re.compile(r"^[0-9]+(\.[0-9]+){0,3}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid clause_reference format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid clause_reference format: {v}"
            raise ValueError(err_msg)
        return v


class ModelDesigner(AIProducer):
    """
    Producer role responsible for designing AI models (Clause 5.19.3).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/iso22989'})

    stakeholder_role_type: AIStakeholderRoleType = Field(default=AIStakeholderRoleType.ai_producer, description="""Canonical stakeholder role type as defined in Clause 5.19.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIStakeholderRole'],
         'ifabsent': 'AIStakeholderRoleType(ai_producer)'} })
    organization_name: Optional[str] = Field(default=None, description="""Name of the organisation acting in the stakeholder role.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIStakeholderRole']} })
    contact: Optional[str] = Field(default=None, description="""Contact identifier (e.g. email) for the stakeholder.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIStakeholderRole']} })
    responsibilities: Optional[list[str]] = Field(default=None, description="""Free-text statements of responsibility.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIStakeholderRole']} })
    id: str = Field(default=..., description="""Unique CURIE or URI identifying the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:identifier'} })
    name: str = Field(default=..., description="""Human-readable label for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['dcterms:title', 'schema:name'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Free-text description of the entity (paraphrased; verbatim ISO text excluded).""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:description'} })
    clause_reference: Optional[str] = Field(default=None, description="""ISO/IEC 22989:2022 clause identifier (e.g. \"5.11.4\") the element corresponds to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'AutonomyAssessment',
                       'VerificationValidationFramework']} })
    aliases: Optional[list[str]] = Field(default=None, description="""Alternative names or synonyms for the term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:altLabel'} })
    preferred_label: Optional[str] = Field(default=None, description="""Preferred natural-language label.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:prefLabel'} })
    see_also_uri: Optional[list[str]] = Field(default=None, description="""Pointers to related external resources or term records.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:seeAlso'} })

    @field_validator('clause_reference')
    def pattern_clause_reference(cls, v):
        pattern=re.compile(r"^[0-9]+(\.[0-9]+){0,3}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid clause_reference format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid clause_reference format: {v}"
            raise ValueError(err_msg)
        return v


class ModelImplementer(AIProducer):
    """
    Producer role responsible for implementing AI models in code (Clause 5.19.3).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/iso22989'})

    stakeholder_role_type: AIStakeholderRoleType = Field(default=AIStakeholderRoleType.ai_producer, description="""Canonical stakeholder role type as defined in Clause 5.19.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIStakeholderRole'],
         'ifabsent': 'AIStakeholderRoleType(ai_producer)'} })
    organization_name: Optional[str] = Field(default=None, description="""Name of the organisation acting in the stakeholder role.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIStakeholderRole']} })
    contact: Optional[str] = Field(default=None, description="""Contact identifier (e.g. email) for the stakeholder.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIStakeholderRole']} })
    responsibilities: Optional[list[str]] = Field(default=None, description="""Free-text statements of responsibility.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIStakeholderRole']} })
    id: str = Field(default=..., description="""Unique CURIE or URI identifying the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:identifier'} })
    name: str = Field(default=..., description="""Human-readable label for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['dcterms:title', 'schema:name'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Free-text description of the entity (paraphrased; verbatim ISO text excluded).""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:description'} })
    clause_reference: Optional[str] = Field(default=None, description="""ISO/IEC 22989:2022 clause identifier (e.g. \"5.11.4\") the element corresponds to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'AutonomyAssessment',
                       'VerificationValidationFramework']} })
    aliases: Optional[list[str]] = Field(default=None, description="""Alternative names or synonyms for the term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:altLabel'} })
    preferred_label: Optional[str] = Field(default=None, description="""Preferred natural-language label.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:prefLabel'} })
    see_also_uri: Optional[list[str]] = Field(default=None, description="""Pointers to related external resources or term records.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:seeAlso'} })

    @field_validator('clause_reference')
    def pattern_clause_reference(cls, v):
        pattern=re.compile(r"^[0-9]+(\.[0-9]+){0,3}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid clause_reference format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid clause_reference format: {v}"
            raise ValueError(err_msg)
        return v


class ComputationVerifier(AIProducer):
    """
    Producer role verifying the computational behaviour of an AI system (Clause 5.19.3).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/iso22989'})

    stakeholder_role_type: AIStakeholderRoleType = Field(default=AIStakeholderRoleType.ai_producer, description="""Canonical stakeholder role type as defined in Clause 5.19.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIStakeholderRole'],
         'ifabsent': 'AIStakeholderRoleType(ai_producer)'} })
    organization_name: Optional[str] = Field(default=None, description="""Name of the organisation acting in the stakeholder role.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIStakeholderRole']} })
    contact: Optional[str] = Field(default=None, description="""Contact identifier (e.g. email) for the stakeholder.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIStakeholderRole']} })
    responsibilities: Optional[list[str]] = Field(default=None, description="""Free-text statements of responsibility.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIStakeholderRole']} })
    id: str = Field(default=..., description="""Unique CURIE or URI identifying the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:identifier'} })
    name: str = Field(default=..., description="""Human-readable label for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['dcterms:title', 'schema:name'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Free-text description of the entity (paraphrased; verbatim ISO text excluded).""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:description'} })
    clause_reference: Optional[str] = Field(default=None, description="""ISO/IEC 22989:2022 clause identifier (e.g. \"5.11.4\") the element corresponds to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'AutonomyAssessment',
                       'VerificationValidationFramework']} })
    aliases: Optional[list[str]] = Field(default=None, description="""Alternative names or synonyms for the term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:altLabel'} })
    preferred_label: Optional[str] = Field(default=None, description="""Preferred natural-language label.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:prefLabel'} })
    see_also_uri: Optional[list[str]] = Field(default=None, description="""Pointers to related external resources or term records.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:seeAlso'} })

    @field_validator('clause_reference')
    def pattern_clause_reference(cls, v):
        pattern=re.compile(r"^[0-9]+(\.[0-9]+){0,3}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid clause_reference format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid clause_reference format: {v}"
            raise ValueError(err_msg)
        return v


class ModelVerifier(AIProducer):
    """
    Producer role verifying that models meet specified requirements (Clause 5.19.3).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/iso22989'})

    stakeholder_role_type: AIStakeholderRoleType = Field(default=AIStakeholderRoleType.ai_producer, description="""Canonical stakeholder role type as defined in Clause 5.19.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIStakeholderRole'],
         'ifabsent': 'AIStakeholderRoleType(ai_producer)'} })
    organization_name: Optional[str] = Field(default=None, description="""Name of the organisation acting in the stakeholder role.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIStakeholderRole']} })
    contact: Optional[str] = Field(default=None, description="""Contact identifier (e.g. email) for the stakeholder.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIStakeholderRole']} })
    responsibilities: Optional[list[str]] = Field(default=None, description="""Free-text statements of responsibility.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIStakeholderRole']} })
    id: str = Field(default=..., description="""Unique CURIE or URI identifying the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:identifier'} })
    name: str = Field(default=..., description="""Human-readable label for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['dcterms:title', 'schema:name'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Free-text description of the entity (paraphrased; verbatim ISO text excluded).""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:description'} })
    clause_reference: Optional[str] = Field(default=None, description="""ISO/IEC 22989:2022 clause identifier (e.g. \"5.11.4\") the element corresponds to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'AutonomyAssessment',
                       'VerificationValidationFramework']} })
    aliases: Optional[list[str]] = Field(default=None, description="""Alternative names or synonyms for the term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:altLabel'} })
    preferred_label: Optional[str] = Field(default=None, description="""Preferred natural-language label.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:prefLabel'} })
    see_also_uri: Optional[list[str]] = Field(default=None, description="""Pointers to related external resources or term records.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:seeAlso'} })

    @field_validator('clause_reference')
    def pattern_clause_reference(cls, v):
        pattern=re.compile(r"^[0-9]+(\.[0-9]+){0,3}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid clause_reference format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid clause_reference format: {v}"
            raise ValueError(err_msg)
        return v


class AIUser(AICustomer):
    """
    End user of an AI system or AI-backed service (Clause 5.19.4).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'close_mappings': ['gist_linkml:Person'],
         'exact_mappings': ['nist_ai_100_1:AiActorTaskEnum#END_USERS',
                            'nist_ai_600_1:GaiActorTaskEnum#END_USERS'],
         'from_schema': 'https://w3id.org/lmodel/iso22989'})

    stakeholder_role_type: AIStakeholderRoleType = Field(default=AIStakeholderRoleType.ai_customer, description="""Canonical stakeholder role type as defined in Clause 5.19.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIStakeholderRole'],
         'ifabsent': 'AIStakeholderRoleType(ai_customer)'} })
    organization_name: Optional[str] = Field(default=None, description="""Name of the organisation acting in the stakeholder role.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIStakeholderRole']} })
    contact: Optional[str] = Field(default=None, description="""Contact identifier (e.g. email) for the stakeholder.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIStakeholderRole']} })
    responsibilities: Optional[list[str]] = Field(default=None, description="""Free-text statements of responsibility.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIStakeholderRole']} })
    id: str = Field(default=..., description="""Unique CURIE or URI identifying the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:identifier'} })
    name: str = Field(default=..., description="""Human-readable label for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['dcterms:title', 'schema:name'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Free-text description of the entity (paraphrased; verbatim ISO text excluded).""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:description'} })
    clause_reference: Optional[str] = Field(default=None, description="""ISO/IEC 22989:2022 clause identifier (e.g. \"5.11.4\") the element corresponds to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'AutonomyAssessment',
                       'VerificationValidationFramework']} })
    aliases: Optional[list[str]] = Field(default=None, description="""Alternative names or synonyms for the term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:altLabel'} })
    preferred_label: Optional[str] = Field(default=None, description="""Preferred natural-language label.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:prefLabel'} })
    see_also_uri: Optional[list[str]] = Field(default=None, description="""Pointers to related external resources or term records.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:seeAlso'} })

    @field_validator('clause_reference')
    def pattern_clause_reference(cls, v):
        pattern=re.compile(r"^[0-9]+(\.[0-9]+){0,3}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid clause_reference format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid clause_reference format: {v}"
            raise ValueError(err_msg)
        return v


class AISystemIntegrator(AIPartner):
    """
    Partner integrating AI components into a wider system (Clause 5.19.5).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/iso22989'})

    stakeholder_role_type: AIStakeholderRoleType = Field(default=AIStakeholderRoleType.ai_partner, description="""Canonical stakeholder role type as defined in Clause 5.19.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIStakeholderRole'],
         'ifabsent': 'AIStakeholderRoleType(ai_partner)'} })
    organization_name: Optional[str] = Field(default=None, description="""Name of the organisation acting in the stakeholder role.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIStakeholderRole']} })
    contact: Optional[str] = Field(default=None, description="""Contact identifier (e.g. email) for the stakeholder.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIStakeholderRole']} })
    responsibilities: Optional[list[str]] = Field(default=None, description="""Free-text statements of responsibility.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIStakeholderRole']} })
    id: str = Field(default=..., description="""Unique CURIE or URI identifying the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:identifier'} })
    name: str = Field(default=..., description="""Human-readable label for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['dcterms:title', 'schema:name'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Free-text description of the entity (paraphrased; verbatim ISO text excluded).""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:description'} })
    clause_reference: Optional[str] = Field(default=None, description="""ISO/IEC 22989:2022 clause identifier (e.g. \"5.11.4\") the element corresponds to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'AutonomyAssessment',
                       'VerificationValidationFramework']} })
    aliases: Optional[list[str]] = Field(default=None, description="""Alternative names or synonyms for the term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:altLabel'} })
    preferred_label: Optional[str] = Field(default=None, description="""Preferred natural-language label.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:prefLabel'} })
    see_also_uri: Optional[list[str]] = Field(default=None, description="""Pointers to related external resources or term records.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:seeAlso'} })

    @field_validator('clause_reference')
    def pattern_clause_reference(cls, v):
        pattern=re.compile(r"^[0-9]+(\.[0-9]+){0,3}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid clause_reference format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid clause_reference format: {v}"
            raise ValueError(err_msg)
        return v


class DataProvider(AIPartner):
    """
    Partner supplying datasets used by AI systems (Clause 5.19.5).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'close_mappings': ['iso29100:PIIController'],
         'from_schema': 'https://w3id.org/lmodel/iso22989'})

    stakeholder_role_type: AIStakeholderRoleType = Field(default=AIStakeholderRoleType.ai_partner, description="""Canonical stakeholder role type as defined in Clause 5.19.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIStakeholderRole'],
         'ifabsent': 'AIStakeholderRoleType(ai_partner)'} })
    organization_name: Optional[str] = Field(default=None, description="""Name of the organisation acting in the stakeholder role.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIStakeholderRole']} })
    contact: Optional[str] = Field(default=None, description="""Contact identifier (e.g. email) for the stakeholder.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIStakeholderRole']} })
    responsibilities: Optional[list[str]] = Field(default=None, description="""Free-text statements of responsibility.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIStakeholderRole']} })
    id: str = Field(default=..., description="""Unique CURIE or URI identifying the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:identifier'} })
    name: str = Field(default=..., description="""Human-readable label for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['dcterms:title', 'schema:name'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Free-text description of the entity (paraphrased; verbatim ISO text excluded).""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:description'} })
    clause_reference: Optional[str] = Field(default=None, description="""ISO/IEC 22989:2022 clause identifier (e.g. \"5.11.4\") the element corresponds to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'AutonomyAssessment',
                       'VerificationValidationFramework']} })
    aliases: Optional[list[str]] = Field(default=None, description="""Alternative names or synonyms for the term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:altLabel'} })
    preferred_label: Optional[str] = Field(default=None, description="""Preferred natural-language label.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:prefLabel'} })
    see_also_uri: Optional[list[str]] = Field(default=None, description="""Pointers to related external resources or term records.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:seeAlso'} })

    @field_validator('clause_reference')
    def pattern_clause_reference(cls, v):
        pattern=re.compile(r"^[0-9]+(\.[0-9]+){0,3}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid clause_reference format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid clause_reference format: {v}"
            raise ValueError(err_msg)
        return v


class AIAuditor(AIPartner):
    """
    Partner performing independent audits of AI systems (Clause 5.19.5).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'close_mappings': ['nist_ai_100_1:AiActorTaskEnum#TEVV',
                            'nist_ai_600_1:GaiActorTaskEnum#TEVV'],
         'from_schema': 'https://w3id.org/lmodel/iso22989'})

    stakeholder_role_type: AIStakeholderRoleType = Field(default=AIStakeholderRoleType.ai_partner, description="""Canonical stakeholder role type as defined in Clause 5.19.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIStakeholderRole'],
         'ifabsent': 'AIStakeholderRoleType(ai_partner)'} })
    organization_name: Optional[str] = Field(default=None, description="""Name of the organisation acting in the stakeholder role.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIStakeholderRole']} })
    contact: Optional[str] = Field(default=None, description="""Contact identifier (e.g. email) for the stakeholder.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIStakeholderRole']} })
    responsibilities: Optional[list[str]] = Field(default=None, description="""Free-text statements of responsibility.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIStakeholderRole']} })
    id: str = Field(default=..., description="""Unique CURIE or URI identifying the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:identifier'} })
    name: str = Field(default=..., description="""Human-readable label for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['dcterms:title', 'schema:name'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Free-text description of the entity (paraphrased; verbatim ISO text excluded).""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:description'} })
    clause_reference: Optional[str] = Field(default=None, description="""ISO/IEC 22989:2022 clause identifier (e.g. \"5.11.4\") the element corresponds to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'AutonomyAssessment',
                       'VerificationValidationFramework']} })
    aliases: Optional[list[str]] = Field(default=None, description="""Alternative names or synonyms for the term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:altLabel'} })
    preferred_label: Optional[str] = Field(default=None, description="""Preferred natural-language label.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:prefLabel'} })
    see_also_uri: Optional[list[str]] = Field(default=None, description="""Pointers to related external resources or term records.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:seeAlso'} })

    @field_validator('clause_reference')
    def pattern_clause_reference(cls, v):
        pattern=re.compile(r"^[0-9]+(\.[0-9]+){0,3}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid clause_reference format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid clause_reference format: {v}"
            raise ValueError(err_msg)
        return v


class AIEvaluator(AIPartner):
    """
    Partner performing evaluations of AI system performance and trustworthiness (Clause 5.19.5).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/iso22989'})

    stakeholder_role_type: AIStakeholderRoleType = Field(default=AIStakeholderRoleType.ai_partner, description="""Canonical stakeholder role type as defined in Clause 5.19.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIStakeholderRole'],
         'ifabsent': 'AIStakeholderRoleType(ai_partner)'} })
    organization_name: Optional[str] = Field(default=None, description="""Name of the organisation acting in the stakeholder role.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIStakeholderRole']} })
    contact: Optional[str] = Field(default=None, description="""Contact identifier (e.g. email) for the stakeholder.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIStakeholderRole']} })
    responsibilities: Optional[list[str]] = Field(default=None, description="""Free-text statements of responsibility.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIStakeholderRole']} })
    id: str = Field(default=..., description="""Unique CURIE or URI identifying the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:identifier'} })
    name: str = Field(default=..., description="""Human-readable label for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['dcterms:title', 'schema:name'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Free-text description of the entity (paraphrased; verbatim ISO text excluded).""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:description'} })
    clause_reference: Optional[str] = Field(default=None, description="""ISO/IEC 22989:2022 clause identifier (e.g. \"5.11.4\") the element corresponds to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'AutonomyAssessment',
                       'VerificationValidationFramework']} })
    aliases: Optional[list[str]] = Field(default=None, description="""Alternative names or synonyms for the term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:altLabel'} })
    preferred_label: Optional[str] = Field(default=None, description="""Preferred natural-language label.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:prefLabel'} })
    see_also_uri: Optional[list[str]] = Field(default=None, description="""Pointers to related external resources or term records.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:seeAlso'} })

    @field_validator('clause_reference')
    def pattern_clause_reference(cls, v):
        pattern=re.compile(r"^[0-9]+(\.[0-9]+){0,3}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid clause_reference format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid clause_reference format: {v}"
            raise ValueError(err_msg)
        return v


class DataSubject(AISubject):
    """
    Individual whose personal data is processed by an AI system (Clause 5.19.6).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'close_mappings': ['gist_linkml:Person'],
         'exact_mappings': ['iso29100:PIIPrincipal'],
         'from_schema': 'https://w3id.org/lmodel/iso22989'})

    stakeholder_role_type: AIStakeholderRoleType = Field(default=AIStakeholderRoleType.ai_subject, description="""Canonical stakeholder role type as defined in Clause 5.19.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIStakeholderRole'],
         'ifabsent': 'AIStakeholderRoleType(ai_subject)'} })
    organization_name: Optional[str] = Field(default=None, description="""Name of the organisation acting in the stakeholder role.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIStakeholderRole']} })
    contact: Optional[str] = Field(default=None, description="""Contact identifier (e.g. email) for the stakeholder.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIStakeholderRole']} })
    responsibilities: Optional[list[str]] = Field(default=None, description="""Free-text statements of responsibility.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIStakeholderRole']} })
    id: str = Field(default=..., description="""Unique CURIE or URI identifying the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:identifier'} })
    name: str = Field(default=..., description="""Human-readable label for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['dcterms:title', 'schema:name'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Free-text description of the entity (paraphrased; verbatim ISO text excluded).""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:description'} })
    clause_reference: Optional[str] = Field(default=None, description="""ISO/IEC 22989:2022 clause identifier (e.g. \"5.11.4\") the element corresponds to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'AutonomyAssessment',
                       'VerificationValidationFramework']} })
    aliases: Optional[list[str]] = Field(default=None, description="""Alternative names or synonyms for the term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:altLabel'} })
    preferred_label: Optional[str] = Field(default=None, description="""Preferred natural-language label.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:prefLabel'} })
    see_also_uri: Optional[list[str]] = Field(default=None, description="""Pointers to related external resources or term records.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:seeAlso'} })

    @field_validator('clause_reference')
    def pattern_clause_reference(cls, v):
        pattern=re.compile(r"^[0-9]+(\.[0-9]+){0,3}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid clause_reference format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid clause_reference format: {v}"
            raise ValueError(err_msg)
        return v


class PolicyMaker(RelevantAuthority):
    """
    Authority defining policy applicable to AI systems (Clause 5.19.7).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/iso22989'})

    stakeholder_role_type: AIStakeholderRoleType = Field(default=AIStakeholderRoleType.relevant_authority, description="""Canonical stakeholder role type as defined in Clause 5.19.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIStakeholderRole'],
         'ifabsent': 'AIStakeholderRoleType(relevant_authority)'} })
    organization_name: Optional[str] = Field(default=None, description="""Name of the organisation acting in the stakeholder role.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIStakeholderRole']} })
    contact: Optional[str] = Field(default=None, description="""Contact identifier (e.g. email) for the stakeholder.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIStakeholderRole']} })
    responsibilities: Optional[list[str]] = Field(default=None, description="""Free-text statements of responsibility.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIStakeholderRole']} })
    id: str = Field(default=..., description="""Unique CURIE or URI identifying the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:identifier'} })
    name: str = Field(default=..., description="""Human-readable label for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['dcterms:title', 'schema:name'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Free-text description of the entity (paraphrased; verbatim ISO text excluded).""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:description'} })
    clause_reference: Optional[str] = Field(default=None, description="""ISO/IEC 22989:2022 clause identifier (e.g. \"5.11.4\") the element corresponds to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'AutonomyAssessment',
                       'VerificationValidationFramework']} })
    aliases: Optional[list[str]] = Field(default=None, description="""Alternative names or synonyms for the term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:altLabel'} })
    preferred_label: Optional[str] = Field(default=None, description="""Preferred natural-language label.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:prefLabel'} })
    see_also_uri: Optional[list[str]] = Field(default=None, description="""Pointers to related external resources or term records.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:seeAlso'} })

    @field_validator('clause_reference')
    def pattern_clause_reference(cls, v):
        pattern=re.compile(r"^[0-9]+(\.[0-9]+){0,3}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid clause_reference format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid clause_reference format: {v}"
            raise ValueError(err_msg)
        return v


class Regulator(RelevantAuthority):
    """
    Authority responsible for regulatory oversight of AI systems (Clause 5.19.7).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/iso22989'})

    stakeholder_role_type: AIStakeholderRoleType = Field(default=AIStakeholderRoleType.relevant_authority, description="""Canonical stakeholder role type as defined in Clause 5.19.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIStakeholderRole'],
         'ifabsent': 'AIStakeholderRoleType(relevant_authority)'} })
    organization_name: Optional[str] = Field(default=None, description="""Name of the organisation acting in the stakeholder role.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIStakeholderRole']} })
    contact: Optional[str] = Field(default=None, description="""Contact identifier (e.g. email) for the stakeholder.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIStakeholderRole']} })
    responsibilities: Optional[list[str]] = Field(default=None, description="""Free-text statements of responsibility.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIStakeholderRole']} })
    id: str = Field(default=..., description="""Unique CURIE or URI identifying the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:identifier'} })
    name: str = Field(default=..., description="""Human-readable label for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['dcterms:title', 'schema:name'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Free-text description of the entity (paraphrased; verbatim ISO text excluded).""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:description'} })
    clause_reference: Optional[str] = Field(default=None, description="""ISO/IEC 22989:2022 clause identifier (e.g. \"5.11.4\") the element corresponds to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'AutonomyAssessment',
                       'VerificationValidationFramework']} })
    aliases: Optional[list[str]] = Field(default=None, description="""Alternative names or synonyms for the term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:altLabel'} })
    preferred_label: Optional[str] = Field(default=None, description="""Preferred natural-language label.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:prefLabel'} })
    see_also_uri: Optional[list[str]] = Field(default=None, description="""Pointers to related external resources or term records.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:seeAlso'} })

    @field_validator('clause_reference')
    def pattern_clause_reference(cls, v):
        pattern=re.compile(r"^[0-9]+(\.[0-9]+){0,3}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid clause_reference format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid clause_reference format: {v}"
            raise ValueError(err_msg)
        return v


class AutonomyAssessment(NamedEntity):
    """
    Structured assessment of the autonomy level of an AI system using the criteria listed in Clause 5.13.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/iso22989',
         'in_subset': ['ai_concepts']})

    autonomy_level: Optional[AutonomyLevel] = Field(default=None, description="""Operational autonomy level of the AI system.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIAgent', 'AISystem', 'AutonomyAssessment']} })
    autonomy_criterion_scores: Optional[list[str]] = Field(default=None, description="""Free-form scores or judgements for autonomy criteria (Clause 5.13).""", json_schema_extra = { "linkml_meta": {'domain_of': ['AutonomyAssessment']} })
    clause_reference: Optional[str] = Field(default=None, description="""ISO/IEC 22989:2022 clause identifier (e.g. \"5.11.4\") the element corresponds to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'AutonomyAssessment',
                       'VerificationValidationFramework']} })
    id: str = Field(default=..., description="""Unique CURIE or URI identifying the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:identifier'} })
    name: str = Field(default=..., description="""Human-readable label for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['dcterms:title', 'schema:name'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Free-text description of the entity (paraphrased; verbatim ISO text excluded).""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:description'} })
    aliases: Optional[list[str]] = Field(default=None, description="""Alternative names or synonyms for the term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:altLabel'} })
    preferred_label: Optional[str] = Field(default=None, description="""Preferred natural-language label.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:prefLabel'} })
    see_also_uri: Optional[list[str]] = Field(default=None, description="""Pointers to related external resources or term records.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:seeAlso'} })

    @field_validator('clause_reference')
    def pattern_clause_reference(cls, v):
        pattern=re.compile(r"^[0-9]+(\.[0-9]+){0,3}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid clause_reference format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid clause_reference format: {v}"
            raise ValueError(err_msg)
        return v


class VerificationValidationFramework(NamedEntity):
    """
    Verifiability and validatability claim for an AI system characterised according to the levels in Clause 5.16.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/iso22989',
         'in_subset': ['trustworthiness']})

    verification_validation_level: Optional[VerificationValidationLevel] = Field(default=None, description="""Verifiability / validatability claim (Clause 5.16).""", json_schema_extra = { "linkml_meta": {'domain_of': ['VerificationValidationFramework']} })
    clause_reference: Optional[str] = Field(default=None, description="""ISO/IEC 22989:2022 clause identifier (e.g. \"5.11.4\") the element corresponds to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'AutonomyAssessment',
                       'VerificationValidationFramework']} })
    verification_methods: Optional[list[str]] = Field(default=None, description="""Verification methods applied or applicable to the system.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VerificationValidationFramework']} })
    validation_methods: Optional[list[str]] = Field(default=None, description="""Validation methods applied or applicable to the system.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VerificationValidationFramework']} })
    id: str = Field(default=..., description="""Unique CURIE or URI identifying the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:identifier'} })
    name: str = Field(default=..., description="""Human-readable label for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['dcterms:title', 'schema:name'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Free-text description of the entity (paraphrased; verbatim ISO text excluded).""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:description'} })
    aliases: Optional[list[str]] = Field(default=None, description="""Alternative names or synonyms for the term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:altLabel'} })
    preferred_label: Optional[str] = Field(default=None, description="""Preferred natural-language label.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:prefLabel'} })
    see_also_uri: Optional[list[str]] = Field(default=None, description="""Pointers to related external resources or term records.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:seeAlso'} })

    @field_validator('clause_reference')
    def pattern_clause_reference(cls, v):
        pattern=re.compile(r"^[0-9]+(\.[0-9]+){0,3}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid clause_reference format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid clause_reference format: {v}"
            raise ValueError(err_msg)
        return v


class HumanMachineTeam(AIConcept):
    """
    Collaboration arrangement combining one or more humans with one or more AI systems to pursue shared goals (Clauses 3.3.3, 5.13).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'close_mappings': ['nist_ai_600_1:GaiRiskCategoryEnum#HUMAN_AI_CONFIGURATION'],
         'from_schema': 'https://w3id.org/lmodel/iso22989'})

    human_roles: Optional[list[str]] = Field(default=None, description="""Roles played by humans in the team.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HumanMachineTeam']} })
    ai_systems_involved: Optional[list[str]] = Field(default=None, description="""AI systems participating in the team.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HumanMachineTeam']} })
    task_allocation: Optional[str] = Field(default=None, description="""Free-text description of how tasks are allocated between humans and AI.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HumanMachineTeam']} })
    id: str = Field(default=..., description="""Unique CURIE or URI identifying the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:identifier'} })
    name: str = Field(default=..., description="""Human-readable label for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['dcterms:title', 'schema:name'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Free-text description of the entity (paraphrased; verbatim ISO text excluded).""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:description'} })
    clause_reference: Optional[str] = Field(default=None, description="""ISO/IEC 22989:2022 clause identifier (e.g. \"5.11.4\") the element corresponds to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'AutonomyAssessment',
                       'VerificationValidationFramework']} })
    aliases: Optional[list[str]] = Field(default=None, description="""Alternative names or synonyms for the term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:altLabel'} })
    preferred_label: Optional[str] = Field(default=None, description="""Preferred natural-language label.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:prefLabel'} })
    see_also_uri: Optional[list[str]] = Field(default=None, description="""Pointers to related external resources or term records.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:seeAlso'} })

    @field_validator('clause_reference')
    def pattern_clause_reference(cls, v):
        pattern=re.compile(r"^[0-9]+(\.[0-9]+){0,3}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid clause_reference format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid clause_reference format: {v}"
            raise ValueError(err_msg)
        return v


class IntelligenceAugmentation(AIConcept):
    """
    Use of AI to enhance the cognitive capabilities of humans rather than replace them (Clause 5.13 context).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/iso22989'})

    augmented_capability: Optional[list[str]] = Field(default=None, description="""Cognitive capabilities being augmented.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IntelligenceAugmentation']} })
    id: str = Field(default=..., description="""Unique CURIE or URI identifying the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:identifier'} })
    name: str = Field(default=..., description="""Human-readable label for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['dcterms:title', 'schema:name'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Free-text description of the entity (paraphrased; verbatim ISO text excluded).""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:description'} })
    clause_reference: Optional[str] = Field(default=None, description="""ISO/IEC 22989:2022 clause identifier (e.g. \"5.11.4\") the element corresponds to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'AutonomyAssessment',
                       'VerificationValidationFramework']} })
    aliases: Optional[list[str]] = Field(default=None, description="""Alternative names or synonyms for the term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:altLabel'} })
    preferred_label: Optional[str] = Field(default=None, description="""Preferred natural-language label.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:prefLabel'} })
    see_also_uri: Optional[list[str]] = Field(default=None, description="""Pointers to related external resources or term records.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:seeAlso'} })

    @field_validator('clause_reference')
    def pattern_clause_reference(cls, v):
        pattern=re.compile(r"^[0-9]+(\.[0-9]+){0,3}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid clause_reference format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid clause_reference format: {v}"
            raise ValueError(err_msg)
        return v


class Recommendation(NamedEntity):
    """
    Recommendation produced by an AI system (Clauses 7.4, 10).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/iso22989',
         'in_subset': ['ai_functional_view']})

    recommendation_outcome_type: Optional[RecommendationOutcomeType] = Field(default=None, description="""High-level outcome type of a recommendation (Clauses 7.4, 10).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Recommendation']} })
    confidence: Optional[float] = Field(default=None, description="""Normalised confidence value associated with an output or claim.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Prediction', 'Recommendation']} })
    recommended_items: Optional[list[str]] = Field(default=None, description="""Items recommended by the system, serialised as strings.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Recommendation']} })
    based_on_predictions: Optional[list[str]] = Field(default=None, description="""Predictions supporting the recommendation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Decision', 'Recommendation']} })
    id: str = Field(default=..., description="""Unique CURIE or URI identifying the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:identifier'} })
    name: str = Field(default=..., description="""Human-readable label for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['dcterms:title', 'schema:name'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Free-text description of the entity (paraphrased; verbatim ISO text excluded).""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:description'} })
    clause_reference: Optional[str] = Field(default=None, description="""ISO/IEC 22989:2022 clause identifier (e.g. \"5.11.4\") the element corresponds to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'AutonomyAssessment',
                       'VerificationValidationFramework']} })
    aliases: Optional[list[str]] = Field(default=None, description="""Alternative names or synonyms for the term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:altLabel'} })
    preferred_label: Optional[str] = Field(default=None, description="""Preferred natural-language label.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:prefLabel'} })
    see_also_uri: Optional[list[str]] = Field(default=None, description="""Pointers to related external resources or term records.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:seeAlso'} })

    @field_validator('clause_reference')
    def pattern_clause_reference(cls, v):
        pattern=re.compile(r"^[0-9]+(\.[0-9]+){0,3}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid clause_reference format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid clause_reference format: {v}"
            raise ValueError(err_msg)
        return v


class EvaluationMetric(NamedEntity):
    """
    Metric used to evaluate AI system or model performance (Clause 7.4.3).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/iso22989',
         'in_subset': ['trustworthiness']})

    metric_name: str = Field(default=..., description="""Name of the metric (e.g. accuracy, F1, MAE).""", json_schema_extra = { "linkml_meta": {'domain_of': ['EvaluationMetric']} })
    metric_value: Optional[float] = Field(default=None, description="""Observed numeric value of the metric.""", json_schema_extra = { "linkml_meta": {'domain_of': ['EvaluationMetric']} })
    metric_unit: Optional[str] = Field(default=None, description="""Unit of the metric, when applicable.""", json_schema_extra = { "linkml_meta": {'domain_of': ['EvaluationMetric']} })
    reference_dataset: Optional[str] = Field(default=None, description="""Dataset against which the metric was computed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['EvaluationMetric']} })
    id: str = Field(default=..., description="""Unique CURIE or URI identifying the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:identifier'} })
    name: str = Field(default=..., description="""Human-readable label for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['dcterms:title', 'schema:name'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Free-text description of the entity (paraphrased; verbatim ISO text excluded).""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:description'} })
    clause_reference: Optional[str] = Field(default=None, description="""ISO/IEC 22989:2022 clause identifier (e.g. \"5.11.4\") the element corresponds to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'AutonomyAssessment',
                       'VerificationValidationFramework']} })
    aliases: Optional[list[str]] = Field(default=None, description="""Alternative names or synonyms for the term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:altLabel'} })
    preferred_label: Optional[str] = Field(default=None, description="""Preferred natural-language label.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:prefLabel'} })
    see_also_uri: Optional[list[str]] = Field(default=None, description="""Pointers to related external resources or term records.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:seeAlso'} })

    @field_validator('clause_reference')
    def pattern_clause_reference(cls, v):
        pattern=re.compile(r"^[0-9]+(\.[0-9]+){0,3}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid clause_reference format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid clause_reference format: {v}"
            raise ValueError(err_msg)
        return v


class Threshold(NamedEntity):
    """
    Decision threshold applied to a metric, prediction or score (Clause 7.4.3).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/iso22989',
         'in_subset': ['ai_functional_view']})

    threshold_value: float = Field(default=..., description="""Numeric threshold value.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Threshold']} })
    applies_to_metric: Optional[str] = Field(default=None, description="""Name of the metric or score the threshold applies to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Threshold']} })
    threshold_policy: Optional[str] = Field(default=None, description="""Policy describing how the threshold is interpreted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Threshold']} })
    id: str = Field(default=..., description="""Unique CURIE or URI identifying the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:identifier'} })
    name: str = Field(default=..., description="""Human-readable label for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['dcterms:title', 'schema:name'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Free-text description of the entity (paraphrased; verbatim ISO text excluded).""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:description'} })
    clause_reference: Optional[str] = Field(default=None, description="""ISO/IEC 22989:2022 clause identifier (e.g. \"5.11.4\") the element corresponds to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'AutonomyAssessment',
                       'VerificationValidationFramework']} })
    aliases: Optional[list[str]] = Field(default=None, description="""Alternative names or synonyms for the term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:altLabel'} })
    preferred_label: Optional[str] = Field(default=None, description="""Preferred natural-language label.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:prefLabel'} })
    see_also_uri: Optional[list[str]] = Field(default=None, description="""Pointers to related external resources or term records.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:seeAlso'} })

    @field_validator('clause_reference')
    def pattern_clause_reference(cls, v):
        pattern=re.compile(r"^[0-9]+(\.[0-9]+){0,3}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid clause_reference format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid clause_reference format: {v}"
            raise ValueError(err_msg)
        return v


class Neuron(AIConcept):
    """
    Computational unit in a neural network combining weighted inputs with a bias and an activation function (Clause 3.4.9).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/iso22989'})

    activation_function: Optional[ActivationFunctionType] = Field(default=None, description="""Activation function applied at the neuron output.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AIModel', 'Neuron']} })
    input_arity: Optional[int] = Field(default=None, description="""Number of inputs combined by the neuron.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['Neuron']} })
    id: str = Field(default=..., description="""Unique CURIE or URI identifying the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:identifier'} })
    name: str = Field(default=..., description="""Human-readable label for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['dcterms:title', 'schema:name'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Free-text description of the entity (paraphrased; verbatim ISO text excluded).""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:description'} })
    clause_reference: Optional[str] = Field(default=None, description="""ISO/IEC 22989:2022 clause identifier (e.g. \"5.11.4\") the element corresponds to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'AutonomyAssessment',
                       'VerificationValidationFramework']} })
    aliases: Optional[list[str]] = Field(default=None, description="""Alternative names or synonyms for the term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:altLabel'} })
    preferred_label: Optional[str] = Field(default=None, description="""Preferred natural-language label.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:prefLabel'} })
    see_also_uri: Optional[list[str]] = Field(default=None, description="""Pointers to related external resources or term records.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:seeAlso'} })

    @field_validator('clause_reference')
    def pattern_clause_reference(cls, v):
        pattern=re.compile(r"^[0-9]+(\.[0-9]+){0,3}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid clause_reference format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid clause_reference format: {v}"
            raise ValueError(err_msg)
        return v


class ConvolutionOperation(AIConcept):
    """
    Convolution operation as used in convolutional neural networks (Clause 3.4.3).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/iso22989'})

    kernel_size: Optional[list[int]] = Field(default=None, description="""Spatial dimensions of the convolution kernel.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ConvolutionOperation']} })
    stride: Optional[int] = Field(default=None, description="""Stride applied when sliding the kernel over the input.""", ge=1, json_schema_extra = { "linkml_meta": {'domain_of': ['ConvolutionOperation']} })
    padding: Optional[str] = Field(default=None, description="""Padding mode (e.g. valid, same).""", json_schema_extra = { "linkml_meta": {'domain_of': ['ConvolutionOperation']} })
    id: str = Field(default=..., description="""Unique CURIE or URI identifying the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:identifier'} })
    name: str = Field(default=..., description="""Human-readable label for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['dcterms:title', 'schema:name'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Free-text description of the entity (paraphrased; verbatim ISO text excluded).""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:description'} })
    clause_reference: Optional[str] = Field(default=None, description="""ISO/IEC 22989:2022 clause identifier (e.g. \"5.11.4\") the element corresponds to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'AutonomyAssessment',
                       'VerificationValidationFramework']} })
    aliases: Optional[list[str]] = Field(default=None, description="""Alternative names or synonyms for the term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:altLabel'} })
    preferred_label: Optional[str] = Field(default=None, description="""Preferred natural-language label.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:prefLabel'} })
    see_also_uri: Optional[list[str]] = Field(default=None, description="""Pointers to related external resources or term records.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:seeAlso'} })

    @field_validator('clause_reference')
    def pattern_clause_reference(cls, v):
        pattern=re.compile(r"^[0-9]+(\.[0-9]+){0,3}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid clause_reference format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid clause_reference format: {v}"
            raise ValueError(err_msg)
        return v


class DataDrift(NamedEntity):
    """
    Observed change in the statistical distribution of operational data relative to training data (Clause 5.11.9.1).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/iso22989',
         'in_subset': ['terminology']})

    drift_type: Optional[str] = Field(default=None, description="""Type of drift (covariate, label, concept).""", json_schema_extra = { "linkml_meta": {'domain_of': ['DataDrift']} })
    detected_at: Optional[str] = Field(default=None, description="""Timestamp or interval at which drift was detected.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DataDrift']} })
    affected_dataset: Optional[str] = Field(default=None, description="""Dataset in which drift was observed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DataDrift']} })
    id: str = Field(default=..., description="""Unique CURIE or URI identifying the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:identifier'} })
    name: str = Field(default=..., description="""Human-readable label for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['dcterms:title', 'schema:name'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Free-text description of the entity (paraphrased; verbatim ISO text excluded).""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:description'} })
    clause_reference: Optional[str] = Field(default=None, description="""ISO/IEC 22989:2022 clause identifier (e.g. \"5.11.4\") the element corresponds to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'AutonomyAssessment',
                       'VerificationValidationFramework']} })
    aliases: Optional[list[str]] = Field(default=None, description="""Alternative names or synonyms for the term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:altLabel'} })
    preferred_label: Optional[str] = Field(default=None, description="""Preferred natural-language label.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:prefLabel'} })
    see_also_uri: Optional[list[str]] = Field(default=None, description="""Pointers to related external resources or term records.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:seeAlso'} })

    @field_validator('clause_reference')
    def pattern_clause_reference(cls, v):
        pattern=re.compile(r"^[0-9]+(\.[0-9]+){0,3}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid clause_reference format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid clause_reference format: {v}"
            raise ValueError(err_msg)
        return v


class CatastrophicForgetting(NamedEntity):
    """
    Phenomenon by which a continually-trained model loses previously acquired competence (Clause 5.11.9.1).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/iso22989',
         'in_subset': ['terminology']})

    affected_model: Optional[str] = Field(default=None, description="""Model in which the phenomenon was observed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatastrophicForgetting']} })
    mitigation_strategy: Optional[str] = Field(default=None, description="""Strategy applied to mitigate the phenomenon.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatastrophicForgetting', 'RiskItem']} })
    id: str = Field(default=..., description="""Unique CURIE or URI identifying the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:identifier'} })
    name: str = Field(default=..., description="""Human-readable label for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['dcterms:title', 'schema:name'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Free-text description of the entity (paraphrased; verbatim ISO text excluded).""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:description'} })
    clause_reference: Optional[str] = Field(default=None, description="""ISO/IEC 22989:2022 clause identifier (e.g. \"5.11.4\") the element corresponds to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'AutonomyAssessment',
                       'VerificationValidationFramework']} })
    aliases: Optional[list[str]] = Field(default=None, description="""Alternative names or synonyms for the term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:altLabel'} })
    preferred_label: Optional[str] = Field(default=None, description="""Preferred natural-language label.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:prefLabel'} })
    see_also_uri: Optional[list[str]] = Field(default=None, description="""Pointers to related external resources or term records.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:seeAlso'} })

    @field_validator('clause_reference')
    def pattern_clause_reference(cls, v):
        pattern=re.compile(r"^[0-9]+(\.[0-9]+){0,3}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid clause_reference format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid clause_reference format: {v}"
            raise ValueError(err_msg)
        return v


class FaultToleranceMechanism(NamedEntity):
    """
    Mechanism enabling an AI system to continue operating correctly in the presence of component faults (Clause 5.15.4 context).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/iso22989',
         'in_subset': ['trustworthiness']})

    mechanism_type: Optional[str] = Field(default=None, description="""Type of mechanism (redundancy, graceful degradation, failover, etc.).""", json_schema_extra = { "linkml_meta": {'domain_of': ['FaultToleranceMechanism']} })
    coverage_scope: Optional[str] = Field(default=None, description="""Scope of failure modes the mechanism covers.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FaultToleranceMechanism']} })
    id: str = Field(default=..., description="""Unique CURIE or URI identifying the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:identifier'} })
    name: str = Field(default=..., description="""Human-readable label for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['dcterms:title', 'schema:name'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Free-text description of the entity (paraphrased; verbatim ISO text excluded).""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:description'} })
    clause_reference: Optional[str] = Field(default=None, description="""ISO/IEC 22989:2022 clause identifier (e.g. \"5.11.4\") the element corresponds to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'AutonomyAssessment',
                       'VerificationValidationFramework']} })
    aliases: Optional[list[str]] = Field(default=None, description="""Alternative names or synonyms for the term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:altLabel'} })
    preferred_label: Optional[str] = Field(default=None, description="""Preferred natural-language label.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:prefLabel'} })
    see_also_uri: Optional[list[str]] = Field(default=None, description="""Pointers to related external resources or term records.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:seeAlso'} })

    @field_validator('clause_reference')
    def pattern_clause_reference(cls, v):
        pattern=re.compile(r"^[0-9]+(\.[0-9]+){0,3}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid clause_reference format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid clause_reference format: {v}"
            raise ValueError(err_msg)
        return v


class NaturalLanguage(AIConcept):
    """
    Natural language treated as an object of processing or generation by an AI system (Clause 9.2).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/iso22989', 'in_subset': ['ai_fields']})

    language_code: Optional[str] = Field(default=None, description="""BCP-47 language tag.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NaturalLanguage']} })
    script: Optional[str] = Field(default=None, description="""ISO 15924 script code, when relevant.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NaturalLanguage']} })
    id: str = Field(default=..., description="""Unique CURIE or URI identifying the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:identifier'} })
    name: str = Field(default=..., description="""Human-readable label for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['dcterms:title', 'schema:name'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Free-text description of the entity (paraphrased; verbatim ISO text excluded).""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:description'} })
    clause_reference: Optional[str] = Field(default=None, description="""ISO/IEC 22989:2022 clause identifier (e.g. \"5.11.4\") the element corresponds to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'AutonomyAssessment',
                       'VerificationValidationFramework']} })
    aliases: Optional[list[str]] = Field(default=None, description="""Alternative names or synonyms for the term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:altLabel'} })
    preferred_label: Optional[str] = Field(default=None, description="""Preferred natural-language label.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:prefLabel'} })
    see_also_uri: Optional[list[str]] = Field(default=None, description="""Pointers to related external resources or term records.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:seeAlso'} })

    @field_validator('clause_reference')
    def pattern_clause_reference(cls, v):
        pattern=re.compile(r"^[0-9]+(\.[0-9]+){0,3}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid clause_reference format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid clause_reference format: {v}"
            raise ValueError(err_msg)
        return v


class RiskItem(NamedEntity):
    """
    Risk associated with an AI system, capturing source, potential event, consequence and treatment metadata (Clause 3.5.11; aligned with ISO/IEC 23894 risk concepts).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'close_mappings': ['iso27001:Risk',
                            'iso29100:PrivacyRisk',
                            'nist_ai_600_1:GaiRisk'],
         'exact_mappings': ['nist_ai_100_1:Risk'],
         'from_schema': 'https://w3id.org/lmodel/iso22989',
         'in_subset': ['trustworthiness', 'ai_lifecycle']})

    risk_source: Optional[str] = Field(default=None, description="""Source from which the risk originates.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RiskItem']} })
    potential_event: Optional[str] = Field(default=None, description="""Potential event whose occurrence would realise the risk.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RiskItem']} })
    consequence: Optional[str] = Field(default=None, description="""Consequence to one or more stakeholders if the event occurs.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RiskItem']} })
    likelihood: Optional[float] = Field(default=None, description="""Estimated likelihood of the event (0.0–1.0).""", json_schema_extra = { "linkml_meta": {'domain_of': ['RiskItem']} })
    severity: Optional[str] = Field(default=None, description="""Qualitative severity assessment of the consequence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RiskItem']} })
    mitigation_strategy: Optional[list[str]] = Field(default=None, description="""Strategies to reduce likelihood or severity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatastrophicForgetting', 'RiskItem']} })
    affected_stakeholders: Optional[list[str]] = Field(default=None, description="""Stakeholder roles affected by the risk.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RiskItem']} })
    id: str = Field(default=..., description="""Unique CURIE or URI identifying the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:identifier'} })
    name: str = Field(default=..., description="""Human-readable label for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['dcterms:title', 'schema:name'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Free-text description of the entity (paraphrased; verbatim ISO text excluded).""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:description'} })
    clause_reference: Optional[str] = Field(default=None, description="""ISO/IEC 22989:2022 clause identifier (e.g. \"5.11.4\") the element corresponds to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'AutonomyAssessment',
                       'VerificationValidationFramework']} })
    aliases: Optional[list[str]] = Field(default=None, description="""Alternative names or synonyms for the term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:altLabel'} })
    preferred_label: Optional[str] = Field(default=None, description="""Preferred natural-language label.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:prefLabel'} })
    see_also_uri: Optional[list[str]] = Field(default=None, description="""Pointers to related external resources or term records.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:seeAlso'} })

    @field_validator('clause_reference')
    def pattern_clause_reference(cls, v):
        pattern=re.compile(r"^[0-9]+(\.[0-9]+){0,3}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid clause_reference format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid clause_reference format: {v}"
            raise ValueError(err_msg)
        return v


class InputData(NamedEntity):
    """
    Data presented to an AI system at inference time or during training (Clause 3.2.9).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/iso22989',
         'in_subset': ['terminology']})

    data_source_type: Optional[DataSourceType] = Field(default=None, description="""Classification of a data source (Clause 8.6.1).""", json_schema_extra = { "linkml_meta": {'domain_of': ['InputData']} })
    data_collection_method: Optional[DataCollectionMethod] = Field(default=None, description="""Method used to collect data (Clause 8.6.1).""", json_schema_extra = { "linkml_meta": {'domain_of': ['InputData']} })
    modality: Optional[DataModality] = Field(default=None, description="""Modality of the input data.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InputData']} })
    consumed_by: Optional[str] = Field(default=None, description="""AI system that consumes the input.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InputData']} })
    id: str = Field(default=..., description="""Unique CURIE or URI identifying the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:identifier'} })
    name: str = Field(default=..., description="""Human-readable label for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['dcterms:title', 'schema:name'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Free-text description of the entity (paraphrased; verbatim ISO text excluded).""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:description'} })
    clause_reference: Optional[str] = Field(default=None, description="""ISO/IEC 22989:2022 clause identifier (e.g. \"5.11.4\") the element corresponds to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'AutonomyAssessment',
                       'VerificationValidationFramework']} })
    aliases: Optional[list[str]] = Field(default=None, description="""Alternative names or synonyms for the term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:altLabel'} })
    preferred_label: Optional[str] = Field(default=None, description="""Preferred natural-language label.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:prefLabel'} })
    see_also_uri: Optional[list[str]] = Field(default=None, description="""Pointers to related external resources or term records.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:seeAlso'} })

    @field_validator('clause_reference')
    def pattern_clause_reference(cls, v):
        pattern=re.compile(r"^[0-9]+(\.[0-9]+){0,3}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid clause_reference format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid clause_reference format: {v}"
            raise ValueError(err_msg)
        return v


class Inference(NamedEntity):
    """
    Act of deriving conclusions, predictions or recommendations from a model or knowledge base (Clause 3.1.17).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/iso22989',
         'in_subset': ['ai_functional_view']})

    inference_strategy: Optional[str] = Field(default=None, description="""Strategy used (forward-chaining, backward-chaining, probabilistic, neural forward pass).""", json_schema_extra = { "linkml_meta": {'domain_of': ['InferenceEngine', 'Inference']} })
    performed_by: Optional[str] = Field(default=None, description="""Engine that performed the inference.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Inference']} })
    over_model: Optional[str] = Field(default=None, description="""Model over which the inference was performed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Inference']} })
    produced_output: Optional[str] = Field(default=None, description="""Serialised representation of the inference output.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Inference']} })
    id: str = Field(default=..., description="""Unique CURIE or URI identifying the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:identifier'} })
    name: str = Field(default=..., description="""Human-readable label for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['dcterms:title', 'schema:name'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Free-text description of the entity (paraphrased; verbatim ISO text excluded).""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:description'} })
    clause_reference: Optional[str] = Field(default=None, description="""ISO/IEC 22989:2022 clause identifier (e.g. \"5.11.4\") the element corresponds to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'AutonomyAssessment',
                       'VerificationValidationFramework']} })
    aliases: Optional[list[str]] = Field(default=None, description="""Alternative names or synonyms for the term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:altLabel'} })
    preferred_label: Optional[str] = Field(default=None, description="""Preferred natural-language label.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:prefLabel'} })
    see_also_uri: Optional[list[str]] = Field(default=None, description="""Pointers to related external resources or term records.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:seeAlso'} })

    @field_validator('clause_reference')
    def pattern_clause_reference(cls, v):
        pattern=re.compile(r"^[0-9]+(\.[0-9]+){0,3}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid clause_reference format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid clause_reference format: {v}"
            raise ValueError(err_msg)
        return v


class OECDLifecycleMapping(NamedEntity):
    """
    Informative mapping between an ISO/IEC 22989 life-cycle stage and an OECD life-cycle stage (Annex A).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/iso22989',
         'in_subset': ['ai_lifecycle']})

    iso_stage: AILifecycleStage = Field(default=..., description="""ISO/IEC 22989 life-cycle stage.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OECDLifecycleMapping']} })
    oecd_stage: OECDLifecycleStage = Field(default=..., description="""Corresponding OECD life-cycle stage.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OECDLifecycleMapping']} })
    mapping_notes: Optional[str] = Field(default=None, description="""Free-text notes on the mapping relationship.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OECDLifecycleMapping']} })
    id: str = Field(default=..., description="""Unique CURIE or URI identifying the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:identifier'} })
    name: str = Field(default=..., description="""Human-readable label for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['dcterms:title', 'schema:name'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Free-text description of the entity (paraphrased; verbatim ISO text excluded).""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:description'} })
    clause_reference: Optional[str] = Field(default=None, description="""ISO/IEC 22989:2022 clause identifier (e.g. \"5.11.4\") the element corresponds to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'AutonomyAssessment',
                       'VerificationValidationFramework']} })
    aliases: Optional[list[str]] = Field(default=None, description="""Alternative names or synonyms for the term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:altLabel'} })
    preferred_label: Optional[str] = Field(default=None, description="""Preferred natural-language label.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:prefLabel'} })
    see_also_uri: Optional[list[str]] = Field(default=None, description="""Pointers to related external resources or term records.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:seeAlso'} })

    @field_validator('clause_reference')
    def pattern_clause_reference(cls, v):
        pattern=re.compile(r"^[0-9]+(\.[0-9]+){0,3}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid clause_reference format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid clause_reference format: {v}"
            raise ValueError(err_msg)
        return v


class Organization(NamedEntity):
    """
    Organisation that establishes and operates an AI management system; Annex SL harmonised anchor shared across ISO management-system standards (ISO/IEC 42001, ISO/IEC 27001).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['gist_linkml:Organization',
                            'iso27001:Organization',
                            'iso42001:Organization'],
         'from_schema': 'https://w3id.org/lmodel/iso22989'})

    id: str = Field(default=..., description="""Unique CURIE or URI identifying the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:identifier'} })
    name: str = Field(default=..., description="""Human-readable label for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['dcterms:title', 'schema:name'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Free-text description of the entity (paraphrased; verbatim ISO text excluded).""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:description'} })
    clause_reference: Optional[str] = Field(default=None, description="""ISO/IEC 22989:2022 clause identifier (e.g. \"5.11.4\") the element corresponds to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'AutonomyAssessment',
                       'VerificationValidationFramework']} })
    aliases: Optional[list[str]] = Field(default=None, description="""Alternative names or synonyms for the term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:altLabel'} })
    preferred_label: Optional[str] = Field(default=None, description="""Preferred natural-language label.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:prefLabel'} })
    see_also_uri: Optional[list[str]] = Field(default=None, description="""Pointers to related external resources or term records.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:seeAlso'} })

    @field_validator('clause_reference')
    def pattern_clause_reference(cls, v):
        pattern=re.compile(r"^[0-9]+(\.[0-9]+){0,3}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid clause_reference format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid clause_reference format: {v}"
            raise ValueError(err_msg)
        return v


class InterestedParty(NamedEntity):
    """
    Person or organisation that can affect, be affected by, or perceive itself to be affected by a decision or activity; Annex SL harmonised stakeholder anchor shared across ISO management-system standards.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['iso27001:InterestedParty', 'iso42001:InterestedParty'],
         'from_schema': 'https://w3id.org/lmodel/iso22989'})

    id: str = Field(default=..., description="""Unique CURIE or URI identifying the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:identifier'} })
    name: str = Field(default=..., description="""Human-readable label for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'exact_mappings': ['dcterms:title', 'schema:name'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Free-text description of the entity (paraphrased; verbatim ISO text excluded).""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:description'} })
    clause_reference: Optional[str] = Field(default=None, description="""ISO/IEC 22989:2022 clause identifier (e.g. \"5.11.4\") the element corresponds to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'AutonomyAssessment',
                       'VerificationValidationFramework']} })
    aliases: Optional[list[str]] = Field(default=None, description="""Alternative names or synonyms for the term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:altLabel'} })
    preferred_label: Optional[str] = Field(default=None, description="""Preferred natural-language label.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'skos:prefLabel'} })
    see_also_uri: Optional[list[str]] = Field(default=None, description="""Pointers to related external resources or term records.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:seeAlso'} })

    @field_validator('clause_reference')
    def pattern_clause_reference(cls, v):
        pattern=re.compile(r"^[0-9]+(\.[0-9]+){0,3}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid clause_reference format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid clause_reference format: {v}"
            raise ValueError(err_msg)
        return v


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
NamedEntity.model_rebuild()
Term.model_rebuild()
AITerm.model_rebuild()
DataTerm.model_rebuild()
MachineLearningTerm.model_rebuild()
NeuralNetworkTerm.model_rebuild()
TrustworthinessTerm.model_rebuild()
NLPTerm.model_rebuild()
ComputerVisionTerm.model_rebuild()
AbbreviatedTerm.model_rebuild()
AIConcept.model_rebuild()
AIAgent.model_rebuild()
KnowledgeRepresentation.model_rebuild()
AISystem.model_rebuild()
AIComponent.model_rebuild()
AIModel.model_rebuild()
NeuralNetworkModel.model_rebuild()
Dataset.model_rebuild()
TrustworthinessProperty.model_rebuild()
AILifecycleProcess.model_rebuild()
AIStakeholderRole.model_rebuild()
AIProvider.model_rebuild()
AIProducer.model_rebuild()
AICustomer.model_rebuild()
AIPartner.model_rebuild()
AISubject.model_rebuild()
RelevantAuthority.model_rebuild()
AIEcosystem.model_rebuild()
ResourcePool.model_rebuild()
NLPComponent.model_rebuild()
ComputerVisionFunction.model_rebuild()
AIApplication.model_rebuild()
Task.model_rebuild()
Prediction.model_rebuild()
Decision.model_rebuild()
Action.model_rebuild()
InferenceEngine.model_rebuild()
KnowledgeGraph.model_rebuild()
ExpertSystem.model_rebuild()
CognitiveComputingSystem.model_rebuild()
SemanticComputingSystem.model_rebuild()
SoftComputingSystem.model_rebuild()
DataProcess.model_rebuild()
DataSample.model_rebuild()
DataLabel.model_rebuild()
GroundTruthRecord.model_rebuild()
Robot.model_rebuild()
IoTDevice.model_rebuild()
IoTSystem.model_rebuild()
CyberPhysicalSystem.model_rebuild()
AbbreviationEntry.model_rebuild()
AIConceptsCollection.model_rebuild()
AIPlatformProvider.model_rebuild()
AIServiceProductProvider.model_rebuild()
ModelDesigner.model_rebuild()
ModelImplementer.model_rebuild()
ComputationVerifier.model_rebuild()
ModelVerifier.model_rebuild()
AIUser.model_rebuild()
AISystemIntegrator.model_rebuild()
DataProvider.model_rebuild()
AIAuditor.model_rebuild()
AIEvaluator.model_rebuild()
DataSubject.model_rebuild()
PolicyMaker.model_rebuild()
Regulator.model_rebuild()
AutonomyAssessment.model_rebuild()
VerificationValidationFramework.model_rebuild()
HumanMachineTeam.model_rebuild()
IntelligenceAugmentation.model_rebuild()
Recommendation.model_rebuild()
EvaluationMetric.model_rebuild()
Threshold.model_rebuild()
Neuron.model_rebuild()
ConvolutionOperation.model_rebuild()
DataDrift.model_rebuild()
CatastrophicForgetting.model_rebuild()
FaultToleranceMechanism.model_rebuild()
NaturalLanguage.model_rebuild()
RiskItem.model_rebuild()
InputData.model_rebuild()
Inference.model_rebuild()
OECDLifecycleMapping.model_rebuild()
Organization.model_rebuild()
InterestedParty.model_rebuild()
