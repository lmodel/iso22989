export type AicRecordMixinAicId = string;
export type AicEcosystemAicId = string;
export type AicSystemAicId = string;
export type AicAgentAicId = string;
export type AicExpertSystemAicId = string;
export type AicRobotAicId = string;
export type AicComponentAicId = string;
export type AicKnowledgeAicId = string;
export type AicTaskAicId = string;
export type AicModelAicId = string;
export type AicMachineLearningModelAicId = string;
export type AicNeuralNetworkModelAicId = string;
export type AicDatasetAicId = string;
export type AicTrustworthinessClaimAicId = string;
export type AicAssessmentAicId = string;
export type AicLifecycleProcessAicId = string;
export type AicStakeholderAicId = string;
export type AicPredictionAicId = string;
export type AicDecisionAicId = string;
export type AicActionAicId = string;
export type AicApplicationAicId = string;
export type AicResourcePoolAicId = string;
export type AicIotDeviceAicId = string;
export type AicIotSystemAicId = string;
export type AicCyberPhysicalSystemAicId = string;
/**
* How wide a range of problems a system can take on.
*/
export enum AicSystemScope {
    
    /** Built for a bounded set of problems, and cannot move beyond them. */
    narrow_ai = "narrow_ai",
    /** Able to take on problems of many kinds, including ones it was not built for. */
    general_ai = "general_ai",
};
/**
* Whether a system works on explicit symbols or on learned numeric encodings.
*/
export enum AicApproach {
    
    /** Works by manipulating explicit symbols and the rules that relate them. */
    symbolic = "symbolic",
    /** Works on numeric encodings that carry meaning only as a whole, such as the weights of a network. */
    subsymbolic = "subsymbolic",
};
/**
* A family of techniques a system is built with.
*/
export enum AicTechnique {
    
    /** Fits a model's numbers to data rather than having a person write the logic. */
    machine_learning = "machine_learning",
    /** Machine learning that stacks many layers of a network. */
    deep_learning = "deep_learning",
    /** Aims at interaction with people that feels closer to how people deal with one another. */
    cognitive_computing = "cognitive_computing",
    /** Works out what content and requests mean, so that it can act on the meaning. */
    semantic_computing = "semantic_computing",
    /** Accepts inexact or uncertain reasoning where an exact answer would cost too much. */
    soft_computing = "soft_computing",
    /** Searches by breeding and selecting candidate answers over many generations. */
    genetic_algorithm = "genetic_algorithm",
    /** States facts and rules in logic, and lets a solver reach the conclusions. */
    logic_programming = "logic_programming",
};
/**
* Whether a system can change its own remit or stays under outside direction.
*/
export enum AicAutonomy {
    
    /** Can change what it is for or where it applies with nobody directing it. */
    autonomous = "autonomous",
    /** Stays under the direction of a person or another system. */
    heteronomous = "heteronomous",
};
/**
* How a body of knowledge is put.
*/
export enum AicKnowledgeKind {
    
    /** States what is the case. */
    declarative = "declarative",
    /** States what to do, step by step. */
    procedural = "procedural",
};
/**
* A step in how a system gets from data to acting on its results.
*/
export enum AicFunctionalStep {
    
    /** Taking in data and giving it meaning. */
    data_and_information = "data_and_information",
    /** Building up what the system knows, and learning from more data. */
    knowledge_and_learning = "knowledge_and_learning",
    /** Working out a likely result for the case in hand. */
    prediction = "prediction",
    /** Choosing what to do, given the results so far. */
    decision = "decision",
    /** Carrying out what was chosen. */
    action = "action",
};
/**
* How a model learns from its data.
*/
export enum AicLearningParadigm {
    
