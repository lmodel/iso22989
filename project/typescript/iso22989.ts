export type NamedEntityId = string;
export type TermId = string;
export type AITermId = string;
export type DataTermId = string;
export type MachineLearningTermId = string;
export type NeuralNetworkTermId = string;
export type TrustworthinessTermId = string;
export type NLPTermId = string;
export type ComputerVisionTermId = string;
export type AbbreviatedTermId = string;
export type AIConceptId = string;
export type AIAgentId = string;
export type KnowledgeRepresentationId = string;
export type AISystemId = string;
export type AIComponentId = string;
export type AIModelId = string;
export type NeuralNetworkModelId = string;
export type DatasetId = string;
export type TrustworthinessPropertyId = string;
export type AILifecycleProcessId = string;
export type AIStakeholderRoleId = string;
export type AIProviderId = string;
export type AIProducerId = string;
export type AICustomerId = string;
export type AIPartnerId = string;
export type AISubjectId = string;
export type RelevantAuthorityId = string;
export type AIEcosystemId = string;
export type ResourcePoolId = string;
export type NLPComponentId = string;
export type ComputerVisionFunctionId = string;
export type AIApplicationId = string;
export type TaskId = string;
export type PredictionId = string;
export type DecisionId = string;
export type ActionId = string;
export type InferenceEngineId = string;
export type KnowledgeGraphId = string;
export type ExpertSystemId = string;
export type CognitiveComputingSystemId = string;
export type SemanticComputingSystemId = string;
export type SoftComputingSystemId = string;
export type DataProcessId = string;
export type DataSampleId = string;
export type DataLabelId = string;
export type GroundTruthRecordId = string;
export type RobotId = string;
export type IoTDeviceId = string;
export type IoTSystemId = string;
export type CyberPhysicalSystemId = string;
export type AbbreviationEntryId = string;
export type AIPlatformProviderId = string;
export type AIServiceProductProviderId = string;
export type ModelDesignerId = string;
export type ModelImplementerId = string;
export type ComputationVerifierId = string;
export type ModelVerifierId = string;
export type AIUserId = string;
export type AISystemIntegratorId = string;
export type DataProviderId = string;
export type AIAuditorId = string;
export type AIEvaluatorId = string;
export type DataSubjectId = string;
export type PolicyMakerId = string;
export type RegulatorId = string;
export type AutonomyAssessmentId = string;
export type VerificationValidationFrameworkId = string;
export type HumanMachineTeamId = string;
export type IntelligenceAugmentationId = string;
export type RecommendationId = string;
export type EvaluationMetricId = string;
export type ThresholdId = string;
export type NeuronId = string;
export type ConvolutionOperationId = string;
export type DataDriftId = string;
export type CatastrophicForgettingId = string;
export type FaultToleranceMechanismId = string;
export type NaturalLanguageId = string;
export type RiskItemId = string;
export type InputDataId = string;
export type InferenceId = string;
export type OECDLifecycleMappingId = string;
export type OrganizationId = string;
export type InterestedPartyId = string;
/**
* High-level capability classification of an AI system, from narrow (single-task) through general (broad cross-domain) systems and the historical strong/weak AI distinction in Clause 5.2.
*/
export enum AISystemType {
    
    /** AI system designed and deployed for a single, well-bounded task. */
    narrow_ai = "narrow_ai",
    /** Hypothetical AI system able to perform any cognitive task a human can perform. */
    general_ai = "general_ai",
    /** Historical term largely overlapping with narrow AI; emphasises tool-like behaviour. */
    weak_ai = "weak_ai",
    /** Historical term largely overlapping with general AI; emphasises human-equivalent cognition. */
    strong_ai = "strong_ai",
};
/**
* The symbolic vs subsymbolic axis used in Clause 5.9 to classify AI reasoning techniques.
*/
export enum SymbolicApproach {
    
    /** Approaches that manipulate explicit symbolic representations (rules, logic, knowledge graphs). */
    symbolic = "symbolic",
    /** Approaches that operate on distributed numeric representations (neural networks, statistical models). */
    subsymbolic = "subsymbolic",
    /** Approaches that combine symbolic and subsymbolic techniques (neuro-symbolic AI). */
    hybrid = "hybrid",
};
/**
* Top-level machine-learning paradigms enumerated in Clause 5.11.
*/
export enum MachineLearningParadigm {
    
    /** Learning from labelled input-output examples. */
    supervised = "supervised",
    /** Learning structure from unlabelled data (clustering, density estimation, dimensionality reduction). */
    unsupervised = "unsupervised",
    /** Learning from a mixture of labelled and unlabelled data. */
    semi_supervised = "semi_supervised",
    /** Learning policies by interaction with an environment that issues rewards. */
    reinforcement = "reinforcement",
    /** Reusing knowledge learned on one task to accelerate learning on a related task. */
    transfer = "transfer",
    /** Learning representations from data using auxiliary tasks derived from the data itself. */
    self_supervised = "self_supervised",
};
/**
* Example machine-learning algorithm families enumerated in Clause 5.12.
*/
export enum MLAlgorithmFamily {
    
    /** Networks of interconnected processing units (artificial neurons) trained by gradient methods. */
    neural_network = "neural_network",
    /** Probabilistic graphical models encoding conditional dependencies between variables. */
    bayesian_network = "bayesian_network",
    /** Tree-structured models splitting the input space on feature thresholds. */
    decision_tree = "decision_tree",
    /** Margin-maximising classifiers operating in (possibly kernelised) feature spaces. */
    support_vector_machine = "support_vector_machine",
    /** Population-based optimisation inspired by biological evolution (Clause 5.8). */
    genetic_algorithm = "genetic_algorithm",
};
/**
* Degree of system autonomy as discussed in Clause 5.13 (autonomy, heteronomy and automation). Encodes both the qualitative axis (autonomous / heteronomous / automated) and the six-level operational autonomy gradient widely used by ISO/IEC JTC 1/SC 42 work products.
*/
export enum AutonomyLevel {
    
    /** System executes a fixed predefined behaviour without runtime adaptation. */
    automated = "automated",
    /** System operates under external direction or supervision. */
    heteronomous = "heteronomous",
    /** System pursues goals using its own decision-making within a defined operating envelope. */
    autonomous = "autonomous",
    /** Human performs all tasks; no autonomous functionality (Clause 5.13). */
    level_0_no_automation = "level_0_no_automation",
    /** System assists the operator with one or more specific tasks. */
    level_1_assistance = "level_1_assistance",
    /** System performs some sub-functions; operator retains overall control. */
    level_2_partial_automation = "level_2_partial_automation",
    /** System handles defined tasks but expects the operator to intervene when requested. */
    level_3_conditional_automation = "level_3_conditional_automation",
    /** System performs the mission within a defined operating envelope without operator intervention. */
    level_4_high_automation = "level_4_high_automation",
    /** System performs the entire mission autonomously across all conditions. */
    level_5_full_automation = "level_5_full_automation",
};
/**
* Properties contributing to AI trustworthiness, enumerated in Clause 5.15 (robustness, reliability, resilience, controllability, explainability, predictability, transparency, fairness and bias-related properties).
*/
export enum TrustworthinessPropertyType {
    
    /** Ability to maintain performance under varied or adversarial conditions. */
    robustness = "robustness",
    /** Consistent intended behaviour over time under stated conditions. */
    reliability = "reliability",
    /** Ability to recover acceptable behaviour after disruption or failure. */
    resilience = "resilience",
    /** Property of allowing authorised humans to intervene in system behaviour. */
    controllability = "controllability",
    /** Property of producing explanations of system behaviour that are intelligible to relevant audiences. */
    explainability = "explainability",
    /** Property of behaviour being anticipatable given known inputs and state. */
    predictability = "predictability",
    /** Property of disclosing meaningful information about the system to interested parties. */
    transparency = "transparency",
    /** Property of avoiding inappropriate or harmful discrimination across groups. */
    fairness = "fairness",
    /** Property of identifying and reducing unwanted bias in data, models or outcomes. */
    bias_mitigation = "bias_mitigation",
    /** Property of having identifiable parties answerable for system behaviour and outcomes. */
    accountability = "accountability",
    /** Property of respecting personal data and individual privacy expectations. */
    privacy = "privacy",
    /** Property of not causing unacceptable risk of harm to people, property or environment. */
    safety = "safety",
    /** Property of being accessible and usable on demand by authorised entities (Clause 5.15.3 context). */
    availability = "availability",
    /** Property of safeguarding accuracy and completeness of data, models and outputs (Clause 5.15 Note). */
    integrity = "integrity",
    /** Property of being able to verify the origin and identity of inputs, models and outputs (Clause 5.15 Note). */
    authenticity = "authenticity",
    /** Property of preserving confidentiality, integrity and availability of the AI system and its data (Clause 5.15 context). */
    security = "security",
    /** Property of being effectively, efficiently and satisfactorily usable by the intended users (Clause 5.15 Note). */
    usability = "usability",
    /** Aggregate property reflecting how well the AI system meets stated and implied needs (Clause 5.15 Note). */
    quality = "quality",
    /** Property of continuing to operate correctly in the presence of component faults (Clause 5.15.4 context). */
    fault_tolerance = "fault_tolerance",
};
/**
* Categories of bias relevant to AI systems as discussed in Clause 5.15.9 and ISO/IEC TR 24027.
*/
export enum BiasType {
    
