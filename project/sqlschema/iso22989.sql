-- # Abstract Class: NamedEntity Description: Abstract base class for any addressable entity in the schema, carrying identity, label and clause-reference metadata.
--     * Slot: id Description: Unique CURIE or URI identifying the entity.
--     * Slot: name Description: Human-readable label for the entity.
--     * Slot: description Description: Free-text description of the entity (paraphrased; verbatim ISO text excluded).
--     * Slot: clause_reference Description: ISO/IEC 22989:2022 clause identifier (e.g. "5.11.4") the element corresponds to.
--     * Slot: preferred_label Description: Preferred natural-language label.
-- # Abstract Class: Term Description: Abstract base class for a glossary term defined in Clause 3. Concrete subclasses partition the terminology along Clauses 3.1–3.7.
--     * Slot: id Description: Unique CURIE or URI identifying the entity.
--     * Slot: name Description: Human-readable label for the entity.
--     * Slot: description Description: Free-text description of the entity (paraphrased; verbatim ISO text excluded).
--     * Slot: clause_reference Description: ISO/IEC 22989:2022 clause identifier (e.g. "5.11.4") the element corresponds to.
--     * Slot: preferred_label Description: Preferred natural-language label.
-- # Class: AITerm Description: Term defined in Clause 3.1 (terms related to AI).
--     * Slot: id Description: Unique CURIE or URI identifying the entity.
--     * Slot: name Description: Human-readable label for the entity.
--     * Slot: description Description: Free-text description of the entity (paraphrased; verbatim ISO text excluded).
--     * Slot: clause_reference Description: ISO/IEC 22989:2022 clause identifier (e.g. "5.11.4") the element corresponds to.
--     * Slot: preferred_label Description: Preferred natural-language label.
-- # Class: DataTerm Description: Term defined in Clause 3.2 (terms related to data).
--     * Slot: id Description: Unique CURIE or URI identifying the entity.
--     * Slot: name Description: Human-readable label for the entity.
--     * Slot: description Description: Free-text description of the entity (paraphrased; verbatim ISO text excluded).
--     * Slot: clause_reference Description: ISO/IEC 22989:2022 clause identifier (e.g. "5.11.4") the element corresponds to.
--     * Slot: preferred_label Description: Preferred natural-language label.
-- # Class: MachineLearningTerm Description: Term defined in Clause 3.3 (terms related to machine learning).
--     * Slot: id Description: Unique CURIE or URI identifying the entity.
--     * Slot: name Description: Human-readable label for the entity.
--     * Slot: description Description: Free-text description of the entity (paraphrased; verbatim ISO text excluded).
--     * Slot: clause_reference Description: ISO/IEC 22989:2022 clause identifier (e.g. "5.11.4") the element corresponds to.
--     * Slot: preferred_label Description: Preferred natural-language label.
-- # Class: NeuralNetworkTerm Description: Term defined in Clause 3.4 (terms related to neural networks).
--     * Slot: id Description: Unique CURIE or URI identifying the entity.
--     * Slot: name Description: Human-readable label for the entity.
--     * Slot: description Description: Free-text description of the entity (paraphrased; verbatim ISO text excluded).
--     * Slot: clause_reference Description: ISO/IEC 22989:2022 clause identifier (e.g. "5.11.4") the element corresponds to.
--     * Slot: preferred_label Description: Preferred natural-language label.
-- # Class: TrustworthinessTerm Description: Term defined in Clause 3.5 (terms related to trustworthiness).
--     * Slot: id Description: Unique CURIE or URI identifying the entity.
--     * Slot: name Description: Human-readable label for the entity.
--     * Slot: description Description: Free-text description of the entity (paraphrased; verbatim ISO text excluded).
--     * Slot: clause_reference Description: ISO/IEC 22989:2022 clause identifier (e.g. "5.11.4") the element corresponds to.
--     * Slot: preferred_label Description: Preferred natural-language label.
-- # Class: NLPTerm Description: Term defined in Clause 3.6 (terms related to natural-language processing).
--     * Slot: id Description: Unique CURIE or URI identifying the entity.
--     * Slot: name Description: Human-readable label for the entity.
--     * Slot: description Description: Free-text description of the entity (paraphrased; verbatim ISO text excluded).
--     * Slot: clause_reference Description: ISO/IEC 22989:2022 clause identifier (e.g. "5.11.4") the element corresponds to.
--     * Slot: preferred_label Description: Preferred natural-language label.
-- # Class: ComputerVisionTerm Description: Term defined in Clause 3.7 (terms related to computer vision).
--     * Slot: id Description: Unique CURIE or URI identifying the entity.
--     * Slot: name Description: Human-readable label for the entity.
--     * Slot: description Description: Free-text description of the entity (paraphrased; verbatim ISO text excluded).
--     * Slot: clause_reference Description: ISO/IEC 22989:2022 clause identifier (e.g. "5.11.4") the element corresponds to.
--     * Slot: preferred_label Description: Preferred natural-language label.
-- # Class: AbbreviatedTerm Description: Abbreviation or acronym listed in Clause 4 with its expansion and optional definition reference.
--     * Slot: expansion Description: Expanded form of the abbreviation.
--     * Slot: id Description: Unique CURIE or URI identifying the entity.
--     * Slot: name Description: Human-readable label for the entity.
--     * Slot: description Description: Free-text description of the entity (paraphrased; verbatim ISO text excluded).
--     * Slot: clause_reference Description: ISO/IEC 22989:2022 clause identifier (e.g. "5.11.4") the element corresponds to.
--     * Slot: preferred_label Description: Preferred natural-language label.
-- # Abstract Class: AIConcept Description: Abstract base for Clause 5 conceptual entities (agent, knowledge, cognition, autonomy, etc.).
--     * Slot: id Description: Unique CURIE or URI identifying the entity.
--     * Slot: name Description: Human-readable label for the entity.
--     * Slot: description Description: Free-text description of the entity (paraphrased; verbatim ISO text excluded).
--     * Slot: clause_reference Description: ISO/IEC 22989:2022 clause identifier (e.g. "5.11.4") the element corresponds to.
--     * Slot: preferred_label Description: Preferred natural-language label.
-- # Class: AIAgent Description: Entity that perceives its environment and acts upon it to achieve goals (Clause 5.3).
--     * Slot: autonomy_level Description: Operational autonomy level of the AI system.
--     * Slot: symbolic_approach Description: Predominant symbolic vs subsymbolic approach used by the system.
--     * Slot: agent_architecture Description: Agent architecture realised by the entity (Clause 5.3).
--     * Slot: id Description: Unique CURIE or URI identifying the entity.
--     * Slot: name Description: Human-readable label for the entity.
--     * Slot: description Description: Free-text description of the entity (paraphrased; verbatim ISO text excluded).
--     * Slot: clause_reference Description: ISO/IEC 22989:2022 clause identifier (e.g. "5.11.4") the element corresponds to.
--     * Slot: preferred_label Description: Preferred natural-language label.
-- # Class: KnowledgeRepresentation Description: Representation of knowledge usable by an AI system (Clause 5.4), including knowledge graphs, ontologies and rule bases.
--     * Slot: symbolic_approach Description: Predominant symbolic vs subsymbolic approach used by the system.
--     * Slot: knowledge_type Description: Type of knowledge captured (Clause 3.1.12, 3.1.28).
--     * Slot: representation_form Description: Concrete form of representation (rules, frames, ontology, graph, vectors).
--     * Slot: id Description: Unique CURIE or URI identifying the entity.
--     * Slot: name Description: Human-readable label for the entity.
--     * Slot: description Description: Free-text description of the entity (paraphrased; verbatim ISO text excluded).
--     * Slot: clause_reference Description: ISO/IEC 22989:2022 clause identifier (e.g. "5.11.4") the element corresponds to.
--     * Slot: preferred_label Description: Preferred natural-language label.
-- # Class: AISystem Description: Engineered system that uses AI techniques to perform tasks delegated to it. Aggregates lifecycle, functional, model and stakeholder data.
--     * Slot: ai_system_type Description: Capability classification of the AI system.
--     * Slot: symbolic_approach Description: Predominant symbolic vs subsymbolic approach used by the system.
--     * Slot: autonomy_level Description: Operational autonomy level of the AI system.
--     * Slot: intended_purpose Description: Stated intended purpose of the AI system.
--     * Slot: lifecycle_stage Description: Current life-cycle stage of the AI system.
--     * Slot: agent_architecture Description: Agent architecture, if the AI system is structured as an agent (Clause 5.3).
--     * Slot: iot_integration Description: IoT/CPS system this AI system is integrated with, if any (Clause 5.14).
--     * Slot: id Description: Unique CURIE or URI identifying the entity.
--     * Slot: name Description: Human-readable label for the entity.
--     * Slot: description Description: Free-text description of the entity (paraphrased; verbatim ISO text excluded).
--     * Slot: clause_reference Description: ISO/IEC 22989:2022 clause identifier (e.g. "5.11.4") the element corresponds to.
--     * Slot: preferred_label Description: Preferred natural-language label.
--     * Slot: AIEcosystem_id Description: Autocreated FK slot
--     * Slot: AIConceptsCollection_id Description: Autocreated FK slot
-- # Class: AIComponent Description: Functional component of an AI system, such as a data pipeline, preprocessor, model server, or post-processing module.
--     * Slot: component_function Description: Functional view component implemented by an AI component (Clause 7).
--     * Slot: id Description: Unique CURIE or URI identifying the entity.
--     * Slot: name Description: Human-readable label for the entity.
--     * Slot: description Description: Free-text description of the entity (paraphrased; verbatim ISO text excluded).
--     * Slot: clause_reference Description: ISO/IEC 22989:2022 clause identifier (e.g. "5.11.4") the element corresponds to.
--     * Slot: preferred_label Description: Preferred natural-language label.
--     * Slot: AISystem_id Description: Autocreated FK slot
-- # Class: AIModel Description: Trained or rule-based model embedded in an AI system. Carries paradigm, algorithm family, dataset references and version metadata.
--     * Slot: model_paradigm Description: Machine-learning paradigm under which the model was trained.
--     * Slot: algorithm_family Description: Algorithm family the model belongs to.
--     * Slot: engineering_approach Description: Non-learning engineering approach used (for symbolic/knowledge-based models).
--     * Slot: training_dataset Description: Dataset used to fit the model.
--     * Slot: validation_dataset Description: Dataset used for hyperparameter tuning and model selection.
--     * Slot: test_dataset Description: Dataset used to estimate generalisation performance.
--     * Slot: model_version Description: Version identifier of the trained model artefact.
--     * Slot: trained_on Description: Date or version reference for when the model was last trained.
--     * Slot: supports_continuous_learning Description: Whether a model supports continuous or online learning (Clause 3.1.9, 5.11.9.2).
--     * Slot: catastrophic_forgetting_risk Description: Estimated risk of catastrophic forgetting on retraining (Clause 5.11.9.1).
--     * Slot: parameter_count Description: Approximate count of trainable model parameters.
--     * Slot: training_duration Description: Wall-clock duration of model training, expressed as an ISO 8601 duration.
--     * Slot: inference_latency_ms Description: Typical end-to-end inference latency in milliseconds.
--     * Slot: model_compression_applied Description: Whether the model has had compression or distillation applied for deployment (Clause 8.6.2).
--     * Slot: neural_network_architecture Description: Neural-network architecture, when algorithm_family is neural_network (Clauses 3.4, 5.12.1).
--     * Slot: activation_function Description: Predominant activation function used in the network (Clause 3.4.1).
--     * Slot: id Description: Unique CURIE or URI identifying the entity.
--     * Slot: name Description: Human-readable label for the entity.
--     * Slot: description Description: Free-text description of the entity (paraphrased; verbatim ISO text excluded).
--     * Slot: clause_reference Description: ISO/IEC 22989:2022 clause identifier (e.g. "5.11.4") the element corresponds to.
--     * Slot: preferred_label Description: Preferred natural-language label.
--     * Slot: AISystem_id Description: Autocreated FK slot
--     * Slot: AIConceptsCollection_id Description: Autocreated FK slot
-- # Class: NeuralNetworkModel Description: AIModel realised as a neural network (Clause 5.12.1, Clause 3.4 terms).
--     * Slot: number_of_layers Description: Number of layers in the network.
--     * Slot: number_of_parameters Description: Approximate number of trainable parameters.
--     * Slot: model_paradigm Description: Machine-learning paradigm under which the model was trained.
--     * Slot: algorithm_family Description: Algorithm family the model belongs to.
--     * Slot: engineering_approach Description: Non-learning engineering approach used (for symbolic/knowledge-based models).
--     * Slot: training_dataset Description: Dataset used to fit the model.
--     * Slot: validation_dataset Description: Dataset used for hyperparameter tuning and model selection.
--     * Slot: test_dataset Description: Dataset used to estimate generalisation performance.
--     * Slot: model_version Description: Version identifier of the trained model artefact.
--     * Slot: trained_on Description: Date or version reference for when the model was last trained.
--     * Slot: supports_continuous_learning Description: Whether a model supports continuous or online learning (Clause 3.1.9, 5.11.9.2).
--     * Slot: catastrophic_forgetting_risk Description: Estimated risk of catastrophic forgetting on retraining (Clause 5.11.9.1).
--     * Slot: parameter_count Description: Approximate count of trainable model parameters.
--     * Slot: training_duration Description: Wall-clock duration of model training, expressed as an ISO 8601 duration.
--     * Slot: inference_latency_ms Description: Typical end-to-end inference latency in milliseconds.
--     * Slot: model_compression_applied Description: Whether the model has had compression or distillation applied for deployment (Clause 8.6.2).
--     * Slot: neural_network_architecture Description: Neural-network architecture, when algorithm_family is neural_network (Clauses 3.4, 5.12.1).
--     * Slot: activation_function Description: Predominant activation function used in the network (Clause 3.4.1).
--     * Slot: id Description: Unique CURIE or URI identifying the entity.
--     * Slot: name Description: Human-readable label for the entity.
--     * Slot: description Description: Free-text description of the entity (paraphrased; verbatim ISO text excluded).
--     * Slot: clause_reference Description: ISO/IEC 22989:2022 clause identifier (e.g. "5.11.4") the element corresponds to.
--     * Slot: preferred_label Description: Preferred natural-language label.
-- # Class: Dataset Description: Collection of data items used by an AI system in a training, validation, test, reference or production role.
--     * Slot: dataset_role Description: Role the dataset plays in the ML workflow.
--     * Slot: data_provenance Description: Provenance statement for the dataset (origin, collection method, licensing).
--     * Slot: record_count Description: Number of records or examples in the dataset.
--     * Slot: data_quality_notes Description: Notes on data quality, completeness or representativeness.
--     * Slot: contains_personal_data Description: Whether the dataset contains personal or personally identifiable information.
--     * Slot: label_type Description: Type of target label associated with the dataset (Clause 3.2.10).
--     * Slot: ground_truth_available Description: Whether trusted ground-truth labels are available (Clause 3.2.7).
--     * Slot: feature_count Description: Number of features per record.
--     * Slot: id Description: Unique CURIE or URI identifying the entity.
--     * Slot: name Description: Human-readable label for the entity.
--     * Slot: description Description: Free-text description of the entity (paraphrased; verbatim ISO text excluded).
--     * Slot: clause_reference Description: ISO/IEC 22989:2022 clause identifier (e.g. "5.11.4") the element corresponds to.
--     * Slot: preferred_label Description: Preferred natural-language label.
--     * Slot: AISystem_id Description: Autocreated FK slot
--     * Slot: AIConceptsCollection_id Description: Autocreated FK slot
-- # Class: TrustworthinessProperty Description: Claim about a trustworthiness property of an AI system or model, with evidence and measurement metadata.
--     * Slot: trustworthiness_property_type Description: Which trustworthiness property is being characterised.
--     * Slot: measurement_method Description: How the property was assessed or measured.
--     * Slot: confidence_score Description: Normalised confidence in the property claim.
--     * Slot: id Description: Unique CURIE or URI identifying the entity.
--     * Slot: name Description: Human-readable label for the entity.
--     * Slot: description Description: Free-text description of the entity (paraphrased; verbatim ISO text excluded).
--     * Slot: clause_reference Description: ISO/IEC 22989:2022 clause identifier (e.g. "5.11.4") the element corresponds to.
--     * Slot: preferred_label Description: Preferred natural-language label.
--     * Slot: AISystem_id Description: Autocreated FK slot
--     * Slot: AIConceptsCollection_id Description: Autocreated FK slot
-- # Class: AILifecycleProcess Description: Process or activity associated with a stage of the AI system life cycle (Clause 6).
--     * Slot: process_stage Description: Life-cycle stage the process belongs to.
--     * Slot: responsible_role Description: Stakeholder role responsible for executing the process.
--     * Slot: start_date Description: Date the process started.
--     * Slot: end_date Description: Date the process completed.
--     * Slot: process_sub_type Description: Free-text refinement of the process within its life-cycle stage (e.g. "objectives", "requirements").
--     * Slot: id Description: Unique CURIE or URI identifying the entity.
--     * Slot: name Description: Human-readable label for the entity.
--     * Slot: description Description: Free-text description of the entity (paraphrased; verbatim ISO text excluded).
--     * Slot: clause_reference Description: ISO/IEC 22989:2022 clause identifier (e.g. "5.11.4") the element corresponds to.
--     * Slot: preferred_label Description: Preferred natural-language label.
--     * Slot: AIConceptsCollection_id Description: Autocreated FK slot
-- # Class: AIStakeholderRole Description: Stakeholder role enacted by an organisation or individual in relation to an AI system (Clause 5.19).
--     * Slot: stakeholder_role_type Description: Canonical stakeholder role type as defined in Clause 5.19.
--     * Slot: organization_name Description: Name of the organisation acting in the stakeholder role.
--     * Slot: contact Description: Contact identifier (e.g. email) for the stakeholder.
--     * Slot: id Description: Unique CURIE or URI identifying the entity.
--     * Slot: name Description: Human-readable label for the entity.
--     * Slot: description Description: Free-text description of the entity (paraphrased; verbatim ISO text excluded).
--     * Slot: clause_reference Description: ISO/IEC 22989:2022 clause identifier (e.g. "5.11.4") the element corresponds to.
--     * Slot: preferred_label Description: Preferred natural-language label.
--     * Slot: AISystem_id Description: Autocreated FK slot
--     * Slot: AIEcosystem_id Description: Autocreated FK slot
--     * Slot: AIConceptsCollection_id Description: Autocreated FK slot
-- # Class: AIProvider Description: Stakeholder making an AI system available to customers (Clause 5.19.2).
--     * Slot: stakeholder_role_type Description: Canonical stakeholder role type as defined in Clause 5.19.
--     * Slot: organization_name Description: Name of the organisation acting in the stakeholder role.
--     * Slot: contact Description: Contact identifier (e.g. email) for the stakeholder.
--     * Slot: id Description: Unique CURIE or URI identifying the entity.
--     * Slot: name Description: Human-readable label for the entity.
--     * Slot: description Description: Free-text description of the entity (paraphrased; verbatim ISO text excluded).
--     * Slot: clause_reference Description: ISO/IEC 22989:2022 clause identifier (e.g. "5.11.4") the element corresponds to.
--     * Slot: preferred_label Description: Preferred natural-language label.
-- # Class: AIProducer Description: Stakeholder designing, developing or assembling AI systems (Clause 5.19.3).
--     * Slot: stakeholder_role_type Description: Canonical stakeholder role type as defined in Clause 5.19.
--     * Slot: organization_name Description: Name of the organisation acting in the stakeholder role.
--     * Slot: contact Description: Contact identifier (e.g. email) for the stakeholder.
--     * Slot: id Description: Unique CURIE or URI identifying the entity.
--     * Slot: name Description: Human-readable label for the entity.
--     * Slot: description Description: Free-text description of the entity (paraphrased; verbatim ISO text excluded).
--     * Slot: clause_reference Description: ISO/IEC 22989:2022 clause identifier (e.g. "5.11.4") the element corresponds to.
--     * Slot: preferred_label Description: Preferred natural-language label.
-- # Class: AICustomer Description: Stakeholder using an AI system or AI-backed service (Clause 5.19.4).
--     * Slot: stakeholder_role_type Description: Canonical stakeholder role type as defined in Clause 5.19.
--     * Slot: organization_name Description: Name of the organisation acting in the stakeholder role.
--     * Slot: contact Description: Contact identifier (e.g. email) for the stakeholder.
--     * Slot: id Description: Unique CURIE or URI identifying the entity.
--     * Slot: name Description: Human-readable label for the entity.
--     * Slot: description Description: Free-text description of the entity (paraphrased; verbatim ISO text excluded).
--     * Slot: clause_reference Description: ISO/IEC 22989:2022 clause identifier (e.g. "5.11.4") the element corresponds to.
--     * Slot: preferred_label Description: Preferred natural-language label.
-- # Class: AIPartner Description: Stakeholder providing supporting services across the AI life cycle (Clause 5.19.5).
--     * Slot: stakeholder_role_type Description: Canonical stakeholder role type as defined in Clause 5.19.
--     * Slot: organization_name Description: Name of the organisation acting in the stakeholder role.
--     * Slot: contact Description: Contact identifier (e.g. email) for the stakeholder.
--     * Slot: id Description: Unique CURIE or URI identifying the entity.
--     * Slot: name Description: Human-readable label for the entity.
--     * Slot: description Description: Free-text description of the entity (paraphrased; verbatim ISO text excluded).
--     * Slot: clause_reference Description: ISO/IEC 22989:2022 clause identifier (e.g. "5.11.4") the element corresponds to.
--     * Slot: preferred_label Description: Preferred natural-language label.
-- # Class: AISubject Description: Person or group affected by an AI system (Clause 5.19.6).
--     * Slot: stakeholder_role_type Description: Canonical stakeholder role type as defined in Clause 5.19.
--     * Slot: organization_name Description: Name of the organisation acting in the stakeholder role.
--     * Slot: contact Description: Contact identifier (e.g. email) for the stakeholder.
--     * Slot: id Description: Unique CURIE or URI identifying the entity.
--     * Slot: name Description: Human-readable label for the entity.
--     * Slot: description Description: Free-text description of the entity (paraphrased; verbatim ISO text excluded).
--     * Slot: clause_reference Description: ISO/IEC 22989:2022 clause identifier (e.g. "5.11.4") the element corresponds to.
--     * Slot: preferred_label Description: Preferred natural-language label.
-- # Class: RelevantAuthority Description: Regulator or standards-setting body with oversight responsibilities (Clause 5.19.7).
--     * Slot: stakeholder_role_type Description: Canonical stakeholder role type as defined in Clause 5.19.
--     * Slot: organization_name Description: Name of the organisation acting in the stakeholder role.
--     * Slot: contact Description: Contact identifier (e.g. email) for the stakeholder.
--     * Slot: id Description: Unique CURIE or URI identifying the entity.
--     * Slot: name Description: Human-readable label for the entity.
--     * Slot: description Description: Free-text description of the entity (paraphrased; verbatim ISO text excluded).
--     * Slot: clause_reference Description: ISO/IEC 22989:2022 clause identifier (e.g. "5.11.4") the element corresponds to.
--     * Slot: preferred_label Description: Preferred natural-language label.
-- # Class: AIEcosystem Description: Aggregation of the AI systems, data sources, computing resources and stakeholder roles that surround a deployment context (Clause 8).
--     * Slot: id Description: Unique CURIE or URI identifying the entity.
--     * Slot: name Description: Human-readable label for the entity.
--     * Slot: description Description: Free-text description of the entity (paraphrased; verbatim ISO text excluded).
--     * Slot: clause_reference Description: ISO/IEC 22989:2022 clause identifier (e.g. "5.11.4") the element corresponds to.
--     * Slot: preferred_label Description: Preferred natural-language label.
-- # Class: ResourcePool Description: Pool of computing resources (CPU/GPU/TPU/ASIC/FPGA) available to AI workloads (Clause 8.7).
--     * Slot: resource_type Description: Category of computing resource (Clause 8.7).
--     * Slot: capacity_units Description: Capacity expressed in units appropriate to the resource type.
--     * Slot: id Description: Unique CURIE or URI identifying the entity.
--     * Slot: name Description: Human-readable label for the entity.
--     * Slot: description Description: Free-text description of the entity (paraphrased; verbatim ISO text excluded).
--     * Slot: clause_reference Description: ISO/IEC 22989:2022 clause identifier (e.g. "5.11.4") the element corresponds to.
--     * Slot: preferred_label Description: Preferred natural-language label.
-- # Class: NLPComponent Description: Component of a natural-language-processing pipeline (Clause 9.2).
--     * Slot: nlp_component_type Description: Type of NLP pipeline component (Clause 9.2.2).
--     * Slot: id Description: Unique CURIE or URI identifying the entity.
--     * Slot: name Description: Human-readable label for the entity.
--     * Slot: description Description: Free-text description of the entity (paraphrased; verbatim ISO text excluded).
--     * Slot: clause_reference Description: ISO/IEC 22989:2022 clause identifier (e.g. "5.11.4") the element corresponds to.
--     * Slot: preferred_label Description: Preferred natural-language label.
-- # Class: ComputerVisionFunction Description: Computer-vision capability provided by an AI system (Clause 9.1).
--     * Slot: cv_task Description: Type of computer-vision task (Clause 9.1).
--     * Slot: id Description: Unique CURIE or URI identifying the entity.
--     * Slot: name Description: Human-readable label for the entity.
--     * Slot: description Description: Free-text description of the entity (paraphrased; verbatim ISO text excluded).
--     * Slot: clause_reference Description: ISO/IEC 22989:2022 clause identifier (e.g. "5.11.4") the element corresponds to.
--     * Slot: preferred_label Description: Preferred natural-language label.
-- # Class: AIApplication Description: Description of an AI application instance situated in a domain (Clause 10).
--     * Slot: intended_purpose Description: Stated intended purpose of the AI system.
--     * Slot: hosting_system Description: AI system that provides the application.
--     * Slot: id Description: Unique CURIE or URI identifying the entity.
--     * Slot: name Description: Human-readable label for the entity.
--     * Slot: description Description: Free-text description of the entity (paraphrased; verbatim ISO text excluded).
--     * Slot: clause_reference Description: ISO/IEC 22989:2022 clause identifier (e.g. "5.11.4") the element corresponds to.
--     * Slot: preferred_label Description: Preferred natural-language label.
--     * Slot: AIConceptsCollection_id Description: Autocreated FK slot
-- # Class: Task Description: AI task addressed by a model or system (e.g. classification, regression, planning). Provides a first-class entity for the task categories enumerated across Clause 3 terminology.
--     * Slot: task_category Description: Category of AI task being addressed.
--     * Slot: output_label_type Description: Type of output label produced by a task, when applicable.
--     * Slot: id Description: Unique CURIE or URI identifying the entity.
--     * Slot: name Description: Human-readable label for the entity.
--     * Slot: description Description: Free-text description of the entity (paraphrased; verbatim ISO text excluded).
--     * Slot: clause_reference Description: ISO/IEC 22989:2022 clause identifier (e.g. "5.11.4") the element corresponds to.
--     * Slot: preferred_label Description: Preferred natural-language label.
--     * Slot: AIConceptsCollection_id Description: Autocreated FK slot
-- # Class: Prediction Description: Prediction produced by an AI model (Clause 7.4.2).
--     * Slot: predicted_value Description: Serialised representation of a predicted value (Clause 7.4.2).
--     * Slot: confidence Description: Normalised confidence value associated with an output or claim.
--     * Slot: produced_by Description: Model that produced the prediction.
--     * Slot: id Description: Unique CURIE or URI identifying the entity.
--     * Slot: name Description: Human-readable label for the entity.
--     * Slot: description Description: Free-text description of the entity (paraphrased; verbatim ISO text excluded).
--     * Slot: clause_reference Description: ISO/IEC 22989:2022 clause identifier (e.g. "5.11.4") the element corresponds to.
--     * Slot: preferred_label Description: Preferred natural-language label.
-- # Class: Decision Description: Decision produced by an AI system on the basis of one or more predictions (Clause 7.4.3).
--     * Slot: decision_outcome Description: Chosen course of action resulting from a decision (Clause 7.4.3).
--     * Slot: decision_policy Description: Policy or rule used to translate predictions into a decision.
--     * Slot: id Description: Unique CURIE or URI identifying the entity.
--     * Slot: name Description: Human-readable label for the entity.
--     * Slot: description Description: Free-text description of the entity (paraphrased; verbatim ISO text excluded).
--     * Slot: clause_reference Description: ISO/IEC 22989:2022 clause identifier (e.g. "5.11.4") the element corresponds to.
--     * Slot: preferred_label Description: Preferred natural-language label.
-- # Class: Action Description: Action carried out as a result of an AI-system decision (Clause 7.4.4).
--     * Slot: action_target Description: Entity or system on which an action is performed (Clause 7.4.4).
--     * Slot: execution_status Description: Execution status of an action or process.
--     * Slot: triggered_by Description: Decision that triggered the action.
--     * Slot: id Description: Unique CURIE or URI identifying the entity.
--     * Slot: name Description: Human-readable label for the entity.
--     * Slot: description Description: Free-text description of the entity (paraphrased; verbatim ISO text excluded).
--     * Slot: clause_reference Description: ISO/IEC 22989:2022 clause identifier (e.g. "5.11.4") the element corresponds to.
--     * Slot: preferred_label Description: Preferred natural-language label.
-- # Class: InferenceEngine Description: Component performing inference over a model or knowledge base (Clause 3.1.17).
--     * Slot: inference_strategy Description: Inference strategy used (e.g. forward_chaining, backward_chaining, probabilistic).
--     * Slot: uses_model Description: Model the inference engine evaluates.
--     * Slot: id Description: Unique CURIE or URI identifying the entity.
--     * Slot: name Description: Human-readable label for the entity.
--     * Slot: description Description: Free-text description of the entity (paraphrased; verbatim ISO text excluded).
--     * Slot: clause_reference Description: ISO/IEC 22989:2022 clause identifier (e.g. "5.11.4") the element corresponds to.
--     * Slot: preferred_label Description: Preferred natural-language label.
-- # Class: KnowledgeGraph Description: Graph-structured knowledge representation, often used for reasoning and retrieval (Clause 8.5).
--     * Slot: node_count Description: Approximate number of nodes in a graph-structured artefact.
--     * Slot: edge_count Description: Approximate number of edges in a graph-structured artefact.
--     * Slot: symbolic_approach Description: Predominant symbolic vs subsymbolic approach used by the system.
--     * Slot: knowledge_type Description: Type of knowledge captured (Clause 3.1.12, 3.1.28).
--     * Slot: representation_form Description: Concrete form of representation (rules, frames, ontology, graph, vectors).
--     * Slot: id Description: Unique CURIE or URI identifying the entity.
--     * Slot: name Description: Human-readable label for the entity.
--     * Slot: description Description: Free-text description of the entity (paraphrased; verbatim ISO text excluded).
--     * Slot: clause_reference Description: ISO/IEC 22989:2022 clause identifier (e.g. "5.11.4") the element corresponds to.
--     * Slot: preferred_label Description: Preferred natural-language label.
--     * Slot: AIConceptsCollection_id Description: Autocreated FK slot
-- # Class: ExpertSystem Description: Rule-based system encoding domain expertise (Clause 8.5.2).
--     * Slot: rule_count Description: Approximate count of rules in a rule-based knowledge base.
--     * Slot: id Description: Unique CURIE or URI identifying the entity.
--     * Slot: name Description: Human-readable label for the entity.
--     * Slot: description Description: Free-text description of the entity (paraphrased; verbatim ISO text excluded).
--     * Slot: clause_reference Description: ISO/IEC 22989:2022 clause identifier (e.g. "5.11.4") the element corresponds to.
--     * Slot: preferred_label Description: Preferred natural-language label.
--     * Slot: AIConceptsCollection_id Description: Autocreated FK slot
--     * Slot: inference_engine_id Description: Inference engine used by the expert system.
-- # Class: CognitiveComputingSystem Description: System combining AI techniques to emulate human cognitive functions (Clause 5.5).
--     * Slot: id Description: Unique CURIE or URI identifying the entity.
--     * Slot: name Description: Human-readable label for the entity.
--     * Slot: description Description: Free-text description of the entity (paraphrased; verbatim ISO text excluded).
--     * Slot: clause_reference Description: ISO/IEC 22989:2022 clause identifier (e.g. "5.11.4") the element corresponds to.
--     * Slot: preferred_label Description: Preferred natural-language label.
-- # Class: SemanticComputingSystem Description: System whose behaviour is driven by the explicit semantics of its inputs and knowledge sources (Clause 5.6).
--     * Slot: semantic_model Description: Reference to the semantic model or ontology used.
--     * Slot: id Description: Unique CURIE or URI identifying the entity.
--     * Slot: name Description: Human-readable label for the entity.
--     * Slot: description Description: Free-text description of the entity (paraphrased; verbatim ISO text excluded).
--     * Slot: clause_reference Description: ISO/IEC 22989:2022 clause identifier (e.g. "5.11.4") the element corresponds to.
--     * Slot: preferred_label Description: Preferred natural-language label.
-- # Class: SoftComputingSystem Description: System employing soft computing techniques tolerant of imprecision and uncertainty (Clause 5.7).
--     * Slot: id Description: Unique CURIE or URI identifying the entity.
--     * Slot: name Description: Human-readable label for the entity.
--     * Slot: description Description: Free-text description of the entity (paraphrased; verbatim ISO text excluded).
--     * Slot: clause_reference Description: ISO/IEC 22989:2022 clause identifier (e.g. "5.11.4") the element corresponds to.
--     * Slot: preferred_label Description: Preferred natural-language label.
-- # Class: DataProcess Description: Discrete data-handling process applied to a dataset during AI system development or operation (Clause 5.10).
--     * Slot: process_type Description: Type of data-handling process performed.
--     * Slot: input_dataset Description: Dataset consumed by the process.
--     * Slot: output_dataset Description: Dataset produced by the process.
--     * Slot: executed_by Description: Stakeholder role that executed the process.
--     * Slot: id Description: Unique CURIE or URI identifying the entity.
--     * Slot: name Description: Human-readable label for the entity.
--     * Slot: description Description: Free-text description of the entity (paraphrased; verbatim ISO text excluded).
--     * Slot: clause_reference Description: ISO/IEC 22989:2022 clause identifier (e.g. "5.11.4") the element corresponds to.
--     * Slot: preferred_label Description: Preferred natural-language label.
--     * Slot: AISystem_id Description: Autocreated FK slot
--     * Slot: Dataset_id Description: Autocreated FK slot
--     * Slot: AIConceptsCollection_id Description: Autocreated FK slot
-- # Class: DataSample Description: Individual data record within a dataset (Clause 3.2.13).
--     * Slot: sample_payload Description: Serialised representation of the sample contents.
--     * Slot: sample_label Description: Label or target value associated with the sample.
--     * Slot: id Description: Unique CURIE or URI identifying the entity.
--     * Slot: name Description: Human-readable label for the entity.
--     * Slot: description Description: Free-text description of the entity (paraphrased; verbatim ISO text excluded).
--     * Slot: clause_reference Description: ISO/IEC 22989:2022 clause identifier (e.g. "5.11.4") the element corresponds to.
--     * Slot: preferred_label Description: Preferred natural-language label.
-- # Class: DataLabel Description: Label or annotation attached to one or more data samples (Clause 3.2.10).
--     * Slot: label_value Description: Concrete label value.
--     * Slot: label_type Description: Type of target label associated with a dataset, sample or annotation (Clause 3.2.10).
--     * Slot: annotator Description: Role of the party that produced the label.
--     * Slot: id Description: Unique CURIE or URI identifying the entity.
--     * Slot: name Description: Human-readable label for the entity.
--     * Slot: description Description: Free-text description of the entity (paraphrased; verbatim ISO text excluded).
--     * Slot: clause_reference Description: ISO/IEC 22989:2022 clause identifier (e.g. "5.11.4") the element corresponds to.
--     * Slot: preferred_label Description: Preferred natural-language label.
-- # Class: GroundTruthRecord Description: Trusted reference record used to evaluate or train an AI model (Clause 3.2.7).
--     * Slot: ground_truth_value Description: Trusted reference value (Clause 3.2.7).
--     * Slot: provenance_statement Description: Provenance description for an artefact.
--     * Slot: id Description: Unique CURIE or URI identifying the entity.
--     * Slot: name Description: Human-readable label for the entity.
--     * Slot: description Description: Free-text description of the entity (paraphrased; verbatim ISO text excluded).
--     * Slot: clause_reference Description: ISO/IEC 22989:2022 clause identifier (e.g. "5.11.4") the element corresponds to.
--     * Slot: preferred_label Description: Preferred natural-language label.
-- # Class: Robot Description: Embodied agent able to perceive its environment and act in the physical world (Clause 5.3 / Clause 9.5 robotics field).
--     * Slot: embodiment Description: Free-text description of the physical embodiment.
--     * Slot: controlled_by Description: AI system that controls the robot.
--     * Slot: id Description: Unique CURIE or URI identifying the entity.
--     * Slot: name Description: Human-readable label for the entity.
--     * Slot: description Description: Free-text description of the entity (paraphrased; verbatim ISO text excluded).
--     * Slot: clause_reference Description: ISO/IEC 22989:2022 clause identifier (e.g. "5.11.4") the element corresponds to.
--     * Slot: preferred_label Description: Preferred natural-language label.
-- # Class: IoTDevice Description: Device participating in an Internet-of-Things deployment (Clause 5.14.2).
--     * Slot: device_role Description: Role played by a device in an IoT or cyber-physical system (Clause 5.14.2).
--     * Slot: id Description: Unique CURIE or URI identifying the entity.
--     * Slot: name Description: Human-readable label for the entity.
--     * Slot: description Description: Free-text description of the entity (paraphrased; verbatim ISO text excluded).
--     * Slot: clause_reference Description: ISO/IEC 22989:2022 clause identifier (e.g. "5.11.4") the element corresponds to.
--     * Slot: preferred_label Description: Preferred natural-language label.
--     * Slot: IoTSystem_id Description: Autocreated FK slot
-- # Class: IoTSystem Description: Networked system composed of IoT devices, possibly enhanced with AI capabilities (Clause 5.14.2).
--     * Slot: id Description: Unique CURIE or URI identifying the entity.
--     * Slot: name Description: Human-readable label for the entity.
--     * Slot: description Description: Free-text description of the entity (paraphrased; verbatim ISO text excluded).
--     * Slot: clause_reference Description: ISO/IEC 22989:2022 clause identifier (e.g. "5.11.4") the element corresponds to.
--     * Slot: preferred_label Description: Preferred natural-language label.
--     * Slot: AIConceptsCollection_id Description: Autocreated FK slot
-- # Class: CyberPhysicalSystem Description: System that tightly integrates computational and physical components, typically with feedback loops between sensing and actuation (Clause 5.14.3).
--     * Slot: iot_subsystem Description: IoT subsystem the CPS relies on, if any.
--     * Slot: id Description: Unique CURIE or URI identifying the entity.
--     * Slot: name Description: Human-readable label for the entity.
--     * Slot: description Description: Free-text description of the entity (paraphrased; verbatim ISO text excluded).
--     * Slot: clause_reference Description: ISO/IEC 22989:2022 clause identifier (e.g. "5.11.4") the element corresponds to.
--     * Slot: preferred_label Description: Preferred natural-language label.
--     * Slot: AIConceptsCollection_id Description: Autocreated FK slot
-- # Class: AbbreviationEntry Description: Record of a single abbreviation listed in Clause 4 of the standard.
--     * Slot: abbreviation_code Description: Acronym or abbreviation code (Clause 4).
--     * Slot: expansion Description: Expanded form of an abbreviation (Clause 4).
--     * Slot: id Description: Unique CURIE or URI identifying the entity.
--     * Slot: name Description: Human-readable label for the entity.
--     * Slot: description Description: Free-text description of the entity (paraphrased; verbatim ISO text excluded).
--     * Slot: clause_reference Description: ISO/IEC 22989:2022 clause identifier (e.g. "5.11.4") the element corresponds to.
--     * Slot: preferred_label Description: Preferred natural-language label.
--     * Slot: AIConceptsCollection_id Description: Autocreated FK slot
-- # Class: AIConceptsCollection Description: Top-level container aggregating AI systems, models, datasets, lifecycle processes, stakeholder roles, applications and trustworthiness records for serialisation as a single artefact.
--     * Slot: id
-- # Class: AIPlatformProvider Description: Provider of platform infrastructure on which AI services are operated (Clause 5.19.2).
--     * Slot: stakeholder_role_type Description: Canonical stakeholder role type as defined in Clause 5.19.
--     * Slot: organization_name Description: Name of the organisation acting in the stakeholder role.
--     * Slot: contact Description: Contact identifier (e.g. email) for the stakeholder.
--     * Slot: id Description: Unique CURIE or URI identifying the entity.
--     * Slot: name Description: Human-readable label for the entity.
--     * Slot: description Description: Free-text description of the entity (paraphrased; verbatim ISO text excluded).
--     * Slot: clause_reference Description: ISO/IEC 22989:2022 clause identifier (e.g. "5.11.4") the element corresponds to.
--     * Slot: preferred_label Description: Preferred natural-language label.
-- # Class: AIServiceProductProvider Description: Provider of an AI-enabled service or product to customers (Clause 5.19.2).
--     * Slot: stakeholder_role_type Description: Canonical stakeholder role type as defined in Clause 5.19.
--     * Slot: organization_name Description: Name of the organisation acting in the stakeholder role.
--     * Slot: contact Description: Contact identifier (e.g. email) for the stakeholder.
--     * Slot: id Description: Unique CURIE or URI identifying the entity.
--     * Slot: name Description: Human-readable label for the entity.
--     * Slot: description Description: Free-text description of the entity (paraphrased; verbatim ISO text excluded).
--     * Slot: clause_reference Description: ISO/IEC 22989:2022 clause identifier (e.g. "5.11.4") the element corresponds to.
--     * Slot: preferred_label Description: Preferred natural-language label.
-- # Class: ModelDesigner Description: Producer role responsible for designing AI models (Clause 5.19.3).
--     * Slot: stakeholder_role_type Description: Canonical stakeholder role type as defined in Clause 5.19.
--     * Slot: organization_name Description: Name of the organisation acting in the stakeholder role.
--     * Slot: contact Description: Contact identifier (e.g. email) for the stakeholder.
--     * Slot: id Description: Unique CURIE or URI identifying the entity.
--     * Slot: name Description: Human-readable label for the entity.
--     * Slot: description Description: Free-text description of the entity (paraphrased; verbatim ISO text excluded).
--     * Slot: clause_reference Description: ISO/IEC 22989:2022 clause identifier (e.g. "5.11.4") the element corresponds to.
--     * Slot: preferred_label Description: Preferred natural-language label.
-- # Class: ModelImplementer Description: Producer role responsible for implementing AI models in code (Clause 5.19.3).
--     * Slot: stakeholder_role_type Description: Canonical stakeholder role type as defined in Clause 5.19.
--     * Slot: organization_name Description: Name of the organisation acting in the stakeholder role.
--     * Slot: contact Description: Contact identifier (e.g. email) for the stakeholder.
--     * Slot: id Description: Unique CURIE or URI identifying the entity.
--     * Slot: name Description: Human-readable label for the entity.
--     * Slot: description Description: Free-text description of the entity (paraphrased; verbatim ISO text excluded).
--     * Slot: clause_reference Description: ISO/IEC 22989:2022 clause identifier (e.g. "5.11.4") the element corresponds to.
--     * Slot: preferred_label Description: Preferred natural-language label.
-- # Class: ComputationVerifier Description: Producer role verifying the computational behaviour of an AI system (Clause 5.19.3).
--     * Slot: stakeholder_role_type Description: Canonical stakeholder role type as defined in Clause 5.19.
--     * Slot: organization_name Description: Name of the organisation acting in the stakeholder role.
--     * Slot: contact Description: Contact identifier (e.g. email) for the stakeholder.
--     * Slot: id Description: Unique CURIE or URI identifying the entity.
--     * Slot: name Description: Human-readable label for the entity.
--     * Slot: description Description: Free-text description of the entity (paraphrased; verbatim ISO text excluded).
--     * Slot: clause_reference Description: ISO/IEC 22989:2022 clause identifier (e.g. "5.11.4") the element corresponds to.
--     * Slot: preferred_label Description: Preferred natural-language label.
-- # Class: ModelVerifier Description: Producer role verifying that models meet specified requirements (Clause 5.19.3).
--     * Slot: stakeholder_role_type Description: Canonical stakeholder role type as defined in Clause 5.19.
--     * Slot: organization_name Description: Name of the organisation acting in the stakeholder role.
--     * Slot: contact Description: Contact identifier (e.g. email) for the stakeholder.
--     * Slot: id Description: Unique CURIE or URI identifying the entity.
--     * Slot: name Description: Human-readable label for the entity.
--     * Slot: description Description: Free-text description of the entity (paraphrased; verbatim ISO text excluded).
--     * Slot: clause_reference Description: ISO/IEC 22989:2022 clause identifier (e.g. "5.11.4") the element corresponds to.
--     * Slot: preferred_label Description: Preferred natural-language label.
-- # Class: AIUser Description: End user of an AI system or AI-backed service (Clause 5.19.4).
--     * Slot: stakeholder_role_type Description: Canonical stakeholder role type as defined in Clause 5.19.
--     * Slot: organization_name Description: Name of the organisation acting in the stakeholder role.
--     * Slot: contact Description: Contact identifier (e.g. email) for the stakeholder.
--     * Slot: id Description: Unique CURIE or URI identifying the entity.
--     * Slot: name Description: Human-readable label for the entity.
--     * Slot: description Description: Free-text description of the entity (paraphrased; verbatim ISO text excluded).
--     * Slot: clause_reference Description: ISO/IEC 22989:2022 clause identifier (e.g. "5.11.4") the element corresponds to.
--     * Slot: preferred_label Description: Preferred natural-language label.
-- # Class: AISystemIntegrator Description: Partner integrating AI components into a wider system (Clause 5.19.5).
--     * Slot: stakeholder_role_type Description: Canonical stakeholder role type as defined in Clause 5.19.
--     * Slot: organization_name Description: Name of the organisation acting in the stakeholder role.
--     * Slot: contact Description: Contact identifier (e.g. email) for the stakeholder.
--     * Slot: id Description: Unique CURIE or URI identifying the entity.
--     * Slot: name Description: Human-readable label for the entity.
--     * Slot: description Description: Free-text description of the entity (paraphrased; verbatim ISO text excluded).
--     * Slot: clause_reference Description: ISO/IEC 22989:2022 clause identifier (e.g. "5.11.4") the element corresponds to.
--     * Slot: preferred_label Description: Preferred natural-language label.
-- # Class: DataProvider Description: Partner supplying datasets used by AI systems (Clause 5.19.5).
--     * Slot: stakeholder_role_type Description: Canonical stakeholder role type as defined in Clause 5.19.
--     * Slot: organization_name Description: Name of the organisation acting in the stakeholder role.
--     * Slot: contact Description: Contact identifier (e.g. email) for the stakeholder.
--     * Slot: id Description: Unique CURIE or URI identifying the entity.
--     * Slot: name Description: Human-readable label for the entity.
--     * Slot: description Description: Free-text description of the entity (paraphrased; verbatim ISO text excluded).
--     * Slot: clause_reference Description: ISO/IEC 22989:2022 clause identifier (e.g. "5.11.4") the element corresponds to.
--     * Slot: preferred_label Description: Preferred natural-language label.
-- # Class: AIAuditor Description: Partner performing independent audits of AI systems (Clause 5.19.5).
--     * Slot: stakeholder_role_type Description: Canonical stakeholder role type as defined in Clause 5.19.
--     * Slot: organization_name Description: Name of the organisation acting in the stakeholder role.
--     * Slot: contact Description: Contact identifier (e.g. email) for the stakeholder.
--     * Slot: id Description: Unique CURIE or URI identifying the entity.
--     * Slot: name Description: Human-readable label for the entity.
--     * Slot: description Description: Free-text description of the entity (paraphrased; verbatim ISO text excluded).
--     * Slot: clause_reference Description: ISO/IEC 22989:2022 clause identifier (e.g. "5.11.4") the element corresponds to.
--     * Slot: preferred_label Description: Preferred natural-language label.
-- # Class: AIEvaluator Description: Partner performing evaluations of AI system performance and trustworthiness (Clause 5.19.5).
--     * Slot: stakeholder_role_type Description: Canonical stakeholder role type as defined in Clause 5.19.
--     * Slot: organization_name Description: Name of the organisation acting in the stakeholder role.
--     * Slot: contact Description: Contact identifier (e.g. email) for the stakeholder.
--     * Slot: id Description: Unique CURIE or URI identifying the entity.
--     * Slot: name Description: Human-readable label for the entity.
--     * Slot: description Description: Free-text description of the entity (paraphrased; verbatim ISO text excluded).
--     * Slot: clause_reference Description: ISO/IEC 22989:2022 clause identifier (e.g. "5.11.4") the element corresponds to.
--     * Slot: preferred_label Description: Preferred natural-language label.
-- # Class: DataSubject Description: Individual whose personal data is processed by an AI system (Clause 5.19.6).
--     * Slot: stakeholder_role_type Description: Canonical stakeholder role type as defined in Clause 5.19.
--     * Slot: organization_name Description: Name of the organisation acting in the stakeholder role.
--     * Slot: contact Description: Contact identifier (e.g. email) for the stakeholder.
--     * Slot: id Description: Unique CURIE or URI identifying the entity.
--     * Slot: name Description: Human-readable label for the entity.
--     * Slot: description Description: Free-text description of the entity (paraphrased; verbatim ISO text excluded).
--     * Slot: clause_reference Description: ISO/IEC 22989:2022 clause identifier (e.g. "5.11.4") the element corresponds to.
--     * Slot: preferred_label Description: Preferred natural-language label.
-- # Class: PolicyMaker Description: Authority defining policy applicable to AI systems (Clause 5.19.7).
--     * Slot: stakeholder_role_type Description: Canonical stakeholder role type as defined in Clause 5.19.
--     * Slot: organization_name Description: Name of the organisation acting in the stakeholder role.
--     * Slot: contact Description: Contact identifier (e.g. email) for the stakeholder.
--     * Slot: id Description: Unique CURIE or URI identifying the entity.
--     * Slot: name Description: Human-readable label for the entity.
--     * Slot: description Description: Free-text description of the entity (paraphrased; verbatim ISO text excluded).
--     * Slot: clause_reference Description: ISO/IEC 22989:2022 clause identifier (e.g. "5.11.4") the element corresponds to.
--     * Slot: preferred_label Description: Preferred natural-language label.
-- # Class: Regulator Description: Authority responsible for regulatory oversight of AI systems (Clause 5.19.7).
--     * Slot: stakeholder_role_type Description: Canonical stakeholder role type as defined in Clause 5.19.
--     * Slot: organization_name Description: Name of the organisation acting in the stakeholder role.
--     * Slot: contact Description: Contact identifier (e.g. email) for the stakeholder.
--     * Slot: id Description: Unique CURIE or URI identifying the entity.
--     * Slot: name Description: Human-readable label for the entity.
--     * Slot: description Description: Free-text description of the entity (paraphrased; verbatim ISO text excluded).
--     * Slot: clause_reference Description: ISO/IEC 22989:2022 clause identifier (e.g. "5.11.4") the element corresponds to.
--     * Slot: preferred_label Description: Preferred natural-language label.
-- # Class: AutonomyAssessment Description: Structured assessment of the autonomy level of an AI system using the criteria listed in Clause 5.13.
--     * Slot: autonomy_level Description: Operational autonomy level of the AI system.
--     * Slot: clause_reference Description: ISO/IEC 22989:2022 clause identifier (e.g. "5.11.4") the element corresponds to.
--     * Slot: id Description: Unique CURIE or URI identifying the entity.
--     * Slot: name Description: Human-readable label for the entity.
--     * Slot: description Description: Free-text description of the entity (paraphrased; verbatim ISO text excluded).
--     * Slot: preferred_label Description: Preferred natural-language label.
-- # Class: VerificationValidationFramework Description: Verifiability and validatability claim for an AI system characterised according to the levels in Clause 5.16.
--     * Slot: verification_validation_level Description: Verifiability / validatability claim (Clause 5.16).
--     * Slot: clause_reference Description: ISO/IEC 22989:2022 clause identifier (e.g. "5.11.4") the element corresponds to.
--     * Slot: id Description: Unique CURIE or URI identifying the entity.
--     * Slot: name Description: Human-readable label for the entity.
--     * Slot: description Description: Free-text description of the entity (paraphrased; verbatim ISO text excluded).
--     * Slot: preferred_label Description: Preferred natural-language label.
-- # Class: HumanMachineTeam Description: Collaboration arrangement combining one or more humans with one or more AI systems to pursue shared goals (Clauses 3.3.3, 5.13).
--     * Slot: task_allocation Description: Free-text description of how tasks are allocated between humans and AI.
--     * Slot: id Description: Unique CURIE or URI identifying the entity.
--     * Slot: name Description: Human-readable label for the entity.
--     * Slot: description Description: Free-text description of the entity (paraphrased; verbatim ISO text excluded).
--     * Slot: clause_reference Description: ISO/IEC 22989:2022 clause identifier (e.g. "5.11.4") the element corresponds to.
--     * Slot: preferred_label Description: Preferred natural-language label.
-- # Class: IntelligenceAugmentation Description: Use of AI to enhance the cognitive capabilities of humans rather than replace them (Clause 5.13 context).
--     * Slot: id Description: Unique CURIE or URI identifying the entity.
--     * Slot: name Description: Human-readable label for the entity.
--     * Slot: description Description: Free-text description of the entity (paraphrased; verbatim ISO text excluded).
--     * Slot: clause_reference Description: ISO/IEC 22989:2022 clause identifier (e.g. "5.11.4") the element corresponds to.
--     * Slot: preferred_label Description: Preferred natural-language label.
-- # Class: Recommendation Description: Recommendation produced by an AI system (Clauses 7.4, 10).
--     * Slot: recommendation_outcome_type Description: High-level outcome type of a recommendation (Clauses 7.4, 10).
--     * Slot: confidence Description: Normalised confidence value associated with an output or claim.
--     * Slot: id Description: Unique CURIE or URI identifying the entity.
--     * Slot: name Description: Human-readable label for the entity.
--     * Slot: description Description: Free-text description of the entity (paraphrased; verbatim ISO text excluded).
--     * Slot: clause_reference Description: ISO/IEC 22989:2022 clause identifier (e.g. "5.11.4") the element corresponds to.
--     * Slot: preferred_label Description: Preferred natural-language label.
-- # Class: EvaluationMetric Description: Metric used to evaluate AI system or model performance (Clause 7.4.3).
--     * Slot: metric_name Description: Name of the metric (e.g. accuracy, F1, MAE).
--     * Slot: metric_value Description: Observed numeric value of the metric.
--     * Slot: metric_unit Description: Unit of the metric, when applicable.
--     * Slot: reference_dataset Description: Dataset against which the metric was computed.
--     * Slot: id Description: Unique CURIE or URI identifying the entity.
--     * Slot: name Description: Human-readable label for the entity.
--     * Slot: description Description: Free-text description of the entity (paraphrased; verbatim ISO text excluded).
--     * Slot: clause_reference Description: ISO/IEC 22989:2022 clause identifier (e.g. "5.11.4") the element corresponds to.
--     * Slot: preferred_label Description: Preferred natural-language label.
-- # Class: Threshold Description: Decision threshold applied to a metric, prediction or score (Clause 7.4.3).
--     * Slot: threshold_value Description: Numeric threshold value.
--     * Slot: applies_to_metric Description: Name of the metric or score the threshold applies to.
--     * Slot: threshold_policy Description: Policy describing how the threshold is interpreted.
--     * Slot: id Description: Unique CURIE or URI identifying the entity.
--     * Slot: name Description: Human-readable label for the entity.
--     * Slot: description Description: Free-text description of the entity (paraphrased; verbatim ISO text excluded).
--     * Slot: clause_reference Description: ISO/IEC 22989:2022 clause identifier (e.g. "5.11.4") the element corresponds to.
--     * Slot: preferred_label Description: Preferred natural-language label.
-- # Class: Neuron Description: Computational unit in a neural network combining weighted inputs with a bias and an activation function (Clause 3.4.9).
--     * Slot: activation_function Description: Activation function applied at the neuron output.
--     * Slot: input_arity Description: Number of inputs combined by the neuron.
--     * Slot: id Description: Unique CURIE or URI identifying the entity.
--     * Slot: name Description: Human-readable label for the entity.
--     * Slot: description Description: Free-text description of the entity (paraphrased; verbatim ISO text excluded).
--     * Slot: clause_reference Description: ISO/IEC 22989:2022 clause identifier (e.g. "5.11.4") the element corresponds to.
--     * Slot: preferred_label Description: Preferred natural-language label.
-- # Class: ConvolutionOperation Description: Convolution operation as used in convolutional neural networks (Clause 3.4.3).
--     * Slot: stride Description: Stride applied when sliding the kernel over the input.
--     * Slot: padding Description: Padding mode (e.g. valid, same).
--     * Slot: id Description: Unique CURIE or URI identifying the entity.
--     * Slot: name Description: Human-readable label for the entity.
--     * Slot: description Description: Free-text description of the entity (paraphrased; verbatim ISO text excluded).
--     * Slot: clause_reference Description: ISO/IEC 22989:2022 clause identifier (e.g. "5.11.4") the element corresponds to.
--     * Slot: preferred_label Description: Preferred natural-language label.
-- # Class: DataDrift Description: Observed change in the statistical distribution of operational data relative to training data (Clause 5.11.9.1).
--     * Slot: drift_type Description: Type of drift (covariate, label, concept).
--     * Slot: detected_at Description: Timestamp or interval at which drift was detected.
--     * Slot: affected_dataset Description: Dataset in which drift was observed.
--     * Slot: id Description: Unique CURIE or URI identifying the entity.
--     * Slot: name Description: Human-readable label for the entity.
--     * Slot: description Description: Free-text description of the entity (paraphrased; verbatim ISO text excluded).
--     * Slot: clause_reference Description: ISO/IEC 22989:2022 clause identifier (e.g. "5.11.4") the element corresponds to.
--     * Slot: preferred_label Description: Preferred natural-language label.
-- # Class: CatastrophicForgetting Description: Phenomenon by which a continually-trained model loses previously acquired competence (Clause 5.11.9.1).
--     * Slot: affected_model Description: Model in which the phenomenon was observed.
--     * Slot: mitigation_strategy Description: Strategy applied to mitigate the phenomenon.
--     * Slot: id Description: Unique CURIE or URI identifying the entity.
--     * Slot: name Description: Human-readable label for the entity.
--     * Slot: description Description: Free-text description of the entity (paraphrased; verbatim ISO text excluded).
--     * Slot: clause_reference Description: ISO/IEC 22989:2022 clause identifier (e.g. "5.11.4") the element corresponds to.
--     * Slot: preferred_label Description: Preferred natural-language label.
-- # Class: FaultToleranceMechanism Description: Mechanism enabling an AI system to continue operating correctly in the presence of component faults (Clause 5.15.4 context).
--     * Slot: mechanism_type Description: Type of mechanism (redundancy, graceful degradation, failover, etc.).
--     * Slot: coverage_scope Description: Scope of failure modes the mechanism covers.
--     * Slot: id Description: Unique CURIE or URI identifying the entity.
--     * Slot: name Description: Human-readable label for the entity.
--     * Slot: description Description: Free-text description of the entity (paraphrased; verbatim ISO text excluded).
--     * Slot: clause_reference Description: ISO/IEC 22989:2022 clause identifier (e.g. "5.11.4") the element corresponds to.
--     * Slot: preferred_label Description: Preferred natural-language label.
-- # Class: NaturalLanguage Description: Natural language treated as an object of processing or generation by an AI system (Clause 9.2).
--     * Slot: language_code Description: BCP-47 language tag.
--     * Slot: script Description: ISO 15924 script code, when relevant.
--     * Slot: id Description: Unique CURIE or URI identifying the entity.
--     * Slot: name Description: Human-readable label for the entity.
--     * Slot: description Description: Free-text description of the entity (paraphrased; verbatim ISO text excluded).
--     * Slot: clause_reference Description: ISO/IEC 22989:2022 clause identifier (e.g. "5.11.4") the element corresponds to.
--     * Slot: preferred_label Description: Preferred natural-language label.
-- # Class: RiskItem Description: Risk associated with an AI system, capturing source, potential event, consequence and treatment metadata (Clause 3.5.11; aligned with ISO/IEC 23894 risk concepts).
--     * Slot: risk_source Description: Source from which the risk originates.
--     * Slot: potential_event Description: Potential event whose occurrence would realise the risk.
--     * Slot: consequence Description: Consequence to one or more stakeholders if the event occurs.
--     * Slot: likelihood Description: Estimated likelihood of the event (0.0–1.0).
--     * Slot: severity Description: Qualitative severity assessment of the consequence.
--     * Slot: id Description: Unique CURIE or URI identifying the entity.
--     * Slot: name Description: Human-readable label for the entity.
--     * Slot: description Description: Free-text description of the entity (paraphrased; verbatim ISO text excluded).
--     * Slot: clause_reference Description: ISO/IEC 22989:2022 clause identifier (e.g. "5.11.4") the element corresponds to.
--     * Slot: preferred_label Description: Preferred natural-language label.
-- # Class: InputData Description: Data presented to an AI system at inference time or during training (Clause 3.2.9).
--     * Slot: data_source_type Description: Classification of a data source (Clause 8.6.1).
--     * Slot: data_collection_method Description: Method used to collect data (Clause 8.6.1).
--     * Slot: modality Description: Modality of the input data.
--     * Slot: consumed_by Description: AI system that consumes the input.
--     * Slot: id Description: Unique CURIE or URI identifying the entity.
--     * Slot: name Description: Human-readable label for the entity.
--     * Slot: description Description: Free-text description of the entity (paraphrased; verbatim ISO text excluded).
--     * Slot: clause_reference Description: ISO/IEC 22989:2022 clause identifier (e.g. "5.11.4") the element corresponds to.
--     * Slot: preferred_label Description: Preferred natural-language label.
-- # Class: Inference Description: Act of deriving conclusions, predictions or recommendations from a model or knowledge base (Clause 3.1.17).
--     * Slot: inference_strategy Description: Strategy used (forward-chaining, backward-chaining, probabilistic, neural forward pass).
--     * Slot: performed_by Description: Engine that performed the inference.
--     * Slot: over_model Description: Model over which the inference was performed.
--     * Slot: produced_output Description: Serialised representation of the inference output.
--     * Slot: id Description: Unique CURIE or URI identifying the entity.
--     * Slot: name Description: Human-readable label for the entity.
--     * Slot: description Description: Free-text description of the entity (paraphrased; verbatim ISO text excluded).
--     * Slot: clause_reference Description: ISO/IEC 22989:2022 clause identifier (e.g. "5.11.4") the element corresponds to.
--     * Slot: preferred_label Description: Preferred natural-language label.
-- # Class: OECDLifecycleMapping Description: Informative mapping between an ISO/IEC 22989 life-cycle stage and an OECD life-cycle stage (Annex A).
--     * Slot: iso_stage Description: ISO/IEC 22989 life-cycle stage.
--     * Slot: oecd_stage Description: Corresponding OECD life-cycle stage.
--     * Slot: mapping_notes Description: Free-text notes on the mapping relationship.
--     * Slot: id Description: Unique CURIE or URI identifying the entity.
--     * Slot: name Description: Human-readable label for the entity.
--     * Slot: description Description: Free-text description of the entity (paraphrased; verbatim ISO text excluded).
--     * Slot: clause_reference Description: ISO/IEC 22989:2022 clause identifier (e.g. "5.11.4") the element corresponds to.
--     * Slot: preferred_label Description: Preferred natural-language label.
-- # Class: Organization Description: Organisation that establishes and operates an AI management system; Annex SL harmonised anchor shared across ISO management-system standards (ISO/IEC 42001, ISO/IEC 27001).
--     * Slot: id Description: Unique CURIE or URI identifying the entity.
--     * Slot: name Description: Human-readable label for the entity.
--     * Slot: description Description: Free-text description of the entity (paraphrased; verbatim ISO text excluded).
--     * Slot: clause_reference Description: ISO/IEC 22989:2022 clause identifier (e.g. "5.11.4") the element corresponds to.
--     * Slot: preferred_label Description: Preferred natural-language label.
-- # Class: InterestedParty Description: Person or organisation that can affect, be affected by, or perceive itself to be affected by a decision or activity; Annex SL harmonised stakeholder anchor shared across ISO management-system standards.
--     * Slot: id Description: Unique CURIE or URI identifying the entity.
--     * Slot: name Description: Human-readable label for the entity.
--     * Slot: description Description: Free-text description of the entity (paraphrased; verbatim ISO text excluded).
--     * Slot: clause_reference Description: ISO/IEC 22989:2022 clause identifier (e.g. "5.11.4") the element corresponds to.
--     * Slot: preferred_label Description: Preferred natural-language label.
-- # Class: NamedEntity_aliases
--     * Slot: NamedEntity_id Description: Autocreated FK slot
--     * Slot: aliases Description: Alternative names or synonyms for the term.
-- # Class: NamedEntity_see_also_uri
--     * Slot: NamedEntity_id Description: Autocreated FK slot
--     * Slot: see_also_uri Description: Pointers to related external resources or term records.
-- # Class: Term_aliases
--     * Slot: Term_id Description: Autocreated FK slot
--     * Slot: aliases Description: Alternative names or synonyms for the term.
-- # Class: Term_see_also_uri
--     * Slot: Term_id Description: Autocreated FK slot
--     * Slot: see_also_uri Description: Pointers to related external resources or term records.
-- # Class: AITerm_aliases
--     * Slot: AITerm_id Description: Autocreated FK slot
--     * Slot: aliases Description: Alternative names or synonyms for the term.
-- # Class: AITerm_see_also_uri
--     * Slot: AITerm_id Description: Autocreated FK slot
--     * Slot: see_also_uri Description: Pointers to related external resources or term records.
-- # Class: DataTerm_aliases
--     * Slot: DataTerm_id Description: Autocreated FK slot
--     * Slot: aliases Description: Alternative names or synonyms for the term.
-- # Class: DataTerm_see_also_uri
--     * Slot: DataTerm_id Description: Autocreated FK slot
--     * Slot: see_also_uri Description: Pointers to related external resources or term records.
-- # Class: MachineLearningTerm_aliases
--     * Slot: MachineLearningTerm_id Description: Autocreated FK slot
--     * Slot: aliases Description: Alternative names or synonyms for the term.
-- # Class: MachineLearningTerm_see_also_uri
--     * Slot: MachineLearningTerm_id Description: Autocreated FK slot
--     * Slot: see_also_uri Description: Pointers to related external resources or term records.
-- # Class: NeuralNetworkTerm_aliases
--     * Slot: NeuralNetworkTerm_id Description: Autocreated FK slot
--     * Slot: aliases Description: Alternative names or synonyms for the term.
-- # Class: NeuralNetworkTerm_see_also_uri
--     * Slot: NeuralNetworkTerm_id Description: Autocreated FK slot
--     * Slot: see_also_uri Description: Pointers to related external resources or term records.
-- # Class: TrustworthinessTerm_aliases
--     * Slot: TrustworthinessTerm_id Description: Autocreated FK slot
--     * Slot: aliases Description: Alternative names or synonyms for the term.
-- # Class: TrustworthinessTerm_see_also_uri
--     * Slot: TrustworthinessTerm_id Description: Autocreated FK slot
--     * Slot: see_also_uri Description: Pointers to related external resources or term records.
-- # Class: NLPTerm_aliases
--     * Slot: NLPTerm_id Description: Autocreated FK slot
--     * Slot: aliases Description: Alternative names or synonyms for the term.
-- # Class: NLPTerm_see_also_uri
--     * Slot: NLPTerm_id Description: Autocreated FK slot
--     * Slot: see_also_uri Description: Pointers to related external resources or term records.
-- # Class: ComputerVisionTerm_aliases
--     * Slot: ComputerVisionTerm_id Description: Autocreated FK slot
--     * Slot: aliases Description: Alternative names or synonyms for the term.
-- # Class: ComputerVisionTerm_see_also_uri
--     * Slot: ComputerVisionTerm_id Description: Autocreated FK slot
--     * Slot: see_also_uri Description: Pointers to related external resources or term records.
-- # Class: AbbreviatedTerm_aliases
--     * Slot: AbbreviatedTerm_id Description: Autocreated FK slot
--     * Slot: aliases Description: Alternative names or synonyms for the term.
-- # Class: AbbreviatedTerm_see_also_uri
--     * Slot: AbbreviatedTerm_id Description: Autocreated FK slot
--     * Slot: see_also_uri Description: Pointers to related external resources or term records.
-- # Class: AIConcept_aliases
--     * Slot: AIConcept_id Description: Autocreated FK slot
--     * Slot: aliases Description: Alternative names or synonyms for the term.
-- # Class: AIConcept_see_also_uri
--     * Slot: AIConcept_id Description: Autocreated FK slot
--     * Slot: see_also_uri Description: Pointers to related external resources or term records.
-- # Class: AIAgent_goal_set
--     * Slot: AIAgent_id Description: Autocreated FK slot
--     * Slot: goal_set Description: Goals the agent is configured to pursue.
-- # Class: AIAgent_aliases
--     * Slot: AIAgent_id Description: Autocreated FK slot
--     * Slot: aliases Description: Alternative names or synonyms for the term.
-- # Class: AIAgent_see_also_uri
--     * Slot: AIAgent_id Description: Autocreated FK slot
--     * Slot: see_also_uri Description: Pointers to related external resources or term records.
-- # Class: KnowledgeRepresentation_aliases
--     * Slot: KnowledgeRepresentation_id Description: Autocreated FK slot
--     * Slot: aliases Description: Alternative names or synonyms for the term.
-- # Class: KnowledgeRepresentation_see_also_uri
--     * Slot: KnowledgeRepresentation_id Description: Autocreated FK slot
--     * Slot: see_also_uri Description: Pointers to related external resources or term records.
-- # Class: AISystem_application_domain
--     * Slot: AISystem_id Description: Autocreated FK slot
--     * Slot: application_domain Description: Application domain(s) the AI system targets.
-- # Class: AISystem_ai_field
--     * Slot: AISystem_id Description: Autocreated FK slot
--     * Slot: ai_field Description: AI sub-field(s) the system draws on.
-- # Class: AISystem_functional_components
--     * Slot: AISystem_id Description: Autocreated FK slot
--     * Slot: functional_components Description: Functional components exhibited by the system (Clause 7).
-- # Class: AISystem_jurisdictional_issues
--     * Slot: AISystem_id Description: Autocreated FK slot
--     * Slot: jurisdictional_issues Description: Jurisdictional issues considered in scope for the application.
-- # Class: AISystem_societal_impacts
--     * Slot: AISystem_id Description: Autocreated FK slot
--     * Slot: societal_impacts Description: Societal impact categories considered in scope.
-- # Class: AISystem_system_characteristics
--     * Slot: AISystem_id Description: Autocreated FK slot
--     * Slot: system_characteristics Description: Distinguishing characteristics from Clause 5.1.
-- # Class: AISystem_task_categories
--     * Slot: AISystem_id Description: Autocreated FK slot
--     * Slot: task_categories Description: Task categories the AI system addresses.
-- # Class: AISystem_aliases
--     * Slot: AISystem_id Description: Autocreated FK slot
--     * Slot: aliases Description: Alternative names or synonyms for the term.
-- # Class: AISystem_see_also_uri
--     * Slot: AISystem_id Description: Autocreated FK slot
--     * Slot: see_also_uri Description: Pointers to related external resources or term records.
-- # Class: AIComponent_depends_on
--     * Slot: AIComponent_id Description: Autocreated FK slot
--     * Slot: depends_on_id Description: Other components this component depends on at runtime.
-- # Class: AIComponent_aliases
--     * Slot: AIComponent_id Description: Autocreated FK slot
--     * Slot: aliases Description: Alternative names or synonyms for the term.
-- # Class: AIComponent_see_also_uri
--     * Slot: AIComponent_id Description: Autocreated FK slot
--     * Slot: see_also_uri Description: Pointers to related external resources or term records.
-- # Class: AIModel_hyperparameters
--     * Slot: AIModel_id Description: Autocreated FK slot
--     * Slot: hyperparameters Description: Free-form record of model hyperparameter settings.
-- # Class: AIModel_training_phenomena
--     * Slot: AIModel_id Description: Autocreated FK slot
--     * Slot: training_phenomena Description: Training-time phenomena observed for the model (Clause 3.4).
-- # Class: AIModel_aliases
--     * Slot: AIModel_id Description: Autocreated FK slot
--     * Slot: aliases Description: Alternative names or synonyms for the term.
-- # Class: AIModel_see_also_uri
--     * Slot: AIModel_id Description: Autocreated FK slot
--     * Slot: see_also_uri Description: Pointers to related external resources or term records.
-- # Class: NeuralNetworkModel_hyperparameters
--     * Slot: NeuralNetworkModel_id Description: Autocreated FK slot
--     * Slot: hyperparameters Description: Free-form record of model hyperparameter settings.
-- # Class: NeuralNetworkModel_training_phenomena
--     * Slot: NeuralNetworkModel_id Description: Autocreated FK slot
--     * Slot: training_phenomena Description: Training-time phenomena observed for the model (Clause 3.4).
-- # Class: NeuralNetworkModel_aliases
--     * Slot: NeuralNetworkModel_id Description: Autocreated FK slot
--     * Slot: aliases Description: Alternative names or synonyms for the term.
-- # Class: NeuralNetworkModel_see_also_uri
--     * Slot: NeuralNetworkModel_id Description: Autocreated FK slot
--     * Slot: see_also_uri Description: Pointers to related external resources or term records.
-- # Class: Dataset_data_modality
--     * Slot: Dataset_id Description: Autocreated FK slot
--     * Slot: data_modality Description: Modalities present in the dataset.
-- # Class: Dataset_aliases
--     * Slot: Dataset_id Description: Autocreated FK slot
--     * Slot: aliases Description: Alternative names or synonyms for the term.
-- # Class: Dataset_see_also_uri
--     * Slot: Dataset_id Description: Autocreated FK slot
--     * Slot: see_also_uri Description: Pointers to related external resources or term records.
-- # Class: TrustworthinessProperty_property_evidence
--     * Slot: TrustworthinessProperty_id Description: Autocreated FK slot
--     * Slot: property_evidence Description: References to evidence supporting the property claim.
-- # Class: TrustworthinessProperty_applicable_biases
--     * Slot: TrustworthinessProperty_id Description: Autocreated FK slot
--     * Slot: applicable_biases Description: Bias categories considered relevant to this property assessment.
-- # Class: TrustworthinessProperty_aliases
--     * Slot: TrustworthinessProperty_id Description: Autocreated FK slot
--     * Slot: aliases Description: Alternative names or synonyms for the term.
-- # Class: TrustworthinessProperty_see_also_uri
--     * Slot: TrustworthinessProperty_id Description: Autocreated FK slot
--     * Slot: see_also_uri Description: Pointers to related external resources or term records.
-- # Class: AILifecycleProcess_process_inputs
--     * Slot: AILifecycleProcess_id Description: Autocreated FK slot
--     * Slot: process_inputs Description: Inputs consumed by the process.
-- # Class: AILifecycleProcess_process_outputs
--     * Slot: AILifecycleProcess_id Description: Autocreated FK slot
--     * Slot: process_outputs Description: Outputs produced by the process.
-- # Class: AILifecycleProcess_risk_items
--     * Slot: AILifecycleProcess_id Description: Autocreated FK slot
--     * Slot: risk_items Description: Risks identified or addressed by a process or assessment.
-- # Class: AILifecycleProcess_approval_criteria
--     * Slot: AILifecycleProcess_id Description: Autocreated FK slot
--     * Slot: approval_criteria Description: Criteria that must be met for an output or process to be approved.
-- # Class: AILifecycleProcess_aliases
--     * Slot: AILifecycleProcess_id Description: Autocreated FK slot
--     * Slot: aliases Description: Alternative names or synonyms for the term.
-- # Class: AILifecycleProcess_see_also_uri
--     * Slot: AILifecycleProcess_id Description: Autocreated FK slot
--     * Slot: see_also_uri Description: Pointers to related external resources or term records.
-- # Class: AIStakeholderRole_responsibilities
--     * Slot: AIStakeholderRole_id Description: Autocreated FK slot
--     * Slot: responsibilities Description: Free-text statements of responsibility.
-- # Class: AIStakeholderRole_aliases
--     * Slot: AIStakeholderRole_id Description: Autocreated FK slot
--     * Slot: aliases Description: Alternative names or synonyms for the term.
-- # Class: AIStakeholderRole_see_also_uri
--     * Slot: AIStakeholderRole_id Description: Autocreated FK slot
--     * Slot: see_also_uri Description: Pointers to related external resources or term records.
-- # Class: AIProvider_responsibilities
--     * Slot: AIProvider_id Description: Autocreated FK slot
--     * Slot: responsibilities Description: Free-text statements of responsibility.
-- # Class: AIProvider_aliases
--     * Slot: AIProvider_id Description: Autocreated FK slot
--     * Slot: aliases Description: Alternative names or synonyms for the term.
-- # Class: AIProvider_see_also_uri
--     * Slot: AIProvider_id Description: Autocreated FK slot
--     * Slot: see_also_uri Description: Pointers to related external resources or term records.
-- # Class: AIProducer_responsibilities
--     * Slot: AIProducer_id Description: Autocreated FK slot
--     * Slot: responsibilities Description: Free-text statements of responsibility.
-- # Class: AIProducer_aliases
--     * Slot: AIProducer_id Description: Autocreated FK slot
--     * Slot: aliases Description: Alternative names or synonyms for the term.
-- # Class: AIProducer_see_also_uri
--     * Slot: AIProducer_id Description: Autocreated FK slot
--     * Slot: see_also_uri Description: Pointers to related external resources or term records.
-- # Class: AICustomer_responsibilities
--     * Slot: AICustomer_id Description: Autocreated FK slot
--     * Slot: responsibilities Description: Free-text statements of responsibility.
-- # Class: AICustomer_aliases
--     * Slot: AICustomer_id Description: Autocreated FK slot
--     * Slot: aliases Description: Alternative names or synonyms for the term.
-- # Class: AICustomer_see_also_uri
--     * Slot: AICustomer_id Description: Autocreated FK slot
--     * Slot: see_also_uri Description: Pointers to related external resources or term records.
-- # Class: AIPartner_responsibilities
--     * Slot: AIPartner_id Description: Autocreated FK slot
--     * Slot: responsibilities Description: Free-text statements of responsibility.
-- # Class: AIPartner_aliases
--     * Slot: AIPartner_id Description: Autocreated FK slot
--     * Slot: aliases Description: Alternative names or synonyms for the term.
-- # Class: AIPartner_see_also_uri
--     * Slot: AIPartner_id Description: Autocreated FK slot
--     * Slot: see_also_uri Description: Pointers to related external resources or term records.
-- # Class: AISubject_responsibilities
--     * Slot: AISubject_id Description: Autocreated FK slot
--     * Slot: responsibilities Description: Free-text statements of responsibility.
-- # Class: AISubject_aliases
--     * Slot: AISubject_id Description: Autocreated FK slot
--     * Slot: aliases Description: Alternative names or synonyms for the term.
-- # Class: AISubject_see_also_uri
--     * Slot: AISubject_id Description: Autocreated FK slot
--     * Slot: see_also_uri Description: Pointers to related external resources or term records.
-- # Class: RelevantAuthority_responsibilities
--     * Slot: RelevantAuthority_id Description: Autocreated FK slot
--     * Slot: responsibilities Description: Free-text statements of responsibility.
-- # Class: RelevantAuthority_aliases
--     * Slot: RelevantAuthority_id Description: Autocreated FK slot
--     * Slot: aliases Description: Alternative names or synonyms for the term.
-- # Class: RelevantAuthority_see_also_uri
--     * Slot: RelevantAuthority_id Description: Autocreated FK slot
--     * Slot: see_also_uri Description: Pointers to related external resources or term records.
-- # Class: AIEcosystem_computing_resources
--     * Slot: AIEcosystem_id Description: Autocreated FK slot
--     * Slot: computing_resources Description: Computing resource types relied upon.
-- # Class: AIEcosystem_data_sources
--     * Slot: AIEcosystem_id Description: Autocreated FK slot
--     * Slot: data_sources Description: Identifiers or descriptions of data sources feeding the ecosystem.
-- # Class: AIEcosystem_ecosystem_components
--     * Slot: AIEcosystem_id Description: Autocreated FK slot
--     * Slot: ecosystem_components Description: Free-text or CURIE references to ecosystem components.
-- # Class: AIEcosystem_big_data_characteristics
--     * Slot: AIEcosystem_id Description: Autocreated FK slot
--     * Slot: big_data_characteristics Description: Big-data characteristics that the ecosystem exhibits (Clause 8.6.1).
-- # Class: AIEcosystem_aliases
--     * Slot: AIEcosystem_id Description: Autocreated FK slot
--     * Slot: aliases Description: Alternative names or synonyms for the term.
-- # Class: AIEcosystem_see_also_uri
--     * Slot: AIEcosystem_id Description: Autocreated FK slot
--     * Slot: see_also_uri Description: Pointers to related external resources or term records.
-- # Class: ResourcePool_aliases
--     * Slot: ResourcePool_id Description: Autocreated FK slot
--     * Slot: aliases Description: Alternative names or synonyms for the term.
-- # Class: ResourcePool_see_also_uri
--     * Slot: ResourcePool_id Description: Autocreated FK slot
--     * Slot: see_also_uri Description: Pointers to related external resources or term records.
-- # Class: NLPComponent_aliases
--     * Slot: NLPComponent_id Description: Autocreated FK slot
--     * Slot: aliases Description: Alternative names or synonyms for the term.
-- # Class: NLPComponent_see_also_uri
--     * Slot: NLPComponent_id Description: Autocreated FK slot
--     * Slot: see_also_uri Description: Pointers to related external resources or term records.
-- # Class: ComputerVisionFunction_aliases
--     * Slot: ComputerVisionFunction_id Description: Autocreated FK slot
--     * Slot: aliases Description: Alternative names or synonyms for the term.
-- # Class: ComputerVisionFunction_see_also_uri
--     * Slot: ComputerVisionFunction_id Description: Autocreated FK slot
--     * Slot: see_also_uri Description: Pointers to related external resources or term records.
-- # Class: AIApplication_application_domain
--     * Slot: AIApplication_id Description: Autocreated FK slot
--     * Slot: application_domain Description: Application domain(s) the AI system targets.
-- # Class: AIApplication_jurisdictional_issues
--     * Slot: AIApplication_id Description: Autocreated FK slot
--     * Slot: jurisdictional_issues Description: Jurisdictional issues considered in scope for the application.
-- # Class: AIApplication_societal_impacts
--     * Slot: AIApplication_id Description: Autocreated FK slot
--     * Slot: societal_impacts Description: Societal impact categories considered in scope.
-- # Class: AIApplication_aliases
--     * Slot: AIApplication_id Description: Autocreated FK slot
--     * Slot: aliases Description: Alternative names or synonyms for the term.
-- # Class: AIApplication_see_also_uri
--     * Slot: AIApplication_id Description: Autocreated FK slot
--     * Slot: see_also_uri Description: Pointers to related external resources or term records.
-- # Class: Task_input_modalities
--     * Slot: Task_id Description: Autocreated FK slot
--     * Slot: input_modalities Description: Modalities of input accepted by a task or component.
-- # Class: Task_performance_metric
--     * Slot: Task_id Description: Autocreated FK slot
--     * Slot: performance_metric Description: Metrics used to evaluate performance.
-- # Class: Task_aliases
--     * Slot: Task_id Description: Autocreated FK slot
--     * Slot: aliases Description: Alternative names or synonyms for the term.
-- # Class: Task_see_also_uri
--     * Slot: Task_id Description: Autocreated FK slot
--     * Slot: see_also_uri Description: Pointers to related external resources or term records.
-- # Class: Prediction_aliases
--     * Slot: Prediction_id Description: Autocreated FK slot
--     * Slot: aliases Description: Alternative names or synonyms for the term.
-- # Class: Prediction_see_also_uri
--     * Slot: Prediction_id Description: Autocreated FK slot
--     * Slot: see_also_uri Description: Pointers to related external resources or term records.
-- # Class: Decision_based_on_predictions
--     * Slot: Decision_id Description: Autocreated FK slot
--     * Slot: based_on_predictions_id Description: Predictions that supported the decision.
-- # Class: Decision_aliases
--     * Slot: Decision_id Description: Autocreated FK slot
--     * Slot: aliases Description: Alternative names or synonyms for the term.
-- # Class: Decision_see_also_uri
--     * Slot: Decision_id Description: Autocreated FK slot
--     * Slot: see_also_uri Description: Pointers to related external resources or term records.
-- # Class: Action_aliases
--     * Slot: Action_id Description: Autocreated FK slot
--     * Slot: aliases Description: Alternative names or synonyms for the term.
-- # Class: Action_see_also_uri
--     * Slot: Action_id Description: Autocreated FK slot
--     * Slot: see_also_uri Description: Pointers to related external resources or term records.
-- # Class: InferenceEngine_aliases
--     * Slot: InferenceEngine_id Description: Autocreated FK slot
--     * Slot: aliases Description: Alternative names or synonyms for the term.
-- # Class: InferenceEngine_see_also_uri
--     * Slot: InferenceEngine_id Description: Autocreated FK slot
--     * Slot: see_also_uri Description: Pointers to related external resources or term records.
-- # Class: KnowledgeGraph_ontology_reference
--     * Slot: KnowledgeGraph_id Description: Autocreated FK slot
--     * Slot: ontology_reference Description: Ontologies referenced by a knowledge artefact.
-- # Class: KnowledgeGraph_aliases
--     * Slot: KnowledgeGraph_id Description: Autocreated FK slot
--     * Slot: aliases Description: Alternative names or synonyms for the term.
-- # Class: KnowledgeGraph_see_also_uri
--     * Slot: KnowledgeGraph_id Description: Autocreated FK slot
--     * Slot: see_also_uri Description: Pointers to related external resources or term records.
-- # Class: ExpertSystem_aliases
--     * Slot: ExpertSystem_id Description: Autocreated FK slot
--     * Slot: aliases Description: Alternative names or synonyms for the term.
-- # Class: ExpertSystem_see_also_uri
--     * Slot: ExpertSystem_id Description: Autocreated FK slot
--     * Slot: see_also_uri Description: Pointers to related external resources or term records.
-- # Class: CognitiveComputingSystem_cognitive_capabilities
--     * Slot: CognitiveComputingSystem_id Description: Autocreated FK slot
--     * Slot: cognitive_capabilities Description: Cognitive capabilities the system provides (e.g. perception, reasoning, learning).
-- # Class: CognitiveComputingSystem_aliases
--     * Slot: CognitiveComputingSystem_id Description: Autocreated FK slot
--     * Slot: aliases Description: Alternative names or synonyms for the term.
-- # Class: CognitiveComputingSystem_see_also_uri
--     * Slot: CognitiveComputingSystem_id Description: Autocreated FK slot
--     * Slot: see_also_uri Description: Pointers to related external resources or term records.
-- # Class: SemanticComputingSystem_aliases
--     * Slot: SemanticComputingSystem_id Description: Autocreated FK slot
--     * Slot: aliases Description: Alternative names or synonyms for the term.
-- # Class: SemanticComputingSystem_see_also_uri
--     * Slot: SemanticComputingSystem_id Description: Autocreated FK slot
--     * Slot: see_also_uri Description: Pointers to related external resources or term records.
-- # Class: SoftComputingSystem_soft_computing_techniques
--     * Slot: SoftComputingSystem_id Description: Autocreated FK slot
--     * Slot: soft_computing_techniques Description: Soft-computing techniques the system employs.
-- # Class: SoftComputingSystem_aliases
--     * Slot: SoftComputingSystem_id Description: Autocreated FK slot
--     * Slot: aliases Description: Alternative names or synonyms for the term.
-- # Class: SoftComputingSystem_see_also_uri
--     * Slot: SoftComputingSystem_id Description: Autocreated FK slot
--     * Slot: see_also_uri Description: Pointers to related external resources or term records.
-- # Class: DataProcess_parameters
--     * Slot: DataProcess_id Description: Autocreated FK slot
--     * Slot: parameters Description: Free-form parameters configuring the process.
-- # Class: DataProcess_aliases
--     * Slot: DataProcess_id Description: Autocreated FK slot
--     * Slot: aliases Description: Alternative names or synonyms for the term.
-- # Class: DataProcess_see_also_uri
--     * Slot: DataProcess_id Description: Autocreated FK slot
--     * Slot: see_also_uri Description: Pointers to related external resources or term records.
-- # Class: DataSample_aliases
--     * Slot: DataSample_id Description: Autocreated FK slot
--     * Slot: aliases Description: Alternative names or synonyms for the term.
-- # Class: DataSample_see_also_uri
--     * Slot: DataSample_id Description: Autocreated FK slot
--     * Slot: see_also_uri Description: Pointers to related external resources or term records.
-- # Class: DataLabel_aliases
--     * Slot: DataLabel_id Description: Autocreated FK slot
--     * Slot: aliases Description: Alternative names or synonyms for the term.
-- # Class: DataLabel_see_also_uri
--     * Slot: DataLabel_id Description: Autocreated FK slot
--     * Slot: see_also_uri Description: Pointers to related external resources or term records.
-- # Class: GroundTruthRecord_aliases
--     * Slot: GroundTruthRecord_id Description: Autocreated FK slot
--     * Slot: aliases Description: Alternative names or synonyms for the term.
-- # Class: GroundTruthRecord_see_also_uri
--     * Slot: GroundTruthRecord_id Description: Autocreated FK slot
--     * Slot: see_also_uri Description: Pointers to related external resources or term records.
-- # Class: Robot_aliases
--     * Slot: Robot_id Description: Autocreated FK slot
--     * Slot: aliases Description: Alternative names or synonyms for the term.
-- # Class: Robot_see_also_uri
--     * Slot: Robot_id Description: Autocreated FK slot
--     * Slot: see_also_uri Description: Pointers to related external resources or term records.
-- # Class: IoTDevice_sensing_capabilities
--     * Slot: IoTDevice_id Description: Autocreated FK slot
--     * Slot: sensing_capabilities Description: Sensing capabilities of the device.
-- # Class: IoTDevice_actuating_capabilities
--     * Slot: IoTDevice_id Description: Autocreated FK slot
--     * Slot: actuating_capabilities Description: Actuating capabilities of the device.
-- # Class: IoTDevice_aliases
--     * Slot: IoTDevice_id Description: Autocreated FK slot
--     * Slot: aliases Description: Alternative names or synonyms for the term.
-- # Class: IoTDevice_see_also_uri
--     * Slot: IoTDevice_id Description: Autocreated FK slot
--     * Slot: see_also_uri Description: Pointers to related external resources or term records.
-- # Class: IoTSystem_ai_components
--     * Slot: IoTSystem_id Description: Autocreated FK slot
--     * Slot: ai_components_id Description: AI components that operate within the IoT system.
-- # Class: IoTSystem_aliases
--     * Slot: IoTSystem_id Description: Autocreated FK slot
--     * Slot: aliases Description: Alternative names or synonyms for the term.
-- # Class: IoTSystem_see_also_uri
--     * Slot: IoTSystem_id Description: Autocreated FK slot
--     * Slot: see_also_uri Description: Pointers to related external resources or term records.
-- # Class: CyberPhysicalSystem_physical_processes
--     * Slot: CyberPhysicalSystem_id Description: Autocreated FK slot
--     * Slot: physical_processes Description: Physical processes the system monitors or controls.
-- # Class: CyberPhysicalSystem_cyber_components
--     * Slot: CyberPhysicalSystem_id Description: Autocreated FK slot
--     * Slot: cyber_components_id Description: Computational components participating in the system.
-- # Class: CyberPhysicalSystem_aliases
--     * Slot: CyberPhysicalSystem_id Description: Autocreated FK slot
--     * Slot: aliases Description: Alternative names or synonyms for the term.
-- # Class: CyberPhysicalSystem_see_also_uri
--     * Slot: CyberPhysicalSystem_id Description: Autocreated FK slot
--     * Slot: see_also_uri Description: Pointers to related external resources or term records.
-- # Class: AbbreviationEntry_aliases
--     * Slot: AbbreviationEntry_id Description: Autocreated FK slot
--     * Slot: aliases Description: Alternative names or synonyms for the term.
-- # Class: AbbreviationEntry_see_also_uri
--     * Slot: AbbreviationEntry_id Description: Autocreated FK slot
--     * Slot: see_also_uri Description: Pointers to related external resources or term records.
-- # Class: AIPlatformProvider_responsibilities
--     * Slot: AIPlatformProvider_id Description: Autocreated FK slot
--     * Slot: responsibilities Description: Free-text statements of responsibility.
-- # Class: AIPlatformProvider_aliases
--     * Slot: AIPlatformProvider_id Description: Autocreated FK slot
--     * Slot: aliases Description: Alternative names or synonyms for the term.
-- # Class: AIPlatformProvider_see_also_uri
--     * Slot: AIPlatformProvider_id Description: Autocreated FK slot
--     * Slot: see_also_uri Description: Pointers to related external resources or term records.
-- # Class: AIServiceProductProvider_responsibilities
--     * Slot: AIServiceProductProvider_id Description: Autocreated FK slot
--     * Slot: responsibilities Description: Free-text statements of responsibility.
-- # Class: AIServiceProductProvider_aliases
--     * Slot: AIServiceProductProvider_id Description: Autocreated FK slot
--     * Slot: aliases Description: Alternative names or synonyms for the term.
-- # Class: AIServiceProductProvider_see_also_uri
--     * Slot: AIServiceProductProvider_id Description: Autocreated FK slot
--     * Slot: see_also_uri Description: Pointers to related external resources or term records.
-- # Class: ModelDesigner_responsibilities
--     * Slot: ModelDesigner_id Description: Autocreated FK slot
--     * Slot: responsibilities Description: Free-text statements of responsibility.
-- # Class: ModelDesigner_aliases
--     * Slot: ModelDesigner_id Description: Autocreated FK slot
--     * Slot: aliases Description: Alternative names or synonyms for the term.
-- # Class: ModelDesigner_see_also_uri
--     * Slot: ModelDesigner_id Description: Autocreated FK slot
--     * Slot: see_also_uri Description: Pointers to related external resources or term records.
-- # Class: ModelImplementer_responsibilities
--     * Slot: ModelImplementer_id Description: Autocreated FK slot
--     * Slot: responsibilities Description: Free-text statements of responsibility.
-- # Class: ModelImplementer_aliases
--     * Slot: ModelImplementer_id Description: Autocreated FK slot
--     * Slot: aliases Description: Alternative names or synonyms for the term.
-- # Class: ModelImplementer_see_also_uri
--     * Slot: ModelImplementer_id Description: Autocreated FK slot
--     * Slot: see_also_uri Description: Pointers to related external resources or term records.
-- # Class: ComputationVerifier_responsibilities
--     * Slot: ComputationVerifier_id Description: Autocreated FK slot
--     * Slot: responsibilities Description: Free-text statements of responsibility.
-- # Class: ComputationVerifier_aliases
--     * Slot: ComputationVerifier_id Description: Autocreated FK slot
--     * Slot: aliases Description: Alternative names or synonyms for the term.
-- # Class: ComputationVerifier_see_also_uri
--     * Slot: ComputationVerifier_id Description: Autocreated FK slot
--     * Slot: see_also_uri Description: Pointers to related external resources or term records.
-- # Class: ModelVerifier_responsibilities
--     * Slot: ModelVerifier_id Description: Autocreated FK slot
--     * Slot: responsibilities Description: Free-text statements of responsibility.
-- # Class: ModelVerifier_aliases
--     * Slot: ModelVerifier_id Description: Autocreated FK slot
--     * Slot: aliases Description: Alternative names or synonyms for the term.
-- # Class: ModelVerifier_see_also_uri
--     * Slot: ModelVerifier_id Description: Autocreated FK slot
--     * Slot: see_also_uri Description: Pointers to related external resources or term records.
-- # Class: AIUser_responsibilities
--     * Slot: AIUser_id Description: Autocreated FK slot
--     * Slot: responsibilities Description: Free-text statements of responsibility.
-- # Class: AIUser_aliases
--     * Slot: AIUser_id Description: Autocreated FK slot
--     * Slot: aliases Description: Alternative names or synonyms for the term.
-- # Class: AIUser_see_also_uri
--     * Slot: AIUser_id Description: Autocreated FK slot
--     * Slot: see_also_uri Description: Pointers to related external resources or term records.
-- # Class: AISystemIntegrator_responsibilities
--     * Slot: AISystemIntegrator_id Description: Autocreated FK slot
--     * Slot: responsibilities Description: Free-text statements of responsibility.
-- # Class: AISystemIntegrator_aliases
--     * Slot: AISystemIntegrator_id Description: Autocreated FK slot
--     * Slot: aliases Description: Alternative names or synonyms for the term.
-- # Class: AISystemIntegrator_see_also_uri
--     * Slot: AISystemIntegrator_id Description: Autocreated FK slot
--     * Slot: see_also_uri Description: Pointers to related external resources or term records.
-- # Class: DataProvider_responsibilities
--     * Slot: DataProvider_id Description: Autocreated FK slot
--     * Slot: responsibilities Description: Free-text statements of responsibility.
-- # Class: DataProvider_aliases
--     * Slot: DataProvider_id Description: Autocreated FK slot
--     * Slot: aliases Description: Alternative names or synonyms for the term.
-- # Class: DataProvider_see_also_uri
--     * Slot: DataProvider_id Description: Autocreated FK slot
--     * Slot: see_also_uri Description: Pointers to related external resources or term records.
-- # Class: AIAuditor_responsibilities
--     * Slot: AIAuditor_id Description: Autocreated FK slot
--     * Slot: responsibilities Description: Free-text statements of responsibility.
-- # Class: AIAuditor_aliases
--     * Slot: AIAuditor_id Description: Autocreated FK slot
--     * Slot: aliases Description: Alternative names or synonyms for the term.
-- # Class: AIAuditor_see_also_uri
--     * Slot: AIAuditor_id Description: Autocreated FK slot
--     * Slot: see_also_uri Description: Pointers to related external resources or term records.
-- # Class: AIEvaluator_responsibilities
--     * Slot: AIEvaluator_id Description: Autocreated FK slot
--     * Slot: responsibilities Description: Free-text statements of responsibility.
-- # Class: AIEvaluator_aliases
--     * Slot: AIEvaluator_id Description: Autocreated FK slot
--     * Slot: aliases Description: Alternative names or synonyms for the term.
-- # Class: AIEvaluator_see_also_uri
--     * Slot: AIEvaluator_id Description: Autocreated FK slot
--     * Slot: see_also_uri Description: Pointers to related external resources or term records.
-- # Class: DataSubject_responsibilities
--     * Slot: DataSubject_id Description: Autocreated FK slot
--     * Slot: responsibilities Description: Free-text statements of responsibility.
-- # Class: DataSubject_aliases
--     * Slot: DataSubject_id Description: Autocreated FK slot
--     * Slot: aliases Description: Alternative names or synonyms for the term.
-- # Class: DataSubject_see_also_uri
--     * Slot: DataSubject_id Description: Autocreated FK slot
--     * Slot: see_also_uri Description: Pointers to related external resources or term records.
-- # Class: PolicyMaker_responsibilities
--     * Slot: PolicyMaker_id Description: Autocreated FK slot
--     * Slot: responsibilities Description: Free-text statements of responsibility.
-- # Class: PolicyMaker_aliases
--     * Slot: PolicyMaker_id Description: Autocreated FK slot
--     * Slot: aliases Description: Alternative names or synonyms for the term.
-- # Class: PolicyMaker_see_also_uri
--     * Slot: PolicyMaker_id Description: Autocreated FK slot
--     * Slot: see_also_uri Description: Pointers to related external resources or term records.
-- # Class: Regulator_responsibilities
--     * Slot: Regulator_id Description: Autocreated FK slot
--     * Slot: responsibilities Description: Free-text statements of responsibility.
-- # Class: Regulator_aliases
--     * Slot: Regulator_id Description: Autocreated FK slot
--     * Slot: aliases Description: Alternative names or synonyms for the term.
-- # Class: Regulator_see_also_uri
--     * Slot: Regulator_id Description: Autocreated FK slot
--     * Slot: see_also_uri Description: Pointers to related external resources or term records.
-- # Class: AutonomyAssessment_autonomy_criterion_scores
--     * Slot: AutonomyAssessment_id Description: Autocreated FK slot
--     * Slot: autonomy_criterion_scores Description: Free-form scores or judgements for autonomy criteria (Clause 5.13).
-- # Class: AutonomyAssessment_aliases
--     * Slot: AutonomyAssessment_id Description: Autocreated FK slot
--     * Slot: aliases Description: Alternative names or synonyms for the term.
-- # Class: AutonomyAssessment_see_also_uri
--     * Slot: AutonomyAssessment_id Description: Autocreated FK slot
--     * Slot: see_also_uri Description: Pointers to related external resources or term records.
-- # Class: VerificationValidationFramework_verification_methods
--     * Slot: VerificationValidationFramework_id Description: Autocreated FK slot
--     * Slot: verification_methods Description: Verification methods applied or applicable to the system.
-- # Class: VerificationValidationFramework_validation_methods
--     * Slot: VerificationValidationFramework_id Description: Autocreated FK slot
--     * Slot: validation_methods Description: Validation methods applied or applicable to the system.
-- # Class: VerificationValidationFramework_aliases
--     * Slot: VerificationValidationFramework_id Description: Autocreated FK slot
--     * Slot: aliases Description: Alternative names or synonyms for the term.
-- # Class: VerificationValidationFramework_see_also_uri
--     * Slot: VerificationValidationFramework_id Description: Autocreated FK slot
--     * Slot: see_also_uri Description: Pointers to related external resources or term records.
-- # Class: HumanMachineTeam_human_roles
--     * Slot: HumanMachineTeam_id Description: Autocreated FK slot
--     * Slot: human_roles Description: Roles played by humans in the team.
-- # Class: HumanMachineTeam_ai_systems_involved
--     * Slot: HumanMachineTeam_id Description: Autocreated FK slot
--     * Slot: ai_systems_involved_id Description: AI systems participating in the team.
-- # Class: HumanMachineTeam_aliases
--     * Slot: HumanMachineTeam_id Description: Autocreated FK slot
--     * Slot: aliases Description: Alternative names or synonyms for the term.
-- # Class: HumanMachineTeam_see_also_uri
--     * Slot: HumanMachineTeam_id Description: Autocreated FK slot
--     * Slot: see_also_uri Description: Pointers to related external resources or term records.
-- # Class: IntelligenceAugmentation_augmented_capability
--     * Slot: IntelligenceAugmentation_id Description: Autocreated FK slot
--     * Slot: augmented_capability Description: Cognitive capabilities being augmented.
-- # Class: IntelligenceAugmentation_aliases
--     * Slot: IntelligenceAugmentation_id Description: Autocreated FK slot
--     * Slot: aliases Description: Alternative names or synonyms for the term.
-- # Class: IntelligenceAugmentation_see_also_uri
--     * Slot: IntelligenceAugmentation_id Description: Autocreated FK slot
--     * Slot: see_also_uri Description: Pointers to related external resources or term records.
-- # Class: Recommendation_recommended_items
--     * Slot: Recommendation_id Description: Autocreated FK slot
--     * Slot: recommended_items Description: Items recommended by the system, serialised as strings.
-- # Class: Recommendation_based_on_predictions
--     * Slot: Recommendation_id Description: Autocreated FK slot
--     * Slot: based_on_predictions_id Description: Predictions supporting the recommendation.
-- # Class: Recommendation_aliases
--     * Slot: Recommendation_id Description: Autocreated FK slot
--     * Slot: aliases Description: Alternative names or synonyms for the term.
-- # Class: Recommendation_see_also_uri
--     * Slot: Recommendation_id Description: Autocreated FK slot
--     * Slot: see_also_uri Description: Pointers to related external resources or term records.
-- # Class: EvaluationMetric_aliases
--     * Slot: EvaluationMetric_id Description: Autocreated FK slot
--     * Slot: aliases Description: Alternative names or synonyms for the term.
-- # Class: EvaluationMetric_see_also_uri
--     * Slot: EvaluationMetric_id Description: Autocreated FK slot
--     * Slot: see_also_uri Description: Pointers to related external resources or term records.
-- # Class: Threshold_aliases
--     * Slot: Threshold_id Description: Autocreated FK slot
--     * Slot: aliases Description: Alternative names or synonyms for the term.
-- # Class: Threshold_see_also_uri
--     * Slot: Threshold_id Description: Autocreated FK slot
--     * Slot: see_also_uri Description: Pointers to related external resources or term records.
-- # Class: Neuron_aliases
--     * Slot: Neuron_id Description: Autocreated FK slot
--     * Slot: aliases Description: Alternative names or synonyms for the term.
-- # Class: Neuron_see_also_uri
--     * Slot: Neuron_id Description: Autocreated FK slot
--     * Slot: see_also_uri Description: Pointers to related external resources or term records.
-- # Class: ConvolutionOperation_kernel_size
--     * Slot: ConvolutionOperation_id Description: Autocreated FK slot
--     * Slot: kernel_size Description: Spatial dimensions of the convolution kernel.
-- # Class: ConvolutionOperation_aliases
--     * Slot: ConvolutionOperation_id Description: Autocreated FK slot
--     * Slot: aliases Description: Alternative names or synonyms for the term.
-- # Class: ConvolutionOperation_see_also_uri
--     * Slot: ConvolutionOperation_id Description: Autocreated FK slot
--     * Slot: see_also_uri Description: Pointers to related external resources or term records.
-- # Class: DataDrift_aliases
--     * Slot: DataDrift_id Description: Autocreated FK slot
--     * Slot: aliases Description: Alternative names or synonyms for the term.
-- # Class: DataDrift_see_also_uri
--     * Slot: DataDrift_id Description: Autocreated FK slot
--     * Slot: see_also_uri Description: Pointers to related external resources or term records.
-- # Class: CatastrophicForgetting_aliases
--     * Slot: CatastrophicForgetting_id Description: Autocreated FK slot
--     * Slot: aliases Description: Alternative names or synonyms for the term.
-- # Class: CatastrophicForgetting_see_also_uri
--     * Slot: CatastrophicForgetting_id Description: Autocreated FK slot
--     * Slot: see_also_uri Description: Pointers to related external resources or term records.
-- # Class: FaultToleranceMechanism_aliases
--     * Slot: FaultToleranceMechanism_id Description: Autocreated FK slot
--     * Slot: aliases Description: Alternative names or synonyms for the term.
-- # Class: FaultToleranceMechanism_see_also_uri
--     * Slot: FaultToleranceMechanism_id Description: Autocreated FK slot
--     * Slot: see_also_uri Description: Pointers to related external resources or term records.
-- # Class: NaturalLanguage_aliases
--     * Slot: NaturalLanguage_id Description: Autocreated FK slot
--     * Slot: aliases Description: Alternative names or synonyms for the term.
-- # Class: NaturalLanguage_see_also_uri
--     * Slot: NaturalLanguage_id Description: Autocreated FK slot
--     * Slot: see_also_uri Description: Pointers to related external resources or term records.
-- # Class: RiskItem_mitigation_strategy
--     * Slot: RiskItem_id Description: Autocreated FK slot
--     * Slot: mitigation_strategy Description: Strategies to reduce likelihood or severity.
-- # Class: RiskItem_affected_stakeholders
--     * Slot: RiskItem_id Description: Autocreated FK slot
--     * Slot: affected_stakeholders_id Description: Stakeholder roles affected by the risk.
-- # Class: RiskItem_aliases
--     * Slot: RiskItem_id Description: Autocreated FK slot
--     * Slot: aliases Description: Alternative names or synonyms for the term.
-- # Class: RiskItem_see_also_uri
--     * Slot: RiskItem_id Description: Autocreated FK slot
--     * Slot: see_also_uri Description: Pointers to related external resources or term records.
-- # Class: InputData_aliases
--     * Slot: InputData_id Description: Autocreated FK slot
--     * Slot: aliases Description: Alternative names or synonyms for the term.
-- # Class: InputData_see_also_uri
--     * Slot: InputData_id Description: Autocreated FK slot
--     * Slot: see_also_uri Description: Pointers to related external resources or term records.
-- # Class: Inference_aliases
--     * Slot: Inference_id Description: Autocreated FK slot
--     * Slot: aliases Description: Alternative names or synonyms for the term.
-- # Class: Inference_see_also_uri
--     * Slot: Inference_id Description: Autocreated FK slot
--     * Slot: see_also_uri Description: Pointers to related external resources or term records.
-- # Class: OECDLifecycleMapping_aliases
--     * Slot: OECDLifecycleMapping_id Description: Autocreated FK slot
--     * Slot: aliases Description: Alternative names or synonyms for the term.
-- # Class: OECDLifecycleMapping_see_also_uri
--     * Slot: OECDLifecycleMapping_id Description: Autocreated FK slot
--     * Slot: see_also_uri Description: Pointers to related external resources or term records.
-- # Class: Organization_aliases
--     * Slot: Organization_id Description: Autocreated FK slot
--     * Slot: aliases Description: Alternative names or synonyms for the term.
-- # Class: Organization_see_also_uri
--     * Slot: Organization_id Description: Autocreated FK slot
--     * Slot: see_also_uri Description: Pointers to related external resources or term records.
-- # Class: InterestedParty_aliases
--     * Slot: InterestedParty_id Description: Autocreated FK slot
--     * Slot: aliases Description: Alternative names or synonyms for the term.
-- # Class: InterestedParty_see_also_uri
--     * Slot: InterestedParty_id Description: Autocreated FK slot
--     * Slot: see_also_uri Description: Pointers to related external resources or term records.