    /** Every example comes with the answer it should give. */
    supervised = "supervised",
    /** No example comes with an answer, so the model looks for structure. */
    unsupervised = "unsupervised",
    /** Some examples come with answers and the rest do not. */
    semi_supervised = "semi_supervised",
    /** The model acts, gets a reward or penalty, and adjusts to earn more reward. */
    reinforcement = "reinforcement",
    /** What was learned on one problem gives a start on another. */
    transfer = "transfer",
};
/**
* A family of algorithms that fit machine learning models.
*/
export enum AicAlgorithmFamily {
    
    /** Layers of simple units whose connection weights are tuned to the data. */
    neural_network = "neural_network",
    /** A graph of variables and how the probability of one depends on others. */
    bayesian_network = "bayesian_network",
    /** A series of branching tests that end in a result. */
    decision_tree = "decision_tree",
    /** Finds the widest gap that separates the classes of example. */
    support_vector_machine = "support_vector_machine",
};
/**
* How the layers of a neural network are connected.
*/
export enum AicNetworkArchitecture {
    
    /** Signals pass one way, from first layer to last, with no loops. */
    feed_forward = "feed_forward",
    /** Outputs feed back as inputs, so the network can follow a sequence. */
    recurrent = "recurrent",
    /** A recurrent design whose gates let it carry a signal across long sequences. */
    long_short_term_memory = "long_short_term_memory",
    /** Layers slide small filters across the input, as is usual for images. */
    convolutional = "convolutional",
};
/**
* What a dataset is used for.
*/
export enum AicDatasetRole {
    
    /** Used to fit a model. */
    training = "training",
    /** Used while developing a model, to compare versions and tune settings. */
    validation = "validation",
    /** Held back from development, to judge the finished model. */
    test = "test",
    /** Gathered while the system runs, when it is deployed and in real use. */
    production = "production",
    /** What a system is given so that it can work out a result. */
    input = "input",
};
/**
* A kind of work done on data before or while a model uses it.
*/
export enum AicDataProcessKind {
    
    /** Adds descriptive notes to data and leaves the data itself as it was. */
    data_annotation = "data_annotation",
    /** Looks for gaps, skew and whatever else would limit the data's use. */
    data_quality_checking = "data_quality_checking",
    /** Makes new samples out of existing ones by altering them. */
    data_augmentation = "data_augmentation",
    /** Picks a smaller part of the data that behaves like the whole. */
    data_sampling = "data_sampling",
    /** A first look at data to learn its shape and what it may hold. */
    exploratory_data_analysis = "exploratory_data_analysis",
    /** Fills gaps with values worked out from what is there. */
    imputation = "imputation",
};
/**
* A property a trustworthiness claim is about.
*/
export enum AicTrustworthinessProperty {
    
    /** Keeps performing well when conditions turn hostile or unusual. */
    robustness = "robustness",
    /** Behaves and delivers as intended, time after time. */
    reliability = "reliability",
    /** Gets back to working order soon after something goes wrong. */
    resilience = "resilience",
    /** A person or another system can step in and steer it. */
    controllability = "controllability",
    /** Can say, in terms people follow, what drove a result. */
    explainability = "explainability",
    /** Lets people form sound expectations of what it will produce. */
    predictability = "predictability",
    /** The organization tells those concerned what it does and decides. */
    organizational_transparency = "organizational_transparency",
    /** Those concerned can learn what they need to know about the system. */
    system_transparency = "system_transparency",
    /** Whether the system treats some people or things worse than others, as a pattern. */
    bias_and_fairness = "bias_and_fairness",
    /** Someone answers for what the system does and decides. */
    accountability = "accountability",
    /** Those entitled to use it can reach it and use it when they ask. */
    availability = "availability",
};
/**
* Which question an assessment answers.
*/
export enum AicAssessmentKind {
    
    /** Evidence shows that the system meets what was specified for it. */
    verification = "verification",
    /** Evidence shows that the system suits the use it is meant for. */
    validation = "validation",
};
/**
* The part a party plays around an AI system.
*/
export enum AicStakeholderRole {
    