    /** Bias introduced through sampling, labelling or representation of training data. */
    data_bias = "data_bias",
    /** Bias introduced through model or algorithm choice and parameterisation. */
    algorithmic_bias = "algorithmic_bias",
    /** Bias reflecting structural inequalities in the data-generating environment. */
    societal_bias = "societal_bias",
    /** Bias introduced through human cognition during design, labelling or interpretation. */
    cognitive_bias = "cognitive_bias",
    /** Tendency of users to over-rely on automated outputs. */
    automation_bias = "automation_bias",
};
/**
* AI system life-cycle stages identified in Clause 6.2.
*/
export enum AILifecycleStage {
    
    /** Identification of need, opportunity and high-level objectives for the AI system. */
    inception = "inception",
    /** Architecture, model selection, data preparation, training and integration activities. */
    design_and_development = "design_and_development",
    /** Evidence-gathering activities establishing that the system meets specified requirements. */
    verification_and_validation = "verification_and_validation",
    /** Release of the AI system into its operational environment. */
    deployment = "deployment",
    /** Routine use of the AI system with ongoing observation of behaviour and performance. */
    operation_and_monitoring = "operation_and_monitoring",
    /** Ongoing checks that the system continues to meet validation criteria during operation. */
    continuous_validation = "continuous_validation",
    /** Periodic or event-triggered reassessment of the system, often leading to retraining or redesign. */
    re_evaluation = "re_evaluation",
    /** Decommissioning of the AI system and management of residual data and artefacts. */
    retirement = "retirement",
};
/**
* Functional building blocks of an AI system as introduced in Clause 7.
*/
export enum AIFunctionalComponent {
    
    /** Data acquisition, storage and information management functions. */
    data_and_information = "data_and_information",
    /** Functions producing or maintaining knowledge representations and learned models. */
    knowledge_and_learning = "knowledge_and_learning",
    /** Functions producing predictions from inputs using a trained model or knowledge base. */
    prediction = "prediction",
    /** Functions selecting a course of action based on predictions and constraints. */
    decision = "decision",
    /** Functions enacting decisions on the environment or downstream systems. */
    action = "action",
};
/**
* AI stakeholder roles enumerated in Clause 5.19.
*/
export enum AIStakeholderRoleType {
    
    /** Party that makes an AI system available to AI customers. */
    ai_provider = "ai_provider",
    /** Party that designs, develops or assembles AI systems or components. */
    ai_producer = "ai_producer",
    /** Party that uses an AI system or a service backed by an AI system. */
    ai_customer = "ai_customer",
    /** Party providing services that support the AI life cycle (data brokers, integrators, evaluators). */
    ai_partner = "ai_partner",
    /** Person or group whose data is used by, or who is otherwise affected by, the AI system. */
    ai_subject = "ai_subject",
    /** Body with regulatory, supervisory or standards-setting responsibility for AI. */
    relevant_authority = "relevant_authority",
};
/**
* Non-learning engineering approaches contributing to AI, from Clause 8.5.
*/
export enum EngineeringApproach {
    
    /** Rule-based system encoding domain expertise (Clause 8.5.2). */
    expert_system = "expert_system",
    /** Programming paradigm based on formal logic (Clause 8.5.3). */
    logic_programming = "logic_programming",
    /** Graph-structured knowledge representation used for reasoning and retrieval. */
    knowledge_graph = "knowledge_graph",
    /** Solving problems by satisfying a set of declared constraints. */
    constraint_satisfaction = "constraint_satisfaction",
};
/**
* Categories of computing resource used by AI systems, drawn from Clauses 8.6 (cloud and edge computing) and 8.7 (resource pools).
*/
export enum ComputingResourceType {
    
    /** Centralised, elastically provisioned computing resources accessed over a network. */
    cloud = "cloud",
    /** Computing resources located close to data sources or end users. */
    edge = "edge",
    /** Computing resources owned and operated within the organisation's own facilities. */
    on_premises = "on_premises",
    /** General-purpose central-processing-unit compute capacity. */
    cpu = "cpu",
    /** Graphics-processing-unit compute capacity, commonly used for neural network training and inference. */
    gpu = "gpu",
    /** Tensor-processing-unit or similar accelerator specialised for ML workloads. */
    tpu = "tpu",
    /** Application-specific integrated circuit designed for a fixed AI workload (Clause 8.7.2). */
    asic = "asic",
    /** Field-programmable gate array offering reconfigurable hardware acceleration. */
    fpga = "fpga",
    /** Neural-network processing unit specialised for neural-network inference and training. */
    npu = "npu",
    /** Digital signal processor used to accelerate signal-processing workloads. */
    dsp = "dsp",
};
/**
* Modalities of input data handled by AI systems, drawn from the data, NLP and CV terminology sections (Clauses 3.2, 3.6, 3.7).
*/
export enum DataModality {
    
    /** Tabular or relational data with an explicit schema. */
    structured = "structured",
    /** Data with self-describing structure such as JSON, XML or graph formats. */
    semi_structured = "semi_structured",
    /** Data without an explicit schema (free text, images, audio, video). */
    unstructured = "unstructured",
    /** Natural-language text data. */
    text = "text",
    /** Two-dimensional visual data. */
    image = "image",
    /** Temporal sequences of visual frames. */
    video = "video",
    /** Acoustic signal data. */
    audio = "audio",
    /** Telemetry or measurement data from physical sensors. */
    sensor = "sensor",
    /** Ordered observations indexed by time. */
    time_series = "time_series",
    /** Data represented as nodes and edges. */
    graph = "graph",
};
/**
* Role a dataset plays in a machine-learning workflow, drawn from Clauses 5.11.6–5.11.8.
*/
export enum DatasetRole {
    
    /** Dataset used to fit model parameters. */
    training = "training",
    /** Dataset used to tune hyperparameters and select among candidate models. */
    validation = "validation",
    /** Dataset used for a final unbiased estimate of model performance. */
    test = "test",
    /** Live data observed during operational deployment. */
    production = "production",
    /** Curated dataset used as a benchmark across experiments. */
    reference = "reference",
};
/**
* Components of a natural-language-processing pipeline as enumerated in Clauses 3.6 and 9.2.
*/
export enum NLPComponentType {
    
    /** Segmenting text into tokens such as words or subwords. */
    tokenisation = "tokenisation",
    /** Reducing tokens to their canonical dictionary form. */
    lemmatisation = "lemmatisation",
    /** Assigning grammatical category labels to tokens. */
    part_of_speech_tagging = "part_of_speech_tagging",
    /** Producing syntactic structure for sentences. */
    syntactic_parsing = "syntactic_parsing",
    /** Deriving meaning representations from text. */
    semantic_analysis = "semantic_analysis",
    /** Identifying and classifying named entities in text. */
    named_entity_recognition = "named_entity_recognition",
    /** Estimating subjective polarity or affect in text. */
    sentiment_analysis = "sentiment_analysis",
    /** Automatically translating text between natural languages. */
    machine_translation = "machine_translation",
    /** Converting acoustic speech signals into text. */
    speech_recognition = "speech_recognition",
    /** Generating speech audio from text. */
    speech_synthesis = "speech_synthesis",
    /** Deriving structured meaning, intent or entities from natural-language input (Clause 9.2). */
    natural_language_understanding = "natural_language_understanding",
    /** Producing natural-language output from structured inputs (Clause 9.2). */
    natural_language_generation = "natural_language_generation",
    /** Producing condensed summaries of longer text (Clause 3.6.1). */
    automatic_summarization = "automatic_summarization",
    /** Controlling multi-turn conversational interaction (Clause 9.2.2). */
    dialogue_management = "dialogue_management",
    /** Finding relevant documents or passages in a collection in response to a query. */
    information_retrieval = "information_retrieval",
    /** Producing direct answers to natural-language questions. */
    question_answering = "question_answering",
    /** Identifying typed relationships between entities mentioned in text. */
    relationship_extraction = "relationship_extraction",
    /** Detecting affective or emotional state expressed in text or speech. */
    emotion_recognition = "emotion_recognition",
    /** Converting images of printed or handwritten text into machine-readable text (Clause 3.6.12). */
    optical_character_recognition = "optical_character_recognition",
    /** Linking mentions in text that refer to the same entity. */
    coreference_resolution = "coreference_resolution",
};
/**
* Computer-vision tasks drawn from Clauses 3.7 and 9.1.
*/
export enum ComputerVisionTask {
    