CREATE TABLE "NamedEntity" (
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	clause_reference TEXT,
	preferred_label TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_NamedEntity_id" ON "NamedEntity" (id);

CREATE TABLE "Term" (
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	clause_reference TEXT,
	preferred_label TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_Term_id" ON "Term" (id);

CREATE TABLE "AITerm" (
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	clause_reference TEXT,
	preferred_label TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_AITerm_id" ON "AITerm" (id);

CREATE TABLE "DataTerm" (
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	clause_reference TEXT,
	preferred_label TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_DataTerm_id" ON "DataTerm" (id);

CREATE TABLE "MachineLearningTerm" (
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	clause_reference TEXT,
	preferred_label TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_MachineLearningTerm_id" ON "MachineLearningTerm" (id);

CREATE TABLE "NeuralNetworkTerm" (
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	clause_reference TEXT,
	preferred_label TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_NeuralNetworkTerm_id" ON "NeuralNetworkTerm" (id);

CREATE TABLE "TrustworthinessTerm" (
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	clause_reference TEXT,
	preferred_label TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_TrustworthinessTerm_id" ON "TrustworthinessTerm" (id);

CREATE TABLE "NLPTerm" (
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	clause_reference TEXT,
	preferred_label TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_NLPTerm_id" ON "NLPTerm" (id);

CREATE TABLE "ComputerVisionTerm" (
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	clause_reference TEXT,
	preferred_label TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_ComputerVisionTerm_id" ON "ComputerVisionTerm" (id);

CREATE TABLE "AbbreviatedTerm" (
	expansion TEXT NOT NULL,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	clause_reference TEXT,
	preferred_label TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_AbbreviatedTerm_id" ON "AbbreviatedTerm" (id);

CREATE TABLE "AIConcept" (
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	clause_reference TEXT,
	preferred_label TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_AIConcept_id" ON "AIConcept" (id);

CREATE TABLE "AIAgent" (
	autonomy_level VARCHAR(30),
	symbolic_approach VARCHAR(11),
	agent_architecture VARCHAR(19),
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	clause_reference TEXT,
	preferred_label TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_AIAgent_id" ON "AIAgent" (id);

CREATE TABLE "KnowledgeRepresentation" (
	symbolic_approach VARCHAR(11),
	knowledge_type VARCHAR(15),
	representation_form TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	clause_reference TEXT,
	preferred_label TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_KnowledgeRepresentation_id" ON "KnowledgeRepresentation" (id);

CREATE TABLE "AIProvider" (
	stakeholder_role_type VARCHAR(18) NOT NULL,
	organization_name TEXT,
	contact TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	clause_reference TEXT,
	preferred_label TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_AIProvider_id" ON "AIProvider" (id);

CREATE TABLE "AIProducer" (
	stakeholder_role_type VARCHAR(18) NOT NULL,
	organization_name TEXT,
	contact TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	clause_reference TEXT,
	preferred_label TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_AIProducer_id" ON "AIProducer" (id);

CREATE TABLE "AICustomer" (
	stakeholder_role_type VARCHAR(18) NOT NULL,
	organization_name TEXT,
	contact TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	clause_reference TEXT,
	preferred_label TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_AICustomer_id" ON "AICustomer" (id);

CREATE TABLE "AIPartner" (
	stakeholder_role_type VARCHAR(18) NOT NULL,
	organization_name TEXT,
	contact TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	clause_reference TEXT,
	preferred_label TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_AIPartner_id" ON "AIPartner" (id);

CREATE TABLE "AISubject" (
	stakeholder_role_type VARCHAR(18) NOT NULL,
	organization_name TEXT,
	contact TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	clause_reference TEXT,
	preferred_label TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_AISubject_id" ON "AISubject" (id);

CREATE TABLE "RelevantAuthority" (
	stakeholder_role_type VARCHAR(18) NOT NULL,
	organization_name TEXT,
	contact TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	clause_reference TEXT,
	preferred_label TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_RelevantAuthority_id" ON "RelevantAuthority" (id);

CREATE TABLE "AIEcosystem" (
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	clause_reference TEXT,
	preferred_label TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_AIEcosystem_id" ON "AIEcosystem" (id);

CREATE TABLE "ResourcePool" (
	resource_type VARCHAR(11) NOT NULL,
	capacity_units TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	clause_reference TEXT,
	preferred_label TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_ResourcePool_id" ON "ResourcePool" (id);

CREATE TABLE "NLPComponent" (
	nlp_component_type VARCHAR(30) NOT NULL,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	clause_reference TEXT,
	preferred_label TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_NLPComponent_id" ON "NLPComponent" (id);

CREATE TABLE "ComputerVisionFunction" (
	cv_task VARCHAR(29) NOT NULL,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	clause_reference TEXT,
	preferred_label TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_ComputerVisionFunction_id" ON "ComputerVisionFunction" (id);

CREATE TABLE "Decision" (
	decision_outcome TEXT,
	decision_policy TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	clause_reference TEXT,
	preferred_label TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_Decision_id" ON "Decision" (id);

CREATE TABLE "CognitiveComputingSystem" (
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	clause_reference TEXT,
	preferred_label TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_CognitiveComputingSystem_id" ON "CognitiveComputingSystem" (id);

CREATE TABLE "SemanticComputingSystem" (
	semantic_model TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	clause_reference TEXT,
	preferred_label TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_SemanticComputingSystem_id" ON "SemanticComputingSystem" (id);

CREATE TABLE "SoftComputingSystem" (
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	clause_reference TEXT,
	preferred_label TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_SoftComputingSystem_id" ON "SoftComputingSystem" (id);

CREATE TABLE "DataSample" (
	sample_payload TEXT,
	sample_label TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	clause_reference TEXT,
	preferred_label TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_DataSample_id" ON "DataSample" (id);

CREATE TABLE "GroundTruthRecord" (
	ground_truth_value TEXT NOT NULL,
	provenance_statement TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	clause_reference TEXT,
	preferred_label TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_GroundTruthRecord_id" ON "GroundTruthRecord" (id);

CREATE TABLE "AIConceptsCollection" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_AIConceptsCollection_id" ON "AIConceptsCollection" (id);

CREATE TABLE "AIPlatformProvider" (
	stakeholder_role_type VARCHAR(18) NOT NULL,
	organization_name TEXT,
	contact TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	clause_reference TEXT,
	preferred_label TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_AIPlatformProvider_id" ON "AIPlatformProvider" (id);

CREATE TABLE "AIServiceProductProvider" (
	stakeholder_role_type VARCHAR(18) NOT NULL,
	organization_name TEXT,
	contact TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	clause_reference TEXT,
	preferred_label TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_AIServiceProductProvider_id" ON "AIServiceProductProvider" (id);

CREATE TABLE "ModelDesigner" (
	stakeholder_role_type VARCHAR(18) NOT NULL,
	organization_name TEXT,
	contact TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	clause_reference TEXT,
	preferred_label TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_ModelDesigner_id" ON "ModelDesigner" (id);

CREATE TABLE "ModelImplementer" (
	stakeholder_role_type VARCHAR(18) NOT NULL,
	organization_name TEXT,
	contact TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	clause_reference TEXT,
	preferred_label TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_ModelImplementer_id" ON "ModelImplementer" (id);

CREATE TABLE "ComputationVerifier" (
	stakeholder_role_type VARCHAR(18) NOT NULL,
	organization_name TEXT,
	contact TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	clause_reference TEXT,
	preferred_label TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_ComputationVerifier_id" ON "ComputationVerifier" (id);

CREATE TABLE "ModelVerifier" (
	stakeholder_role_type VARCHAR(18) NOT NULL,
	organization_name TEXT,
	contact TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	clause_reference TEXT,
	preferred_label TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_ModelVerifier_id" ON "ModelVerifier" (id);

CREATE TABLE "AIUser" (
	stakeholder_role_type VARCHAR(18) NOT NULL,
	organization_name TEXT,
	contact TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	clause_reference TEXT,
	preferred_label TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_AIUser_id" ON "AIUser" (id);

CREATE TABLE "AISystemIntegrator" (
	stakeholder_role_type VARCHAR(18) NOT NULL,
	organization_name TEXT,
	contact TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	clause_reference TEXT,
	preferred_label TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_AISystemIntegrator_id" ON "AISystemIntegrator" (id);

CREATE TABLE "DataProvider" (
	stakeholder_role_type VARCHAR(18) NOT NULL,
	organization_name TEXT,
	contact TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	clause_reference TEXT,
	preferred_label TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_DataProvider_id" ON "DataProvider" (id);

CREATE TABLE "AIAuditor" (
	stakeholder_role_type VARCHAR(18) NOT NULL,
	organization_name TEXT,
	contact TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	clause_reference TEXT,
	preferred_label TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_AIAuditor_id" ON "AIAuditor" (id);

CREATE TABLE "AIEvaluator" (
	stakeholder_role_type VARCHAR(18) NOT NULL,
	organization_name TEXT,
	contact TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	clause_reference TEXT,
	preferred_label TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_AIEvaluator_id" ON "AIEvaluator" (id);

CREATE TABLE "DataSubject" (
	stakeholder_role_type VARCHAR(18) NOT NULL,
	organization_name TEXT,
	contact TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	clause_reference TEXT,
	preferred_label TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_DataSubject_id" ON "DataSubject" (id);

CREATE TABLE "PolicyMaker" (
	stakeholder_role_type VARCHAR(18) NOT NULL,
	organization_name TEXT,
	contact TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	clause_reference TEXT,
	preferred_label TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_PolicyMaker_id" ON "PolicyMaker" (id);

CREATE TABLE "Regulator" (
	stakeholder_role_type VARCHAR(18) NOT NULL,
	organization_name TEXT,
	contact TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	clause_reference TEXT,
	preferred_label TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_Regulator_id" ON "Regulator" (id);

CREATE TABLE "AutonomyAssessment" (
	autonomy_level VARCHAR(30),
	clause_reference TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	preferred_label TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_AutonomyAssessment_id" ON "AutonomyAssessment" (id);

CREATE TABLE "VerificationValidationFramework" (
	verification_validation_level VARCHAR(34),
	clause_reference TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	preferred_label TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_VerificationValidationFramework_id" ON "VerificationValidationFramework" (id);

CREATE TABLE "HumanMachineTeam" (
	task_allocation TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	clause_reference TEXT,
	preferred_label TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_HumanMachineTeam_id" ON "HumanMachineTeam" (id);

CREATE TABLE "IntelligenceAugmentation" (
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	clause_reference TEXT,
	preferred_label TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_IntelligenceAugmentation_id" ON "IntelligenceAugmentation" (id);

CREATE TABLE "Recommendation" (
	recommendation_outcome_type VARCHAR(22),
	confidence FLOAT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	clause_reference TEXT,
	preferred_label TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_Recommendation_id" ON "Recommendation" (id);

CREATE TABLE "Threshold" (
	threshold_value FLOAT NOT NULL,
	applies_to_metric TEXT,
	threshold_policy TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	clause_reference TEXT,
	preferred_label TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_Threshold_id" ON "Threshold" (id);

CREATE TABLE "Neuron" (
	activation_function VARCHAR(10),
	input_arity INTEGER,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	clause_reference TEXT,
	preferred_label TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_Neuron_id" ON "Neuron" (id);

CREATE TABLE "ConvolutionOperation" (
	stride INTEGER,
	padding TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	clause_reference TEXT,
	preferred_label TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_ConvolutionOperation_id" ON "ConvolutionOperation" (id);

CREATE TABLE "FaultToleranceMechanism" (
	mechanism_type TEXT,
	coverage_scope TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	clause_reference TEXT,
	preferred_label TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_FaultToleranceMechanism_id" ON "FaultToleranceMechanism" (id);

CREATE TABLE "NaturalLanguage" (
	language_code TEXT,
	script TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	clause_reference TEXT,
	preferred_label TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_NaturalLanguage_id" ON "NaturalLanguage" (id);

CREATE TABLE "RiskItem" (
	risk_source TEXT,
	potential_event TEXT,
	consequence TEXT,
	likelihood FLOAT,
	severity TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	clause_reference TEXT,
	preferred_label TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_RiskItem_id" ON "RiskItem" (id);

CREATE TABLE "OECDLifecycleMapping" (
	iso_stage VARCHAR(27) NOT NULL,
	oecd_stage VARCHAR(24) NOT NULL,
	mapping_notes TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	clause_reference TEXT,
	preferred_label TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_OECDLifecycleMapping_id" ON "OECDLifecycleMapping" (id);

CREATE TABLE "Organization" (
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	clause_reference TEXT,
	preferred_label TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_Organization_id" ON "Organization" (id);

CREATE TABLE "InterestedParty" (
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	clause_reference TEXT,
	preferred_label TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_InterestedParty_id" ON "InterestedParty" (id);

CREATE TABLE "AILifecycleProcess" (
	process_stage VARCHAR(27) NOT NULL,
	responsible_role VARCHAR(18),
	start_date DATE,
	end_date DATE,
	process_sub_type TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	clause_reference TEXT,
	preferred_label TEXT,
	"AIConceptsCollection_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("AIConceptsCollection_id") REFERENCES "AIConceptsCollection" (id)
);
CREATE INDEX "ix_AILifecycleProcess_id" ON "AILifecycleProcess" (id);

CREATE TABLE "Task" (
	task_category VARCHAR(24) NOT NULL,
	output_label_type VARCHAR(11),
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	clause_reference TEXT,
	preferred_label TEXT,
	"AIConceptsCollection_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("AIConceptsCollection_id") REFERENCES "AIConceptsCollection" (id)
);
CREATE INDEX "ix_Task_id" ON "Task" (id);

CREATE TABLE "Action" (
	action_target TEXT,
	execution_status VARCHAR(11),
	triggered_by TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	clause_reference TEXT,
	preferred_label TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(triggered_by) REFERENCES "Decision" (id)
);
CREATE INDEX "ix_Action_id" ON "Action" (id);

CREATE TABLE "KnowledgeGraph" (
	node_count INTEGER,
	edge_count INTEGER,
	symbolic_approach VARCHAR(11),
	knowledge_type VARCHAR(15),
	representation_form TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	clause_reference TEXT,
	preferred_label TEXT,
	"AIConceptsCollection_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("AIConceptsCollection_id") REFERENCES "AIConceptsCollection" (id)
);
CREATE INDEX "ix_KnowledgeGraph_id" ON "KnowledgeGraph" (id);

CREATE TABLE "IoTSystem" (
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	clause_reference TEXT,
	preferred_label TEXT,
	"AIConceptsCollection_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("AIConceptsCollection_id") REFERENCES "AIConceptsCollection" (id)
);
CREATE INDEX "ix_IoTSystem_id" ON "IoTSystem" (id);

CREATE TABLE "AbbreviationEntry" (
	abbreviation_code VARCHAR(8) NOT NULL,
	expansion TEXT NOT NULL,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	clause_reference TEXT,
	preferred_label TEXT,
	"AIConceptsCollection_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("AIConceptsCollection_id") REFERENCES "AIConceptsCollection" (id)
);
CREATE INDEX "ix_AbbreviationEntry_id" ON "AbbreviationEntry" (id);

CREATE TABLE "NamedEntity_aliases" (
	"NamedEntity_id" TEXT,
	aliases TEXT,
	PRIMARY KEY ("NamedEntity_id", aliases),
	FOREIGN KEY("NamedEntity_id") REFERENCES "NamedEntity" (id)
);
CREATE INDEX "ix_NamedEntity_aliases_aliases" ON "NamedEntity_aliases" (aliases);
CREATE INDEX "ix_NamedEntity_aliases_NamedEntity_id" ON "NamedEntity_aliases" ("NamedEntity_id");

CREATE TABLE "NamedEntity_see_also_uri" (
	"NamedEntity_id" TEXT,
	see_also_uri TEXT,
	PRIMARY KEY ("NamedEntity_id", see_also_uri),
	FOREIGN KEY("NamedEntity_id") REFERENCES "NamedEntity" (id)
);
CREATE INDEX "ix_NamedEntity_see_also_uri_see_also_uri" ON "NamedEntity_see_also_uri" (see_also_uri);
CREATE INDEX "ix_NamedEntity_see_also_uri_NamedEntity_id" ON "NamedEntity_see_also_uri" ("NamedEntity_id");

CREATE TABLE "Term_aliases" (
	"Term_id" TEXT,
	aliases TEXT,
	PRIMARY KEY ("Term_id", aliases),
	FOREIGN KEY("Term_id") REFERENCES "Term" (id)
);
CREATE INDEX "ix_Term_aliases_aliases" ON "Term_aliases" (aliases);
CREATE INDEX "ix_Term_aliases_Term_id" ON "Term_aliases" ("Term_id");

CREATE TABLE "Term_see_also_uri" (
	"Term_id" TEXT,
	see_also_uri TEXT,
	PRIMARY KEY ("Term_id", see_also_uri),
	FOREIGN KEY("Term_id") REFERENCES "Term" (id)
);
CREATE INDEX "ix_Term_see_also_uri_see_also_uri" ON "Term_see_also_uri" (see_also_uri);
CREATE INDEX "ix_Term_see_also_uri_Term_id" ON "Term_see_also_uri" ("Term_id");

CREATE TABLE "AITerm_aliases" (
	"AITerm_id" TEXT,
	aliases TEXT,
	PRIMARY KEY ("AITerm_id", aliases),
	FOREIGN KEY("AITerm_id") REFERENCES "AITerm" (id)
);
CREATE INDEX "ix_AITerm_aliases_aliases" ON "AITerm_aliases" (aliases);
CREATE INDEX "ix_AITerm_aliases_AITerm_id" ON "AITerm_aliases" ("AITerm_id");

CREATE TABLE "AITerm_see_also_uri" (
	"AITerm_id" TEXT,
	see_also_uri TEXT,
	PRIMARY KEY ("AITerm_id", see_also_uri),
	FOREIGN KEY("AITerm_id") REFERENCES "AITerm" (id)
);
CREATE INDEX "ix_AITerm_see_also_uri_AITerm_id" ON "AITerm_see_also_uri" ("AITerm_id");
CREATE INDEX "ix_AITerm_see_also_uri_see_also_uri" ON "AITerm_see_also_uri" (see_also_uri);

CREATE TABLE "DataTerm_aliases" (
	"DataTerm_id" TEXT,
	aliases TEXT,
	PRIMARY KEY ("DataTerm_id", aliases),
	FOREIGN KEY("DataTerm_id") REFERENCES "DataTerm" (id)
);
CREATE INDEX "ix_DataTerm_aliases_DataTerm_id" ON "DataTerm_aliases" ("DataTerm_id");
CREATE INDEX "ix_DataTerm_aliases_aliases" ON "DataTerm_aliases" (aliases);

CREATE TABLE "DataTerm_see_also_uri" (
	"DataTerm_id" TEXT,
	see_also_uri TEXT,
	PRIMARY KEY ("DataTerm_id", see_also_uri),
	FOREIGN KEY("DataTerm_id") REFERENCES "DataTerm" (id)
);
CREATE INDEX "ix_DataTerm_see_also_uri_DataTerm_id" ON "DataTerm_see_also_uri" ("DataTerm_id");
CREATE INDEX "ix_DataTerm_see_also_uri_see_also_uri" ON "DataTerm_see_also_uri" (see_also_uri);

CREATE TABLE "MachineLearningTerm_aliases" (
	"MachineLearningTerm_id" TEXT,
	aliases TEXT,
	PRIMARY KEY ("MachineLearningTerm_id", aliases),
	FOREIGN KEY("MachineLearningTerm_id") REFERENCES "MachineLearningTerm" (id)
);
CREATE INDEX "ix_MachineLearningTerm_aliases_aliases" ON "MachineLearningTerm_aliases" (aliases);
CREATE INDEX "ix_MachineLearningTerm_aliases_MachineLearningTerm_id" ON "MachineLearningTerm_aliases" ("MachineLearningTerm_id");

CREATE TABLE "MachineLearningTerm_see_also_uri" (
	"MachineLearningTerm_id" TEXT,
	see_also_uri TEXT,
	PRIMARY KEY ("MachineLearningTerm_id", see_also_uri),
	FOREIGN KEY("MachineLearningTerm_id") REFERENCES "MachineLearningTerm" (id)
);
CREATE INDEX "ix_MachineLearningTerm_see_also_uri_MachineLearningTerm_id" ON "MachineLearningTerm_see_also_uri" ("MachineLearningTerm_id");
CREATE INDEX "ix_MachineLearningTerm_see_also_uri_see_also_uri" ON "MachineLearningTerm_see_also_uri" (see_also_uri);

CREATE TABLE "NeuralNetworkTerm_aliases" (
	"NeuralNetworkTerm_id" TEXT,
	aliases TEXT,
	PRIMARY KEY ("NeuralNetworkTerm_id", aliases),
	FOREIGN KEY("NeuralNetworkTerm_id") REFERENCES "NeuralNetworkTerm" (id)
);
CREATE INDEX "ix_NeuralNetworkTerm_aliases_aliases" ON "NeuralNetworkTerm_aliases" (aliases);
CREATE INDEX "ix_NeuralNetworkTerm_aliases_NeuralNetworkTerm_id" ON "NeuralNetworkTerm_aliases" ("NeuralNetworkTerm_id");

CREATE TABLE "NeuralNetworkTerm_see_also_uri" (
	"NeuralNetworkTerm_id" TEXT,
	see_also_uri TEXT,
	PRIMARY KEY ("NeuralNetworkTerm_id", see_also_uri),
	FOREIGN KEY("NeuralNetworkTerm_id") REFERENCES "NeuralNetworkTerm" (id)
);
CREATE INDEX "ix_NeuralNetworkTerm_see_also_uri_see_also_uri" ON "NeuralNetworkTerm_see_also_uri" (see_also_uri);
CREATE INDEX "ix_NeuralNetworkTerm_see_also_uri_NeuralNetworkTerm_id" ON "NeuralNetworkTerm_see_also_uri" ("NeuralNetworkTerm_id");

CREATE TABLE "TrustworthinessTerm_aliases" (
	"TrustworthinessTerm_id" TEXT,
	aliases TEXT,
	PRIMARY KEY ("TrustworthinessTerm_id", aliases),
	FOREIGN KEY("TrustworthinessTerm_id") REFERENCES "TrustworthinessTerm" (id)
);
CREATE INDEX "ix_TrustworthinessTerm_aliases_aliases" ON "TrustworthinessTerm_aliases" (aliases);
CREATE INDEX "ix_TrustworthinessTerm_aliases_TrustworthinessTerm_id" ON "TrustworthinessTerm_aliases" ("TrustworthinessTerm_id");

CREATE TABLE "TrustworthinessTerm_see_also_uri" (
	"TrustworthinessTerm_id" TEXT,
	see_also_uri TEXT,
	PRIMARY KEY ("TrustworthinessTerm_id", see_also_uri),
	FOREIGN KEY("TrustworthinessTerm_id") REFERENCES "TrustworthinessTerm" (id)
);
CREATE INDEX "ix_TrustworthinessTerm_see_also_uri_TrustworthinessTerm_id" ON "TrustworthinessTerm_see_also_uri" ("TrustworthinessTerm_id");
CREATE INDEX "ix_TrustworthinessTerm_see_also_uri_see_also_uri" ON "TrustworthinessTerm_see_also_uri" (see_also_uri);

CREATE TABLE "NLPTerm_aliases" (
	"NLPTerm_id" TEXT,
	aliases TEXT,
	PRIMARY KEY ("NLPTerm_id", aliases),
	FOREIGN KEY("NLPTerm_id") REFERENCES "NLPTerm" (id)
);
CREATE INDEX "ix_NLPTerm_aliases_NLPTerm_id" ON "NLPTerm_aliases" ("NLPTerm_id");
CREATE INDEX "ix_NLPTerm_aliases_aliases" ON "NLPTerm_aliases" (aliases);

CREATE TABLE "NLPTerm_see_also_uri" (
	"NLPTerm_id" TEXT,
	see_also_uri TEXT,
	PRIMARY KEY ("NLPTerm_id", see_also_uri),
	FOREIGN KEY("NLPTerm_id") REFERENCES "NLPTerm" (id)
);
CREATE INDEX "ix_NLPTerm_see_also_uri_see_also_uri" ON "NLPTerm_see_also_uri" (see_also_uri);
CREATE INDEX "ix_NLPTerm_see_also_uri_NLPTerm_id" ON "NLPTerm_see_also_uri" ("NLPTerm_id");

CREATE TABLE "ComputerVisionTerm_aliases" (
	"ComputerVisionTerm_id" TEXT,
	aliases TEXT,
	PRIMARY KEY ("ComputerVisionTerm_id", aliases),
	FOREIGN KEY("ComputerVisionTerm_id") REFERENCES "ComputerVisionTerm" (id)
);
CREATE INDEX "ix_ComputerVisionTerm_aliases_aliases" ON "ComputerVisionTerm_aliases" (aliases);
CREATE INDEX "ix_ComputerVisionTerm_aliases_ComputerVisionTerm_id" ON "ComputerVisionTerm_aliases" ("ComputerVisionTerm_id");

CREATE TABLE "ComputerVisionTerm_see_also_uri" (
	"ComputerVisionTerm_id" TEXT,
	see_also_uri TEXT,
	PRIMARY KEY ("ComputerVisionTerm_id", see_also_uri),
	FOREIGN KEY("ComputerVisionTerm_id") REFERENCES "ComputerVisionTerm" (id)
);
CREATE INDEX "ix_ComputerVisionTerm_see_also_uri_see_also_uri" ON "ComputerVisionTerm_see_also_uri" (see_also_uri);
CREATE INDEX "ix_ComputerVisionTerm_see_also_uri_ComputerVisionTerm_id" ON "ComputerVisionTerm_see_also_uri" ("ComputerVisionTerm_id");

CREATE TABLE "AbbreviatedTerm_aliases" (
	"AbbreviatedTerm_id" TEXT,
	aliases TEXT,
	PRIMARY KEY ("AbbreviatedTerm_id", aliases),
	FOREIGN KEY("AbbreviatedTerm_id") REFERENCES "AbbreviatedTerm" (id)
);
CREATE INDEX "ix_AbbreviatedTerm_aliases_aliases" ON "AbbreviatedTerm_aliases" (aliases);
CREATE INDEX "ix_AbbreviatedTerm_aliases_AbbreviatedTerm_id" ON "AbbreviatedTerm_aliases" ("AbbreviatedTerm_id");

CREATE TABLE "AbbreviatedTerm_see_also_uri" (
	"AbbreviatedTerm_id" TEXT,
	see_also_uri TEXT,
	PRIMARY KEY ("AbbreviatedTerm_id", see_also_uri),
	FOREIGN KEY("AbbreviatedTerm_id") REFERENCES "AbbreviatedTerm" (id)
);
CREATE INDEX "ix_AbbreviatedTerm_see_also_uri_AbbreviatedTerm_id" ON "AbbreviatedTerm_see_also_uri" ("AbbreviatedTerm_id");
CREATE INDEX "ix_AbbreviatedTerm_see_also_uri_see_also_uri" ON "AbbreviatedTerm_see_also_uri" (see_also_uri);

CREATE TABLE "AIConcept_aliases" (
	"AIConcept_id" TEXT,
	aliases TEXT,
	PRIMARY KEY ("AIConcept_id", aliases),
	FOREIGN KEY("AIConcept_id") REFERENCES "AIConcept" (id)
);
CREATE INDEX "ix_AIConcept_aliases_AIConcept_id" ON "AIConcept_aliases" ("AIConcept_id");
CREATE INDEX "ix_AIConcept_aliases_aliases" ON "AIConcept_aliases" (aliases);

CREATE TABLE "AIConcept_see_also_uri" (
	"AIConcept_id" TEXT,
	see_also_uri TEXT,
	PRIMARY KEY ("AIConcept_id", see_also_uri),
	FOREIGN KEY("AIConcept_id") REFERENCES "AIConcept" (id)
);
CREATE INDEX "ix_AIConcept_see_also_uri_see_also_uri" ON "AIConcept_see_also_uri" (see_also_uri);
CREATE INDEX "ix_AIConcept_see_also_uri_AIConcept_id" ON "AIConcept_see_also_uri" ("AIConcept_id");

CREATE TABLE "AIAgent_goal_set" (
	"AIAgent_id" TEXT,
	goal_set TEXT,
	PRIMARY KEY ("AIAgent_id", goal_set),
	FOREIGN KEY("AIAgent_id") REFERENCES "AIAgent" (id)
);
CREATE INDEX "ix_AIAgent_goal_set_goal_set" ON "AIAgent_goal_set" (goal_set);
CREATE INDEX "ix_AIAgent_goal_set_AIAgent_id" ON "AIAgent_goal_set" ("AIAgent_id");

CREATE TABLE "AIAgent_aliases" (
	"AIAgent_id" TEXT,
	aliases TEXT,
	PRIMARY KEY ("AIAgent_id", aliases),
	FOREIGN KEY("AIAgent_id") REFERENCES "AIAgent" (id)
);
CREATE INDEX "ix_AIAgent_aliases_AIAgent_id" ON "AIAgent_aliases" ("AIAgent_id");
CREATE INDEX "ix_AIAgent_aliases_aliases" ON "AIAgent_aliases" (aliases);

CREATE TABLE "AIAgent_see_also_uri" (
	"AIAgent_id" TEXT,
	see_also_uri TEXT,
	PRIMARY KEY ("AIAgent_id", see_also_uri),
	FOREIGN KEY("AIAgent_id") REFERENCES "AIAgent" (id)
);
CREATE INDEX "ix_AIAgent_see_also_uri_see_also_uri" ON "AIAgent_see_also_uri" (see_also_uri);
CREATE INDEX "ix_AIAgent_see_also_uri_AIAgent_id" ON "AIAgent_see_also_uri" ("AIAgent_id");

CREATE TABLE "KnowledgeRepresentation_aliases" (
	"KnowledgeRepresentation_id" TEXT,
	aliases TEXT,
	PRIMARY KEY ("KnowledgeRepresentation_id", aliases),
	FOREIGN KEY("KnowledgeRepresentation_id") REFERENCES "KnowledgeRepresentation" (id)
);
CREATE INDEX "ix_KnowledgeRepresentation_aliases_aliases" ON "KnowledgeRepresentation_aliases" (aliases);
CREATE INDEX "ix_KnowledgeRepresentation_aliases_KnowledgeRepresentation_id" ON "KnowledgeRepresentation_aliases" ("KnowledgeRepresentation_id");

CREATE TABLE "KnowledgeRepresentation_see_also_uri" (
	"KnowledgeRepresentation_id" TEXT,
	see_also_uri TEXT,
	PRIMARY KEY ("KnowledgeRepresentation_id", see_also_uri),
	FOREIGN KEY("KnowledgeRepresentation_id") REFERENCES "KnowledgeRepresentation" (id)
);
CREATE INDEX "ix_KnowledgeRepresentation_see_also_uri_KnowledgeRepresentation_id" ON "KnowledgeRepresentation_see_also_uri" ("KnowledgeRepresentation_id");
CREATE INDEX "ix_KnowledgeRepresentation_see_also_uri_see_also_uri" ON "KnowledgeRepresentation_see_also_uri" (see_also_uri);

CREATE TABLE "AIProvider_responsibilities" (
	"AIProvider_id" TEXT,
	responsibilities TEXT,
	PRIMARY KEY ("AIProvider_id", responsibilities),
	FOREIGN KEY("AIProvider_id") REFERENCES "AIProvider" (id)
);
CREATE INDEX "ix_AIProvider_responsibilities_responsibilities" ON "AIProvider_responsibilities" (responsibilities);
CREATE INDEX "ix_AIProvider_responsibilities_AIProvider_id" ON "AIProvider_responsibilities" ("AIProvider_id");

CREATE TABLE "AIProvider_aliases" (
	"AIProvider_id" TEXT,
	aliases TEXT,
	PRIMARY KEY ("AIProvider_id", aliases),
	FOREIGN KEY("AIProvider_id") REFERENCES "AIProvider" (id)
);
CREATE INDEX "ix_AIProvider_aliases_AIProvider_id" ON "AIProvider_aliases" ("AIProvider_id");
CREATE INDEX "ix_AIProvider_aliases_aliases" ON "AIProvider_aliases" (aliases);

CREATE TABLE "AIProvider_see_also_uri" (
	"AIProvider_id" TEXT,
	see_also_uri TEXT,
	PRIMARY KEY ("AIProvider_id", see_also_uri),
	FOREIGN KEY("AIProvider_id") REFERENCES "AIProvider" (id)
);
CREATE INDEX "ix_AIProvider_see_also_uri_see_also_uri" ON "AIProvider_see_also_uri" (see_also_uri);
CREATE INDEX "ix_AIProvider_see_also_uri_AIProvider_id" ON "AIProvider_see_also_uri" ("AIProvider_id");

CREATE TABLE "AIProducer_responsibilities" (
	"AIProducer_id" TEXT,
	responsibilities TEXT,
	PRIMARY KEY ("AIProducer_id", responsibilities),
	FOREIGN KEY("AIProducer_id") REFERENCES "AIProducer" (id)
);
CREATE INDEX "ix_AIProducer_responsibilities_AIProducer_id" ON "AIProducer_responsibilities" ("AIProducer_id");
CREATE INDEX "ix_AIProducer_responsibilities_responsibilities" ON "AIProducer_responsibilities" (responsibilities);

CREATE TABLE "AIProducer_aliases" (
	"AIProducer_id" TEXT,
	aliases TEXT,
	PRIMARY KEY ("AIProducer_id", aliases),
	FOREIGN KEY("AIProducer_id") REFERENCES "AIProducer" (id)
);
CREATE INDEX "ix_AIProducer_aliases_AIProducer_id" ON "AIProducer_aliases" ("AIProducer_id");
CREATE INDEX "ix_AIProducer_aliases_aliases" ON "AIProducer_aliases" (aliases);

CREATE TABLE "AIProducer_see_also_uri" (
	"AIProducer_id" TEXT,
	see_also_uri TEXT,
	PRIMARY KEY ("AIProducer_id", see_also_uri),
	FOREIGN KEY("AIProducer_id") REFERENCES "AIProducer" (id)
);
CREATE INDEX "ix_AIProducer_see_also_uri_AIProducer_id" ON "AIProducer_see_also_uri" ("AIProducer_id");
CREATE INDEX "ix_AIProducer_see_also_uri_see_also_uri" ON "AIProducer_see_also_uri" (see_also_uri);

CREATE TABLE "AICustomer_responsibilities" (
	"AICustomer_id" TEXT,
	responsibilities TEXT,
	PRIMARY KEY ("AICustomer_id", responsibilities),
	FOREIGN KEY("AICustomer_id") REFERENCES "AICustomer" (id)
);
CREATE INDEX "ix_AICustomer_responsibilities_AICustomer_id" ON "AICustomer_responsibilities" ("AICustomer_id");
CREATE INDEX "ix_AICustomer_responsibilities_responsibilities" ON "AICustomer_responsibilities" (responsibilities);

CREATE TABLE "AICustomer_aliases" (
	"AICustomer_id" TEXT,
	aliases TEXT,
	PRIMARY KEY ("AICustomer_id", aliases),
	FOREIGN KEY("AICustomer_id") REFERENCES "AICustomer" (id)
);
CREATE INDEX "ix_AICustomer_aliases_AICustomer_id" ON "AICustomer_aliases" ("AICustomer_id");
CREATE INDEX "ix_AICustomer_aliases_aliases" ON "AICustomer_aliases" (aliases);

CREATE TABLE "AICustomer_see_also_uri" (
	"AICustomer_id" TEXT,
	see_also_uri TEXT,
	PRIMARY KEY ("AICustomer_id", see_also_uri),
	FOREIGN KEY("AICustomer_id") REFERENCES "AICustomer" (id)
);
CREATE INDEX "ix_AICustomer_see_also_uri_AICustomer_id" ON "AICustomer_see_also_uri" ("AICustomer_id");
CREATE INDEX "ix_AICustomer_see_also_uri_see_also_uri" ON "AICustomer_see_also_uri" (see_also_uri);

CREATE TABLE "AIPartner_responsibilities" (
	"AIPartner_id" TEXT,
	responsibilities TEXT,
	PRIMARY KEY ("AIPartner_id", responsibilities),
	FOREIGN KEY("AIPartner_id") REFERENCES "AIPartner" (id)
);
CREATE INDEX "ix_AIPartner_responsibilities_AIPartner_id" ON "AIPartner_responsibilities" ("AIPartner_id");
CREATE INDEX "ix_AIPartner_responsibilities_responsibilities" ON "AIPartner_responsibilities" (responsibilities);

CREATE TABLE "AIPartner_aliases" (
	"AIPartner_id" TEXT,
	aliases TEXT,
	PRIMARY KEY ("AIPartner_id", aliases),
	FOREIGN KEY("AIPartner_id") REFERENCES "AIPartner" (id)
);
CREATE INDEX "ix_AIPartner_aliases_AIPartner_id" ON "AIPartner_aliases" ("AIPartner_id");
CREATE INDEX "ix_AIPartner_aliases_aliases" ON "AIPartner_aliases" (aliases);

CREATE TABLE "AIPartner_see_also_uri" (
	"AIPartner_id" TEXT,
	see_also_uri TEXT,
	PRIMARY KEY ("AIPartner_id", see_also_uri),
	FOREIGN KEY("AIPartner_id") REFERENCES "AIPartner" (id)
);
CREATE INDEX "ix_AIPartner_see_also_uri_AIPartner_id" ON "AIPartner_see_also_uri" ("AIPartner_id");
CREATE INDEX "ix_AIPartner_see_also_uri_see_also_uri" ON "AIPartner_see_also_uri" (see_also_uri);

CREATE TABLE "AISubject_responsibilities" (
	"AISubject_id" TEXT,
	responsibilities TEXT,
	PRIMARY KEY ("AISubject_id", responsibilities),
	FOREIGN KEY("AISubject_id") REFERENCES "AISubject" (id)
);
CREATE INDEX "ix_AISubject_responsibilities_AISubject_id" ON "AISubject_responsibilities" ("AISubject_id");
CREATE INDEX "ix_AISubject_responsibilities_responsibilities" ON "AISubject_responsibilities" (responsibilities);

CREATE TABLE "AISubject_aliases" (
	"AISubject_id" TEXT,
	aliases TEXT,
	PRIMARY KEY ("AISubject_id", aliases),
	FOREIGN KEY("AISubject_id") REFERENCES "AISubject" (id)
);
CREATE INDEX "ix_AISubject_aliases_AISubject_id" ON "AISubject_aliases" ("AISubject_id");
CREATE INDEX "ix_AISubject_aliases_aliases" ON "AISubject_aliases" (aliases);

CREATE TABLE "AISubject_see_also_uri" (
	"AISubject_id" TEXT,
	see_also_uri TEXT,
	PRIMARY KEY ("AISubject_id", see_also_uri),
	FOREIGN KEY("AISubject_id") REFERENCES "AISubject" (id)
);
CREATE INDEX "ix_AISubject_see_also_uri_AISubject_id" ON "AISubject_see_also_uri" ("AISubject_id");
CREATE INDEX "ix_AISubject_see_also_uri_see_also_uri" ON "AISubject_see_also_uri" (see_also_uri);

CREATE TABLE "RelevantAuthority_responsibilities" (
	"RelevantAuthority_id" TEXT,
	responsibilities TEXT,
	PRIMARY KEY ("RelevantAuthority_id", responsibilities),
	FOREIGN KEY("RelevantAuthority_id") REFERENCES "RelevantAuthority" (id)
);
CREATE INDEX "ix_RelevantAuthority_responsibilities_RelevantAuthority_id" ON "RelevantAuthority_responsibilities" ("RelevantAuthority_id");
CREATE INDEX "ix_RelevantAuthority_responsibilities_responsibilities" ON "RelevantAuthority_responsibilities" (responsibilities);

CREATE TABLE "RelevantAuthority_aliases" (
	"RelevantAuthority_id" TEXT,
	aliases TEXT,
	PRIMARY KEY ("RelevantAuthority_id", aliases),
	FOREIGN KEY("RelevantAuthority_id") REFERENCES "RelevantAuthority" (id)
);
CREATE INDEX "ix_RelevantAuthority_aliases_RelevantAuthority_id" ON "RelevantAuthority_aliases" ("RelevantAuthority_id");
CREATE INDEX "ix_RelevantAuthority_aliases_aliases" ON "RelevantAuthority_aliases" (aliases);

CREATE TABLE "RelevantAuthority_see_also_uri" (
	"RelevantAuthority_id" TEXT,
	see_also_uri TEXT,
	PRIMARY KEY ("RelevantAuthority_id", see_also_uri),
	FOREIGN KEY("RelevantAuthority_id") REFERENCES "RelevantAuthority" (id)
);
CREATE INDEX "ix_RelevantAuthority_see_also_uri_RelevantAuthority_id" ON "RelevantAuthority_see_also_uri" ("RelevantAuthority_id");
CREATE INDEX "ix_RelevantAuthority_see_also_uri_see_also_uri" ON "RelevantAuthority_see_also_uri" (see_also_uri);

CREATE TABLE "AIEcosystem_computing_resources" (
	"AIEcosystem_id" TEXT,
	computing_resources VARCHAR(11),
	PRIMARY KEY ("AIEcosystem_id", computing_resources),
	FOREIGN KEY("AIEcosystem_id") REFERENCES "AIEcosystem" (id)
);
CREATE INDEX "ix_AIEcosystem_computing_resources_computing_resources" ON "AIEcosystem_computing_resources" (computing_resources);
CREATE INDEX "ix_AIEcosystem_computing_resources_AIEcosystem_id" ON "AIEcosystem_computing_resources" ("AIEcosystem_id");

CREATE TABLE "AIEcosystem_data_sources" (
	"AIEcosystem_id" TEXT,
	data_sources TEXT,
	PRIMARY KEY ("AIEcosystem_id", data_sources),
	FOREIGN KEY("AIEcosystem_id") REFERENCES "AIEcosystem" (id)
);
CREATE INDEX "ix_AIEcosystem_data_sources_data_sources" ON "AIEcosystem_data_sources" (data_sources);
CREATE INDEX "ix_AIEcosystem_data_sources_AIEcosystem_id" ON "AIEcosystem_data_sources" ("AIEcosystem_id");

CREATE TABLE "AIEcosystem_ecosystem_components" (
	"AIEcosystem_id" TEXT,
	ecosystem_components TEXT,
	PRIMARY KEY ("AIEcosystem_id", ecosystem_components),
	FOREIGN KEY("AIEcosystem_id") REFERENCES "AIEcosystem" (id)
);
CREATE INDEX "ix_AIEcosystem_ecosystem_components_AIEcosystem_id" ON "AIEcosystem_ecosystem_components" ("AIEcosystem_id");
CREATE INDEX "ix_AIEcosystem_ecosystem_components_ecosystem_components" ON "AIEcosystem_ecosystem_components" (ecosystem_components);

CREATE TABLE "AIEcosystem_big_data_characteristics" (
	"AIEcosystem_id" TEXT,
	big_data_characteristics VARCHAR(11),
	PRIMARY KEY ("AIEcosystem_id", big_data_characteristics),
	FOREIGN KEY("AIEcosystem_id") REFERENCES "AIEcosystem" (id)
);
CREATE INDEX "ix_AIEcosystem_big_data_characteristics_AIEcosystem_id" ON "AIEcosystem_big_data_characteristics" ("AIEcosystem_id");
CREATE INDEX "ix_AIEcosystem_big_data_characteristics_big_data_characteristics" ON "AIEcosystem_big_data_characteristics" (big_data_characteristics);

CREATE TABLE "AIEcosystem_aliases" (
	"AIEcosystem_id" TEXT,
	aliases TEXT,
	PRIMARY KEY ("AIEcosystem_id", aliases),
	FOREIGN KEY("AIEcosystem_id") REFERENCES "AIEcosystem" (id)
);
CREATE INDEX "ix_AIEcosystem_aliases_AIEcosystem_id" ON "AIEcosystem_aliases" ("AIEcosystem_id");
CREATE INDEX "ix_AIEcosystem_aliases_aliases" ON "AIEcosystem_aliases" (aliases);

CREATE TABLE "AIEcosystem_see_also_uri" (
	"AIEcosystem_id" TEXT,
	see_also_uri TEXT,
	PRIMARY KEY ("AIEcosystem_id", see_also_uri),
	FOREIGN KEY("AIEcosystem_id") REFERENCES "AIEcosystem" (id)
);
CREATE INDEX "ix_AIEcosystem_see_also_uri_see_also_uri" ON "AIEcosystem_see_also_uri" (see_also_uri);
CREATE INDEX "ix_AIEcosystem_see_also_uri_AIEcosystem_id" ON "AIEcosystem_see_also_uri" ("AIEcosystem_id");

CREATE TABLE "ResourcePool_aliases" (
	"ResourcePool_id" TEXT,
	aliases TEXT,
	PRIMARY KEY ("ResourcePool_id", aliases),
	FOREIGN KEY("ResourcePool_id") REFERENCES "ResourcePool" (id)
);
CREATE INDEX "ix_ResourcePool_aliases_ResourcePool_id" ON "ResourcePool_aliases" ("ResourcePool_id");
CREATE INDEX "ix_ResourcePool_aliases_aliases" ON "ResourcePool_aliases" (aliases);

CREATE TABLE "ResourcePool_see_also_uri" (
	"ResourcePool_id" TEXT,
	see_also_uri TEXT,
	PRIMARY KEY ("ResourcePool_id", see_also_uri),
	FOREIGN KEY("ResourcePool_id") REFERENCES "ResourcePool" (id)
);
CREATE INDEX "ix_ResourcePool_see_also_uri_ResourcePool_id" ON "ResourcePool_see_also_uri" ("ResourcePool_id");
CREATE INDEX "ix_ResourcePool_see_also_uri_see_also_uri" ON "ResourcePool_see_also_uri" (see_also_uri);

CREATE TABLE "NLPComponent_aliases" (
	"NLPComponent_id" TEXT,
	aliases TEXT,
	PRIMARY KEY ("NLPComponent_id", aliases),
	FOREIGN KEY("NLPComponent_id") REFERENCES "NLPComponent" (id)
);
CREATE INDEX "ix_NLPComponent_aliases_NLPComponent_id" ON "NLPComponent_aliases" ("NLPComponent_id");
CREATE INDEX "ix_NLPComponent_aliases_aliases" ON "NLPComponent_aliases" (aliases);

CREATE TABLE "NLPComponent_see_also_uri" (
	"NLPComponent_id" TEXT,
	see_also_uri TEXT,
	PRIMARY KEY ("NLPComponent_id", see_also_uri),
	FOREIGN KEY("NLPComponent_id") REFERENCES "NLPComponent" (id)
);
CREATE INDEX "ix_NLPComponent_see_also_uri_NLPComponent_id" ON "NLPComponent_see_also_uri" ("NLPComponent_id");
CREATE INDEX "ix_NLPComponent_see_also_uri_see_also_uri" ON "NLPComponent_see_also_uri" (see_also_uri);

CREATE TABLE "ComputerVisionFunction_aliases" (
	"ComputerVisionFunction_id" TEXT,
	aliases TEXT,
	PRIMARY KEY ("ComputerVisionFunction_id", aliases),
	FOREIGN KEY("ComputerVisionFunction_id") REFERENCES "ComputerVisionFunction" (id)
);
CREATE INDEX "ix_ComputerVisionFunction_aliases_ComputerVisionFunction_id" ON "ComputerVisionFunction_aliases" ("ComputerVisionFunction_id");
CREATE INDEX "ix_ComputerVisionFunction_aliases_aliases" ON "ComputerVisionFunction_aliases" (aliases);

CREATE TABLE "ComputerVisionFunction_see_also_uri" (
	"ComputerVisionFunction_id" TEXT,
	see_also_uri TEXT,
	PRIMARY KEY ("ComputerVisionFunction_id", see_also_uri),
	FOREIGN KEY("ComputerVisionFunction_id") REFERENCES "ComputerVisionFunction" (id)
);
CREATE INDEX "ix_ComputerVisionFunction_see_also_uri_ComputerVisionFunction_id" ON "ComputerVisionFunction_see_also_uri" ("ComputerVisionFunction_id");
CREATE INDEX "ix_ComputerVisionFunction_see_also_uri_see_also_uri" ON "ComputerVisionFunction_see_also_uri" (see_also_uri);

CREATE TABLE "Decision_aliases" (
	"Decision_id" TEXT,
	aliases TEXT,
	PRIMARY KEY ("Decision_id", aliases),
	FOREIGN KEY("Decision_id") REFERENCES "Decision" (id)
);
CREATE INDEX "ix_Decision_aliases_aliases" ON "Decision_aliases" (aliases);
CREATE INDEX "ix_Decision_aliases_Decision_id" ON "Decision_aliases" ("Decision_id");

CREATE TABLE "Decision_see_also_uri" (
	"Decision_id" TEXT,
	see_also_uri TEXT,
	PRIMARY KEY ("Decision_id", see_also_uri),
	FOREIGN KEY("Decision_id") REFERENCES "Decision" (id)
);
CREATE INDEX "ix_Decision_see_also_uri_see_also_uri" ON "Decision_see_also_uri" (see_also_uri);
CREATE INDEX "ix_Decision_see_also_uri_Decision_id" ON "Decision_see_also_uri" ("Decision_id");

CREATE TABLE "CognitiveComputingSystem_cognitive_capabilities" (
	"CognitiveComputingSystem_id" TEXT,
	cognitive_capabilities TEXT,
	PRIMARY KEY ("CognitiveComputingSystem_id", cognitive_capabilities),
	FOREIGN KEY("CognitiveComputingSystem_id") REFERENCES "CognitiveComputingSystem" (id)
);
CREATE INDEX "ix_CognitiveComputingSystem_cognitive_capabilities_cognitive_capabilities" ON "CognitiveComputingSystem_cognitive_capabilities" (cognitive_capabilities);
CREATE INDEX "ix_CognitiveComputingSystem_cognitive_capabilities_CognitiveComputingSystem_id" ON "CognitiveComputingSystem_cognitive_capabilities" ("CognitiveComputingSystem_id");

CREATE TABLE "CognitiveComputingSystem_aliases" (
	"CognitiveComputingSystem_id" TEXT,
	aliases TEXT,
	PRIMARY KEY ("CognitiveComputingSystem_id", aliases),
	FOREIGN KEY("CognitiveComputingSystem_id") REFERENCES "CognitiveComputingSystem" (id)
);
CREATE INDEX "ix_CognitiveComputingSystem_aliases_CognitiveComputingSystem_id" ON "CognitiveComputingSystem_aliases" ("CognitiveComputingSystem_id");
CREATE INDEX "ix_CognitiveComputingSystem_aliases_aliases" ON "CognitiveComputingSystem_aliases" (aliases);

CREATE TABLE "CognitiveComputingSystem_see_also_uri" (
	"CognitiveComputingSystem_id" TEXT,
	see_also_uri TEXT,
	PRIMARY KEY ("CognitiveComputingSystem_id", see_also_uri),
	FOREIGN KEY("CognitiveComputingSystem_id") REFERENCES "CognitiveComputingSystem" (id)
);
CREATE INDEX "ix_CognitiveComputingSystem_see_also_uri_see_also_uri" ON "CognitiveComputingSystem_see_also_uri" (see_also_uri);
CREATE INDEX "ix_CognitiveComputingSystem_see_also_uri_CognitiveComputingSystem_id" ON "CognitiveComputingSystem_see_also_uri" ("CognitiveComputingSystem_id");

CREATE TABLE "SemanticComputingSystem_aliases" (
	"SemanticComputingSystem_id" TEXT,
	aliases TEXT,
	PRIMARY KEY ("SemanticComputingSystem_id", aliases),
	FOREIGN KEY("SemanticComputingSystem_id") REFERENCES "SemanticComputingSystem" (id)
);
CREATE INDEX "ix_SemanticComputingSystem_aliases_SemanticComputingSystem_id" ON "SemanticComputingSystem_aliases" ("SemanticComputingSystem_id");
CREATE INDEX "ix_SemanticComputingSystem_aliases_aliases" ON "SemanticComputingSystem_aliases" (aliases);

CREATE TABLE "SemanticComputingSystem_see_also_uri" (
	"SemanticComputingSystem_id" TEXT,
	see_also_uri TEXT,
	PRIMARY KEY ("SemanticComputingSystem_id", see_also_uri),
	FOREIGN KEY("SemanticComputingSystem_id") REFERENCES "SemanticComputingSystem" (id)
);
CREATE INDEX "ix_SemanticComputingSystem_see_also_uri_SemanticComputingSystem_id" ON "SemanticComputingSystem_see_also_uri" ("SemanticComputingSystem_id");
CREATE INDEX "ix_SemanticComputingSystem_see_also_uri_see_also_uri" ON "SemanticComputingSystem_see_also_uri" (see_also_uri);

CREATE TABLE "SoftComputingSystem_soft_computing_techniques" (
	"SoftComputingSystem_id" TEXT,
	soft_computing_techniques VARCHAR(23) NOT NULL,
	PRIMARY KEY ("SoftComputingSystem_id", soft_computing_techniques),
	FOREIGN KEY("SoftComputingSystem_id") REFERENCES "SoftComputingSystem" (id)
);
CREATE INDEX "ix_SoftComputingSystem_soft_computing_techniques_soft_computing_techniques" ON "SoftComputingSystem_soft_computing_techniques" (soft_computing_techniques);
CREATE INDEX "ix_SoftComputingSystem_soft_computing_techniques_SoftComputingSystem_id" ON "SoftComputingSystem_soft_computing_techniques" ("SoftComputingSystem_id");

CREATE TABLE "SoftComputingSystem_aliases" (
	"SoftComputingSystem_id" TEXT,
	aliases TEXT,
	PRIMARY KEY ("SoftComputingSystem_id", aliases),
	FOREIGN KEY("SoftComputingSystem_id") REFERENCES "SoftComputingSystem" (id)
);
CREATE INDEX "ix_SoftComputingSystem_aliases_aliases" ON "SoftComputingSystem_aliases" (aliases);
CREATE INDEX "ix_SoftComputingSystem_aliases_SoftComputingSystem_id" ON "SoftComputingSystem_aliases" ("SoftComputingSystem_id");

CREATE TABLE "SoftComputingSystem_see_also_uri" (
	"SoftComputingSystem_id" TEXT,
	see_also_uri TEXT,
	PRIMARY KEY ("SoftComputingSystem_id", see_also_uri),
	FOREIGN KEY("SoftComputingSystem_id") REFERENCES "SoftComputingSystem" (id)
);
CREATE INDEX "ix_SoftComputingSystem_see_also_uri_SoftComputingSystem_id" ON "SoftComputingSystem_see_also_uri" ("SoftComputingSystem_id");
CREATE INDEX "ix_SoftComputingSystem_see_also_uri_see_also_uri" ON "SoftComputingSystem_see_also_uri" (see_also_uri);

CREATE TABLE "DataSample_aliases" (
	"DataSample_id" TEXT,
	aliases TEXT,
	PRIMARY KEY ("DataSample_id", aliases),
	FOREIGN KEY("DataSample_id") REFERENCES "DataSample" (id)
);
CREATE INDEX "ix_DataSample_aliases_DataSample_id" ON "DataSample_aliases" ("DataSample_id");
CREATE INDEX "ix_DataSample_aliases_aliases" ON "DataSample_aliases" (aliases);

CREATE TABLE "DataSample_see_also_uri" (
	"DataSample_id" TEXT,
	see_also_uri TEXT,
	PRIMARY KEY ("DataSample_id", see_also_uri),
	FOREIGN KEY("DataSample_id") REFERENCES "DataSample" (id)
);
CREATE INDEX "ix_DataSample_see_also_uri_DataSample_id" ON "DataSample_see_also_uri" ("DataSample_id");
CREATE INDEX "ix_DataSample_see_also_uri_see_also_uri" ON "DataSample_see_also_uri" (see_also_uri);

CREATE TABLE "GroundTruthRecord_aliases" (
	"GroundTruthRecord_id" TEXT,
	aliases TEXT,
	PRIMARY KEY ("GroundTruthRecord_id", aliases),
	FOREIGN KEY("GroundTruthRecord_id") REFERENCES "GroundTruthRecord" (id)
);
CREATE INDEX "ix_GroundTruthRecord_aliases_GroundTruthRecord_id" ON "GroundTruthRecord_aliases" ("GroundTruthRecord_id");
CREATE INDEX "ix_GroundTruthRecord_aliases_aliases" ON "GroundTruthRecord_aliases" (aliases);

CREATE TABLE "GroundTruthRecord_see_also_uri" (
	"GroundTruthRecord_id" TEXT,
	see_also_uri TEXT,
	PRIMARY KEY ("GroundTruthRecord_id", see_also_uri),
	FOREIGN KEY("GroundTruthRecord_id") REFERENCES "GroundTruthRecord" (id)
);
CREATE INDEX "ix_GroundTruthRecord_see_also_uri_GroundTruthRecord_id" ON "GroundTruthRecord_see_also_uri" ("GroundTruthRecord_id");
CREATE INDEX "ix_GroundTruthRecord_see_also_uri_see_also_uri" ON "GroundTruthRecord_see_also_uri" (see_also_uri);

CREATE TABLE "AIPlatformProvider_responsibilities" (
	"AIPlatformProvider_id" TEXT,
	responsibilities TEXT,
	PRIMARY KEY ("AIPlatformProvider_id", responsibilities),
	FOREIGN KEY("AIPlatformProvider_id") REFERENCES "AIPlatformProvider" (id)
);
CREATE INDEX "ix_AIPlatformProvider_responsibilities_AIPlatformProvider_id" ON "AIPlatformProvider_responsibilities" ("AIPlatformProvider_id");
CREATE INDEX "ix_AIPlatformProvider_responsibilities_responsibilities" ON "AIPlatformProvider_responsibilities" (responsibilities);

CREATE TABLE "AIPlatformProvider_aliases" (
	"AIPlatformProvider_id" TEXT,
	aliases TEXT,
	PRIMARY KEY ("AIPlatformProvider_id", aliases),
	FOREIGN KEY("AIPlatformProvider_id") REFERENCES "AIPlatformProvider" (id)
);
CREATE INDEX "ix_AIPlatformProvider_aliases_AIPlatformProvider_id" ON "AIPlatformProvider_aliases" ("AIPlatformProvider_id");
CREATE INDEX "ix_AIPlatformProvider_aliases_aliases" ON "AIPlatformProvider_aliases" (aliases);

CREATE TABLE "AIPlatformProvider_see_also_uri" (
	"AIPlatformProvider_id" TEXT,
	see_also_uri TEXT,
	PRIMARY KEY ("AIPlatformProvider_id", see_also_uri),
	FOREIGN KEY("AIPlatformProvider_id") REFERENCES "AIPlatformProvider" (id)
);
CREATE INDEX "ix_AIPlatformProvider_see_also_uri_AIPlatformProvider_id" ON "AIPlatformProvider_see_also_uri" ("AIPlatformProvider_id");
CREATE INDEX "ix_AIPlatformProvider_see_also_uri_see_also_uri" ON "AIPlatformProvider_see_also_uri" (see_also_uri);

CREATE TABLE "AIServiceProductProvider_responsibilities" (
	"AIServiceProductProvider_id" TEXT,
	responsibilities TEXT,
	PRIMARY KEY ("AIServiceProductProvider_id", responsibilities),
	FOREIGN KEY("AIServiceProductProvider_id") REFERENCES "AIServiceProductProvider" (id)
);
CREATE INDEX "ix_AIServiceProductProvider_responsibilities_AIServiceProductProvider_id" ON "AIServiceProductProvider_responsibilities" ("AIServiceProductProvider_id");
CREATE INDEX "ix_AIServiceProductProvider_responsibilities_responsibilities" ON "AIServiceProductProvider_responsibilities" (responsibilities);

CREATE TABLE "AIServiceProductProvider_aliases" (
	"AIServiceProductProvider_id" TEXT,
	aliases TEXT,
	PRIMARY KEY ("AIServiceProductProvider_id", aliases),
	FOREIGN KEY("AIServiceProductProvider_id") REFERENCES "AIServiceProductProvider" (id)
);
CREATE INDEX "ix_AIServiceProductProvider_aliases_aliases" ON "AIServiceProductProvider_aliases" (aliases);
CREATE INDEX "ix_AIServiceProductProvider_aliases_AIServiceProductProvider_id" ON "AIServiceProductProvider_aliases" ("AIServiceProductProvider_id");

CREATE TABLE "AIServiceProductProvider_see_also_uri" (
	"AIServiceProductProvider_id" TEXT,
	see_also_uri TEXT,
	PRIMARY KEY ("AIServiceProductProvider_id", see_also_uri),
	FOREIGN KEY("AIServiceProductProvider_id") REFERENCES "AIServiceProductProvider" (id)
);
CREATE INDEX "ix_AIServiceProductProvider_see_also_uri_AIServiceProductProvider_id" ON "AIServiceProductProvider_see_also_uri" ("AIServiceProductProvider_id");
CREATE INDEX "ix_AIServiceProductProvider_see_also_uri_see_also_uri" ON "AIServiceProductProvider_see_also_uri" (see_also_uri);

CREATE TABLE "ModelDesigner_responsibilities" (
	"ModelDesigner_id" TEXT,
	responsibilities TEXT,
	PRIMARY KEY ("ModelDesigner_id", responsibilities),
	FOREIGN KEY("ModelDesigner_id") REFERENCES "ModelDesigner" (id)
);
CREATE INDEX "ix_ModelDesigner_responsibilities_ModelDesigner_id" ON "ModelDesigner_responsibilities" ("ModelDesigner_id");
CREATE INDEX "ix_ModelDesigner_responsibilities_responsibilities" ON "ModelDesigner_responsibilities" (responsibilities);

CREATE TABLE "ModelDesigner_aliases" (
	"ModelDesigner_id" TEXT,
	aliases TEXT,
	PRIMARY KEY ("ModelDesigner_id", aliases),
	FOREIGN KEY("ModelDesigner_id") REFERENCES "ModelDesigner" (id)
);
CREATE INDEX "ix_ModelDesigner_aliases_ModelDesigner_id" ON "ModelDesigner_aliases" ("ModelDesigner_id");
CREATE INDEX "ix_ModelDesigner_aliases_aliases" ON "ModelDesigner_aliases" (aliases);

CREATE TABLE "ModelDesigner_see_also_uri" (
	"ModelDesigner_id" TEXT,
	see_also_uri TEXT,
	PRIMARY KEY ("ModelDesigner_id", see_also_uri),
	FOREIGN KEY("ModelDesigner_id") REFERENCES "ModelDesigner" (id)
);
CREATE INDEX "ix_ModelDesigner_see_also_uri_see_also_uri" ON "ModelDesigner_see_also_uri" (see_also_uri);
CREATE INDEX "ix_ModelDesigner_see_also_uri_ModelDesigner_id" ON "ModelDesigner_see_also_uri" ("ModelDesigner_id");

CREATE TABLE "ModelImplementer_responsibilities" (
	"ModelImplementer_id" TEXT,
	responsibilities TEXT,
	PRIMARY KEY ("ModelImplementer_id", responsibilities),
	FOREIGN KEY("ModelImplementer_id") REFERENCES "ModelImplementer" (id)
);
CREATE INDEX "ix_ModelImplementer_responsibilities_ModelImplementer_id" ON "ModelImplementer_responsibilities" ("ModelImplementer_id");
CREATE INDEX "ix_ModelImplementer_responsibilities_responsibilities" ON "ModelImplementer_responsibilities" (responsibilities);

CREATE TABLE "ModelImplementer_aliases" (
	"ModelImplementer_id" TEXT,
	aliases TEXT,
	PRIMARY KEY ("ModelImplementer_id", aliases),
	FOREIGN KEY("ModelImplementer_id") REFERENCES "ModelImplementer" (id)
);
CREATE INDEX "ix_ModelImplementer_aliases_ModelImplementer_id" ON "ModelImplementer_aliases" ("ModelImplementer_id");
CREATE INDEX "ix_ModelImplementer_aliases_aliases" ON "ModelImplementer_aliases" (aliases);

CREATE TABLE "ModelImplementer_see_also_uri" (
	"ModelImplementer_id" TEXT,
	see_also_uri TEXT,
	PRIMARY KEY ("ModelImplementer_id", see_also_uri),
	FOREIGN KEY("ModelImplementer_id") REFERENCES "ModelImplementer" (id)
);
CREATE INDEX "ix_ModelImplementer_see_also_uri_ModelImplementer_id" ON "ModelImplementer_see_also_uri" ("ModelImplementer_id");
CREATE INDEX "ix_ModelImplementer_see_also_uri_see_also_uri" ON "ModelImplementer_see_also_uri" (see_also_uri);

CREATE TABLE "ComputationVerifier_responsibilities" (
	"ComputationVerifier_id" TEXT,
	responsibilities TEXT,
	PRIMARY KEY ("ComputationVerifier_id", responsibilities),
	FOREIGN KEY("ComputationVerifier_id") REFERENCES "ComputationVerifier" (id)
);
CREATE INDEX "ix_ComputationVerifier_responsibilities_responsibilities" ON "ComputationVerifier_responsibilities" (responsibilities);
CREATE INDEX "ix_ComputationVerifier_responsibilities_ComputationVerifier_id" ON "ComputationVerifier_responsibilities" ("ComputationVerifier_id");

CREATE TABLE "ComputationVerifier_aliases" (
	"ComputationVerifier_id" TEXT,
	aliases TEXT,
	PRIMARY KEY ("ComputationVerifier_id", aliases),
	FOREIGN KEY("ComputationVerifier_id") REFERENCES "ComputationVerifier" (id)
);
CREATE INDEX "ix_ComputationVerifier_aliases_ComputationVerifier_id" ON "ComputationVerifier_aliases" ("ComputationVerifier_id");
CREATE INDEX "ix_ComputationVerifier_aliases_aliases" ON "ComputationVerifier_aliases" (aliases);

CREATE TABLE "ComputationVerifier_see_also_uri" (
	"ComputationVerifier_id" TEXT,
	see_also_uri TEXT,
	PRIMARY KEY ("ComputationVerifier_id", see_also_uri),
	FOREIGN KEY("ComputationVerifier_id") REFERENCES "ComputationVerifier" (id)
);
CREATE INDEX "ix_ComputationVerifier_see_also_uri_ComputationVerifier_id" ON "ComputationVerifier_see_also_uri" ("ComputationVerifier_id");
CREATE INDEX "ix_ComputationVerifier_see_also_uri_see_also_uri" ON "ComputationVerifier_see_also_uri" (see_also_uri);

CREATE TABLE "ModelVerifier_responsibilities" (
	"ModelVerifier_id" TEXT,
	responsibilities TEXT,
	PRIMARY KEY ("ModelVerifier_id", responsibilities),
	FOREIGN KEY("ModelVerifier_id") REFERENCES "ModelVerifier" (id)
);
CREATE INDEX "ix_ModelVerifier_responsibilities_ModelVerifier_id" ON "ModelVerifier_responsibilities" ("ModelVerifier_id");
CREATE INDEX "ix_ModelVerifier_responsibilities_responsibilities" ON "ModelVerifier_responsibilities" (responsibilities);

CREATE TABLE "ModelVerifier_aliases" (
	"ModelVerifier_id" TEXT,
	aliases TEXT,
	PRIMARY KEY ("ModelVerifier_id", aliases),
	FOREIGN KEY("ModelVerifier_id") REFERENCES "ModelVerifier" (id)
);
CREATE INDEX "ix_ModelVerifier_aliases_aliases" ON "ModelVerifier_aliases" (aliases);
CREATE INDEX "ix_ModelVerifier_aliases_ModelVerifier_id" ON "ModelVerifier_aliases" ("ModelVerifier_id");

CREATE TABLE "ModelVerifier_see_also_uri" (
	"ModelVerifier_id" TEXT,
	see_also_uri TEXT,
	PRIMARY KEY ("ModelVerifier_id", see_also_uri),
	FOREIGN KEY("ModelVerifier_id") REFERENCES "ModelVerifier" (id)
);
CREATE INDEX "ix_ModelVerifier_see_also_uri_ModelVerifier_id" ON "ModelVerifier_see_also_uri" ("ModelVerifier_id");
CREATE INDEX "ix_ModelVerifier_see_also_uri_see_also_uri" ON "ModelVerifier_see_also_uri" (see_also_uri);

CREATE TABLE "AIUser_responsibilities" (
	"AIUser_id" TEXT,
	responsibilities TEXT,
	PRIMARY KEY ("AIUser_id", responsibilities),
	FOREIGN KEY("AIUser_id") REFERENCES "AIUser" (id)
);
CREATE INDEX "ix_AIUser_responsibilities_AIUser_id" ON "AIUser_responsibilities" ("AIUser_id");
CREATE INDEX "ix_AIUser_responsibilities_responsibilities" ON "AIUser_responsibilities" (responsibilities);

CREATE TABLE "AIUser_aliases" (
	"AIUser_id" TEXT,
	aliases TEXT,
	PRIMARY KEY ("AIUser_id", aliases),
	FOREIGN KEY("AIUser_id") REFERENCES "AIUser" (id)
);
CREATE INDEX "ix_AIUser_aliases_AIUser_id" ON "AIUser_aliases" ("AIUser_id");
CREATE INDEX "ix_AIUser_aliases_aliases" ON "AIUser_aliases" (aliases);

CREATE TABLE "AIUser_see_also_uri" (
	"AIUser_id" TEXT,
	see_also_uri TEXT,
	PRIMARY KEY ("AIUser_id", see_also_uri),
	FOREIGN KEY("AIUser_id") REFERENCES "AIUser" (id)
);
CREATE INDEX "ix_AIUser_see_also_uri_see_also_uri" ON "AIUser_see_also_uri" (see_also_uri);
CREATE INDEX "ix_AIUser_see_also_uri_AIUser_id" ON "AIUser_see_also_uri" ("AIUser_id");

CREATE TABLE "AISystemIntegrator_responsibilities" (
	"AISystemIntegrator_id" TEXT,
	responsibilities TEXT,
	PRIMARY KEY ("AISystemIntegrator_id", responsibilities),
	FOREIGN KEY("AISystemIntegrator_id") REFERENCES "AISystemIntegrator" (id)
);
CREATE INDEX "ix_AISystemIntegrator_responsibilities_AISystemIntegrator_id" ON "AISystemIntegrator_responsibilities" ("AISystemIntegrator_id");
CREATE INDEX "ix_AISystemIntegrator_responsibilities_responsibilities" ON "AISystemIntegrator_responsibilities" (responsibilities);

CREATE TABLE "AISystemIntegrator_aliases" (
	"AISystemIntegrator_id" TEXT,
	aliases TEXT,
	PRIMARY KEY ("AISystemIntegrator_id", aliases),
	FOREIGN KEY("AISystemIntegrator_id") REFERENCES "AISystemIntegrator" (id)
);
CREATE INDEX "ix_AISystemIntegrator_aliases_AISystemIntegrator_id" ON "AISystemIntegrator_aliases" ("AISystemIntegrator_id");
CREATE INDEX "ix_AISystemIntegrator_aliases_aliases" ON "AISystemIntegrator_aliases" (aliases);

CREATE TABLE "AISystemIntegrator_see_also_uri" (
	"AISystemIntegrator_id" TEXT,
	see_also_uri TEXT,
	PRIMARY KEY ("AISystemIntegrator_id", see_also_uri),
	FOREIGN KEY("AISystemIntegrator_id") REFERENCES "AISystemIntegrator" (id)
);
CREATE INDEX "ix_AISystemIntegrator_see_also_uri_AISystemIntegrator_id" ON "AISystemIntegrator_see_also_uri" ("AISystemIntegrator_id");
CREATE INDEX "ix_AISystemIntegrator_see_also_uri_see_also_uri" ON "AISystemIntegrator_see_also_uri" (see_also_uri);

CREATE TABLE "DataProvider_responsibilities" (
	"DataProvider_id" TEXT,
	responsibilities TEXT,
	PRIMARY KEY ("DataProvider_id", responsibilities),
	FOREIGN KEY("DataProvider_id") REFERENCES "DataProvider" (id)
);
CREATE INDEX "ix_DataProvider_responsibilities_responsibilities" ON "DataProvider_responsibilities" (responsibilities);
CREATE INDEX "ix_DataProvider_responsibilities_DataProvider_id" ON "DataProvider_responsibilities" ("DataProvider_id");

CREATE TABLE "DataProvider_aliases" (
	"DataProvider_id" TEXT,
	aliases TEXT,
	PRIMARY KEY ("DataProvider_id", aliases),
	FOREIGN KEY("DataProvider_id") REFERENCES "DataProvider" (id)
);
CREATE INDEX "ix_DataProvider_aliases_DataProvider_id" ON "DataProvider_aliases" ("DataProvider_id");
CREATE INDEX "ix_DataProvider_aliases_aliases" ON "DataProvider_aliases" (aliases);

CREATE TABLE "DataProvider_see_also_uri" (
	"DataProvider_id" TEXT,
	see_also_uri TEXT,
	PRIMARY KEY ("DataProvider_id", see_also_uri),
	FOREIGN KEY("DataProvider_id") REFERENCES "DataProvider" (id)
);
CREATE INDEX "ix_DataProvider_see_also_uri_DataProvider_id" ON "DataProvider_see_also_uri" ("DataProvider_id");
CREATE INDEX "ix_DataProvider_see_also_uri_see_also_uri" ON "DataProvider_see_also_uri" (see_also_uri);

CREATE TABLE "AIAuditor_responsibilities" (
	"AIAuditor_id" TEXT,
	responsibilities TEXT,
	PRIMARY KEY ("AIAuditor_id", responsibilities),
	FOREIGN KEY("AIAuditor_id") REFERENCES "AIAuditor" (id)
);
CREATE INDEX "ix_AIAuditor_responsibilities_AIAuditor_id" ON "AIAuditor_responsibilities" ("AIAuditor_id");
CREATE INDEX "ix_AIAuditor_responsibilities_responsibilities" ON "AIAuditor_responsibilities" (responsibilities);

CREATE TABLE "AIAuditor_aliases" (
	"AIAuditor_id" TEXT,
	aliases TEXT,
	PRIMARY KEY ("AIAuditor_id", aliases),
	FOREIGN KEY("AIAuditor_id") REFERENCES "AIAuditor" (id)
);
CREATE INDEX "ix_AIAuditor_aliases_aliases" ON "AIAuditor_aliases" (aliases);
CREATE INDEX "ix_AIAuditor_aliases_AIAuditor_id" ON "AIAuditor_aliases" ("AIAuditor_id");

CREATE TABLE "AIAuditor_see_also_uri" (
	"AIAuditor_id" TEXT,
	see_also_uri TEXT,
	PRIMARY KEY ("AIAuditor_id", see_also_uri),
	FOREIGN KEY("AIAuditor_id") REFERENCES "AIAuditor" (id)
);
CREATE INDEX "ix_AIAuditor_see_also_uri_AIAuditor_id" ON "AIAuditor_see_also_uri" ("AIAuditor_id");
CREATE INDEX "ix_AIAuditor_see_also_uri_see_also_uri" ON "AIAuditor_see_also_uri" (see_also_uri);

CREATE TABLE "AIEvaluator_responsibilities" (
	"AIEvaluator_id" TEXT,
	responsibilities TEXT,
	PRIMARY KEY ("AIEvaluator_id", responsibilities),
	FOREIGN KEY("AIEvaluator_id") REFERENCES "AIEvaluator" (id)
);
CREATE INDEX "ix_AIEvaluator_responsibilities_AIEvaluator_id" ON "AIEvaluator_responsibilities" ("AIEvaluator_id");
CREATE INDEX "ix_AIEvaluator_responsibilities_responsibilities" ON "AIEvaluator_responsibilities" (responsibilities);

CREATE TABLE "AIEvaluator_aliases" (
	"AIEvaluator_id" TEXT,
	aliases TEXT,
	PRIMARY KEY ("AIEvaluator_id", aliases),
	FOREIGN KEY("AIEvaluator_id") REFERENCES "AIEvaluator" (id)
);
CREATE INDEX "ix_AIEvaluator_aliases_AIEvaluator_id" ON "AIEvaluator_aliases" ("AIEvaluator_id");
CREATE INDEX "ix_AIEvaluator_aliases_aliases" ON "AIEvaluator_aliases" (aliases);

CREATE TABLE "AIEvaluator_see_also_uri" (
	"AIEvaluator_id" TEXT,
	see_also_uri TEXT,
	PRIMARY KEY ("AIEvaluator_id", see_also_uri),
	FOREIGN KEY("AIEvaluator_id") REFERENCES "AIEvaluator" (id)
);
CREATE INDEX "ix_AIEvaluator_see_also_uri_see_also_uri" ON "AIEvaluator_see_also_uri" (see_also_uri);
CREATE INDEX "ix_AIEvaluator_see_also_uri_AIEvaluator_id" ON "AIEvaluator_see_also_uri" ("AIEvaluator_id");

CREATE TABLE "DataSubject_responsibilities" (
	"DataSubject_id" TEXT,
	responsibilities TEXT,
	PRIMARY KEY ("DataSubject_id", responsibilities),
	FOREIGN KEY("DataSubject_id") REFERENCES "DataSubject" (id)
);
CREATE INDEX "ix_DataSubject_responsibilities_DataSubject_id" ON "DataSubject_responsibilities" ("DataSubject_id");
CREATE INDEX "ix_DataSubject_responsibilities_responsibilities" ON "DataSubject_responsibilities" (responsibilities);

CREATE TABLE "DataSubject_aliases" (
	"DataSubject_id" TEXT,
	aliases TEXT,
	PRIMARY KEY ("DataSubject_id", aliases),
	FOREIGN KEY("DataSubject_id") REFERENCES "DataSubject" (id)
);
CREATE INDEX "ix_DataSubject_aliases_DataSubject_id" ON "DataSubject_aliases" ("DataSubject_id");
CREATE INDEX "ix_DataSubject_aliases_aliases" ON "DataSubject_aliases" (aliases);

CREATE TABLE "DataSubject_see_also_uri" (
	"DataSubject_id" TEXT,
	see_also_uri TEXT,
	PRIMARY KEY ("DataSubject_id", see_also_uri),
	FOREIGN KEY("DataSubject_id") REFERENCES "DataSubject" (id)
);
CREATE INDEX "ix_DataSubject_see_also_uri_DataSubject_id" ON "DataSubject_see_also_uri" ("DataSubject_id");
CREATE INDEX "ix_DataSubject_see_also_uri_see_also_uri" ON "DataSubject_see_also_uri" (see_also_uri);

CREATE TABLE "PolicyMaker_responsibilities" (
	"PolicyMaker_id" TEXT,
	responsibilities TEXT,
	PRIMARY KEY ("PolicyMaker_id", responsibilities),
	FOREIGN KEY("PolicyMaker_id") REFERENCES "PolicyMaker" (id)
);
CREATE INDEX "ix_PolicyMaker_responsibilities_responsibilities" ON "PolicyMaker_responsibilities" (responsibilities);
CREATE INDEX "ix_PolicyMaker_responsibilities_PolicyMaker_id" ON "PolicyMaker_responsibilities" ("PolicyMaker_id");

CREATE TABLE "PolicyMaker_aliases" (
	"PolicyMaker_id" TEXT,
	aliases TEXT,
	PRIMARY KEY ("PolicyMaker_id", aliases),
	FOREIGN KEY("PolicyMaker_id") REFERENCES "PolicyMaker" (id)
);
CREATE INDEX "ix_PolicyMaker_aliases_PolicyMaker_id" ON "PolicyMaker_aliases" ("PolicyMaker_id");
CREATE INDEX "ix_PolicyMaker_aliases_aliases" ON "PolicyMaker_aliases" (aliases);

CREATE TABLE "PolicyMaker_see_also_uri" (
	"PolicyMaker_id" TEXT,
	see_also_uri TEXT,
	PRIMARY KEY ("PolicyMaker_id", see_also_uri),
	FOREIGN KEY("PolicyMaker_id") REFERENCES "PolicyMaker" (id)
);
CREATE INDEX "ix_PolicyMaker_see_also_uri_PolicyMaker_id" ON "PolicyMaker_see_also_uri" ("PolicyMaker_id");
CREATE INDEX "ix_PolicyMaker_see_also_uri_see_also_uri" ON "PolicyMaker_see_also_uri" (see_also_uri);

CREATE TABLE "Regulator_responsibilities" (
	"Regulator_id" TEXT,
	responsibilities TEXT,
	PRIMARY KEY ("Regulator_id", responsibilities),
	FOREIGN KEY("Regulator_id") REFERENCES "Regulator" (id)
);
CREATE INDEX "ix_Regulator_responsibilities_Regulator_id" ON "Regulator_responsibilities" ("Regulator_id");
CREATE INDEX "ix_Regulator_responsibilities_responsibilities" ON "Regulator_responsibilities" (responsibilities);

CREATE TABLE "Regulator_aliases" (
	"Regulator_id" TEXT,
	aliases TEXT,
	PRIMARY KEY ("Regulator_id", aliases),
	FOREIGN KEY("Regulator_id") REFERENCES "Regulator" (id)
);
CREATE INDEX "ix_Regulator_aliases_aliases" ON "Regulator_aliases" (aliases);
CREATE INDEX "ix_Regulator_aliases_Regulator_id" ON "Regulator_aliases" ("Regulator_id");

CREATE TABLE "Regulator_see_also_uri" (
	"Regulator_id" TEXT,
	see_also_uri TEXT,
	PRIMARY KEY ("Regulator_id", see_also_uri),
	FOREIGN KEY("Regulator_id") REFERENCES "Regulator" (id)
);
CREATE INDEX "ix_Regulator_see_also_uri_Regulator_id" ON "Regulator_see_also_uri" ("Regulator_id");
CREATE INDEX "ix_Regulator_see_also_uri_see_also_uri" ON "Regulator_see_also_uri" (see_also_uri);

CREATE TABLE "AutonomyAssessment_autonomy_criterion_scores" (
	"AutonomyAssessment_id" TEXT,
	autonomy_criterion_scores TEXT,
	PRIMARY KEY ("AutonomyAssessment_id", autonomy_criterion_scores),
	FOREIGN KEY("AutonomyAssessment_id") REFERENCES "AutonomyAssessment" (id)
);
CREATE INDEX "ix_AutonomyAssessment_autonomy_criterion_scores_autonomy_criterion_scores" ON "AutonomyAssessment_autonomy_criterion_scores" (autonomy_criterion_scores);
CREATE INDEX "ix_AutonomyAssessment_autonomy_criterion_scores_AutonomyAssessment_id" ON "AutonomyAssessment_autonomy_criterion_scores" ("AutonomyAssessment_id");

CREATE TABLE "AutonomyAssessment_aliases" (
	"AutonomyAssessment_id" TEXT,
	aliases TEXT,
	PRIMARY KEY ("AutonomyAssessment_id", aliases),
	FOREIGN KEY("AutonomyAssessment_id") REFERENCES "AutonomyAssessment" (id)
);
CREATE INDEX "ix_AutonomyAssessment_aliases_AutonomyAssessment_id" ON "AutonomyAssessment_aliases" ("AutonomyAssessment_id");
CREATE INDEX "ix_AutonomyAssessment_aliases_aliases" ON "AutonomyAssessment_aliases" (aliases);

CREATE TABLE "AutonomyAssessment_see_also_uri" (
	"AutonomyAssessment_id" TEXT,
	see_also_uri TEXT,
	PRIMARY KEY ("AutonomyAssessment_id", see_also_uri),
	FOREIGN KEY("AutonomyAssessment_id") REFERENCES "AutonomyAssessment" (id)
);
CREATE INDEX "ix_AutonomyAssessment_see_also_uri_see_also_uri" ON "AutonomyAssessment_see_also_uri" (see_also_uri);
CREATE INDEX "ix_AutonomyAssessment_see_also_uri_AutonomyAssessment_id" ON "AutonomyAssessment_see_also_uri" ("AutonomyAssessment_id");

CREATE TABLE "VerificationValidationFramework_verification_methods" (
	"VerificationValidationFramework_id" TEXT,
	verification_methods TEXT,
	PRIMARY KEY ("VerificationValidationFramework_id", verification_methods),
	FOREIGN KEY("VerificationValidationFramework_id") REFERENCES "VerificationValidationFramework" (id)
);
CREATE INDEX "ix_VerificationValidationFramework_verification_methods_VerificationValidationFramework_id" ON "VerificationValidationFramework_verification_methods" ("VerificationValidationFramework_id");
CREATE INDEX "ix_VerificationValidationFramework_verification_methods_verification_methods" ON "VerificationValidationFramework_verification_methods" (verification_methods);

CREATE TABLE "VerificationValidationFramework_validation_methods" (
	"VerificationValidationFramework_id" TEXT,
	validation_methods TEXT,
	PRIMARY KEY ("VerificationValidationFramework_id", validation_methods),
	FOREIGN KEY("VerificationValidationFramework_id") REFERENCES "VerificationValidationFramework" (id)
);
CREATE INDEX "ix_VerificationValidationFramework_validation_methods_VerificationValidationFramework_id" ON "VerificationValidationFramework_validation_methods" ("VerificationValidationFramework_id");
CREATE INDEX "ix_VerificationValidationFramework_validation_methods_validation_methods" ON "VerificationValidationFramework_validation_methods" (validation_methods);

CREATE TABLE "VerificationValidationFramework_aliases" (
	"VerificationValidationFramework_id" TEXT,
	aliases TEXT,
	PRIMARY KEY ("VerificationValidationFramework_id", aliases),
	FOREIGN KEY("VerificationValidationFramework_id") REFERENCES "VerificationValidationFramework" (id)
);
CREATE INDEX "ix_VerificationValidationFramework_aliases_VerificationValidationFramework_id" ON "VerificationValidationFramework_aliases" ("VerificationValidationFramework_id");
CREATE INDEX "ix_VerificationValidationFramework_aliases_aliases" ON "VerificationValidationFramework_aliases" (aliases);

CREATE TABLE "VerificationValidationFramework_see_also_uri" (
	"VerificationValidationFramework_id" TEXT,
	see_also_uri TEXT,
	PRIMARY KEY ("VerificationValidationFramework_id", see_also_uri),
	FOREIGN KEY("VerificationValidationFramework_id") REFERENCES "VerificationValidationFramework" (id)
);
CREATE INDEX "ix_VerificationValidationFramework_see_also_uri_VerificationValidationFramework_id" ON "VerificationValidationFramework_see_also_uri" ("VerificationValidationFramework_id");
CREATE INDEX "ix_VerificationValidationFramework_see_also_uri_see_also_uri" ON "VerificationValidationFramework_see_also_uri" (see_also_uri);

CREATE TABLE "HumanMachineTeam_human_roles" (
	"HumanMachineTeam_id" TEXT,
	human_roles TEXT,
	PRIMARY KEY ("HumanMachineTeam_id", human_roles),
	FOREIGN KEY("HumanMachineTeam_id") REFERENCES "HumanMachineTeam" (id)
);
CREATE INDEX "ix_HumanMachineTeam_human_roles_HumanMachineTeam_id" ON "HumanMachineTeam_human_roles" ("HumanMachineTeam_id");
CREATE INDEX "ix_HumanMachineTeam_human_roles_human_roles" ON "HumanMachineTeam_human_roles" (human_roles);

CREATE TABLE "HumanMachineTeam_aliases" (
	"HumanMachineTeam_id" TEXT,
	aliases TEXT,
	PRIMARY KEY ("HumanMachineTeam_id", aliases),
	FOREIGN KEY("HumanMachineTeam_id") REFERENCES "HumanMachineTeam" (id)
);
CREATE INDEX "ix_HumanMachineTeam_aliases_aliases" ON "HumanMachineTeam_aliases" (aliases);
CREATE INDEX "ix_HumanMachineTeam_aliases_HumanMachineTeam_id" ON "HumanMachineTeam_aliases" ("HumanMachineTeam_id");

CREATE TABLE "HumanMachineTeam_see_also_uri" (
	"HumanMachineTeam_id" TEXT,
	see_also_uri TEXT,
	PRIMARY KEY ("HumanMachineTeam_id", see_also_uri),
	FOREIGN KEY("HumanMachineTeam_id") REFERENCES "HumanMachineTeam" (id)
);
CREATE INDEX "ix_HumanMachineTeam_see_also_uri_HumanMachineTeam_id" ON "HumanMachineTeam_see_also_uri" ("HumanMachineTeam_id");
CREATE INDEX "ix_HumanMachineTeam_see_also_uri_see_also_uri" ON "HumanMachineTeam_see_also_uri" (see_also_uri);

CREATE TABLE "IntelligenceAugmentation_augmented_capability" (
	"IntelligenceAugmentation_id" TEXT,
	augmented_capability TEXT,
	PRIMARY KEY ("IntelligenceAugmentation_id", augmented_capability),
	FOREIGN KEY("IntelligenceAugmentation_id") REFERENCES "IntelligenceAugmentation" (id)
);
CREATE INDEX "ix_IntelligenceAugmentation_augmented_capability_IntelligenceAugmentation_id" ON "IntelligenceAugmentation_augmented_capability" ("IntelligenceAugmentation_id");
CREATE INDEX "ix_IntelligenceAugmentation_augmented_capability_augmented_capability" ON "IntelligenceAugmentation_augmented_capability" (augmented_capability);

CREATE TABLE "IntelligenceAugmentation_aliases" (
	"IntelligenceAugmentation_id" TEXT,
	aliases TEXT,
	PRIMARY KEY ("IntelligenceAugmentation_id", aliases),
	FOREIGN KEY("IntelligenceAugmentation_id") REFERENCES "IntelligenceAugmentation" (id)
);
CREATE INDEX "ix_IntelligenceAugmentation_aliases_aliases" ON "IntelligenceAugmentation_aliases" (aliases);
CREATE INDEX "ix_IntelligenceAugmentation_aliases_IntelligenceAugmentation_id" ON "IntelligenceAugmentation_aliases" ("IntelligenceAugmentation_id");

CREATE TABLE "IntelligenceAugmentation_see_also_uri" (
	"IntelligenceAugmentation_id" TEXT,
	see_also_uri TEXT,
	PRIMARY KEY ("IntelligenceAugmentation_id", see_also_uri),
	FOREIGN KEY("IntelligenceAugmentation_id") REFERENCES "IntelligenceAugmentation" (id)
);
CREATE INDEX "ix_IntelligenceAugmentation_see_also_uri_IntelligenceAugmentation_id" ON "IntelligenceAugmentation_see_also_uri" ("IntelligenceAugmentation_id");
CREATE INDEX "ix_IntelligenceAugmentation_see_also_uri_see_also_uri" ON "IntelligenceAugmentation_see_also_uri" (see_also_uri);

CREATE TABLE "Recommendation_recommended_items" (
	"Recommendation_id" TEXT,
	recommended_items TEXT,
	PRIMARY KEY ("Recommendation_id", recommended_items),
	FOREIGN KEY("Recommendation_id") REFERENCES "Recommendation" (id)
);
CREATE INDEX "ix_Recommendation_recommended_items_Recommendation_id" ON "Recommendation_recommended_items" ("Recommendation_id");
CREATE INDEX "ix_Recommendation_recommended_items_recommended_items" ON "Recommendation_recommended_items" (recommended_items);

CREATE TABLE "Recommendation_aliases" (
	"Recommendation_id" TEXT,
	aliases TEXT,
	PRIMARY KEY ("Recommendation_id", aliases),
	FOREIGN KEY("Recommendation_id") REFERENCES "Recommendation" (id)
);
CREATE INDEX "ix_Recommendation_aliases_aliases" ON "Recommendation_aliases" (aliases);
CREATE INDEX "ix_Recommendation_aliases_Recommendation_id" ON "Recommendation_aliases" ("Recommendation_id");

CREATE TABLE "Recommendation_see_also_uri" (
	"Recommendation_id" TEXT,
	see_also_uri TEXT,
	PRIMARY KEY ("Recommendation_id", see_also_uri),
	FOREIGN KEY("Recommendation_id") REFERENCES "Recommendation" (id)
);
CREATE INDEX "ix_Recommendation_see_also_uri_Recommendation_id" ON "Recommendation_see_also_uri" ("Recommendation_id");
CREATE INDEX "ix_Recommendation_see_also_uri_see_also_uri" ON "Recommendation_see_also_uri" (see_also_uri);

CREATE TABLE "Threshold_aliases" (
	"Threshold_id" TEXT,
	aliases TEXT,
	PRIMARY KEY ("Threshold_id", aliases),
	FOREIGN KEY("Threshold_id") REFERENCES "Threshold" (id)
);
CREATE INDEX "ix_Threshold_aliases_aliases" ON "Threshold_aliases" (aliases);
CREATE INDEX "ix_Threshold_aliases_Threshold_id" ON "Threshold_aliases" ("Threshold_id");

CREATE TABLE "Threshold_see_also_uri" (
	"Threshold_id" TEXT,
	see_also_uri TEXT,
	PRIMARY KEY ("Threshold_id", see_also_uri),
	FOREIGN KEY("Threshold_id") REFERENCES "Threshold" (id)
);
CREATE INDEX "ix_Threshold_see_also_uri_Threshold_id" ON "Threshold_see_also_uri" ("Threshold_id");
CREATE INDEX "ix_Threshold_see_also_uri_see_also_uri" ON "Threshold_see_also_uri" (see_also_uri);

CREATE TABLE "Neuron_aliases" (
	"Neuron_id" TEXT,
	aliases TEXT,
	PRIMARY KEY ("Neuron_id", aliases),
	FOREIGN KEY("Neuron_id") REFERENCES "Neuron" (id)
);
CREATE INDEX "ix_Neuron_aliases_Neuron_id" ON "Neuron_aliases" ("Neuron_id");
CREATE INDEX "ix_Neuron_aliases_aliases" ON "Neuron_aliases" (aliases);

CREATE TABLE "Neuron_see_also_uri" (
	"Neuron_id" TEXT,
	see_also_uri TEXT,
	PRIMARY KEY ("Neuron_id", see_also_uri),
	FOREIGN KEY("Neuron_id") REFERENCES "Neuron" (id)
);
CREATE INDEX "ix_Neuron_see_also_uri_Neuron_id" ON "Neuron_see_also_uri" ("Neuron_id");
CREATE INDEX "ix_Neuron_see_also_uri_see_also_uri" ON "Neuron_see_also_uri" (see_also_uri);

CREATE TABLE "ConvolutionOperation_kernel_size" (
	"ConvolutionOperation_id" TEXT,
	kernel_size INTEGER,
	PRIMARY KEY ("ConvolutionOperation_id", kernel_size),
	FOREIGN KEY("ConvolutionOperation_id") REFERENCES "ConvolutionOperation" (id)
);
CREATE INDEX "ix_ConvolutionOperation_kernel_size_kernel_size" ON "ConvolutionOperation_kernel_size" (kernel_size);
CREATE INDEX "ix_ConvolutionOperation_kernel_size_ConvolutionOperation_id" ON "ConvolutionOperation_kernel_size" ("ConvolutionOperation_id");

CREATE TABLE "ConvolutionOperation_aliases" (
	"ConvolutionOperation_id" TEXT,
	aliases TEXT,
	PRIMARY KEY ("ConvolutionOperation_id", aliases),
	FOREIGN KEY("ConvolutionOperation_id") REFERENCES "ConvolutionOperation" (id)
);
CREATE INDEX "ix_ConvolutionOperation_aliases_ConvolutionOperation_id" ON "ConvolutionOperation_aliases" ("ConvolutionOperation_id");
CREATE INDEX "ix_ConvolutionOperation_aliases_aliases" ON "ConvolutionOperation_aliases" (aliases);

CREATE TABLE "ConvolutionOperation_see_also_uri" (
	"ConvolutionOperation_id" TEXT,
	see_also_uri TEXT,
	PRIMARY KEY ("ConvolutionOperation_id", see_also_uri),
	FOREIGN KEY("ConvolutionOperation_id") REFERENCES "ConvolutionOperation" (id)
);
CREATE INDEX "ix_ConvolutionOperation_see_also_uri_ConvolutionOperation_id" ON "ConvolutionOperation_see_also_uri" ("ConvolutionOperation_id");
CREATE INDEX "ix_ConvolutionOperation_see_also_uri_see_also_uri" ON "ConvolutionOperation_see_also_uri" (see_also_uri);

CREATE TABLE "FaultToleranceMechanism_aliases" (
	"FaultToleranceMechanism_id" TEXT,
	aliases TEXT,
	PRIMARY KEY ("FaultToleranceMechanism_id", aliases),
	FOREIGN KEY("FaultToleranceMechanism_id") REFERENCES "FaultToleranceMechanism" (id)
);
CREATE INDEX "ix_FaultToleranceMechanism_aliases_FaultToleranceMechanism_id" ON "FaultToleranceMechanism_aliases" ("FaultToleranceMechanism_id");
CREATE INDEX "ix_FaultToleranceMechanism_aliases_aliases" ON "FaultToleranceMechanism_aliases" (aliases);

CREATE TABLE "FaultToleranceMechanism_see_also_uri" (
	"FaultToleranceMechanism_id" TEXT,
	see_also_uri TEXT,
	PRIMARY KEY ("FaultToleranceMechanism_id", see_also_uri),
	FOREIGN KEY("FaultToleranceMechanism_id") REFERENCES "FaultToleranceMechanism" (id)
);
CREATE INDEX "ix_FaultToleranceMechanism_see_also_uri_see_also_uri" ON "FaultToleranceMechanism_see_also_uri" (see_also_uri);
CREATE INDEX "ix_FaultToleranceMechanism_see_also_uri_FaultToleranceMechanism_id" ON "FaultToleranceMechanism_see_also_uri" ("FaultToleranceMechanism_id");

CREATE TABLE "NaturalLanguage_aliases" (
	"NaturalLanguage_id" TEXT,
	aliases TEXT,
	PRIMARY KEY ("NaturalLanguage_id", aliases),
	FOREIGN KEY("NaturalLanguage_id") REFERENCES "NaturalLanguage" (id)
);
CREATE INDEX "ix_NaturalLanguage_aliases_NaturalLanguage_id" ON "NaturalLanguage_aliases" ("NaturalLanguage_id");
CREATE INDEX "ix_NaturalLanguage_aliases_aliases" ON "NaturalLanguage_aliases" (aliases);

CREATE TABLE "NaturalLanguage_see_also_uri" (
	"NaturalLanguage_id" TEXT,
	see_also_uri TEXT,
	PRIMARY KEY ("NaturalLanguage_id", see_also_uri),
	FOREIGN KEY("NaturalLanguage_id") REFERENCES "NaturalLanguage" (id)
);
CREATE INDEX "ix_NaturalLanguage_see_also_uri_NaturalLanguage_id" ON "NaturalLanguage_see_also_uri" ("NaturalLanguage_id");
CREATE INDEX "ix_NaturalLanguage_see_also_uri_see_also_uri" ON "NaturalLanguage_see_also_uri" (see_also_uri);

CREATE TABLE "RiskItem_mitigation_strategy" (
	"RiskItem_id" TEXT,
	mitigation_strategy TEXT,
	PRIMARY KEY ("RiskItem_id", mitigation_strategy),
	FOREIGN KEY("RiskItem_id") REFERENCES "RiskItem" (id)
);
CREATE INDEX "ix_RiskItem_mitigation_strategy_RiskItem_id" ON "RiskItem_mitigation_strategy" ("RiskItem_id");
CREATE INDEX "ix_RiskItem_mitigation_strategy_mitigation_strategy" ON "RiskItem_mitigation_strategy" (mitigation_strategy);

CREATE TABLE "RiskItem_aliases" (
	"RiskItem_id" TEXT,
	aliases TEXT,
	PRIMARY KEY ("RiskItem_id", aliases),
	FOREIGN KEY("RiskItem_id") REFERENCES "RiskItem" (id)
);
CREATE INDEX "ix_RiskItem_aliases_aliases" ON "RiskItem_aliases" (aliases);
CREATE INDEX "ix_RiskItem_aliases_RiskItem_id" ON "RiskItem_aliases" ("RiskItem_id");

CREATE TABLE "RiskItem_see_also_uri" (
	"RiskItem_id" TEXT,
	see_also_uri TEXT,
	PRIMARY KEY ("RiskItem_id", see_also_uri),
	FOREIGN KEY("RiskItem_id") REFERENCES "RiskItem" (id)
);
CREATE INDEX "ix_RiskItem_see_also_uri_RiskItem_id" ON "RiskItem_see_also_uri" ("RiskItem_id");
CREATE INDEX "ix_RiskItem_see_also_uri_see_also_uri" ON "RiskItem_see_also_uri" (see_also_uri);

CREATE TABLE "OECDLifecycleMapping_aliases" (
	"OECDLifecycleMapping_id" TEXT,
	aliases TEXT,
	PRIMARY KEY ("OECDLifecycleMapping_id", aliases),
	FOREIGN KEY("OECDLifecycleMapping_id") REFERENCES "OECDLifecycleMapping" (id)
);
CREATE INDEX "ix_OECDLifecycleMapping_aliases_OECDLifecycleMapping_id" ON "OECDLifecycleMapping_aliases" ("OECDLifecycleMapping_id");
CREATE INDEX "ix_OECDLifecycleMapping_aliases_aliases" ON "OECDLifecycleMapping_aliases" (aliases);

CREATE TABLE "OECDLifecycleMapping_see_also_uri" (
	"OECDLifecycleMapping_id" TEXT,
	see_also_uri TEXT,
	PRIMARY KEY ("OECDLifecycleMapping_id", see_also_uri),
	FOREIGN KEY("OECDLifecycleMapping_id") REFERENCES "OECDLifecycleMapping" (id)
);
CREATE INDEX "ix_OECDLifecycleMapping_see_also_uri_see_also_uri" ON "OECDLifecycleMapping_see_also_uri" (see_also_uri);
CREATE INDEX "ix_OECDLifecycleMapping_see_also_uri_OECDLifecycleMapping_id" ON "OECDLifecycleMapping_see_also_uri" ("OECDLifecycleMapping_id");

CREATE TABLE "Organization_aliases" (
	"Organization_id" TEXT,
	aliases TEXT,
	PRIMARY KEY ("Organization_id", aliases),
	FOREIGN KEY("Organization_id") REFERENCES "Organization" (id)
);
CREATE INDEX "ix_Organization_aliases_Organization_id" ON "Organization_aliases" ("Organization_id");
CREATE INDEX "ix_Organization_aliases_aliases" ON "Organization_aliases" (aliases);

CREATE TABLE "Organization_see_also_uri" (
	"Organization_id" TEXT,
	see_also_uri TEXT,
	PRIMARY KEY ("Organization_id", see_also_uri),
	FOREIGN KEY("Organization_id") REFERENCES "Organization" (id)
);
CREATE INDEX "ix_Organization_see_also_uri_Organization_id" ON "Organization_see_also_uri" ("Organization_id");
CREATE INDEX "ix_Organization_see_also_uri_see_also_uri" ON "Organization_see_also_uri" (see_also_uri);

CREATE TABLE "InterestedParty_aliases" (
	"InterestedParty_id" TEXT,
	aliases TEXT,
	PRIMARY KEY ("InterestedParty_id", aliases),
	FOREIGN KEY("InterestedParty_id") REFERENCES "InterestedParty" (id)
);
CREATE INDEX "ix_InterestedParty_aliases_InterestedParty_id" ON "InterestedParty_aliases" ("InterestedParty_id");
CREATE INDEX "ix_InterestedParty_aliases_aliases" ON "InterestedParty_aliases" (aliases);

CREATE TABLE "InterestedParty_see_also_uri" (
	"InterestedParty_id" TEXT,
	see_also_uri TEXT,
	PRIMARY KEY ("InterestedParty_id", see_also_uri),
	FOREIGN KEY("InterestedParty_id") REFERENCES "InterestedParty" (id)
);
CREATE INDEX "ix_InterestedParty_see_also_uri_see_also_uri" ON "InterestedParty_see_also_uri" (see_also_uri);
CREATE INDEX "ix_InterestedParty_see_also_uri_InterestedParty_id" ON "InterestedParty_see_also_uri" ("InterestedParty_id");

CREATE TABLE "AISystem" (
	ai_system_type VARCHAR(10),
	symbolic_approach VARCHAR(11),
	autonomy_level VARCHAR(30),
	intended_purpose TEXT,
	lifecycle_stage VARCHAR(27),
	agent_architecture VARCHAR(19),
	iot_integration TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	clause_reference TEXT,
	preferred_label TEXT,
	"AIEcosystem_id" TEXT,
	"AIConceptsCollection_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(iot_integration) REFERENCES "IoTSystem" (id),
	FOREIGN KEY("AIEcosystem_id") REFERENCES "AIEcosystem" (id),
	FOREIGN KEY("AIConceptsCollection_id") REFERENCES "AIConceptsCollection" (id)
);
CREATE INDEX "ix_AISystem_id" ON "AISystem" (id);

CREATE TABLE "IoTDevice" (
	device_role VARCHAR(12) NOT NULL,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	clause_reference TEXT,
	preferred_label TEXT,
	"IoTSystem_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("IoTSystem_id") REFERENCES "IoTSystem" (id)
);
CREATE INDEX "ix_IoTDevice_id" ON "IoTDevice" (id);

CREATE TABLE "CyberPhysicalSystem" (
	iot_subsystem TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	clause_reference TEXT,
	preferred_label TEXT,
	"AIConceptsCollection_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(iot_subsystem) REFERENCES "IoTSystem" (id),
	FOREIGN KEY("AIConceptsCollection_id") REFERENCES "AIConceptsCollection" (id)
);
CREATE INDEX "ix_CyberPhysicalSystem_id" ON "CyberPhysicalSystem" (id);

CREATE TABLE "AILifecycleProcess_process_inputs" (
	"AILifecycleProcess_id" TEXT,
	process_inputs TEXT,
	PRIMARY KEY ("AILifecycleProcess_id", process_inputs),
	FOREIGN KEY("AILifecycleProcess_id") REFERENCES "AILifecycleProcess" (id)
);
CREATE INDEX "ix_AILifecycleProcess_process_inputs_AILifecycleProcess_id" ON "AILifecycleProcess_process_inputs" ("AILifecycleProcess_id");
CREATE INDEX "ix_AILifecycleProcess_process_inputs_process_inputs" ON "AILifecycleProcess_process_inputs" (process_inputs);

CREATE TABLE "AILifecycleProcess_process_outputs" (
	"AILifecycleProcess_id" TEXT,
	process_outputs TEXT,
	PRIMARY KEY ("AILifecycleProcess_id", process_outputs),
	FOREIGN KEY("AILifecycleProcess_id") REFERENCES "AILifecycleProcess" (id)
);
CREATE INDEX "ix_AILifecycleProcess_process_outputs_AILifecycleProcess_id" ON "AILifecycleProcess_process_outputs" ("AILifecycleProcess_id");
CREATE INDEX "ix_AILifecycleProcess_process_outputs_process_outputs" ON "AILifecycleProcess_process_outputs" (process_outputs);

CREATE TABLE "AILifecycleProcess_risk_items" (
	"AILifecycleProcess_id" TEXT,
	risk_items TEXT,
	PRIMARY KEY ("AILifecycleProcess_id", risk_items),
	FOREIGN KEY("AILifecycleProcess_id") REFERENCES "AILifecycleProcess" (id)
);
CREATE INDEX "ix_AILifecycleProcess_risk_items_risk_items" ON "AILifecycleProcess_risk_items" (risk_items);
CREATE INDEX "ix_AILifecycleProcess_risk_items_AILifecycleProcess_id" ON "AILifecycleProcess_risk_items" ("AILifecycleProcess_id");

CREATE TABLE "AILifecycleProcess_approval_criteria" (
	"AILifecycleProcess_id" TEXT,
	approval_criteria TEXT,
	PRIMARY KEY ("AILifecycleProcess_id", approval_criteria),
	FOREIGN KEY("AILifecycleProcess_id") REFERENCES "AILifecycleProcess" (id)
);
CREATE INDEX "ix_AILifecycleProcess_approval_criteria_approval_criteria" ON "AILifecycleProcess_approval_criteria" (approval_criteria);
CREATE INDEX "ix_AILifecycleProcess_approval_criteria_AILifecycleProcess_id" ON "AILifecycleProcess_approval_criteria" ("AILifecycleProcess_id");

CREATE TABLE "AILifecycleProcess_aliases" (
	"AILifecycleProcess_id" TEXT,
	aliases TEXT,
	PRIMARY KEY ("AILifecycleProcess_id", aliases),
	FOREIGN KEY("AILifecycleProcess_id") REFERENCES "AILifecycleProcess" (id)
);
CREATE INDEX "ix_AILifecycleProcess_aliases_AILifecycleProcess_id" ON "AILifecycleProcess_aliases" ("AILifecycleProcess_id");
CREATE INDEX "ix_AILifecycleProcess_aliases_aliases" ON "AILifecycleProcess_aliases" (aliases);

CREATE TABLE "AILifecycleProcess_see_also_uri" (
	"AILifecycleProcess_id" TEXT,
	see_also_uri TEXT,
	PRIMARY KEY ("AILifecycleProcess_id", see_also_uri),
	FOREIGN KEY("AILifecycleProcess_id") REFERENCES "AILifecycleProcess" (id)
);
CREATE INDEX "ix_AILifecycleProcess_see_also_uri_AILifecycleProcess_id" ON "AILifecycleProcess_see_also_uri" ("AILifecycleProcess_id");
CREATE INDEX "ix_AILifecycleProcess_see_also_uri_see_also_uri" ON "AILifecycleProcess_see_also_uri" (see_also_uri);

CREATE TABLE "Task_input_modalities" (
	"Task_id" TEXT,
	input_modalities VARCHAR(15),
	PRIMARY KEY ("Task_id", input_modalities),
	FOREIGN KEY("Task_id") REFERENCES "Task" (id)
);
CREATE INDEX "ix_Task_input_modalities_input_modalities" ON "Task_input_modalities" (input_modalities);
CREATE INDEX "ix_Task_input_modalities_Task_id" ON "Task_input_modalities" ("Task_id");

CREATE TABLE "Task_performance_metric" (
	"Task_id" TEXT,
	performance_metric TEXT,
	PRIMARY KEY ("Task_id", performance_metric),
	FOREIGN KEY("Task_id") REFERENCES "Task" (id)
);
CREATE INDEX "ix_Task_performance_metric_performance_metric" ON "Task_performance_metric" (performance_metric);
CREATE INDEX "ix_Task_performance_metric_Task_id" ON "Task_performance_metric" ("Task_id");

CREATE TABLE "Task_aliases" (
	"Task_id" TEXT,
	aliases TEXT,
	PRIMARY KEY ("Task_id", aliases),
	FOREIGN KEY("Task_id") REFERENCES "Task" (id)
);
CREATE INDEX "ix_Task_aliases_aliases" ON "Task_aliases" (aliases);
CREATE INDEX "ix_Task_aliases_Task_id" ON "Task_aliases" ("Task_id");

CREATE TABLE "Task_see_also_uri" (
	"Task_id" TEXT,
	see_also_uri TEXT,
	PRIMARY KEY ("Task_id", see_also_uri),
	FOREIGN KEY("Task_id") REFERENCES "Task" (id)
);
CREATE INDEX "ix_Task_see_also_uri_Task_id" ON "Task_see_also_uri" ("Task_id");
CREATE INDEX "ix_Task_see_also_uri_see_also_uri" ON "Task_see_also_uri" (see_also_uri);

CREATE TABLE "Action_aliases" (
	"Action_id" TEXT,
	aliases TEXT,
	PRIMARY KEY ("Action_id", aliases),
	FOREIGN KEY("Action_id") REFERENCES "Action" (id)
);
CREATE INDEX "ix_Action_aliases_Action_id" ON "Action_aliases" ("Action_id");
CREATE INDEX "ix_Action_aliases_aliases" ON "Action_aliases" (aliases);

CREATE TABLE "Action_see_also_uri" (
	"Action_id" TEXT,
	see_also_uri TEXT,
	PRIMARY KEY ("Action_id", see_also_uri),
	FOREIGN KEY("Action_id") REFERENCES "Action" (id)
);
CREATE INDEX "ix_Action_see_also_uri_Action_id" ON "Action_see_also_uri" ("Action_id");
CREATE INDEX "ix_Action_see_also_uri_see_also_uri" ON "Action_see_also_uri" (see_also_uri);

CREATE TABLE "KnowledgeGraph_ontology_reference" (
	"KnowledgeGraph_id" TEXT,
	ontology_reference TEXT,
	PRIMARY KEY ("KnowledgeGraph_id", ontology_reference),
	FOREIGN KEY("KnowledgeGraph_id") REFERENCES "KnowledgeGraph" (id)
);
CREATE INDEX "ix_KnowledgeGraph_ontology_reference_KnowledgeGraph_id" ON "KnowledgeGraph_ontology_reference" ("KnowledgeGraph_id");
CREATE INDEX "ix_KnowledgeGraph_ontology_reference_ontology_reference" ON "KnowledgeGraph_ontology_reference" (ontology_reference);

CREATE TABLE "KnowledgeGraph_aliases" (
	"KnowledgeGraph_id" TEXT,
	aliases TEXT,
	PRIMARY KEY ("KnowledgeGraph_id", aliases),
	FOREIGN KEY("KnowledgeGraph_id") REFERENCES "KnowledgeGraph" (id)
);
CREATE INDEX "ix_KnowledgeGraph_aliases_KnowledgeGraph_id" ON "KnowledgeGraph_aliases" ("KnowledgeGraph_id");
CREATE INDEX "ix_KnowledgeGraph_aliases_aliases" ON "KnowledgeGraph_aliases" (aliases);

CREATE TABLE "KnowledgeGraph_see_also_uri" (
	"KnowledgeGraph_id" TEXT,
	see_also_uri TEXT,
	PRIMARY KEY ("KnowledgeGraph_id", see_also_uri),
	FOREIGN KEY("KnowledgeGraph_id") REFERENCES "KnowledgeGraph" (id)
);
CREATE INDEX "ix_KnowledgeGraph_see_also_uri_KnowledgeGraph_id" ON "KnowledgeGraph_see_also_uri" ("KnowledgeGraph_id");
CREATE INDEX "ix_KnowledgeGraph_see_also_uri_see_also_uri" ON "KnowledgeGraph_see_also_uri" (see_also_uri);

CREATE TABLE "IoTSystem_aliases" (
	"IoTSystem_id" TEXT,
	aliases TEXT,
	PRIMARY KEY ("IoTSystem_id", aliases),
	FOREIGN KEY("IoTSystem_id") REFERENCES "IoTSystem" (id)
);
CREATE INDEX "ix_IoTSystem_aliases_aliases" ON "IoTSystem_aliases" (aliases);
CREATE INDEX "ix_IoTSystem_aliases_IoTSystem_id" ON "IoTSystem_aliases" ("IoTSystem_id");

CREATE TABLE "IoTSystem_see_also_uri" (
	"IoTSystem_id" TEXT,
	see_also_uri TEXT,
	PRIMARY KEY ("IoTSystem_id", see_also_uri),
	FOREIGN KEY("IoTSystem_id") REFERENCES "IoTSystem" (id)
);
CREATE INDEX "ix_IoTSystem_see_also_uri_IoTSystem_id" ON "IoTSystem_see_also_uri" ("IoTSystem_id");
CREATE INDEX "ix_IoTSystem_see_also_uri_see_also_uri" ON "IoTSystem_see_also_uri" (see_also_uri);

CREATE TABLE "AbbreviationEntry_aliases" (
	"AbbreviationEntry_id" TEXT,
	aliases TEXT,
	PRIMARY KEY ("AbbreviationEntry_id", aliases),
	FOREIGN KEY("AbbreviationEntry_id") REFERENCES "AbbreviationEntry" (id)
);
CREATE INDEX "ix_AbbreviationEntry_aliases_aliases" ON "AbbreviationEntry_aliases" (aliases);
CREATE INDEX "ix_AbbreviationEntry_aliases_AbbreviationEntry_id" ON "AbbreviationEntry_aliases" ("AbbreviationEntry_id");

CREATE TABLE "AbbreviationEntry_see_also_uri" (
	"AbbreviationEntry_id" TEXT,
	see_also_uri TEXT,
	PRIMARY KEY ("AbbreviationEntry_id", see_also_uri),
	FOREIGN KEY("AbbreviationEntry_id") REFERENCES "AbbreviationEntry" (id)
);
CREATE INDEX "ix_AbbreviationEntry_see_also_uri_AbbreviationEntry_id" ON "AbbreviationEntry_see_also_uri" ("AbbreviationEntry_id");
CREATE INDEX "ix_AbbreviationEntry_see_also_uri_see_also_uri" ON "AbbreviationEntry_see_also_uri" (see_also_uri);

CREATE TABLE "AIComponent" (
	component_function VARCHAR(22),
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	clause_reference TEXT,
	preferred_label TEXT,
	"AISystem_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("AISystem_id") REFERENCES "AISystem" (id)
);
CREATE INDEX "ix_AIComponent_id" ON "AIComponent" (id);

CREATE TABLE "Dataset" (
	dataset_role VARCHAR(10),
	data_provenance TEXT,
	record_count INTEGER,
	data_quality_notes TEXT,
	contains_personal_data BOOLEAN,
	label_type VARCHAR(11),
	ground_truth_available BOOLEAN,
	feature_count INTEGER,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	clause_reference TEXT,
	preferred_label TEXT,
	"AISystem_id" TEXT,
	"AIConceptsCollection_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("AISystem_id") REFERENCES "AISystem" (id),
	FOREIGN KEY("AIConceptsCollection_id") REFERENCES "AIConceptsCollection" (id)
);
CREATE INDEX "ix_Dataset_id" ON "Dataset" (id);

CREATE TABLE "TrustworthinessProperty" (
	trustworthiness_property_type VARCHAR(15) NOT NULL,
	measurement_method TEXT,
	confidence_score FLOAT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	clause_reference TEXT,
	preferred_label TEXT,
	"AISystem_id" TEXT,
	"AIConceptsCollection_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("AISystem_id") REFERENCES "AISystem" (id),
	FOREIGN KEY("AIConceptsCollection_id") REFERENCES "AIConceptsCollection" (id)
);
CREATE INDEX "ix_TrustworthinessProperty_id" ON "TrustworthinessProperty" (id);

CREATE TABLE "AIStakeholderRole" (
	stakeholder_role_type VARCHAR(18) NOT NULL,
	organization_name TEXT,
	contact TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	clause_reference TEXT,
	preferred_label TEXT,
	"AISystem_id" TEXT,
	"AIEcosystem_id" TEXT,
	"AIConceptsCollection_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("AISystem_id") REFERENCES "AISystem" (id),
	FOREIGN KEY("AIEcosystem_id") REFERENCES "AIEcosystem" (id),
	FOREIGN KEY("AIConceptsCollection_id") REFERENCES "AIConceptsCollection" (id)
);
CREATE INDEX "ix_AIStakeholderRole_id" ON "AIStakeholderRole" (id);

CREATE TABLE "AIApplication" (
	intended_purpose TEXT,
	hosting_system TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	clause_reference TEXT,
	preferred_label TEXT,
	"AIConceptsCollection_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(hosting_system) REFERENCES "AISystem" (id),
	FOREIGN KEY("AIConceptsCollection_id") REFERENCES "AIConceptsCollection" (id)
);
CREATE INDEX "ix_AIApplication_id" ON "AIApplication" (id);

CREATE TABLE "Robot" (
	embodiment TEXT,
	controlled_by TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	clause_reference TEXT,
	preferred_label TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(controlled_by) REFERENCES "AISystem" (id)
);
CREATE INDEX "ix_Robot_id" ON "Robot" (id);

CREATE TABLE "InputData" (
	data_source_type VARCHAR(13),
	data_collection_method VARCHAR(19),
	modality VARCHAR(15),
	consumed_by TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	clause_reference TEXT,
	preferred_label TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(consumed_by) REFERENCES "AISystem" (id)
);
CREATE INDEX "ix_InputData_id" ON "InputData" (id);

CREATE TABLE "AISystem_application_domain" (
	"AISystem_id" TEXT,
	application_domain VARCHAR(23),
	PRIMARY KEY ("AISystem_id", application_domain),
	FOREIGN KEY("AISystem_id") REFERENCES "AISystem" (id)
);
CREATE INDEX "ix_AISystem_application_domain_AISystem_id" ON "AISystem_application_domain" ("AISystem_id");
CREATE INDEX "ix_AISystem_application_domain_application_domain" ON "AISystem_application_domain" (application_domain);

CREATE TABLE "AISystem_ai_field" (
	"AISystem_id" TEXT,
	ai_field VARCHAR(38),
	PRIMARY KEY ("AISystem_id", ai_field),
	FOREIGN KEY("AISystem_id") REFERENCES "AISystem" (id)
);
CREATE INDEX "ix_AISystem_ai_field_ai_field" ON "AISystem_ai_field" (ai_field);
CREATE INDEX "ix_AISystem_ai_field_AISystem_id" ON "AISystem_ai_field" ("AISystem_id");

CREATE TABLE "AISystem_functional_components" (
	"AISystem_id" TEXT,
	functional_components VARCHAR(22),
	PRIMARY KEY ("AISystem_id", functional_components),
	FOREIGN KEY("AISystem_id") REFERENCES "AISystem" (id)
);
CREATE INDEX "ix_AISystem_functional_components_functional_components" ON "AISystem_functional_components" (functional_components);
CREATE INDEX "ix_AISystem_functional_components_AISystem_id" ON "AISystem_functional_components" ("AISystem_id");

CREATE TABLE "AISystem_jurisdictional_issues" (
	"AISystem_id" TEXT,
	jurisdictional_issues VARCHAR(21),
	PRIMARY KEY ("AISystem_id", jurisdictional_issues),
	FOREIGN KEY("AISystem_id") REFERENCES "AISystem" (id)
);
CREATE INDEX "ix_AISystem_jurisdictional_issues_AISystem_id" ON "AISystem_jurisdictional_issues" ("AISystem_id");
CREATE INDEX "ix_AISystem_jurisdictional_issues_jurisdictional_issues" ON "AISystem_jurisdictional_issues" (jurisdictional_issues);

CREATE TABLE "AISystem_societal_impacts" (
	"AISystem_id" TEXT,
	societal_impacts VARCHAR(20),
	PRIMARY KEY ("AISystem_id", societal_impacts),
	FOREIGN KEY("AISystem_id") REFERENCES "AISystem" (id)
);
CREATE INDEX "ix_AISystem_societal_impacts_AISystem_id" ON "AISystem_societal_impacts" ("AISystem_id");
CREATE INDEX "ix_AISystem_societal_impacts_societal_impacts" ON "AISystem_societal_impacts" (societal_impacts);

CREATE TABLE "AISystem_system_characteristics" (
	"AISystem_id" TEXT,
	system_characteristics VARCHAR(17),
	PRIMARY KEY ("AISystem_id", system_characteristics),
	FOREIGN KEY("AISystem_id") REFERENCES "AISystem" (id)
);
CREATE INDEX "ix_AISystem_system_characteristics_AISystem_id" ON "AISystem_system_characteristics" ("AISystem_id");
CREATE INDEX "ix_AISystem_system_characteristics_system_characteristics" ON "AISystem_system_characteristics" (system_characteristics);

CREATE TABLE "AISystem_task_categories" (
	"AISystem_id" TEXT,
	task_categories VARCHAR(24),
	PRIMARY KEY ("AISystem_id", task_categories),
	FOREIGN KEY("AISystem_id") REFERENCES "AISystem" (id)
);
CREATE INDEX "ix_AISystem_task_categories_AISystem_id" ON "AISystem_task_categories" ("AISystem_id");
CREATE INDEX "ix_AISystem_task_categories_task_categories" ON "AISystem_task_categories" (task_categories);

CREATE TABLE "AISystem_aliases" (
	"AISystem_id" TEXT,
	aliases TEXT,
	PRIMARY KEY ("AISystem_id", aliases),
	FOREIGN KEY("AISystem_id") REFERENCES "AISystem" (id)
);
CREATE INDEX "ix_AISystem_aliases_AISystem_id" ON "AISystem_aliases" ("AISystem_id");
CREATE INDEX "ix_AISystem_aliases_aliases" ON "AISystem_aliases" (aliases);

CREATE TABLE "AISystem_see_also_uri" (
	"AISystem_id" TEXT,
	see_also_uri TEXT,
	PRIMARY KEY ("AISystem_id", see_also_uri),
	FOREIGN KEY("AISystem_id") REFERENCES "AISystem" (id)
);
CREATE INDEX "ix_AISystem_see_also_uri_AISystem_id" ON "AISystem_see_also_uri" ("AISystem_id");
CREATE INDEX "ix_AISystem_see_also_uri_see_also_uri" ON "AISystem_see_also_uri" (see_also_uri);

CREATE TABLE "IoTDevice_sensing_capabilities" (
	"IoTDevice_id" TEXT,
	sensing_capabilities TEXT,
	PRIMARY KEY ("IoTDevice_id", sensing_capabilities),
	FOREIGN KEY("IoTDevice_id") REFERENCES "IoTDevice" (id)
);
CREATE INDEX "ix_IoTDevice_sensing_capabilities_IoTDevice_id" ON "IoTDevice_sensing_capabilities" ("IoTDevice_id");
CREATE INDEX "ix_IoTDevice_sensing_capabilities_sensing_capabilities" ON "IoTDevice_sensing_capabilities" (sensing_capabilities);

CREATE TABLE "IoTDevice_actuating_capabilities" (
	"IoTDevice_id" TEXT,
	actuating_capabilities TEXT,
	PRIMARY KEY ("IoTDevice_id", actuating_capabilities),
	FOREIGN KEY("IoTDevice_id") REFERENCES "IoTDevice" (id)
);
CREATE INDEX "ix_IoTDevice_actuating_capabilities_IoTDevice_id" ON "IoTDevice_actuating_capabilities" ("IoTDevice_id");
CREATE INDEX "ix_IoTDevice_actuating_capabilities_actuating_capabilities" ON "IoTDevice_actuating_capabilities" (actuating_capabilities);

CREATE TABLE "IoTDevice_aliases" (
	"IoTDevice_id" TEXT,
	aliases TEXT,
	PRIMARY KEY ("IoTDevice_id", aliases),
	FOREIGN KEY("IoTDevice_id") REFERENCES "IoTDevice" (id)
);
CREATE INDEX "ix_IoTDevice_aliases_IoTDevice_id" ON "IoTDevice_aliases" ("IoTDevice_id");
CREATE INDEX "ix_IoTDevice_aliases_aliases" ON "IoTDevice_aliases" (aliases);

CREATE TABLE "IoTDevice_see_also_uri" (
	"IoTDevice_id" TEXT,
	see_also_uri TEXT,
	PRIMARY KEY ("IoTDevice_id", see_also_uri),
	FOREIGN KEY("IoTDevice_id") REFERENCES "IoTDevice" (id)
);
CREATE INDEX "ix_IoTDevice_see_also_uri_see_also_uri" ON "IoTDevice_see_also_uri" (see_also_uri);
CREATE INDEX "ix_IoTDevice_see_also_uri_IoTDevice_id" ON "IoTDevice_see_also_uri" ("IoTDevice_id");

CREATE TABLE "CyberPhysicalSystem_physical_processes" (
	"CyberPhysicalSystem_id" TEXT,
	physical_processes TEXT,
	PRIMARY KEY ("CyberPhysicalSystem_id", physical_processes),
	FOREIGN KEY("CyberPhysicalSystem_id") REFERENCES "CyberPhysicalSystem" (id)
);
CREATE INDEX "ix_CyberPhysicalSystem_physical_processes_physical_processes" ON "CyberPhysicalSystem_physical_processes" (physical_processes);
CREATE INDEX "ix_CyberPhysicalSystem_physical_processes_CyberPhysicalSystem_id" ON "CyberPhysicalSystem_physical_processes" ("CyberPhysicalSystem_id");

CREATE TABLE "CyberPhysicalSystem_aliases" (
	"CyberPhysicalSystem_id" TEXT,
	aliases TEXT,
	PRIMARY KEY ("CyberPhysicalSystem_id", aliases),
	FOREIGN KEY("CyberPhysicalSystem_id") REFERENCES "CyberPhysicalSystem" (id)
);
CREATE INDEX "ix_CyberPhysicalSystem_aliases_aliases" ON "CyberPhysicalSystem_aliases" (aliases);
CREATE INDEX "ix_CyberPhysicalSystem_aliases_CyberPhysicalSystem_id" ON "CyberPhysicalSystem_aliases" ("CyberPhysicalSystem_id");

CREATE TABLE "CyberPhysicalSystem_see_also_uri" (
	"CyberPhysicalSystem_id" TEXT,
	see_also_uri TEXT,
	PRIMARY KEY ("CyberPhysicalSystem_id", see_also_uri),
	FOREIGN KEY("CyberPhysicalSystem_id") REFERENCES "CyberPhysicalSystem" (id)
);
CREATE INDEX "ix_CyberPhysicalSystem_see_also_uri_CyberPhysicalSystem_id" ON "CyberPhysicalSystem_see_also_uri" ("CyberPhysicalSystem_id");
CREATE INDEX "ix_CyberPhysicalSystem_see_also_uri_see_also_uri" ON "CyberPhysicalSystem_see_also_uri" (see_also_uri);

CREATE TABLE "HumanMachineTeam_ai_systems_involved" (
	"HumanMachineTeam_id" TEXT,
	ai_systems_involved_id TEXT,
	PRIMARY KEY ("HumanMachineTeam_id", ai_systems_involved_id),
	FOREIGN KEY("HumanMachineTeam_id") REFERENCES "HumanMachineTeam" (id),
	FOREIGN KEY(ai_systems_involved_id) REFERENCES "AISystem" (id)
);
CREATE INDEX "ix_HumanMachineTeam_ai_systems_involved_ai_systems_involved_id" ON "HumanMachineTeam_ai_systems_involved" (ai_systems_involved_id);
CREATE INDEX "ix_HumanMachineTeam_ai_systems_involved_HumanMachineTeam_id" ON "HumanMachineTeam_ai_systems_involved" ("HumanMachineTeam_id");

CREATE TABLE "AIModel" (
	model_paradigm VARCHAR(15),
	algorithm_family VARCHAR(22),
	engineering_approach VARCHAR(23),
	training_dataset TEXT,
	validation_dataset TEXT,
	test_dataset TEXT,
	model_version TEXT,
	trained_on TEXT,
	supports_continuous_learning BOOLEAN,
	catastrophic_forgetting_risk FLOAT,
	parameter_count INTEGER,
	training_duration TEXT,
	inference_latency_ms FLOAT,
	model_compression_applied BOOLEAN,
	neural_network_architecture VARCHAR(22),
	activation_function VARCHAR(10),
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	clause_reference TEXT,
	preferred_label TEXT,
	"AISystem_id" TEXT,
	"AIConceptsCollection_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(training_dataset) REFERENCES "Dataset" (id),
	FOREIGN KEY(validation_dataset) REFERENCES "Dataset" (id),
	FOREIGN KEY(test_dataset) REFERENCES "Dataset" (id),
	FOREIGN KEY("AISystem_id") REFERENCES "AISystem" (id),
	FOREIGN KEY("AIConceptsCollection_id") REFERENCES "AIConceptsCollection" (id)
);
CREATE INDEX "ix_AIModel_id" ON "AIModel" (id);

CREATE TABLE "NeuralNetworkModel" (
	number_of_layers INTEGER,
	number_of_parameters INTEGER,
	model_paradigm VARCHAR(15),
	algorithm_family VARCHAR(22),
	engineering_approach VARCHAR(23),
	training_dataset TEXT,
	validation_dataset TEXT,
	test_dataset TEXT,
	model_version TEXT,
	trained_on TEXT,
	supports_continuous_learning BOOLEAN,
	catastrophic_forgetting_risk FLOAT,
	parameter_count INTEGER,
	training_duration TEXT,
	inference_latency_ms FLOAT,
	model_compression_applied BOOLEAN,
	neural_network_architecture VARCHAR(22),
	activation_function VARCHAR(10),
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	clause_reference TEXT,
	preferred_label TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(training_dataset) REFERENCES "Dataset" (id),
	FOREIGN KEY(validation_dataset) REFERENCES "Dataset" (id),
	FOREIGN KEY(test_dataset) REFERENCES "Dataset" (id)
);
CREATE INDEX "ix_NeuralNetworkModel_id" ON "NeuralNetworkModel" (id);

CREATE TABLE "DataProcess" (
	process_type VARCHAR(34) NOT NULL,
	input_dataset TEXT,
	output_dataset TEXT,
	executed_by TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	clause_reference TEXT,
	preferred_label TEXT,
	"AISystem_id" TEXT,
	"Dataset_id" TEXT,
	"AIConceptsCollection_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(input_dataset) REFERENCES "Dataset" (id),
	FOREIGN KEY(output_dataset) REFERENCES "Dataset" (id),
	FOREIGN KEY(executed_by) REFERENCES "AIStakeholderRole" (id),
	FOREIGN KEY("AISystem_id") REFERENCES "AISystem" (id),
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id),
	FOREIGN KEY("AIConceptsCollection_id") REFERENCES "AIConceptsCollection" (id)
);
CREATE INDEX "ix_DataProcess_id" ON "DataProcess" (id);

CREATE TABLE "DataLabel" (
	label_value TEXT NOT NULL,
	label_type VARCHAR(11),
	annotator TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	clause_reference TEXT,
	preferred_label TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(annotator) REFERENCES "AIStakeholderRole" (id)
);
CREATE INDEX "ix_DataLabel_id" ON "DataLabel" (id);

CREATE TABLE "EvaluationMetric" (
	metric_name TEXT NOT NULL,
	metric_value FLOAT,
	metric_unit TEXT,
	reference_dataset TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	clause_reference TEXT,
	preferred_label TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(reference_dataset) REFERENCES "Dataset" (id)
);
CREATE INDEX "ix_EvaluationMetric_id" ON "EvaluationMetric" (id);

CREATE TABLE "DataDrift" (
	drift_type TEXT,
	detected_at TEXT,
	affected_dataset TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	clause_reference TEXT,
	preferred_label TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(affected_dataset) REFERENCES "Dataset" (id)
);
CREATE INDEX "ix_DataDrift_id" ON "DataDrift" (id);

CREATE TABLE "AIComponent_depends_on" (
	"AIComponent_id" TEXT,
	depends_on_id TEXT,
	PRIMARY KEY ("AIComponent_id", depends_on_id),
	FOREIGN KEY("AIComponent_id") REFERENCES "AIComponent" (id),
	FOREIGN KEY(depends_on_id) REFERENCES "AIComponent" (id)
);
CREATE INDEX "ix_AIComponent_depends_on_depends_on_id" ON "AIComponent_depends_on" (depends_on_id);
CREATE INDEX "ix_AIComponent_depends_on_AIComponent_id" ON "AIComponent_depends_on" ("AIComponent_id");

CREATE TABLE "AIComponent_aliases" (
	"AIComponent_id" TEXT,
	aliases TEXT,
	PRIMARY KEY ("AIComponent_id", aliases),
	FOREIGN KEY("AIComponent_id") REFERENCES "AIComponent" (id)
);
CREATE INDEX "ix_AIComponent_aliases_AIComponent_id" ON "AIComponent_aliases" ("AIComponent_id");
CREATE INDEX "ix_AIComponent_aliases_aliases" ON "AIComponent_aliases" (aliases);

CREATE TABLE "AIComponent_see_also_uri" (
	"AIComponent_id" TEXT,
	see_also_uri TEXT,
	PRIMARY KEY ("AIComponent_id", see_also_uri),
	FOREIGN KEY("AIComponent_id") REFERENCES "AIComponent" (id)
);
CREATE INDEX "ix_AIComponent_see_also_uri_AIComponent_id" ON "AIComponent_see_also_uri" ("AIComponent_id");
CREATE INDEX "ix_AIComponent_see_also_uri_see_also_uri" ON "AIComponent_see_also_uri" (see_also_uri);

CREATE TABLE "Dataset_data_modality" (
	"Dataset_id" TEXT,
	data_modality VARCHAR(15),
	PRIMARY KEY ("Dataset_id", data_modality),
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id)
);
CREATE INDEX "ix_Dataset_data_modality_Dataset_id" ON "Dataset_data_modality" ("Dataset_id");
CREATE INDEX "ix_Dataset_data_modality_data_modality" ON "Dataset_data_modality" (data_modality);

CREATE TABLE "Dataset_aliases" (
	"Dataset_id" TEXT,
	aliases TEXT,
	PRIMARY KEY ("Dataset_id", aliases),
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id)
);
CREATE INDEX "ix_Dataset_aliases_Dataset_id" ON "Dataset_aliases" ("Dataset_id");
CREATE INDEX "ix_Dataset_aliases_aliases" ON "Dataset_aliases" (aliases);

CREATE TABLE "Dataset_see_also_uri" (
	"Dataset_id" TEXT,
	see_also_uri TEXT,
	PRIMARY KEY ("Dataset_id", see_also_uri),
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id)
);
CREATE INDEX "ix_Dataset_see_also_uri_see_also_uri" ON "Dataset_see_also_uri" (see_also_uri);
CREATE INDEX "ix_Dataset_see_also_uri_Dataset_id" ON "Dataset_see_also_uri" ("Dataset_id");

CREATE TABLE "TrustworthinessProperty_property_evidence" (
	"TrustworthinessProperty_id" TEXT,
	property_evidence TEXT,
	PRIMARY KEY ("TrustworthinessProperty_id", property_evidence),
	FOREIGN KEY("TrustworthinessProperty_id") REFERENCES "TrustworthinessProperty" (id)
);
CREATE INDEX "ix_TrustworthinessProperty_property_evidence_TrustworthinessProperty_id" ON "TrustworthinessProperty_property_evidence" ("TrustworthinessProperty_id");
CREATE INDEX "ix_TrustworthinessProperty_property_evidence_property_evidence" ON "TrustworthinessProperty_property_evidence" (property_evidence);

CREATE TABLE "TrustworthinessProperty_applicable_biases" (
	"TrustworthinessProperty_id" TEXT,
	applicable_biases VARCHAR(16),
	PRIMARY KEY ("TrustworthinessProperty_id", applicable_biases),
	FOREIGN KEY("TrustworthinessProperty_id") REFERENCES "TrustworthinessProperty" (id)
);
CREATE INDEX "ix_TrustworthinessProperty_applicable_biases_applicable_biases" ON "TrustworthinessProperty_applicable_biases" (applicable_biases);
CREATE INDEX "ix_TrustworthinessProperty_applicable_biases_TrustworthinessProperty_id" ON "TrustworthinessProperty_applicable_biases" ("TrustworthinessProperty_id");

CREATE TABLE "TrustworthinessProperty_aliases" (
	"TrustworthinessProperty_id" TEXT,
	aliases TEXT,
	PRIMARY KEY ("TrustworthinessProperty_id", aliases),
	FOREIGN KEY("TrustworthinessProperty_id") REFERENCES "TrustworthinessProperty" (id)
);
CREATE INDEX "ix_TrustworthinessProperty_aliases_TrustworthinessProperty_id" ON "TrustworthinessProperty_aliases" ("TrustworthinessProperty_id");
CREATE INDEX "ix_TrustworthinessProperty_aliases_aliases" ON "TrustworthinessProperty_aliases" (aliases);

CREATE TABLE "TrustworthinessProperty_see_also_uri" (
	"TrustworthinessProperty_id" TEXT,
	see_also_uri TEXT,
	PRIMARY KEY ("TrustworthinessProperty_id", see_also_uri),
	FOREIGN KEY("TrustworthinessProperty_id") REFERENCES "TrustworthinessProperty" (id)
);
CREATE INDEX "ix_TrustworthinessProperty_see_also_uri_see_also_uri" ON "TrustworthinessProperty_see_also_uri" (see_also_uri);
CREATE INDEX "ix_TrustworthinessProperty_see_also_uri_TrustworthinessProperty_id" ON "TrustworthinessProperty_see_also_uri" ("TrustworthinessProperty_id");

CREATE TABLE "AIStakeholderRole_responsibilities" (
	"AIStakeholderRole_id" TEXT,
	responsibilities TEXT,
	PRIMARY KEY ("AIStakeholderRole_id", responsibilities),
	FOREIGN KEY("AIStakeholderRole_id") REFERENCES "AIStakeholderRole" (id)
);
CREATE INDEX "ix_AIStakeholderRole_responsibilities_AIStakeholderRole_id" ON "AIStakeholderRole_responsibilities" ("AIStakeholderRole_id");
CREATE INDEX "ix_AIStakeholderRole_responsibilities_responsibilities" ON "AIStakeholderRole_responsibilities" (responsibilities);

CREATE TABLE "AIStakeholderRole_aliases" (
	"AIStakeholderRole_id" TEXT,
	aliases TEXT,
	PRIMARY KEY ("AIStakeholderRole_id", aliases),
	FOREIGN KEY("AIStakeholderRole_id") REFERENCES "AIStakeholderRole" (id)
);
CREATE INDEX "ix_AIStakeholderRole_aliases_aliases" ON "AIStakeholderRole_aliases" (aliases);
CREATE INDEX "ix_AIStakeholderRole_aliases_AIStakeholderRole_id" ON "AIStakeholderRole_aliases" ("AIStakeholderRole_id");

CREATE TABLE "AIStakeholderRole_see_also_uri" (
	"AIStakeholderRole_id" TEXT,
	see_also_uri TEXT,
	PRIMARY KEY ("AIStakeholderRole_id", see_also_uri),
	FOREIGN KEY("AIStakeholderRole_id") REFERENCES "AIStakeholderRole" (id)
);
CREATE INDEX "ix_AIStakeholderRole_see_also_uri_see_also_uri" ON "AIStakeholderRole_see_also_uri" (see_also_uri);
CREATE INDEX "ix_AIStakeholderRole_see_also_uri_AIStakeholderRole_id" ON "AIStakeholderRole_see_also_uri" ("AIStakeholderRole_id");

CREATE TABLE "AIApplication_application_domain" (
	"AIApplication_id" TEXT,
	application_domain VARCHAR(23),
	PRIMARY KEY ("AIApplication_id", application_domain),
	FOREIGN KEY("AIApplication_id") REFERENCES "AIApplication" (id)
);
CREATE INDEX "ix_AIApplication_application_domain_AIApplication_id" ON "AIApplication_application_domain" ("AIApplication_id");
CREATE INDEX "ix_AIApplication_application_domain_application_domain" ON "AIApplication_application_domain" (application_domain);

CREATE TABLE "AIApplication_jurisdictional_issues" (
	"AIApplication_id" TEXT,
	jurisdictional_issues VARCHAR(21),
	PRIMARY KEY ("AIApplication_id", jurisdictional_issues),
	FOREIGN KEY("AIApplication_id") REFERENCES "AIApplication" (id)
);
CREATE INDEX "ix_AIApplication_jurisdictional_issues_jurisdictional_issues" ON "AIApplication_jurisdictional_issues" (jurisdictional_issues);
CREATE INDEX "ix_AIApplication_jurisdictional_issues_AIApplication_id" ON "AIApplication_jurisdictional_issues" ("AIApplication_id");

CREATE TABLE "AIApplication_societal_impacts" (
	"AIApplication_id" TEXT,
	societal_impacts VARCHAR(20),
	PRIMARY KEY ("AIApplication_id", societal_impacts),
	FOREIGN KEY("AIApplication_id") REFERENCES "AIApplication" (id)
);
CREATE INDEX "ix_AIApplication_societal_impacts_AIApplication_id" ON "AIApplication_societal_impacts" ("AIApplication_id");
CREATE INDEX "ix_AIApplication_societal_impacts_societal_impacts" ON "AIApplication_societal_impacts" (societal_impacts);

CREATE TABLE "AIApplication_aliases" (
	"AIApplication_id" TEXT,
	aliases TEXT,
	PRIMARY KEY ("AIApplication_id", aliases),
	FOREIGN KEY("AIApplication_id") REFERENCES "AIApplication" (id)
);
CREATE INDEX "ix_AIApplication_aliases_aliases" ON "AIApplication_aliases" (aliases);
CREATE INDEX "ix_AIApplication_aliases_AIApplication_id" ON "AIApplication_aliases" ("AIApplication_id");

CREATE TABLE "AIApplication_see_also_uri" (
	"AIApplication_id" TEXT,
	see_also_uri TEXT,
	PRIMARY KEY ("AIApplication_id", see_also_uri),
	FOREIGN KEY("AIApplication_id") REFERENCES "AIApplication" (id)
);
CREATE INDEX "ix_AIApplication_see_also_uri_AIApplication_id" ON "AIApplication_see_also_uri" ("AIApplication_id");
CREATE INDEX "ix_AIApplication_see_also_uri_see_also_uri" ON "AIApplication_see_also_uri" (see_also_uri);

CREATE TABLE "Robot_aliases" (
	"Robot_id" TEXT,
	aliases TEXT,
	PRIMARY KEY ("Robot_id", aliases),
	FOREIGN KEY("Robot_id") REFERENCES "Robot" (id)
);
CREATE INDEX "ix_Robot_aliases_Robot_id" ON "Robot_aliases" ("Robot_id");
CREATE INDEX "ix_Robot_aliases_aliases" ON "Robot_aliases" (aliases);

CREATE TABLE "Robot_see_also_uri" (
	"Robot_id" TEXT,
	see_also_uri TEXT,
	PRIMARY KEY ("Robot_id", see_also_uri),
	FOREIGN KEY("Robot_id") REFERENCES "Robot" (id)
);
CREATE INDEX "ix_Robot_see_also_uri_see_also_uri" ON "Robot_see_also_uri" (see_also_uri);
CREATE INDEX "ix_Robot_see_also_uri_Robot_id" ON "Robot_see_also_uri" ("Robot_id");

CREATE TABLE "IoTSystem_ai_components" (
	"IoTSystem_id" TEXT,
	ai_components_id TEXT,
	PRIMARY KEY ("IoTSystem_id", ai_components_id),
	FOREIGN KEY("IoTSystem_id") REFERENCES "IoTSystem" (id),
	FOREIGN KEY(ai_components_id) REFERENCES "AIComponent" (id)
);
CREATE INDEX "ix_IoTSystem_ai_components_IoTSystem_id" ON "IoTSystem_ai_components" ("IoTSystem_id");
CREATE INDEX "ix_IoTSystem_ai_components_ai_components_id" ON "IoTSystem_ai_components" (ai_components_id);

CREATE TABLE "CyberPhysicalSystem_cyber_components" (
	"CyberPhysicalSystem_id" TEXT,
	cyber_components_id TEXT,
	PRIMARY KEY ("CyberPhysicalSystem_id", cyber_components_id),
	FOREIGN KEY("CyberPhysicalSystem_id") REFERENCES "CyberPhysicalSystem" (id),
	FOREIGN KEY(cyber_components_id) REFERENCES "AIComponent" (id)
);
CREATE INDEX "ix_CyberPhysicalSystem_cyber_components_cyber_components_id" ON "CyberPhysicalSystem_cyber_components" (cyber_components_id);
CREATE INDEX "ix_CyberPhysicalSystem_cyber_components_CyberPhysicalSystem_id" ON "CyberPhysicalSystem_cyber_components" ("CyberPhysicalSystem_id");

CREATE TABLE "RiskItem_affected_stakeholders" (
	"RiskItem_id" TEXT,
	affected_stakeholders_id TEXT,
	PRIMARY KEY ("RiskItem_id", affected_stakeholders_id),
	FOREIGN KEY("RiskItem_id") REFERENCES "RiskItem" (id),
	FOREIGN KEY(affected_stakeholders_id) REFERENCES "AIStakeholderRole" (id)
);
CREATE INDEX "ix_RiskItem_affected_stakeholders_RiskItem_id" ON "RiskItem_affected_stakeholders" ("RiskItem_id");
CREATE INDEX "ix_RiskItem_affected_stakeholders_affected_stakeholders_id" ON "RiskItem_affected_stakeholders" (affected_stakeholders_id);

CREATE TABLE "InputData_aliases" (
	"InputData_id" TEXT,
	aliases TEXT,
	PRIMARY KEY ("InputData_id", aliases),
	FOREIGN KEY("InputData_id") REFERENCES "InputData" (id)
);
CREATE INDEX "ix_InputData_aliases_InputData_id" ON "InputData_aliases" ("InputData_id");
CREATE INDEX "ix_InputData_aliases_aliases" ON "InputData_aliases" (aliases);

CREATE TABLE "InputData_see_also_uri" (
	"InputData_id" TEXT,
	see_also_uri TEXT,
	PRIMARY KEY ("InputData_id", see_also_uri),
	FOREIGN KEY("InputData_id") REFERENCES "InputData" (id)
);
CREATE INDEX "ix_InputData_see_also_uri_see_also_uri" ON "InputData_see_also_uri" (see_also_uri);
CREATE INDEX "ix_InputData_see_also_uri_InputData_id" ON "InputData_see_also_uri" ("InputData_id");

CREATE TABLE "Prediction" (
	predicted_value TEXT,
	confidence FLOAT,
	produced_by TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	clause_reference TEXT,
	preferred_label TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(produced_by) REFERENCES "AIModel" (id)
);
CREATE INDEX "ix_Prediction_id" ON "Prediction" (id);

CREATE TABLE "InferenceEngine" (
	inference_strategy TEXT,
	uses_model TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	clause_reference TEXT,
	preferred_label TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(uses_model) REFERENCES "AIModel" (id)
);
CREATE INDEX "ix_InferenceEngine_id" ON "InferenceEngine" (id);

CREATE TABLE "CatastrophicForgetting" (
	affected_model TEXT,
	mitigation_strategy TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	clause_reference TEXT,
	preferred_label TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(affected_model) REFERENCES "AIModel" (id)
);
CREATE INDEX "ix_CatastrophicForgetting_id" ON "CatastrophicForgetting" (id);

CREATE TABLE "AIModel_hyperparameters" (
	"AIModel_id" TEXT,
	hyperparameters TEXT,
	PRIMARY KEY ("AIModel_id", hyperparameters),
	FOREIGN KEY("AIModel_id") REFERENCES "AIModel" (id)
);
CREATE INDEX "ix_AIModel_hyperparameters_AIModel_id" ON "AIModel_hyperparameters" ("AIModel_id");
CREATE INDEX "ix_AIModel_hyperparameters_hyperparameters" ON "AIModel_hyperparameters" (hyperparameters);

CREATE TABLE "AIModel_training_phenomena" (
	"AIModel_id" TEXT,
	training_phenomena VARCHAR(23),
	PRIMARY KEY ("AIModel_id", training_phenomena),
	FOREIGN KEY("AIModel_id") REFERENCES "AIModel" (id)
);
CREATE INDEX "ix_AIModel_training_phenomena_training_phenomena" ON "AIModel_training_phenomena" (training_phenomena);
CREATE INDEX "ix_AIModel_training_phenomena_AIModel_id" ON "AIModel_training_phenomena" ("AIModel_id");

CREATE TABLE "AIModel_aliases" (
	"AIModel_id" TEXT,
	aliases TEXT,
	PRIMARY KEY ("AIModel_id", aliases),
	FOREIGN KEY("AIModel_id") REFERENCES "AIModel" (id)
);
CREATE INDEX "ix_AIModel_aliases_AIModel_id" ON "AIModel_aliases" ("AIModel_id");
CREATE INDEX "ix_AIModel_aliases_aliases" ON "AIModel_aliases" (aliases);

CREATE TABLE "AIModel_see_also_uri" (
	"AIModel_id" TEXT,
	see_also_uri TEXT,
	PRIMARY KEY ("AIModel_id", see_also_uri),
	FOREIGN KEY("AIModel_id") REFERENCES "AIModel" (id)
);
CREATE INDEX "ix_AIModel_see_also_uri_see_also_uri" ON "AIModel_see_also_uri" (see_also_uri);
CREATE INDEX "ix_AIModel_see_also_uri_AIModel_id" ON "AIModel_see_also_uri" ("AIModel_id");

CREATE TABLE "NeuralNetworkModel_hyperparameters" (
	"NeuralNetworkModel_id" TEXT,
	hyperparameters TEXT,
	PRIMARY KEY ("NeuralNetworkModel_id", hyperparameters),
	FOREIGN KEY("NeuralNetworkModel_id") REFERENCES "NeuralNetworkModel" (id)
);
CREATE INDEX "ix_NeuralNetworkModel_hyperparameters_NeuralNetworkModel_id" ON "NeuralNetworkModel_hyperparameters" ("NeuralNetworkModel_id");
CREATE INDEX "ix_NeuralNetworkModel_hyperparameters_hyperparameters" ON "NeuralNetworkModel_hyperparameters" (hyperparameters);

CREATE TABLE "NeuralNetworkModel_training_phenomena" (
	"NeuralNetworkModel_id" TEXT,
	training_phenomena VARCHAR(23),
	PRIMARY KEY ("NeuralNetworkModel_id", training_phenomena),
	FOREIGN KEY("NeuralNetworkModel_id") REFERENCES "NeuralNetworkModel" (id)
);
CREATE INDEX "ix_NeuralNetworkModel_training_phenomena_training_phenomena" ON "NeuralNetworkModel_training_phenomena" (training_phenomena);
CREATE INDEX "ix_NeuralNetworkModel_training_phenomena_NeuralNetworkModel_id" ON "NeuralNetworkModel_training_phenomena" ("NeuralNetworkModel_id");

CREATE TABLE "NeuralNetworkModel_aliases" (
	"NeuralNetworkModel_id" TEXT,
	aliases TEXT,
	PRIMARY KEY ("NeuralNetworkModel_id", aliases),
	FOREIGN KEY("NeuralNetworkModel_id") REFERENCES "NeuralNetworkModel" (id)
);
CREATE INDEX "ix_NeuralNetworkModel_aliases_aliases" ON "NeuralNetworkModel_aliases" (aliases);
CREATE INDEX "ix_NeuralNetworkModel_aliases_NeuralNetworkModel_id" ON "NeuralNetworkModel_aliases" ("NeuralNetworkModel_id");

CREATE TABLE "NeuralNetworkModel_see_also_uri" (
	"NeuralNetworkModel_id" TEXT,
	see_also_uri TEXT,
	PRIMARY KEY ("NeuralNetworkModel_id", see_also_uri),
	FOREIGN KEY("NeuralNetworkModel_id") REFERENCES "NeuralNetworkModel" (id)
);
CREATE INDEX "ix_NeuralNetworkModel_see_also_uri_NeuralNetworkModel_id" ON "NeuralNetworkModel_see_also_uri" ("NeuralNetworkModel_id");
CREATE INDEX "ix_NeuralNetworkModel_see_also_uri_see_also_uri" ON "NeuralNetworkModel_see_also_uri" (see_also_uri);

CREATE TABLE "DataProcess_parameters" (
	"DataProcess_id" TEXT,
	parameters TEXT,
	PRIMARY KEY ("DataProcess_id", parameters),
	FOREIGN KEY("DataProcess_id") REFERENCES "DataProcess" (id)
);
CREATE INDEX "ix_DataProcess_parameters_DataProcess_id" ON "DataProcess_parameters" ("DataProcess_id");
CREATE INDEX "ix_DataProcess_parameters_parameters" ON "DataProcess_parameters" (parameters);

CREATE TABLE "DataProcess_aliases" (
	"DataProcess_id" TEXT,
	aliases TEXT,
	PRIMARY KEY ("DataProcess_id", aliases),
	FOREIGN KEY("DataProcess_id") REFERENCES "DataProcess" (id)
);
CREATE INDEX "ix_DataProcess_aliases_DataProcess_id" ON "DataProcess_aliases" ("DataProcess_id");
CREATE INDEX "ix_DataProcess_aliases_aliases" ON "DataProcess_aliases" (aliases);

CREATE TABLE "DataProcess_see_also_uri" (
	"DataProcess_id" TEXT,
	see_also_uri TEXT,
	PRIMARY KEY ("DataProcess_id", see_also_uri),
	FOREIGN KEY("DataProcess_id") REFERENCES "DataProcess" (id)
);
CREATE INDEX "ix_DataProcess_see_also_uri_see_also_uri" ON "DataProcess_see_also_uri" (see_also_uri);
CREATE INDEX "ix_DataProcess_see_also_uri_DataProcess_id" ON "DataProcess_see_also_uri" ("DataProcess_id");

CREATE TABLE "DataLabel_aliases" (
	"DataLabel_id" TEXT,
	aliases TEXT,
	PRIMARY KEY ("DataLabel_id", aliases),
	FOREIGN KEY("DataLabel_id") REFERENCES "DataLabel" (id)
);
CREATE INDEX "ix_DataLabel_aliases_DataLabel_id" ON "DataLabel_aliases" ("DataLabel_id");
CREATE INDEX "ix_DataLabel_aliases_aliases" ON "DataLabel_aliases" (aliases);

CREATE TABLE "DataLabel_see_also_uri" (
	"DataLabel_id" TEXT,
	see_also_uri TEXT,
	PRIMARY KEY ("DataLabel_id", see_also_uri),
	FOREIGN KEY("DataLabel_id") REFERENCES "DataLabel" (id)
);
CREATE INDEX "ix_DataLabel_see_also_uri_see_also_uri" ON "DataLabel_see_also_uri" (see_also_uri);
CREATE INDEX "ix_DataLabel_see_also_uri_DataLabel_id" ON "DataLabel_see_also_uri" ("DataLabel_id");

CREATE TABLE "EvaluationMetric_aliases" (
	"EvaluationMetric_id" TEXT,
	aliases TEXT,
	PRIMARY KEY ("EvaluationMetric_id", aliases),
	FOREIGN KEY("EvaluationMetric_id") REFERENCES "EvaluationMetric" (id)
);
CREATE INDEX "ix_EvaluationMetric_aliases_EvaluationMetric_id" ON "EvaluationMetric_aliases" ("EvaluationMetric_id");
CREATE INDEX "ix_EvaluationMetric_aliases_aliases" ON "EvaluationMetric_aliases" (aliases);

CREATE TABLE "EvaluationMetric_see_also_uri" (
	"EvaluationMetric_id" TEXT,
	see_also_uri TEXT,
	PRIMARY KEY ("EvaluationMetric_id", see_also_uri),
	FOREIGN KEY("EvaluationMetric_id") REFERENCES "EvaluationMetric" (id)
);
CREATE INDEX "ix_EvaluationMetric_see_also_uri_EvaluationMetric_id" ON "EvaluationMetric_see_also_uri" ("EvaluationMetric_id");
CREATE INDEX "ix_EvaluationMetric_see_also_uri_see_also_uri" ON "EvaluationMetric_see_also_uri" (see_also_uri);

CREATE TABLE "DataDrift_aliases" (
	"DataDrift_id" TEXT,
	aliases TEXT,
	PRIMARY KEY ("DataDrift_id", aliases),
	FOREIGN KEY("DataDrift_id") REFERENCES "DataDrift" (id)
);
CREATE INDEX "ix_DataDrift_aliases_DataDrift_id" ON "DataDrift_aliases" ("DataDrift_id");
CREATE INDEX "ix_DataDrift_aliases_aliases" ON "DataDrift_aliases" (aliases);

CREATE TABLE "DataDrift_see_also_uri" (
	"DataDrift_id" TEXT,
	see_also_uri TEXT,
	PRIMARY KEY ("DataDrift_id", see_also_uri),
	FOREIGN KEY("DataDrift_id") REFERENCES "DataDrift" (id)
);
CREATE INDEX "ix_DataDrift_see_also_uri_see_also_uri" ON "DataDrift_see_also_uri" (see_also_uri);
CREATE INDEX "ix_DataDrift_see_also_uri_DataDrift_id" ON "DataDrift_see_also_uri" ("DataDrift_id");

CREATE TABLE "ExpertSystem" (
	rule_count INTEGER,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	clause_reference TEXT,
	preferred_label TEXT,
	"AIConceptsCollection_id" INTEGER,
	inference_engine_id TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("AIConceptsCollection_id") REFERENCES "AIConceptsCollection" (id),
	FOREIGN KEY(inference_engine_id) REFERENCES "InferenceEngine" (id)
);
CREATE INDEX "ix_ExpertSystem_id" ON "ExpertSystem" (id);

CREATE TABLE "Inference" (
	inference_strategy TEXT,
	performed_by TEXT,
	over_model TEXT,
	produced_output TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	clause_reference TEXT,
	preferred_label TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(performed_by) REFERENCES "InferenceEngine" (id),
	FOREIGN KEY(over_model) REFERENCES "AIModel" (id)
);
CREATE INDEX "ix_Inference_id" ON "Inference" (id);

CREATE TABLE "Prediction_aliases" (
	"Prediction_id" TEXT,
	aliases TEXT,
	PRIMARY KEY ("Prediction_id", aliases),
	FOREIGN KEY("Prediction_id") REFERENCES "Prediction" (id)
);
CREATE INDEX "ix_Prediction_aliases_Prediction_id" ON "Prediction_aliases" ("Prediction_id");
CREATE INDEX "ix_Prediction_aliases_aliases" ON "Prediction_aliases" (aliases);

CREATE TABLE "Prediction_see_also_uri" (
	"Prediction_id" TEXT,
	see_also_uri TEXT,
	PRIMARY KEY ("Prediction_id", see_also_uri),
	FOREIGN KEY("Prediction_id") REFERENCES "Prediction" (id)
);
CREATE INDEX "ix_Prediction_see_also_uri_Prediction_id" ON "Prediction_see_also_uri" ("Prediction_id");
CREATE INDEX "ix_Prediction_see_also_uri_see_also_uri" ON "Prediction_see_also_uri" (see_also_uri);

CREATE TABLE "Decision_based_on_predictions" (
	"Decision_id" TEXT,
	based_on_predictions_id TEXT,
	PRIMARY KEY ("Decision_id", based_on_predictions_id),
	FOREIGN KEY("Decision_id") REFERENCES "Decision" (id),
	FOREIGN KEY(based_on_predictions_id) REFERENCES "Prediction" (id)
);
CREATE INDEX "ix_Decision_based_on_predictions_based_on_predictions_id" ON "Decision_based_on_predictions" (based_on_predictions_id);
CREATE INDEX "ix_Decision_based_on_predictions_Decision_id" ON "Decision_based_on_predictions" ("Decision_id");

CREATE TABLE "InferenceEngine_aliases" (
	"InferenceEngine_id" TEXT,
	aliases TEXT,
	PRIMARY KEY ("InferenceEngine_id", aliases),
	FOREIGN KEY("InferenceEngine_id") REFERENCES "InferenceEngine" (id)
);
CREATE INDEX "ix_InferenceEngine_aliases_InferenceEngine_id" ON "InferenceEngine_aliases" ("InferenceEngine_id");
CREATE INDEX "ix_InferenceEngine_aliases_aliases" ON "InferenceEngine_aliases" (aliases);

CREATE TABLE "InferenceEngine_see_also_uri" (
	"InferenceEngine_id" TEXT,
	see_also_uri TEXT,
	PRIMARY KEY ("InferenceEngine_id", see_also_uri),
	FOREIGN KEY("InferenceEngine_id") REFERENCES "InferenceEngine" (id)
);
CREATE INDEX "ix_InferenceEngine_see_also_uri_see_also_uri" ON "InferenceEngine_see_also_uri" (see_also_uri);
CREATE INDEX "ix_InferenceEngine_see_also_uri_InferenceEngine_id" ON "InferenceEngine_see_also_uri" ("InferenceEngine_id");

CREATE TABLE "Recommendation_based_on_predictions" (
	"Recommendation_id" TEXT,
	based_on_predictions_id TEXT,
	PRIMARY KEY ("Recommendation_id", based_on_predictions_id),
	FOREIGN KEY("Recommendation_id") REFERENCES "Recommendation" (id),
	FOREIGN KEY(based_on_predictions_id) REFERENCES "Prediction" (id)
);
CREATE INDEX "ix_Recommendation_based_on_predictions_Recommendation_id" ON "Recommendation_based_on_predictions" ("Recommendation_id");
CREATE INDEX "ix_Recommendation_based_on_predictions_based_on_predictions_id" ON "Recommendation_based_on_predictions" (based_on_predictions_id);

CREATE TABLE "CatastrophicForgetting_aliases" (
	"CatastrophicForgetting_id" TEXT,
	aliases TEXT,
	PRIMARY KEY ("CatastrophicForgetting_id", aliases),
	FOREIGN KEY("CatastrophicForgetting_id") REFERENCES "CatastrophicForgetting" (id)
);
CREATE INDEX "ix_CatastrophicForgetting_aliases_CatastrophicForgetting_id" ON "CatastrophicForgetting_aliases" ("CatastrophicForgetting_id");
CREATE INDEX "ix_CatastrophicForgetting_aliases_aliases" ON "CatastrophicForgetting_aliases" (aliases);

CREATE TABLE "CatastrophicForgetting_see_also_uri" (
	"CatastrophicForgetting_id" TEXT,
	see_also_uri TEXT,
	PRIMARY KEY ("CatastrophicForgetting_id", see_also_uri),
	FOREIGN KEY("CatastrophicForgetting_id") REFERENCES "CatastrophicForgetting" (id)
);
CREATE INDEX "ix_CatastrophicForgetting_see_also_uri_CatastrophicForgetting_id" ON "CatastrophicForgetting_see_also_uri" ("CatastrophicForgetting_id");
CREATE INDEX "ix_CatastrophicForgetting_see_also_uri_see_also_uri" ON "CatastrophicForgetting_see_also_uri" (see_also_uri);

CREATE TABLE "ExpertSystem_aliases" (
	"ExpertSystem_id" TEXT,
	aliases TEXT,
	PRIMARY KEY ("ExpertSystem_id", aliases),
	FOREIGN KEY("ExpertSystem_id") REFERENCES "ExpertSystem" (id)
);
CREATE INDEX "ix_ExpertSystem_aliases_aliases" ON "ExpertSystem_aliases" (aliases);
CREATE INDEX "ix_ExpertSystem_aliases_ExpertSystem_id" ON "ExpertSystem_aliases" ("ExpertSystem_id");

CREATE TABLE "ExpertSystem_see_also_uri" (
	"ExpertSystem_id" TEXT,
	see_also_uri TEXT,
	PRIMARY KEY ("ExpertSystem_id", see_also_uri),
	FOREIGN KEY("ExpertSystem_id") REFERENCES "ExpertSystem" (id)
);
CREATE INDEX "ix_ExpertSystem_see_also_uri_ExpertSystem_id" ON "ExpertSystem_see_also_uri" ("ExpertSystem_id");
CREATE INDEX "ix_ExpertSystem_see_also_uri_see_also_uri" ON "ExpertSystem_see_also_uri" (see_also_uri);

CREATE TABLE "Inference_aliases" (
	"Inference_id" TEXT,
	aliases TEXT,
	PRIMARY KEY ("Inference_id", aliases),
	FOREIGN KEY("Inference_id") REFERENCES "Inference" (id)
);
CREATE INDEX "ix_Inference_aliases_Inference_id" ON "Inference_aliases" ("Inference_id");
CREATE INDEX "ix_Inference_aliases_aliases" ON "Inference_aliases" (aliases);

CREATE TABLE "Inference_see_also_uri" (
	"Inference_id" TEXT,
	see_also_uri TEXT,
	PRIMARY KEY ("Inference_id", see_also_uri),
	FOREIGN KEY("Inference_id") REFERENCES "Inference" (id)
);
CREATE INDEX "ix_Inference_see_also_uri_Inference_id" ON "Inference_see_also_uri" ("Inference_id");
CREATE INDEX "ix_Inference_see_also_uri_see_also_uri" ON "Inference_see_also_uri" (see_also_uri);