    /** Offers AI products or services, or the platform for them. */
    ai_provider = "ai_provider",
    /** Designs, builds, tests or runs AI systems. */
    ai_producer = "ai_producer",
    /** Takes an AI product or service for its own use. */
    ai_customer = "ai_customer",
    /** Helps others in the ecosystem, by integrating systems or supplying data. */
    ai_partner = "ai_partner",
    /** Is affected by an AI system, or has data about them used in it. */
    ai_subject = "ai_subject",
    /** Sets policy for AI or holds others to the rules on it. */
    relevant_authority = "relevant_authority",
};
/**
* A narrower part within one of the roles.
*/
export enum AicStakeholderSubRole {
    
    /** Offers the platform that others run AI on. */
    ai_platform_provider = "ai_platform_provider",
    /** Offers a finished AI product or a service built on AI. */
    ai_product_or_service_provider = "ai_product_or_service_provider",
    /** Writes and builds the system. */
    ai_developer = "ai_developer",
    /** Uses the system directly. */
    ai_user = "ai_user",
    /** Fits AI parts into a larger system. */
    ai_system_integrator = "ai_system_integrator",
    /** Supplies data that others build or run on. */
    data_provider = "data_provider",
    /** A person the data is about. */
    data_subject = "data_subject",
    /** Anyone else a system affects. */
    other_subject = "other_subject",
    /** Decides policy on AI. */
    policy_maker = "policy_maker",
    /** Holds others to the rules on AI. */
    regulator = "regulator",
};
/**
* A stage in an AI system's life.
*/
export enum AicLifecycleStage {
    
    /** Deciding that a system is wanted, what it is for and whether it can be done. */
    inception = "inception",
    /** Making the system, from its architecture through its data work to its models. */
    design_and_development = "design_and_development",
    /** Checking what was made against its specification and against its purpose. */
    verification_and_validation = "verification_and_validation",
    /** Installing the system where it is to run, and making it ready for use. */
    deployment = "deployment",
    /** Running the system and keeping an eye on how it behaves. */
    operation_and_monitoring = "operation_and_monitoring",
    /** Repeating the checks on a system that goes on learning as it runs. */
    continuous_validation = "continuous_validation",
    /** Looking again at whether the running system still meets its aims. */
    re_evaluation = "re_evaluation",
    /** Taking the system out of use. */
    retirement = "retirement",
};
/**
* A stage of the OECD's account of an AI system's life, which Annex A sets beside the standard's.
*/
export enum AicOecdLifecycleStage {
    
    /** Setting out what the system is for and how it will work. */
    plan_and_design = "plan_and_design",
    /** Gathering and readying the data. */
    collect_and_process_data = "collect_and_process_data",
    /** Making the model and trying it. */
    build_and_use_model = "build_and_use_model",
    /** Checking the model. */
    verify_and_validate = "verify_and_validate",
    /** Putting the system into use. */
    deploy = "deploy",
    /** Running the system and watching it. */
    operate_and_monitor = "operate_and_monitor",
};
/**
* A kind of computing resource AI work runs on.
*/
export enum AicResourceKind {
    
    /** Computing bought as a shared service, in someone else's data centre. */
    cloud = "cloud",
    /** Computing close to where data arises, rather than in a far data centre. */
    edge = "edge",
    /** A chip made for one kind of work, such as training or running a model. */
    application_specific_integrated_circuit = "application_specific_integrated_circuit",
};
/**
* A field of AI a system belongs to.
*/
export enum AicField {
    
    /** Making sense of pictures and video. */
    computer_vision = "computer_vision",
    /** Making sense of, or producing, human language. */
    natural_language_processing = "natural_language_processing",
    /** Finding patterns in large amounts of numbers. */
    data_mining = "data_mining",
    /** Working out a sequence of steps that reaches an aim. */
    planning = "planning",
};
/**
* A named kind of task from the fields of language and vision.
*/
export enum AicTaskKind {
    