    /** Assigning a class label to an image. */
    image_classification = "image_classification",
    /** Localising and classifying objects within an image. */
    object_detection = "object_detection",
    /** Assigning a class label to each pixel in an image. */
    semantic_segmentation = "semantic_segmentation",
    /** Assigning labels to pixels grouped by individual object instance. */
    instance_segmentation = "instance_segmentation",
    /** General recognition of image content, including faces and scenes. */
    image_recognition = "image_recognition",
    /** Estimating the spatial pose of objects or persons. */
    pose_estimation = "pose_estimation",
    /** Extracting machine-readable text from images of printed or handwritten content. */
    optical_character_recognition = "optical_character_recognition",
    /** Identifying or verifying persons from facial images (Clause 3.7.2). */
    face_recognition = "face_recognition",
    /** Classifying the type of scene or environment depicted in an image. */
    scene_recognition = "scene_recognition",
    /** Following the position of objects across successive frames in video. */
    motion_tracking = "motion_tracking",
    /** Identifying visual patterns that deviate from expected behaviour. */
    visual_anomaly_detection = "visual_anomaly_detection",
    /** Recovering three-dimensional structure from one or more images. */
    three_d_reconstruction = "three_d_reconstruction",
    /** Recognising discrete actions performed in video. */
    action_recognition = "action_recognition",
    /** Recognising higher-level activities composed of multiple actions in video. */
    activity_recognition = "activity_recognition",
};
/**
* Sub-fields of AI referenced in Clause 9.
*/
export enum AIField {
    
    /** AI sub-field concerned with interpreting visual information. */
    computer_vision = "computer_vision",
    /** AI sub-field concerned with processing and generating human language. */
    natural_language_processing = "natural_language_processing",
    /** Extraction of patterns and knowledge from large data sets. */
    data_mining = "data_mining",
    /** AI sub-field concerned with sequencing actions to achieve goals. */
    planning = "planning",
    /** AI sub-field concerned with embodied autonomous systems. */
    robotics = "robotics",
    /** AI sub-field concerned with explicit representation and inference over knowledge. */
    knowledge_representation_and_reasoning = "knowledge_representation_and_reasoning",
    /** AI sub-field concerned with processing and producing speech signals. */
    speech_processing = "speech_processing",
    /** AI sub-field concerned with coordination and interaction among multiple agents. */
    multi_agent_systems = "multi_agent_systems",
};
/**
* Example AI application domains presented in Clause 10.
*/
export enum AIApplicationDomain {
    
    /** Identification of fraudulent transactions or behaviours (Clause 10.2). */
    fraud_detection = "fraud_detection",
    /** AI capabilities used in self-driving or driver-assistance systems (Clause 10.3). */
    automated_vehicles = "automated_vehicles",
    /** Anticipating equipment failures from sensor data (Clause 10.4). */
    predictive_maintenance = "predictive_maintenance",
    /** Personalised recommendation of items or actions. */
    recommendation = "recommendation",
    /** AI-assisted diagnostic decision support in healthcare. */
    medical_diagnosis = "medical_diagnosis",
    /** AI-generated text, images, audio or other media. */
    content_generation = "content_generation",
    /** AI applications in farming, crop and livestock management (Clause 10.1). */
    agriculture = "agriculture",
    /** AI applications in vehicle design, manufacture and in-vehicle services (Clause 10.1). */
    automotive = "automotive",
    /** AI applications in banking, finance and capital markets (Clause 10.1). */
    banking_and_finance = "banking_and_finance",
    /** AI applications in defence and physical security (Clause 10.1). */
    defense_and_security = "defense_and_security",
    /** AI applications in learning, teaching and assessment (Clause 10.1). */
    education = "education",
    /** AI applications in energy generation, distribution and consumption (Clause 10.1). */
    energy_and_utilities = "energy_and_utilities",
    /** AI applications in clinical care and health management (Clause 10.1). */
    healthcare = "healthcare",
    /** AI applications in legal research, contracting and compliance (Clause 10.1). */
    legal_services = "legal_services",
    /** AI applications in industrial production (Clause 10.1). */
    manufacturing = "manufacturing",
    /** AI applications in media production, distribution and recommendation (Clause 10.1). */
    media_and_entertainment = "media_and_entertainment",
    /** AI applications in virtual, augmented and mixed reality (Clause 10.1). */
    mixed_reality = "mixed_reality",
    /** AI applications in government and public administration (Clause 10.1). */
    public_sector = "public_sector",
    /** AI applications in retail and e-commerce (Clause 10.1). */
    retail = "retail",
    /** AI applications in space exploration and operations (Clause 10.1). */
    space = "space",
    /** AI applications in telecommunications networks and services (Clause 10.1). */
    telecommunications = "telecommunications",
};
/**
* OECD AI system life-cycle stages used in the informative mapping of Annex A.
*/
export enum OECDLifecycleStage {
    
    /** OECD stage covering planning and design activities. */
    plan_and_design = "plan_and_design",
    /** OECD stage covering data collection and processing. */
    collect_and_process_data = "collect_and_process_data",
    /** OECD stage covering model building and inference. */
    build_and_use_model = "build_and_use_model",
    /** OECD stage covering verification and validation. */
    verify_and_validate = "verify_and_validate",
    /** OECD stage covering deployment of the AI system. */
    deploy = "deploy",
    /** OECD stage covering operation and monitoring of the AI system. */
    operate_and_monitor = "operate_and_monitor",
};
/**
* Categories of jurisdictional issue surfaced in Clause 5.17.
*/
export enum JurisdictionalIssueType {
    
    /** Constraints on the geographical location of stored or processed data. */
    data_residency = "data_residency",
    /** Constraints on movement of data or AI outputs across legal jurisdictions. */
    cross_border_transfer = "cross_border_transfer",
    /** Allocation of legal responsibility for AI-system actions and outcomes. */
    liability = "liability",
    /** Conformity with applicable AI-specific or sector-specific regulations. */
    regulatory_compliance = "regulatory_compliance",
    /** Ownership and licensing of training data, models and outputs. */
    intellectual_property = "intellectual_property",
};
/**
* Categories of societal impact discussed in Clause 5.18.
*/
export enum SocietalImpactCategory {
    
    /** Effects on labour markets and the nature of work. */
    employment = "employment",
    /** Effects on the exercise of fundamental human rights. */
    human_rights = "human_rights",
    /** Environmental footprint of AI development and deployment. */
    environment = "environment",
    /** Effects on political discourse, elections and civic participation. */
    democratic_processes = "democratic_processes",
    /** Differential access to and impact of AI systems across populations. */
    digital_divide = "digital_divide",
};
/**
* Architectural families of neural networks enumerated across Clause 3.4 and Clause 5.12.1.
*/
export enum NeuralNetworkArchitecture {
    
    /** Feed-forward neural network with unidirectional information flow (Clause 3.4.6). */
    feed_forward = "feed_forward",
    /** Recurrent neural network with feedback connections (Clause 3.4.10). */
    recurrent = "recurrent",
    /** LSTM recurrent architecture mitigating short memory in plain RNNs (Clause 3.4.7). */
    long_short_term_memory = "long_short_term_memory",
    /** GRU recurrent architecture, a simplified gating variant of LSTM. */
    gated_recurrent_unit = "gated_recurrent_unit",
    /** Convolutional neural network using local receptive fields (Clause 3.4.2). */
    convolutional = "convolutional",
    /** Attention-based architecture used for sequence modelling. */
    transformer = "transformer",
    /** Encoder-decoder architecture trained to reconstruct inputs for representation learning. */
    autoencoder = "autoencoder",
    /** Adversarial pairing of generator and discriminator networks. */
    generative_adversarial = "generative_adversarial",
    /** Neural network with many hidden layers (deep learning, Clause 3.4.4). */
    deep = "deep",
};
/**
* Training-time phenomena that affect neural-network learning, drawn from Clause 3.4.
*/
export enum NeuralNetworkPhenomenon {
    
    /** Gradient signal shrinks across layers during back-propagation, slowing learning. */
    vanishing_gradient = "vanishing_gradient",
    /** Gradient signal grows without bound across layers during back-propagation (Clause 3.4.5). */
    exploding_gradient = "exploding_gradient",
    /** Previously learned knowledge is lost when the network is retrained on new data. */
    catastrophic_forgetting = "catastrophic_forgetting",
    /** Model fits training data idiosyncrasies and fails to generalise. */
    overfitting = "overfitting",
    /** Model lacks capacity or training to capture the underlying signal. */
    underfitting = "underfitting",
};
/**
* Common activation functions used in neural networks (Clause 3.4.1).
*/
export enum ActivationFunctionType {
    
    /** Logistic sigmoid activation. */
    sigmoid = "sigmoid",
    /** Hyperbolic tangent activation. */
    tanh = "tanh",
    /** Rectified linear unit activation. */
    relu = "relu",
    /** Rectified linear unit with non-zero gradient below zero. */
    leaky_relu = "leaky_relu",
    /** Softmax activation producing a probability distribution. */
    softmax = "softmax",
    /** Identity / linear activation. */
    linear = "linear",
    /** Activation function not enumerated explicitly. */
    other = "other",
};
/**
* Agent architectures discussed in Clause 5.3 (agent paradigm).
*/
export enum AgentArchitectureType {
    
    /** Agent that maps current percepts directly to actions. */
    reflex_agent = "reflex_agent",
    /** Agent that maintains an internal model of the environment to guide action. */
    model_based_agent = "model_based_agent",
    /** Agent that selects actions to achieve explicit goals. */
    goal_based_agent = "goal_based_agent",
    /** Agent that selects actions to maximise an expected utility function. */
    utility_based_agent = "utility_based_agent",
    /** Agent that improves its behaviour through experience. */
    learning_agent = "learning_agent",
    /** Agent operating jointly with other agents in a shared environment. */
    multi_agent = "multi_agent",
};
/**
* Types of knowledge distinguished in Clause 3.1 and Clause 5.4 (declarative versus procedural knowledge, etc.).
*/
export enum KnowledgeType {
    
    /** Knowledge of facts and relationships (Clause 3.1.12). */
    declarative = "declarative",
    /** Knowledge of how to perform tasks (Clause 3.1.28). */
    procedural = "procedural",
    /** Implicit, experience-based knowledge that is hard to articulate. */
    tacit = "tacit",
    /** Background knowledge expected to be shared by typical humans. */
    common_sense = "common_sense",
    /** Knowledge specific to a particular application domain. */
    domain_specific = "domain_specific",
};
/**
* Data-handling processes enumerated in Clause 5.10 and Clause 3.2 (data acquisition, annotation, preparation, quality checking, sampling, augmentation, drift and poisoning handling, etc.).
*/
export enum DataProcessType {
    
    /** Collecting data from one or more sources. */
    data_acquisition = "data_acquisition",
    /** Initial profiling of a dataset to understand its characteristics (Clause 3.2.6). */
    exploratory_data_analysis = "exploratory_data_analysis",
    /** Adding labels or other metadata to data items (Clause 3.2.1). */
    data_annotation = "data_annotation",
    /** Assigning target labels to records for supervised learning. */
    data_labeling = "data_labeling",
    /** Transforming raw data into a form suitable for analysis or training. */
    data_preparation = "data_preparation",
    /** Detecting and correcting errors and inconsistencies in data. */
    data_cleaning = "data_cleaning",
    /** Removing data items that do not match selection criteria. */
    filtering = "filtering",
    /** Rescaling features to a common range or distribution. */
    normalisation = "normalisation",
    /** Removing or transforming personally identifiable information. */
    de_identification = "de_identification",
    /** Assessing completeness, accuracy, representativeness and bias of data (Clause 3.2.2). */
    data_quality_checking = "data_quality_checking",
    /** Selecting a subset of records from a larger population (Clause 3.2.4). */
    data_sampling = "data_sampling",
    /** Creating additional training examples via transformation of existing data (Clause 3.2.3). */
    data_augmentation = "data_augmentation",
    /** Constructing or selecting features used as model inputs. */
    feature_engineering = "feature_engineering",
    /** Replacing missing values with substituted estimates (Clause 3.2.8). */
    imputation = "imputation",
    /** Detecting changes in the statistical distribution of operational data. */
    data_drift_detection = "data_drift_detection",
    /** Identifying adversarial contamination of training data. */
    data_poisoning_detection = "data_poisoning_detection",
    /** Detecting and responding to changes in the relationship between inputs and target labels (Clause 5.11.9.1). */
    concept_drift_handling = "concept_drift_handling",
    /** Strategies to prevent loss of previously learned knowledge during retraining (Clause 5.11.9.1). */
    catastrophic_forgetting_mitigation = "catastrophic_forgetting_mitigation",
    /** Updating an existing trained model on new or revised data (Clause 5.11.9). */
    retraining = "retraining",
};
/**
* Categories of target label produced or consumed by ML workflows.
*/
export enum DataLabelType {
    
    /** Discrete unordered class labels. */
    categorical = "categorical",
    /** Two-class label (typically positive / negative). */
    binary = "binary",
    /** Discrete ordered labels. */
    ordinal = "ordinal",
    /** Continuous numeric target value. */
    numeric = "numeric",
    /** Composite or graph-structured label. */
    structured = "structured",
    /** Ordered sequence of label tokens (e.g. sequence labelling, structured prediction). */
    sequence = "sequence",
    /** Graph-structured label such as a parse tree or relational structure. */
    graph = "graph",
    /** No explicit label (unsupervised or self-supervised setting). */
    none = "none",
};
/**
* Categories of AI task addressed by AI systems, derived from the\n      machine-learning, NLP and computer-vision terminology in Clause 3.
*/
export enum TaskCategory {
    
    /** Assigning a class label to an input. */
    classification = "classification",
    /** Predicting a continuous numeric value. */
    regression = "regression",
    /** Grouping items by similarity without supervision. */
    clustering = "clustering",
    /** Ordering items by relevance or preference. */
    ranking = "ranking",
    /** Suggesting items to a user given context. */
    recommendation = "recommendation",
    /** Identifying inputs that deviate from expected behaviour. */
    anomaly_detection = "anomaly_detection",
    /** Producing a lower-dimensional representation of the data. */
    dimensionality_reduction = "dimensionality_reduction",
    /** Producing new content (text, images, audio, etc.). */
    generation = "generation",
    /** Producing a sequence of actions that achieve a goal. */
    planning = "planning",
    /** Selecting actions to influence a dynamical system. */
    control = "control",
    /** Producing recommendations or explanations to support human decisions. */
    decision_support = "decision_support",
};
/**
* Distinguishing characteristics of AI systems summarised in Clause 5.1.
*/
export enum AISystemCharacteristic {
    
    /** Engages in interaction with users or other systems. */
    interactive = "interactive",
    /** Adapts behaviour to its operational context. */
    contextual = "contextual",
    /** Adjusts behaviour over time in response to new data or feedback. */
    adaptive = "adaptive",
    /** Provides mechanisms for human oversight and intervention. */
    oversight_enabled = "oversight_enabled",
    /** Performance depends materially on the data used to build or operate the system. */
    data_dependent = "data_dependent",
};
/**
* Techniques grouped under soft computing in Clause 5.7.
*/
export enum SoftComputingTechnique {
    
    /** Reasoning with degrees of truth rather than crisp Boolean values. */
    fuzzy_logic = "fuzzy_logic",
    /** Optimisation inspired by biological evolution (including genetic algorithms). */
    evolutionary_computing = "evolutionary_computing",
    /** Optimisation inspired by collective behaviour of decentralised agents. */
    swarm_intelligence = "swarm_intelligence",
    /** Reasoning under uncertainty using probability theory. */
    probabilistic_reasoning = "probabilistic_reasoning",
    /** Computation realised by networks of artificial neurons. */
    neural_computing = "neural_computing",
};
/**
* Characteristics commonly used to describe big data sources in Clause 8.6.1.
*/
export enum BigDataCharacteristic {
    
    /** Total amount of data managed. */
    volume = "volume",
    /** Rate at which data is generated or processed. */
    velocity = "velocity",
    /** Range of data types and sources. */
    variety = "variety",
    /** Trustworthiness and accuracy of the data. */
    veracity = "veracity",
    /** Usefulness of the data for the intended purpose. */
    value = "value",
    /** Degree to which data characteristics change over time. */
    variability = "variability",
};
/**
* Roles played by devices in IoT and cyber-physical systems (Clause 5.14).
*/
export enum IoTDeviceRole {
    
    /** Device that observes the physical environment. */
    sensor = "sensor",
    /** Device that effects changes in the physical environment. */
    actuator = "actuator",
    /** Device that connects local IoT subnets to wider networks. */
    gateway = "gateway",
    /** Device providing local computation at the network edge. */
    edge_compute = "edge_compute",
    /** Device that supervises or coordinates other IoT devices. */
    controller = "controller",
};
/**
* Acronyms and abbreviations listed in Clause 4.
*/
export enum AbbreviationCode {
    
    /** Artificial intelligence. */
    AI = "AI",
    /** Application programming interface. */
    API = "API",
    /** Application-specific integrated circuit. */
    ASIC = "ASIC",
    /** Convolutional neural network. */
    CNN = "CNN",
    /** Cyber-physical system. */
    CPS = "CPS",
    /** Central processing unit. */
    CPU = "CPU",
    /** Cross-industry standard process for data mining. */
    CRISP_DM = "CRISP_DM",
    /** Deep neural network. */
    DNN = "DNN",
    /** Digital signal processor. */
    DSP = "DSP",
    /** Feed-forward neural network. */
    FFNN = "FFNN",
    /** Field-programmable gate array. */
    FPGA = "FPGA",
    /** Genetic algorithm. */
    GA = "GA",
    /** Graphics processing unit. */
    GPU = "GPU",
    /** Hidden Markov model. */
    HMM = "HMM",
    /** Internet of Things. */
    IoT = "IoT",
    /** Information retrieval. */
    IR = "IR",
    /** Information technology. */
    IT = "IT",
    /** Knowledge discovery in data. */
    KDD = "KDD",
    /** Long short-term memory. */
    LSTM = "LSTM",
    /** Machine learning. */
    ML = "ML",
    /** Machine translation. */
    MT = "MT",
    /** Named entity recognition. */
    NER = "NER",
    /** Natural language generation. */
    NLG = "NLG",
    /** Natural language processing. */
    NLP = "NLP",
    /** Natural language understanding. */
    NLU = "NLU",
    /** Neural network. */
    NN = "NN",
    /** Neural-network processing unit. */
    NPU = "NPU",
    /** Optical character recognition. */
    OCR = "OCR",
    /** Organisation for Economic Co-operation and Development. */
    OECD = "OECD",
    /** Personally identifiable information. */
    PII = "PII",
    /** Part of speech. */
    POS = "POS",
    /** Reinforcement learning. */
    RL = "RL",
    /** Recurrent neural network. */
    RNN = "RNN",
    /** Support vector machine. */
    SVM = "SVM",
};
/**
* Strategies for partitioning data and assessing generalisation, drawn from Clause 5.11.8 and Clause 5.16.
*/
export enum ValidationStrategy {
    