    /** Cuts a text down to its main points. */
    automatic_summarization = "automatic_summarization",
    /** Decides what to say next in a conversation. */
    dialogue_management = "dialogue_management",
    /** Works out the feeling a text or voice conveys. */
    emotion_recognition = "emotion_recognition",
    /** Finds stored documents that answer a need. */
    information_retrieval = "information_retrieval",
    /** Renders text from one language in another. */
    machine_translation = "machine_translation",
    /** Spots the people, places and other named things in a text. */
    named_entity_recognition = "named_entity_recognition",
    /** Writes text from data or from an internal form. */
    natural_language_generation = "natural_language_generation",
    /** Takes a text and draws out what it means. */
    natural_language_understanding = "natural_language_understanding",
    /** Reads printed or written characters from a picture. */
    optical_character_recognition = "optical_character_recognition",
    /** Marks each word as a noun, a verb and so on. */
    part_of_speech_tagging = "part_of_speech_tagging",
    /** Replies to a question put in everyday words. */
    question_answering = "question_answering",
    /** Finds how the things a text names relate to one another. */
    relationship_extraction = "relationship_extraction",
    /** Works out the opinion a text expresses. */
    sentiment_analysis = "sentiment_analysis",
    /** Turns spoken words into text. */
    speech_recognition = "speech_recognition",
    /** Turns text into spoken words. */
    speech_synthesis = "speech_synthesis",
    /** Matches a face in a picture against stored faces. */
    face_recognition = "face_recognition",
    /** Says what a picture shows. */
    image_recognition = "image_recognition",
};
/**
* A domain the standard works through as an application of AI.
*/
export enum AicApplicationDomain {
    
    /** Spotting dishonest transactions or claims. */
    fraud_detection = "fraud_detection",
    /** Vehicles that drive part or all of the way without a driver. */
    automated_vehicles = "automated_vehicles",
    /** Forecasting when equipment needs attention, before it fails. */
    predictive_maintenance = "predictive_maintenance",
};


/**
 * What every record has, so that other records can refer to it: an identifier, a title and a description.
 */
export interface AicRecordMixin {
    /** The record's identifier, unique among the records it sits with, such as a URI or a CURIE. Other records refer to the record by it. */
    aic_id: string,
    /** The name the record's author gives it. */
    title: string,
    /** What the record describes, in its author's words. */
    description?: string,
}


/**
 * The AI systems around one context of use, with the data, resources and parties that surround them, each kind of record in a list of its own.
 */
export interface AicEcosystem extends AicRecordMixin {
    /** The AI systems. */
    aic_ecosystem_systems?: AicSystem[],
    /** The parts of those systems. */
    aic_ecosystem_components?: AicComponent[],
    /** The bodies of knowledge those systems draw on. */
    aic_ecosystem_knowledge?: AicKnowledge[],
    /** The tasks those systems take on. */
    aic_ecosystem_tasks?: AicTask[],
    /** The models those systems use. */
    aic_ecosystem_models?: AicModel[],
    /** The datasets those systems and models use. */
    aic_ecosystem_datasets?: AicDataset[],
    /** The parties around those systems. */
    aic_ecosystem_stakeholders?: AicStakeholder[],
    /** The work done at each stage of those systems' lives. */
    aic_ecosystem_lifecycle_processes?: AicLifecycleProcess[],
    /** The trustworthiness claims made for those systems. */
    aic_ecosystem_claims?: AicTrustworthinessClaim[],
    /** The verification and validation of those systems. */
    aic_ecosystem_assessments?: AicAssessment[],
    /** The predictions those systems produced. */
    aic_ecosystem_predictions?: AicPrediction[],
    /** The decisions taken on those predictions. */
    aic_ecosystem_decisions?: AicDecision[],
    /** The actions taken on those decisions. */
    aic_ecosystem_actions?: AicAction[],
    /** Where those systems are applied. */
    aic_ecosystem_applications?: AicApplication[],
    /** The computing resources those systems run on. */
    aic_ecosystem_resource_pools?: AicResourcePool[],
    /** The connected devices in the ecosystem. */
    aic_ecosystem_iot_devices?: AicIotDevice[],
    /** The connected systems in the ecosystem. */
    aic_ecosystem_iot_systems?: AicIotSystem[],
    /** The cyber-physical systems in the ecosystem. */
    aic_ecosystem_cyber_physical_systems?: AicCyberPhysicalSystem[],
}