    /** Single train / validation / test split. */
    holdout = "holdout",
    /** Two-way split (train / test) used when data is limited (Clause 5.11.8). */
    two_way_split = "two_way_split",
    /** K-fold cross-validation. */
    cross_validation = "cross_validation",
    /** Cross-validation that preserves class distribution in each fold. */
    stratified_cross_validation = "stratified_cross_validation",
    /** Resampling-with-replacement estimation of generalisation error. */
    bootstrap = "bootstrap",
    /** Forward-chaining split that respects temporal order. */
    time_series_split = "time_series_split",
};
/**
* Levels of verifiability and validatability used to characterise an AI system in Clause 5.16.
*/
export enum VerificationValidationLevel {
    
    /** System behaviour is fully verifiable against specifications. */
    completely_verifiable = "completely_verifiable",
    /** System is partially verifiable and validatable against specifications. */
    partially_verifiable_validatable = "partially_verifiable_validatable",
    /** System is not verifiable but its behaviour can be validated empirically. */
    unverifiable_validatable = "unverifiable_validatable",
    /** System is not verifiable and only partially validatable. */
    unverifiable_partially_validatable = "unverifiable_partially_validatable",
    /** System is neither verifiable nor validatable with available techniques. */
    unverifiable_unvalidatable = "unverifiable_unvalidatable",
};
/**
* Classification of data sources discussed in Clause 8.6.1.
*/
export enum DataSourceType {
    
    /** Data collected directly by the organisation operating the AI system. */
    first_party = "first_party",
    /** Data shared by a partner organisation under agreement. */
    second_party = "second_party",
    /** Data acquired from an external data provider. */
    third_party = "third_party",
    /** Publicly available data released under an open licence. */
    open_data = "open_data",
    /** Data generated by simulation, sampling or generative models. */
    synthetic = "synthetic",
    /** Data assembled on demand from a union of underlying sources. */
    queried_union = "queried_union",
};
/**
* Methods of data collection enumerated in Clause 8.6.1.
*/
export enum DataCollectionMethod {
    
    /** Captured at the point of a commercial transaction. */
    point_of_sale = "point_of_sale",
    /** Collected through structured questionnaires. */
    survey = "survey",
    /** Collected as part of a designed research study. */
    research_study = "research_study",
    /** Captured by a physical sensor. */
    sensor_capture = "sensor_capture",
    /** Captured by an imaging device. */
    image_capture = "image_capture",
    /** Captured by an audio recording device. */
    audio_capture = "audio_capture",
    /** Extracted from text or document corpora. */
    document_extraction = "document_extraction",
    /** Harvested from publicly accessible web resources. */
    web_scraping = "web_scraping",
    /** Recorded from interactions with software or services. */
    interaction_log = "interaction_log",
    /** Recorded as a side effect of transactional systems. */
    transactional_log = "transactional_log",
};
/**
* Criteria contributing to the assessment of autonomy in Clause 5.13.\n      Each criterion is graded independently when assigning an\n      `AutonomyLevel`.
*/
export enum AutonomyCriterion {
    
    /** Degree to which an external operator supervises the system. */
    external_supervision = "external_supervision",
    /** Degree to which the system understands its operational context. */
    situated_understanding = "situated_understanding",
    /** Degree to which the system reacts to environmental changes. */
    reactivity = "reactivity",
    /** Span over which the system continues operating without intervention. */
    persistence = "persistence",
    /** Degree to which the system adapts behaviour to new conditions. */
    adaptability = "adaptability",
    /** Ability of the system to evaluate its own performance. */
    performance_evaluation = "performance_evaluation",
    /** Ability of the system to plan future actions proactively. */
    proactive_planning = "proactive_planning",
};
/**
* Sub-categorisation of hybrid neuro-symbolic approaches mentioned in\n      Clause 5.9.
*/
export enum NeuroSymbolicApproach {
    
    /** Symbolic reasoning embedded within a primarily subsymbolic architecture. */
    symbolic_in_neural = "symbolic_in_neural",
    /** Subsymbolic components invoked inside a symbolic reasoning framework. */
    neural_in_symbolic = "neural_in_symbolic",
    /** Symbolic and subsymbolic components share representations end-to-end. */
    tightly_coupled = "tightly_coupled",
    /** Symbolic and subsymbolic components exchange information at well-defined interfaces. */
    loosely_coupled = "loosely_coupled",
};
/**
* High-level categorisation of recommendations produced by an AI system\n      (Clauses 7.4, 10).
*/
export enum RecommendationOutcomeType {
    
    /** Suggestion of content items. */
    content_recommendation = "content_recommendation",
    /** Suggestion of an action to take. */
    action_recommendation = "action_recommendation",
    /** Recommendation expressed as a ranked list. */
    ranking_recommendation = "ranking_recommendation",
    /** Recommendation of the single most appropriate next action. */
    next_best_action = "next_best_action",
};
/**
* Execution status values for actions and processes.
*/
export enum ExecutionStatus {
    
    /** Execution has been planned but not yet started. */
    planned = "planned",
    /** Execution is currently in progress. */
    in_progress = "in_progress",
    /** Execution has completed successfully. */
    completed = "completed",
    /** Execution has terminated unsuccessfully. */
    failed = "failed",
    /** Execution was cancelled before completion. */
    cancelled = "cancelled",
};


/**
 * Abstract base class for any addressable entity in the schema, carrying identity, label and clause-reference metadata.
 */
export interface NamedEntity {
    /** Unique CURIE or URI identifying the entity. */
    id: string,
    /** Human-readable label for the entity. */
    name: string,
    /** Free-text description of the entity (paraphrased; verbatim ISO text excluded). */
    description?: string,
    /** ISO/IEC 22989:2022 clause identifier (e.g. "5.11.4") the element corresponds to. */
    clause_reference?: string,
    /** Alternative names or synonyms for the term. */
    aliases?: string[],
    /** Preferred natural-language label. */
    preferred_label?: string,
    /** Pointers to related external resources or term records. */
    see_also_uri?: string[],
}


/**
 * Abstract base class for a glossary term defined in Clause 3. Concrete subclasses partition the terminology along Clauses 3.1–3.7.
 */
export interface Term extends NamedEntity {
}


/**
 * Term defined in Clause 3.1 (terms related to AI).
 */
export interface AITerm extends Term {
}


/**
 * Term defined in Clause 3.2 (terms related to data).
 */
export interface DataTerm extends Term {
}


/**
 * Term defined in Clause 3.3 (terms related to machine learning).
 */
export interface MachineLearningTerm extends Term {
}


/**
 * Term defined in Clause 3.4 (terms related to neural networks).
 */
export interface NeuralNetworkTerm extends Term {
}


/**
 * Term defined in Clause 3.5 (terms related to trustworthiness).
 */
export interface TrustworthinessTerm extends Term {
}


/**
 * Term defined in Clause 3.6 (terms related to natural-language processing).
 */
export interface NLPTerm extends Term {
}


/**
 * Term defined in Clause 3.7 (terms related to computer vision).
 */
export interface ComputerVisionTerm extends Term {
}


/**
 * Abbreviation or acronym listed in Clause 4 with its expansion and optional definition reference.
 */
export interface AbbreviatedTerm extends NamedEntity {
    /** Expanded form of the abbreviation. */
    expansion: string,
}


/**
 * Abstract base for Clause 5 conceptual entities (agent, knowledge, cognition, autonomy, etc.).
 */
export interface AIConcept extends NamedEntity {
}


/**
 * Entity that perceives its environment and acts upon it to achieve goals (Clause 5.3).
 */
export interface AIAgent extends AIConcept {
    /** Operational autonomy level of the AI system. */
    autonomy_level?: string,
    /** Predominant symbolic vs subsymbolic approach used by the system. */
    symbolic_approach?: string,
    /** Agent architecture realised by the entity (Clause 5.3). */
    agent_architecture?: string,
    /** Goals the agent is configured to pursue. */
    goal_set?: string[],
}


/**
 * Representation of knowledge usable by an AI system (Clause 5.4), including knowledge graphs, ontologies and rule bases.
 */
export interface KnowledgeRepresentation extends AIConcept {
    /** Predominant symbolic vs subsymbolic approach used by the system. */
    symbolic_approach?: string,
    /** Type of knowledge captured (Clause 3.1.12, 3.1.28). */
    knowledge_type?: string,
    /** Concrete form of representation (rules, frames, ontology, graph, vectors). */
    representation_form?: string,
}


/**
 * Engineered system that uses AI techniques to perform tasks delegated to it. Aggregates lifecycle, functional, model and stakeholder data.
 */