/**
 * A system built to produce results for goals set by people, using AI techniques, whatever else it is made of.
 */
export interface AicSystem extends AicRecordMixin {
    /** Which class this record is: AicSystem or a kind of it. */
    aic_system_type: string,
    /** What the system is meant to do. */
    aic_system_purpose?: string,
    /** How wide a range of problems the system can take on. */
    aic_system_scope?: string,
    /** Whether it works symbolically, subsymbolically or both ways. */
    aic_system_approaches?: string,
    /** The families of technique it is built with. */
    aic_system_techniques?: string,
    /** Whether it runs without a person acting at each step, under the conditions given. */
    aic_system_automated?: boolean,
    /** Whether it can change its own remit or stays under outside direction. */
    aic_system_autonomy?: string,
    /** How people and the system share the work, if they do. */
    aic_system_human_teaming?: string,
    /** The stage of its life the system is in now. */
    aic_system_stage?: string,
    /** The fields of AI it belongs to. */
    aic_system_fields?: string,
    /** The steps from data to action that it performs. */
    aic_system_steps?: string,
    /** The parts it is made of. */
    aic_system_components?: AicComponentAicId[],
    /** The models it uses. */
    aic_system_models?: AicModelAicId[],
    /** The datasets it uses. */
    aic_system_datasets?: AicDatasetAicId[],
    /** The tasks it takes on. */
    aic_system_tasks?: AicTaskAicId[],
    /** The parties around it. */
    aic_system_stakeholders?: AicStakeholderAicId[],
    /** The computing resources it runs on. */
    aic_system_resource_pools?: AicResourcePoolAicId[],
    /** The legal questions that follow from where it is built, offered or used. */
    aic_system_jurisdictional_issues?: string[],
    /** The effects it may have on people and society beyond its users. */
    aic_system_societal_impacts?: string[],
}


/**
 * A system that perceives its surroundings and acts on them in pursuit of goals.
 */
export interface AicAgent extends AicSystem {
    /** The goals the agent pursues. */
    aic_agent_goals: string[],
    /** The surroundings the agent perceives and acts on. */
    aic_agent_environment?: string,
}


/**
 * A system that puts what human specialists know into a form it can reason with.
 */
export interface AicExpertSystem extends AicSystem {
    /** The bodies of knowledge the system reasons with. */
    aic_expert_knowledge: AicKnowledgeAicId[],
    /** How the system draws conclusions from that knowledge. */
    aic_expert_inference?: string,
}


/**
 * A system that moves or acts on physical things through its own actuators.
 */
export interface AicRobot extends AicSystem {
    /** The actuators through which the robot acts. */
    aic_robot_actuators: string[],
    /** The sensors through which it perceives. */
    aic_robot_sensors?: string[],
}


/**
 * A part of a system that does one job in it.
 */
export interface AicComponent extends AicRecordMixin {
    /** The step from data to action this part performs. */
    aic_component_step?: string,
    /** The other parts this part needs. */
    aic_component_depends_on?: AicComponentAicId[],
}


/**
 * A body of what a system knows, in a form it can use.
 */
export interface AicKnowledge extends AicRecordMixin {
    /** Whether it states what is the case or what to do. */
    aic_knowledge_kind?: string,
    /** The form it is held in, such as rules, a graph or an ontology. */
    aic_knowledge_representation?: string,
}


/**
 * Something a system is asked to get done.
 */