export interface AISystem extends NamedEntity {
    /** Capability classification of the AI system. */
    ai_system_type?: string,
    /** Predominant symbolic vs subsymbolic approach used by the system. */
    symbolic_approach?: string,
    /** Operational autonomy level of the AI system. */
    autonomy_level?: string,
    /** Stated intended purpose of the AI system. */
    intended_purpose?: string,
    /** Application domain(s) the AI system targets. */
    application_domain?: string,
    /** AI sub-field(s) the system draws on. */
    ai_field?: string,
    /** Functional components exhibited by the system (Clause 7). */
    functional_components?: string,
    /** Current life-cycle stage of the AI system. */
    lifecycle_stage?: string,
    /** Stakeholder roles associated with the AI system. */
    stakeholders?: AIStakeholderRole[],
    /** Constituent components of the AI system. */
    components?: AIComponent[],
    /** Trained or knowledge-based models embedded in the AI system. */
    models?: AIModel[],
    /** Datasets used by, or produced by, the AI system. */
    datasets?: Dataset[],
    /** Trustworthiness properties claimed for the AI system. */
    trustworthiness_properties?: TrustworthinessProperty[],
    /** Jurisdictional issues considered in scope for the application. */
    jurisdictional_issues?: string,
    /** Societal impact categories considered in scope. */
    societal_impacts?: string,
    /** Distinguishing characteristics from Clause 5.1. */
    system_characteristics?: string,
    /** Task categories the AI system addresses. */
    task_categories?: string,
    /** Agent architecture, if the AI system is structured as an agent (Clause 5.3). */
    agent_architecture?: string,
    /** Data-handling processes applied within the AI system (Clause 5.10). */
    data_processes?: DataProcess[],
    /** IoT/CPS system this AI system is integrated with, if any (Clause 5.14). */
    iot_integration?: IoTSystemId,
}


/**
 * Functional component of an AI system, such as a data pipeline, preprocessor, model server, or post-processing module.
 */
export interface AIComponent extends NamedEntity {
    /** Functional view component implemented by an AI component (Clause 7). */
    component_function?: string,
    /** Other components this component depends on at runtime. */
    depends_on?: AIComponentId[],
}


/**
 * Trained or rule-based model embedded in an AI system. Carries paradigm, algorithm family, dataset references and version metadata.
 */
export interface AIModel extends NamedEntity {
    /** Machine-learning paradigm under which the model was trained. */
    model_paradigm?: string,
    /** Algorithm family the model belongs to. */
    algorithm_family?: string,
    /** Non-learning engineering approach used (for symbolic/knowledge-based models). */
    engineering_approach?: string,
    /** Dataset used to fit the model. */
    training_dataset?: DatasetId,
    /** Dataset used for hyperparameter tuning and model selection. */
    validation_dataset?: DatasetId,
    /** Dataset used to estimate generalisation performance. */
    test_dataset?: DatasetId,
    /** Free-form record of model hyperparameter settings. */
    hyperparameters?: string[],
    /** Version identifier of the trained model artefact. */
    model_version?: string,
    /** Date or version reference for when the model was last trained. */
    trained_on?: string,
    /** Whether a model supports continuous or online learning (Clause 3.1.9, 5.11.9.2). */
    supports_continuous_learning?: boolean,
    /** Estimated risk of catastrophic forgetting on retraining (Clause 5.11.9.1). */
    catastrophic_forgetting_risk?: number,
    /** Approximate count of trainable model parameters. */
    parameter_count?: number,
    /** Wall-clock duration of model training, expressed as an ISO 8601 duration. */
    training_duration?: string,
    /** Typical end-to-end inference latency in milliseconds. */
    inference_latency_ms?: number,
    /** Whether the model has had compression or distillation applied for deployment (Clause 8.6.2). */
    model_compression_applied?: boolean,
    /** Neural-network architecture, when algorithm_family is neural_network (Clauses 3.4, 5.12.1). */
    neural_network_architecture?: string,
    /** Predominant activation function used in the network (Clause 3.4.1). */
    activation_function?: string,
    /** Training-time phenomena observed for the model (Clause 3.4). */
    training_phenomena?: string,
}


/**
 * AIModel realised as a neural network (Clause 5.12.1, Clause 3.4 terms).
 */
export interface NeuralNetworkModel extends AIModel {
    /** Number of layers in the network. */
    number_of_layers?: number,
    /** Approximate number of trainable parameters. */
    number_of_parameters?: number,
}


/**
 * Collection of data items used by an AI system in a training, validation, test, reference or production role.
 */
export interface Dataset extends NamedEntity {
    /** Modalities present in the dataset. */
    data_modality?: string,
    /** Role the dataset plays in the ML workflow. */
    dataset_role?: string,
    /** Provenance statement for the dataset (origin, collection method, licensing). */
    data_provenance?: string,
    /** Number of records or examples in the dataset. */
    record_count?: number,
    /** Notes on data quality, completeness or representativeness. */
    data_quality_notes?: string,
    /** Whether the dataset contains personal or personally identifiable information. */
    contains_personal_data?: boolean,
    /** Type of target label associated with the dataset (Clause 3.2.10). */
    label_type?: string,
    /** Whether trusted ground-truth labels are available (Clause 3.2.7). */
    ground_truth_available?: boolean,
    /** Number of features per record. */
    feature_count?: number,
    /** Data-handling processes applied to the dataset (Clause 5.10). */
    data_processes_applied?: DataProcess[],
}


/**
 * Claim about a trustworthiness property of an AI system or model, with evidence and measurement metadata.
 */
export interface TrustworthinessProperty extends NamedEntity {
    /** Which trustworthiness property is being characterised. */
    trustworthiness_property_type: string,
    /** References to evidence supporting the property claim. */
    property_evidence?: string[],
    /** How the property was assessed or measured. */
    measurement_method?: string,
    /** Bias categories considered relevant to this property assessment. */
    applicable_biases?: string,
    /** Normalised confidence in the property claim. */
    confidence_score?: number,
}


/**
 * Process or activity associated with a stage of the AI system life cycle (Clause 6).
 */
export interface AILifecycleProcess extends NamedEntity {
    /** Life-cycle stage the process belongs to. */
    process_stage: string,
    /** Inputs consumed by the process. */
    process_inputs?: string[],
    /** Outputs produced by the process. */
    process_outputs?: string[],
    /** Stakeholder role responsible for executing the process. */
    responsible_role?: string,
    /** Date the process started. */
    start_date?: date,
    /** Date the process completed. */
    end_date?: date,
    /** Risks identified or addressed by a process or assessment. */
    risk_items?: string[],
    /** Criteria that must be met for an output or process to be approved. */
    approval_criteria?: string[],
    /** Free-text refinement of the process within its life-cycle stage (e.g. "objectives", "requirements"). */
    process_sub_type?: string,
}


/**
 * Stakeholder role enacted by an organisation or individual in relation to an AI system (Clause 5.19).
 */
export interface AIStakeholderRole extends NamedEntity {
    /** Canonical stakeholder role type as defined in Clause 5.19. */
    stakeholder_role_type: string,
    /** Name of the organisation acting in the stakeholder role. */
    organization_name?: string,
    /** Contact identifier (e.g. email) for the stakeholder. */
    contact?: string,
    /** Free-text statements of responsibility. */
    responsibilities?: string[],
}


/**
 * Stakeholder making an AI system available to customers (Clause 5.19.2).
 */
export interface AIProvider extends AIStakeholderRole {
}


/**
 * Stakeholder designing, developing or assembling AI systems (Clause 5.19.3).
 */
export interface AIProducer extends AIStakeholderRole {
}


/**
 * Stakeholder using an AI system or AI-backed service (Clause 5.19.4).
 */
export interface AICustomer extends AIStakeholderRole {
}


/**
 * Stakeholder providing supporting services across the AI life cycle (Clause 5.19.5).
 */
export interface AIPartner extends AIStakeholderRole {
}


/**
 * Person or group affected by an AI system (Clause 5.19.6).
 */
export interface AISubject extends AIStakeholderRole {
}


/**
 * Regulator or standards-setting body with oversight responsibilities (Clause 5.19.7).
 */
export interface RelevantAuthority extends AIStakeholderRole {
}


/**
 * Aggregation of the AI systems, data sources, computing resources and stakeholder roles that surround a deployment context (Clause 8).
 */
export interface AIEcosystem extends NamedEntity {
    /** Computing resource types relied upon. */
    computing_resources?: string,
    /** Identifiers or descriptions of data sources feeding the ecosystem. */
    data_sources?: string[],
    /** Free-text or CURIE references to ecosystem components. */
    ecosystem_components?: string[],
    /** AI systems documented in the collection. */
    ai_systems?: AISystem[],
    /** Stakeholder role records in the collection. */
    ai_stakeholder_roles?: AIStakeholderRole[],
    /** Big-data characteristics that the ecosystem exhibits (Clause 8.6.1). */
    big_data_characteristics?: string,
}


/**
 * Pool of computing resources (CPU/GPU/TPU/ASIC/FPGA) available to AI workloads (Clause 8.7).
 */
export interface ResourcePool extends NamedEntity {
    /** Category of computing resource (Clause 8.7). */
    resource_type: string,
    /** Capacity expressed in units appropriate to the resource type. */
    capacity_units?: string,
}


/**
 * Component of a natural-language-processing pipeline (Clause 9.2).
 */
export interface NLPComponent extends NamedEntity {
    /** Type of NLP pipeline component (Clause 9.2.2). */
    nlp_component_type: string,
}


/**
 * Computer-vision capability provided by an AI system (Clause 9.1).
 */
export interface ComputerVisionFunction extends NamedEntity {
    /** Type of computer-vision task (Clause 9.1). */
    cv_task: string,
}


/**
 * Description of an AI application instance situated in a domain (Clause 10).
 */