export interface AicTask extends AicRecordMixin {
    /** The named kind of task it is, where it is one. */
    aic_task_kind?: string,
    /** What getting the task done achieves. */
    aic_task_goal?: string,
    /** The human languages the task works in, as language tags such as en or fr-CA. */
    aic_task_languages?: string[],
    /** What is measured to judge how well it is done, such as accuracy. */
    aic_task_performance_measures?: string[],
}


/**
 * A representation of something, made so that a system can compute with it.
 */
export interface AicModel extends AicRecordMixin {
    /** Which class this record is: AicModel or a kind of it. */
    aic_model_type: string,
    /** The version of the model, as its makers number it. */
    aic_model_version?: string,
    /** What the model stands for, such as a process or a body of data. */
    aic_model_represents?: string,
}


/**
 * A model whose numbers were fitted to data by a training run.
 */
export interface AicMachineLearningModel extends AicModel {
    /** How the model learned from its data. */
    aic_ml_paradigm?: string,
    /** The family of algorithm that fitted it. */
    aic_ml_algorithm?: string,
    /** The datasets used to fit, tune and test it. */
    aic_ml_datasets?: AicDatasetAicId[],
    /** The settings fixed before training, each as name=value. */
    aic_ml_hyperparameters?: string[],
    /** How many numbers training fitted. */
    aic_ml_parameter_count?: number,
    /** When the last training run ended. */
    aic_ml_trained_on?: date,
    /** The earlier model that this one updates by training it again on other data. */
    aic_ml_retrained_from?: AicMachineLearningModelAicId,
    /** Whether it goes on learning in small steps while in use. */
    aic_ml_continuous_learning?: boolean,
}


/**
 * A kind of machine learning model built from layers of simple connected units.
 */
export interface AicNeuralNetworkModel extends AicMachineLearningModel {
    /** How its layers are connected. */
    aic_network_architecture?: string,
    /** How many layers it has. */
    aic_network_layer_count?: number,
    /** The functions its units use to turn their inputs into an output. */
    aic_network_activation_functions?: string[],
}


/**
 * A set of data kept together in one format.
 */
export interface AicDataset extends AicRecordMixin {
    /** What the dataset is used for. */
    aic_dataset_roles?: string,
    /** Where the data comes from. */
    aic_dataset_source?: string,
    /** How many samples it holds. */
    aic_dataset_sample_count?: number,
    /** The labels its samples can carry. */
    aic_dataset_labels?: string[],
    /** Where the correct answers for its samples come from. */
    aic_dataset_ground_truth?: string,
    /** Whether it holds data that can identify a person. */
    aic_dataset_holds_pii?: boolean,
    /** The work done on the data. */
    aic_dataset_processes?: AicDataProcess[],
}


/**
 * One piece of work done on a dataset.
 */
export interface AicDataProcess {
    /** The kind of work. */
    aic_data_process_kind: string,
    /** How it was done, such as the tool used. */
    aic_data_process_method?: string,
    /** When it was done. */
    aic_data_process_date?: date,
}


/**
 * A claim that a system has a property people can rely on, with what backs it.
 */
export interface AicTrustworthinessClaim extends AicRecordMixin {
    /** The system the claim is about. */
    aic_claim_system: AicSystemAicId,
    /** The property claimed. */
    aic_claim_property: string,
    /** What backs the claim. */
    aic_claim_evidence?: string[],
    /** How the property was measured, if it was. */
    aic_claim_measure?: string,
}


/**
 * One verification or validation of a system.
 */
export interface AicAssessment extends AicRecordMixin {
    /** Whether it checks the system against its specification or against its purpose. */
    aic_assessment_kind: string,
    /** The system assessed. */
    aic_assessment_system: AicSystemAicId,
    /** How the system was assessed. */
    aic_assessment_method?: string,
    /** What the assessment found. */
    aic_assessment_result?: string,
    /** When it was done. */
    aic_assessment_date?: date,
}


/**
 * A piece of work done at one stage of a system's life.
 */