export interface AIApplication extends NamedEntity {
    /** Application domain(s) the AI system targets. */
    application_domain?: string,
    /** Stated intended purpose of the AI system. */
    intended_purpose?: string,
    /** Jurisdictional issues considered in scope for the application. */
    jurisdictional_issues?: string,
    /** Societal impact categories considered in scope. */
    societal_impacts?: string,
    /** AI system that provides the application. */
    hosting_system?: AISystemId,
}


/**
 * AI task addressed by a model or system (e.g. classification, regression, planning). Provides a first-class entity for the task categories enumerated across Clause 3 terminology.
 */
export interface Task extends NamedEntity {
    /** Category of AI task being addressed. */
    task_category: string,
    /** Modalities of input accepted by a task or component. */
    input_modalities?: string,
    /** Type of output label produced by a task, when applicable. */
    output_label_type?: string,
    /** Metrics used to evaluate performance. */
    performance_metric?: string[],
}


/**
 * Prediction produced by an AI model (Clause 7.4.2).
 */
export interface Prediction extends NamedEntity {
    /** Serialised representation of a predicted value (Clause 7.4.2). */
    predicted_value?: string,
    /** Normalised confidence value associated with an output or claim. */
    confidence?: number,
    /** Model that produced the prediction. */
    produced_by?: AIModelId,
}


/**
 * Decision produced by an AI system on the basis of one or more predictions (Clause 7.4.3).
 */
export interface Decision extends NamedEntity {
    /** Chosen course of action resulting from a decision (Clause 7.4.3). */
    decision_outcome?: string,
    /** Policy or rule used to translate predictions into a decision. */
    decision_policy?: string,
    /** Predictions that supported the decision. */
    based_on_predictions?: PredictionId[],
}


/**
 * Action carried out as a result of an AI-system decision (Clause 7.4.4).
 */
export interface Action extends NamedEntity {
    /** Entity or system on which an action is performed (Clause 7.4.4). */
    action_target?: string,
    /** Execution status of an action or process. */
    execution_status?: string,
    /** Decision that triggered the action. */
    triggered_by?: DecisionId,
}


/**
 * Component performing inference over a model or knowledge base (Clause 3.1.17).
 */
export interface InferenceEngine extends NamedEntity {
    /** Inference strategy used (e.g. forward_chaining, backward_chaining, probabilistic). */
    inference_strategy?: string,
    /** Model the inference engine evaluates. */
    uses_model?: AIModelId,
}


/**
 * Graph-structured knowledge representation, often used for reasoning and retrieval (Clause 8.5).
 */
export interface KnowledgeGraph extends KnowledgeRepresentation {
    /** Approximate number of nodes in a graph-structured artefact. */
    node_count?: number,
    /** Approximate number of edges in a graph-structured artefact. */
    edge_count?: number,
    /** Ontologies referenced by a knowledge artefact. */
    ontology_reference?: string[],
}


/**
 * Rule-based system encoding domain expertise (Clause 8.5.2).
 */
export interface ExpertSystem extends NamedEntity {
    /** Approximate count of rules in a rule-based knowledge base. */
    rule_count?: number,
    /** Inference engine used by the expert system. */
    inference_engine?: InferenceEngine,
}


/**
 * System combining AI techniques to emulate human cognitive functions (Clause 5.5).
 */
export interface CognitiveComputingSystem extends AIConcept {
    /** Cognitive capabilities the system provides (e.g. perception, reasoning, learning). */
    cognitive_capabilities?: string[],
}


/**
 * System whose behaviour is driven by the explicit semantics of its inputs and knowledge sources (Clause 5.6).
 */
export interface SemanticComputingSystem extends AIConcept {
    /** Reference to the semantic model or ontology used. */
    semantic_model?: string,
}


/**
 * System employing soft computing techniques tolerant of imprecision and uncertainty (Clause 5.7).
 */
export interface SoftComputingSystem extends AIConcept {
    /** Soft-computing techniques the system employs. */
    soft_computing_techniques: string,
}


/**
 * Discrete data-handling process applied to a dataset during AI system development or operation (Clause 5.10).
 */
export interface DataProcess extends NamedEntity {
    /** Type of data-handling process performed. */
    process_type: string,
    /** Dataset consumed by the process. */
    input_dataset?: DatasetId,
    /** Dataset produced by the process. */
    output_dataset?: DatasetId,
    /** Free-form parameters configuring the process. */
    parameters?: string[],
    /** Stakeholder role that executed the process. */
    executed_by?: AIStakeholderRoleId,
}


/**
 * Individual data record within a dataset (Clause 3.2.13).
 */
export interface DataSample extends NamedEntity {
    /** Serialised representation of the sample contents. */
    sample_payload?: string,
    /** Label or target value associated with the sample. */
    sample_label?: string,
}


/**
 * Label or annotation attached to one or more data samples (Clause 3.2.10).
 */
export interface DataLabel extends NamedEntity {
    /** Concrete label value. */
    label_value: string,
    /** Type of target label associated with a dataset, sample or annotation (Clause 3.2.10). */
    label_type?: string,
    /** Role of the party that produced the label. */
    annotator?: AIStakeholderRoleId,
}


/**
 * Trusted reference record used to evaluate or train an AI model (Clause 3.2.7).
 */
export interface GroundTruthRecord extends NamedEntity {
    /** Trusted reference value (Clause 3.2.7). */
    ground_truth_value: string,
    /** Provenance description for an artefact. */
    provenance_statement?: string,
}


/**
 * Embodied agent able to perceive its environment and act in the physical world (Clause 5.3 / Clause 9.5 robotics field).
 */
export interface Robot extends NamedEntity {
    /** Free-text description of the physical embodiment. */
    embodiment?: string,
    /** AI system that controls the robot. */
    controlled_by?: AISystemId,
}


/**
 * Device participating in an Internet-of-Things deployment (Clause 5.14.2).
 */
export interface IoTDevice extends NamedEntity {
    /** Role played by a device in an IoT or cyber-physical system (Clause 5.14.2). */
    device_role: string,
    /** Sensing capabilities of the device. */
    sensing_capabilities?: string[],
    /** Actuating capabilities of the device. */
    actuating_capabilities?: string[],
}


/**
 * Networked system composed of IoT devices, possibly enhanced with AI capabilities (Clause 5.14.2).
 */
export interface IoTSystem extends NamedEntity {
    /** Devices that make up the IoT system. */
    devices?: IoTDevice[],
    /** AI components that operate within the IoT system. */
    ai_components?: AIComponentId[],
}


/**
 * System that tightly integrates computational and physical components, typically with feedback loops between sensing and actuation (Clause 5.14.3).
 */
export interface CyberPhysicalSystem extends NamedEntity {
    /** Physical processes the system monitors or controls. */
    physical_processes?: string[],
    /** Computational components participating in the system. */
    cyber_components?: AIComponentId[],
    /** IoT subsystem the CPS relies on, if any. */
    iot_subsystem?: IoTSystemId,
}


/**
 * Record of a single abbreviation listed in Clause 4 of the standard.
 */
export interface AbbreviationEntry extends NamedEntity {
    /** Acronym or abbreviation code (Clause 4). */
    abbreviation_code: string,
    /** Expanded form of an abbreviation (Clause 4). */
    expansion: string,
}


/**
 * Top-level container aggregating AI systems, models, datasets, lifecycle processes, stakeholder roles, applications and trustworthiness records for serialisation as a single artefact.
 */
export interface AIConceptsCollection {
    /** AI systems documented in the collection. */
    ai_systems?: AISystem[],
    /** Trained or knowledge-based models in the collection. */
    ai_models?: AIModel[],
    /** Datasets referenced by entities in the collection. */
    ai_datasets?: Dataset[],
    /** Life-cycle process records in the collection. */
    ai_lifecycle_processes?: AILifecycleProcess[],
    /** Stakeholder role records in the collection. */
    ai_stakeholder_roles?: AIStakeholderRole[],
    /** AI application records in the collection. */
    ai_applications?: AIApplication[],
    /** Trustworthiness property claims documented in the collection. */
    trustworthiness_records?: TrustworthinessProperty[],
    /** Task records in the collection. */
    tasks?: Task[],
    /** Data-handling process records in the collection. */
    data_processes?: DataProcess[],
    /** IoT system records in the collection. */
    iot_systems?: IoTSystem[],
    /** Cyber-physical system records in the collection. */
    cyber_physical_systems?: CyberPhysicalSystem[],
    /** Knowledge-graph records in the collection. */
    knowledge_graphs?: KnowledgeGraph[],
    /** Expert-system records in the collection. */
    expert_systems?: ExpertSystem[],
    /** Clause 4 abbreviation records. */
    abbreviations?: AbbreviationEntry[],
}


/**
 * Provider of platform infrastructure on which AI services are operated (Clause 5.19.2).
 */
export interface AIPlatformProvider extends AIProvider {
}


/**
 * Provider of an AI-enabled service or product to customers (Clause 5.19.2).
 */
export interface AIServiceProductProvider extends AIProvider {
}


/**
 * Producer role responsible for designing AI models (Clause 5.19.3).
 */
export interface ModelDesigner extends AIProducer {
}


/**
 * Producer role responsible for implementing AI models in code (Clause 5.19.3).
 */
export interface ModelImplementer extends AIProducer {
}


/**
 * Producer role verifying the computational behaviour of an AI system (Clause 5.19.3).
 */
export interface ComputationVerifier extends AIProducer {
}


/**
 * Producer role verifying that models meet specified requirements (Clause 5.19.3).
 */
export interface ModelVerifier extends AIProducer {
}


/**
 * End user of an AI system or AI-backed service (Clause 5.19.4).
 */
export interface AIUser extends AICustomer {
}


/**
 * Partner integrating AI components into a wider system (Clause 5.19.5).
 */
export interface AISystemIntegrator extends AIPartner {
}


/**
 * Partner supplying datasets used by AI systems (Clause 5.19.5).
 */
export interface DataProvider extends AIPartner {
}


/**
 * Partner performing independent audits of AI systems (Clause 5.19.5).
 */
export interface AIAuditor extends AIPartner {
}


/**
 * Partner performing evaluations of AI system performance and trustworthiness (Clause 5.19.5).
 */
export interface AIEvaluator extends AIPartner {
}


/**
 * Individual whose personal data is processed by an AI system (Clause 5.19.6).
 */
export interface DataSubject extends AISubject {
}


/**
 * Authority defining policy applicable to AI systems (Clause 5.19.7).
 */
export interface PolicyMaker extends RelevantAuthority {
}


/**
 * Authority responsible for regulatory oversight of AI systems (Clause 5.19.7).
 */
export interface Regulator extends RelevantAuthority {
}


/**
 * Structured assessment of the autonomy level of an AI system using the criteria listed in Clause 5.13.
 */
export interface AutonomyAssessment extends NamedEntity {
    /** Operational autonomy level of the AI system. */
    autonomy_level?: string,
    /** Free-form scores or judgements for autonomy criteria (Clause 5.13). */
    autonomy_criterion_scores?: string[],
    /** ISO/IEC 22989:2022 clause identifier (e.g. "5.11.4") the element corresponds to. */
    clause_reference?: string,
}


/**
 * Verifiability and validatability claim for an AI system characterised according to the levels in Clause 5.16.
 */
export interface VerificationValidationFramework extends NamedEntity {
    /** Verifiability / validatability claim (Clause 5.16). */
    verification_validation_level?: string,
    /** ISO/IEC 22989:2022 clause identifier (e.g. "5.11.4") the element corresponds to. */
    clause_reference?: string,
    /** Verification methods applied or applicable to the system. */
    verification_methods?: string[],
    /** Validation methods applied or applicable to the system. */
    validation_methods?: string[],
}


/**
 * Collaboration arrangement combining one or more humans with one or more AI systems to pursue shared goals (Clauses 3.3.3, 5.13).
 */
export interface HumanMachineTeam extends AIConcept {
    /** Roles played by humans in the team. */
    human_roles?: string[],
    /** AI systems participating in the team. */
    ai_systems_involved?: AISystemId[],
    /** Free-text description of how tasks are allocated between humans and AI. */
    task_allocation?: string,
}


/**
 * Use of AI to enhance the cognitive capabilities of humans rather than replace them (Clause 5.13 context).
 */
export interface IntelligenceAugmentation extends AIConcept {
    /** Cognitive capabilities being augmented. */
    augmented_capability?: string[],
}


/**
 * Recommendation produced by an AI system (Clauses 7.4, 10).
 */
export interface Recommendation extends NamedEntity {
    /** High-level outcome type of a recommendation (Clauses 7.4, 10). */
    recommendation_outcome_type?: string,
    /** Normalised confidence value associated with an output or claim. */
    confidence?: number,
    /** Items recommended by the system, serialised as strings. */
    recommended_items?: string[],
    /** Predictions supporting the recommendation. */
    based_on_predictions?: PredictionId[],
}


/**
 * Metric used to evaluate AI system or model performance (Clause 7.4.3).
 */
export interface EvaluationMetric extends NamedEntity {
    /** Name of the metric (e.g. accuracy, F1, MAE). */
    metric_name: string,
    /** Observed numeric value of the metric. */
    metric_value?: number,
    /** Unit of the metric, when applicable. */
    metric_unit?: string,
    /** Dataset against which the metric was computed. */
    reference_dataset?: DatasetId,
}


/**
 * Decision threshold applied to a metric, prediction or score (Clause 7.4.3).
 */
export interface Threshold extends NamedEntity {
    /** Numeric threshold value. */
    threshold_value: number,
    /** Name of the metric or score the threshold applies to. */
    applies_to_metric?: string,
    /** Policy describing how the threshold is interpreted. */
    threshold_policy?: string,
}


/**
 * Computational unit in a neural network combining weighted inputs with a bias and an activation function (Clause 3.4.9).
 */
export interface Neuron extends AIConcept {
    /** Activation function applied at the neuron output. */
    activation_function?: string,
    /** Number of inputs combined by the neuron. */
    input_arity?: number,
}


/**
 * Convolution operation as used in convolutional neural networks (Clause 3.4.3).
 */
export interface ConvolutionOperation extends AIConcept {
    /** Spatial dimensions of the convolution kernel. */
    kernel_size?: number[],
    /** Stride applied when sliding the kernel over the input. */
    stride?: number,
    /** Padding mode (e.g. valid, same). */
    padding?: string,
}


/**
 * Observed change in the statistical distribution of operational data relative to training data (Clause 5.11.9.1).
 */
export interface DataDrift extends NamedEntity {
    /** Type of drift (covariate, label, concept). */
    drift_type?: string,
    /** Timestamp or interval at which drift was detected. */
    detected_at?: string,
    /** Dataset in which drift was observed. */
    affected_dataset?: DatasetId,
}


/**
 * Phenomenon by which a continually-trained model loses previously acquired competence (Clause 5.11.9.1).
 */
export interface CatastrophicForgetting extends NamedEntity {
    /** Model in which the phenomenon was observed. */
    affected_model?: AIModelId,
    /** Strategy applied to mitigate the phenomenon. */
    mitigation_strategy?: string,
}


/**
 * Mechanism enabling an AI system to continue operating correctly in the presence of component faults (Clause 5.15.4 context).
 */
export interface FaultToleranceMechanism extends NamedEntity {
    /** Type of mechanism (redundancy, graceful degradation, failover, etc.). */
    mechanism_type?: string,
    /** Scope of failure modes the mechanism covers. */
    coverage_scope?: string,
}


/**
 * Natural language treated as an object of processing or generation by an AI system (Clause 9.2).
 */
export interface NaturalLanguage extends AIConcept {
    /** BCP-47 language tag. */
    language_code?: string,
    /** ISO 15924 script code, when relevant. */
    script?: string,
}


/**
 * Risk associated with an AI system, capturing source, potential event, consequence and treatment metadata (Clause 3.5.11; aligned with ISO/IEC 23894 risk concepts).
 */
export interface RiskItem extends NamedEntity {
    /** Source from which the risk originates. */
    risk_source?: string,
    /** Potential event whose occurrence would realise the risk. */
    potential_event?: string,
    /** Consequence to one or more stakeholders if the event occurs. */
    consequence?: string,
    /** Estimated likelihood of the event (0.0–1.0). */
    likelihood?: number,
    /** Qualitative severity assessment of the consequence. */
    severity?: string,
    /** Strategies to reduce likelihood or severity. */
    mitigation_strategy?: string[],
    /** Stakeholder roles affected by the risk. */
    affected_stakeholders?: AIStakeholderRoleId[],
}


/**
 * Data presented to an AI system at inference time or during training (Clause 3.2.9).
 */
export interface InputData extends NamedEntity {
    /** Classification of a data source (Clause 8.6.1). */
    data_source_type?: string,
    /** Method used to collect data (Clause 8.6.1). */
    data_collection_method?: string,
    /** Modality of the input data. */
    modality?: string,
    /** AI system that consumes the input. */
    consumed_by?: AISystemId,
}


/**
 * Act of deriving conclusions, predictions or recommendations from a model or knowledge base (Clause 3.1.17).
 */
export interface Inference extends NamedEntity {
    /** Strategy used (forward-chaining, backward-chaining, probabilistic, neural forward pass). */
    inference_strategy?: string,
    /** Engine that performed the inference. */
    performed_by?: InferenceEngineId,
    /** Model over which the inference was performed. */
    over_model?: AIModelId,
    /** Serialised representation of the inference output. */
    produced_output?: string,
}


/**
 * Informative mapping between an ISO/IEC 22989 life-cycle stage and an OECD life-cycle stage (Annex A).
 */
export interface OECDLifecycleMapping extends NamedEntity {
    /** ISO/IEC 22989 life-cycle stage. */
    iso_stage: string,
    /** Corresponding OECD life-cycle stage. */
    oecd_stage: string,
    /** Free-text notes on the mapping relationship. */
    mapping_notes?: string,
}


/**
 * Organisation that establishes and operates an AI management system; Annex SL harmonised anchor shared across ISO management-system standards (ISO/IEC 42001, ISO/IEC 27001).
 */
export interface Organization extends NamedEntity {
}


/**
 * Person or organisation that can affect, be affected by, or perceive itself to be affected by a decision or activity; Annex SL harmonised stakeholder anchor shared across ISO management-system standards.
 */
export interface InterestedParty extends NamedEntity {
}