export interface AicLifecycleProcess extends AicRecordMixin {
    /** The stage the work belongs to. */
    aic_lifecycle_stage: string,
    /** The system the work is for. */
    aic_lifecycle_system?: AicSystemAicId,
    /** What the work starts from. */
    aic_lifecycle_inputs?: string[],
    /** What the work produces. */
    aic_lifecycle_outputs?: string[],
    /** The party that answers for the work. */
    aic_lifecycle_responsible?: AicStakeholderAicId,
    /** When the work began. */
    aic_lifecycle_start?: date,
    /** When the work ended. */
    aic_lifecycle_end?: date,
}


/**
 * A person, group or organization with a part in an AI system or an interest in it.
 */
export interface AicStakeholder extends AicRecordMixin {
    /** The part the party plays. */
    aic_stakeholder_role: string,
    /** The narrower parts it plays within that role. */
    aic_stakeholder_sub_roles?: string,
    /** The organization the party is or belongs to. */
    aic_stakeholder_organization?: string,
    /** How to reach the party. */
    aic_stakeholder_contact?: string,
    /** What the party answers for. */
    aic_stakeholder_responsibilities?: string[],
}


/**
 * A result a system worked out for one case.
 */
export interface AicPrediction extends AicRecordMixin {
    /** The system that produced it. */
    aic_prediction_system: AicSystemAicId,
    /** What it says. */
    aic_prediction_value: string,
    /** How sure the system was, from 0 to 1. */
    aic_prediction_confidence?: number,
}


/**
 * A choice made on the strength of some predictions.
 */
export interface AicDecision extends AicRecordMixin {
    /** What was chosen. */
    aic_decision_outcome: string,
    /** The predictions it rests on. */
    aic_decision_predictions?: AicPredictionAicId[],
    /** How the choice was made, such as a threshold or a rule. */
    aic_decision_criteria?: string,
}


/**
 * What was done because of a decision.
 */
export interface AicAction extends AicRecordMixin {
    /** The decision it carries out. */
    aic_action_decision: AicDecisionAicId,
    /** What it acted on. */
    aic_action_target?: string,
    /** When it was done. */
    aic_action_time?: string,
}


/**
 * One use of a system in a line of work.
 */
export interface AicApplication extends AicRecordMixin {
    /** The system applied. */
    aic_application_system: AicSystemAicId,
    /** The domain, where it is one the standard works through. */
    aic_application_domain?: string,
    /** The sector, in the words of whoever keeps the record. */
    aic_application_sector?: string,
    /** What this use is for. */
    aic_application_purpose?: string,
}


/**
 * A body of computing resource that AI work can draw on.
 */
export interface AicResourcePool extends AicRecordMixin {
    /** The kind of resource. */
    aic_pool_kind?: string,
    /** The hardware in it, such as a model of accelerator. */
    aic_pool_hardware?: string,
    /** How much it offers, in units its owner uses. */
    aic_pool_capacity?: string,
}


/**
 * A connected device that reads from or acts on its physical surroundings.
 */
export interface AicIotDevice extends AicRecordMixin {
    /** What the device reads from its surroundings. */
    aic_device_senses?: string[],
    /** What the device acts on. */
    aic_device_actuates?: string[],
}


/**
 * A networked system that links devices and offers services built on them.
 */
export interface AicIotSystem extends AicRecordMixin {
    /** The devices in it. */
    aic_iot_devices: AicIotDeviceAicId[],
    /** The AI systems that work with it. */
    aic_iot_ai_systems?: AicSystemAicId[],
}


/**
 * Computing and physical processes tied in a loop, each affecting the other.
 */
export interface AicCyberPhysicalSystem extends AicRecordMixin {
    /** The physical processes it senses and controls. */
    aic_cps_physical_processes: string[],
    /** The connected system it runs on, if it does. */
    aic_cps_iot_system?: AicIotSystemAicId,
    /** The AI systems that work with it. */
    aic_cps_ai_systems?: AicSystemAicId[],
}



