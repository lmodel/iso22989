-- # Class: AicRecordMixin Description: What every record has, so that other records can refer to it: an identifier, a title and a description.
--     * Slot: aic_id Description: The record's identifier, unique among the records it sits with, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the record's author gives it.
--     * Slot: description Description: What the record describes, in its author's words.
-- # Class: AicEcosystem Description: The AI systems around one context of use, with the data, resources and parties that surround them, each kind of record in a list of its own.
--     * Slot: aic_id Description: The record's identifier, unique among the records it sits with, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the record's author gives it.
--     * Slot: description Description: What the record describes, in its author's words.
-- # Class: AicSystem Description: A system built to produce results for goals set by people, using AI techniques, whatever else it is made of.
--     * Slot: aic_system_type Description: Which class this record is: AicSystem or a kind of it.
--     * Slot: aic_system_purpose Description: What the system is meant to do.
--     * Slot: aic_system_scope Description: How wide a range of problems the system can take on.
--     * Slot: aic_system_automated Description: Whether it runs without a person acting at each step, under the conditions given.
--     * Slot: aic_system_autonomy Description: Whether it can change its own remit or stays under outside direction.
--     * Slot: aic_system_human_teaming Description: How people and the system share the work, if they do.
--     * Slot: aic_system_stage Description: The stage of its life the system is in now.
--     * Slot: aic_id Description: The record's identifier, unique among the records it sits with, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the record's author gives it.
--     * Slot: description Description: What the record describes, in its author's words.
--     * Slot: AicEcosystem_aic_id Description: Autocreated FK slot
-- # Class: AicAgent Description: A system that perceives its surroundings and acts on them in pursuit of goals.
--     * Slot: aic_agent_environment Description: The surroundings the agent perceives and acts on.
--     * Slot: aic_system_type Description: Which class this record is: AicSystem or a kind of it.
--     * Slot: aic_system_purpose Description: What the system is meant to do.
--     * Slot: aic_system_scope Description: How wide a range of problems the system can take on.
--     * Slot: aic_system_automated Description: Whether it runs without a person acting at each step, under the conditions given.
--     * Slot: aic_system_autonomy Description: Whether it can change its own remit or stays under outside direction.
--     * Slot: aic_system_human_teaming Description: How people and the system share the work, if they do.
--     * Slot: aic_system_stage Description: The stage of its life the system is in now.
--     * Slot: aic_id Description: The record's identifier, unique among the records it sits with, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the record's author gives it.
--     * Slot: description Description: What the record describes, in its author's words.
-- # Class: AicExpertSystem Description: A system that puts what human specialists know into a form it can reason with.
--     * Slot: aic_expert_inference Description: How the system draws conclusions from that knowledge.
--     * Slot: aic_system_type Description: Which class this record is: AicSystem or a kind of it.
--     * Slot: aic_system_purpose Description: What the system is meant to do.
--     * Slot: aic_system_scope Description: How wide a range of problems the system can take on.
--     * Slot: aic_system_automated Description: Whether it runs without a person acting at each step, under the conditions given.
--     * Slot: aic_system_autonomy Description: Whether it can change its own remit or stays under outside direction.
--     * Slot: aic_system_human_teaming Description: How people and the system share the work, if they do.
--     * Slot: aic_system_stage Description: The stage of its life the system is in now.
--     * Slot: aic_id Description: The record's identifier, unique among the records it sits with, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the record's author gives it.
--     * Slot: description Description: What the record describes, in its author's words.
-- # Class: AicRobot Description: A system that moves or acts on physical things through its own actuators.
--     * Slot: aic_system_type Description: Which class this record is: AicSystem or a kind of it.
--     * Slot: aic_system_purpose Description: What the system is meant to do.
--     * Slot: aic_system_scope Description: How wide a range of problems the system can take on.
--     * Slot: aic_system_automated Description: Whether it runs without a person acting at each step, under the conditions given.
--     * Slot: aic_system_autonomy Description: Whether it can change its own remit or stays under outside direction.
--     * Slot: aic_system_human_teaming Description: How people and the system share the work, if they do.
--     * Slot: aic_system_stage Description: The stage of its life the system is in now.
--     * Slot: aic_id Description: The record's identifier, unique among the records it sits with, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the record's author gives it.
--     * Slot: description Description: What the record describes, in its author's words.
-- # Class: AicComponent Description: A part of a system that does one job in it.
--     * Slot: aic_component_step Description: The step from data to action this part performs.
--     * Slot: aic_id Description: The record's identifier, unique among the records it sits with, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the record's author gives it.
--     * Slot: description Description: What the record describes, in its author's words.
--     * Slot: AicEcosystem_aic_id Description: Autocreated FK slot
-- # Class: AicKnowledge Description: A body of what a system knows, in a form it can use.
--     * Slot: aic_knowledge_kind Description: Whether it states what is the case or what to do.
--     * Slot: aic_knowledge_representation Description: The form it is held in, such as rules, a graph or an ontology.
--     * Slot: aic_id Description: The record's identifier, unique among the records it sits with, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the record's author gives it.
--     * Slot: description Description: What the record describes, in its author's words.
--     * Slot: AicEcosystem_aic_id Description: Autocreated FK slot
-- # Class: AicTask Description: Something a system is asked to get done.
--     * Slot: aic_task_kind Description: The named kind of task it is, where it is one.
--     * Slot: aic_task_goal Description: What getting the task done achieves.
--     * Slot: aic_id Description: The record's identifier, unique among the records it sits with, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the record's author gives it.
--     * Slot: description Description: What the record describes, in its author's words.
--     * Slot: AicEcosystem_aic_id Description: Autocreated FK slot
-- # Class: AicModel Description: A representation of something, made so that a system can compute with it.
--     * Slot: aic_model_type Description: Which class this record is: AicModel or a kind of it.
--     * Slot: aic_model_version Description: The version of the model, as its makers number it.
--     * Slot: aic_model_represents Description: What the model stands for, such as a process or a body of data.
--     * Slot: aic_id Description: The record's identifier, unique among the records it sits with, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the record's author gives it.
--     * Slot: description Description: What the record describes, in its author's words.
--     * Slot: AicEcosystem_aic_id Description: Autocreated FK slot
-- # Class: AicMachineLearningModel Description: A model whose numbers were fitted to data by a training run.
--     * Slot: aic_ml_paradigm Description: How the model learned from its data.
--     * Slot: aic_ml_algorithm Description: The family of algorithm that fitted it.
--     * Slot: aic_ml_parameter_count Description: How many numbers training fitted.
--     * Slot: aic_ml_trained_on Description: When the last training run ended.
--     * Slot: aic_ml_retrained_from Description: The earlier model that this one updates by training it again on other data.
--     * Slot: aic_ml_continuous_learning Description: Whether it goes on learning in small steps while in use.
--     * Slot: aic_model_type Description: Which class this record is: AicModel or a kind of it.
--     * Slot: aic_model_version Description: The version of the model, as its makers number it.
--     * Slot: aic_model_represents Description: What the model stands for, such as a process or a body of data.
--     * Slot: aic_id Description: The record's identifier, unique among the records it sits with, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the record's author gives it.
--     * Slot: description Description: What the record describes, in its author's words.
-- # Class: AicNeuralNetworkModel Description: A kind of machine learning model built from layers of simple connected units.
--     * Slot: aic_network_architecture Description: How its layers are connected.
--     * Slot: aic_network_layer_count Description: How many layers it has.
--     * Slot: aic_ml_paradigm Description: How the model learned from its data.
--     * Slot: aic_ml_algorithm Description: The family of algorithm that fitted it.
--     * Slot: aic_ml_parameter_count Description: How many numbers training fitted.
--     * Slot: aic_ml_trained_on Description: When the last training run ended.
--     * Slot: aic_ml_retrained_from Description: The earlier model that this one updates by training it again on other data.
--     * Slot: aic_ml_continuous_learning Description: Whether it goes on learning in small steps while in use.
--     * Slot: aic_model_type Description: Which class this record is: AicModel or a kind of it.
--     * Slot: aic_model_version Description: The version of the model, as its makers number it.
--     * Slot: aic_model_represents Description: What the model stands for, such as a process or a body of data.
--     * Slot: aic_id Description: The record's identifier, unique among the records it sits with, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the record's author gives it.
--     * Slot: description Description: What the record describes, in its author's words.
-- # Class: AicDataset Description: A set of data kept together in one format.
--     * Slot: aic_dataset_source Description: Where the data comes from.
--     * Slot: aic_dataset_sample_count Description: How many samples it holds.
--     * Slot: aic_dataset_ground_truth Description: Where the correct answers for its samples come from.
--     * Slot: aic_dataset_holds_pii Description: Whether it holds data that can identify a person.
--     * Slot: aic_id Description: The record's identifier, unique among the records it sits with, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the record's author gives it.
--     * Slot: description Description: What the record describes, in its author's words.
--     * Slot: AicEcosystem_aic_id Description: Autocreated FK slot
-- # Class: AicDataProcess Description: One piece of work done on a dataset.
--     * Slot: id
--     * Slot: aic_data_process_kind Description: The kind of work.
--     * Slot: aic_data_process_method Description: How it was done, such as the tool used.
--     * Slot: aic_data_process_date Description: When it was done.
--     * Slot: AicDataset_aic_id Description: Autocreated FK slot
-- # Class: AicTrustworthinessClaim Description: A claim that a system has a property people can rely on, with what backs it.
--     * Slot: aic_claim_system Description: The system the claim is about.
--     * Slot: aic_claim_property Description: The property claimed.
--     * Slot: aic_claim_measure Description: How the property was measured, if it was.
--     * Slot: aic_id Description: The record's identifier, unique among the records it sits with, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the record's author gives it.
--     * Slot: description Description: What the record describes, in its author's words.
--     * Slot: AicEcosystem_aic_id Description: Autocreated FK slot
-- # Class: AicAssessment Description: One verification or validation of a system.
--     * Slot: aic_assessment_kind Description: Whether it checks the system against its specification or against its purpose.
--     * Slot: aic_assessment_system Description: The system assessed.
--     * Slot: aic_assessment_method Description: How the system was assessed.
--     * Slot: aic_assessment_result Description: What the assessment found.
--     * Slot: aic_assessment_date Description: When it was done.
--     * Slot: aic_id Description: The record's identifier, unique among the records it sits with, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the record's author gives it.
--     * Slot: description Description: What the record describes, in its author's words.
--     * Slot: AicEcosystem_aic_id Description: Autocreated FK slot
-- # Class: AicLifecycleProcess Description: A piece of work done at one stage of a system's life.
--     * Slot: aic_lifecycle_stage Description: The stage the work belongs to.
--     * Slot: aic_lifecycle_system Description: The system the work is for.
--     * Slot: aic_lifecycle_responsible Description: The party that answers for the work.
--     * Slot: aic_lifecycle_start Description: When the work began.
--     * Slot: aic_lifecycle_end Description: When the work ended.
--     * Slot: aic_id Description: The record's identifier, unique among the records it sits with, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the record's author gives it.
--     * Slot: description Description: What the record describes, in its author's words.
--     * Slot: AicEcosystem_aic_id Description: Autocreated FK slot
-- # Class: AicStakeholder Description: A person, group or organization with a part in an AI system or an interest in it.
--     * Slot: aic_stakeholder_role Description: The part the party plays.
--     * Slot: aic_stakeholder_organization Description: The organization the party is or belongs to.
--     * Slot: aic_stakeholder_contact Description: How to reach the party.
--     * Slot: aic_id Description: The record's identifier, unique among the records it sits with, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the record's author gives it.
--     * Slot: description Description: What the record describes, in its author's words.
--     * Slot: AicEcosystem_aic_id Description: Autocreated FK slot
-- # Class: AicPrediction Description: A result a system worked out for one case.
--     * Slot: aic_prediction_system Description: The system that produced it.
--     * Slot: aic_prediction_value Description: What it says.
--     * Slot: aic_prediction_confidence Description: How sure the system was, from 0 to 1.
--     * Slot: aic_id Description: The record's identifier, unique among the records it sits with, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the record's author gives it.
--     * Slot: description Description: What the record describes, in its author's words.
--     * Slot: AicEcosystem_aic_id Description: Autocreated FK slot
-- # Class: AicDecision Description: A choice made on the strength of some predictions.
--     * Slot: aic_decision_outcome Description: What was chosen.
--     * Slot: aic_decision_criteria Description: How the choice was made, such as a threshold or a rule.
--     * Slot: aic_id Description: The record's identifier, unique among the records it sits with, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the record's author gives it.
--     * Slot: description Description: What the record describes, in its author's words.
--     * Slot: AicEcosystem_aic_id Description: Autocreated FK slot
-- # Class: AicAction Description: What was done because of a decision.
--     * Slot: aic_action_decision Description: The decision it carries out.
--     * Slot: aic_action_target Description: What it acted on.
--     * Slot: aic_action_time Description: When it was done.
--     * Slot: aic_id Description: The record's identifier, unique among the records it sits with, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the record's author gives it.
--     * Slot: description Description: What the record describes, in its author's words.
--     * Slot: AicEcosystem_aic_id Description: Autocreated FK slot
-- # Class: AicApplication Description: One use of a system in a line of work.
--     * Slot: aic_application_system Description: The system applied.
--     * Slot: aic_application_domain Description: The domain, where it is one the standard works through.
--     * Slot: aic_application_sector Description: The sector, in the words of whoever keeps the record.
--     * Slot: aic_application_purpose Description: What this use is for.
--     * Slot: aic_id Description: The record's identifier, unique among the records it sits with, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the record's author gives it.
--     * Slot: description Description: What the record describes, in its author's words.
--     * Slot: AicEcosystem_aic_id Description: Autocreated FK slot
-- # Class: AicResourcePool Description: A body of computing resource that AI work can draw on.
--     * Slot: aic_pool_kind Description: The kind of resource.
--     * Slot: aic_pool_hardware Description: The hardware in it, such as a model of accelerator.
--     * Slot: aic_pool_capacity Description: How much it offers, in units its owner uses.
--     * Slot: aic_id Description: The record's identifier, unique among the records it sits with, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the record's author gives it.
--     * Slot: description Description: What the record describes, in its author's words.
--     * Slot: AicEcosystem_aic_id Description: Autocreated FK slot
-- # Class: AicIotDevice Description: A connected device that reads from or acts on its physical surroundings.
--     * Slot: aic_id Description: The record's identifier, unique among the records it sits with, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the record's author gives it.
--     * Slot: description Description: What the record describes, in its author's words.
--     * Slot: AicEcosystem_aic_id Description: Autocreated FK slot
-- # Class: AicIotSystem Description: A networked system that links devices and offers services built on them.
--     * Slot: aic_id Description: The record's identifier, unique among the records it sits with, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the record's author gives it.
--     * Slot: description Description: What the record describes, in its author's words.
--     * Slot: AicEcosystem_aic_id Description: Autocreated FK slot
-- # Class: AicCyberPhysicalSystem Description: Computing and physical processes tied in a loop, each affecting the other.
--     * Slot: aic_cps_iot_system Description: The connected system it runs on, if it does.
--     * Slot: aic_id Description: The record's identifier, unique among the records it sits with, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the record's author gives it.
--     * Slot: description Description: What the record describes, in its author's words.
--     * Slot: AicEcosystem_aic_id Description: Autocreated FK slot
-- # Class: AicSystem_aic_system_approaches
--     * Slot: AicSystem_aic_id Description: Autocreated FK slot
--     * Slot: aic_system_approaches Description: Whether it works symbolically, subsymbolically or both ways.
-- # Class: AicSystem_aic_system_techniques
--     * Slot: AicSystem_aic_id Description: Autocreated FK slot
--     * Slot: aic_system_techniques Description: The families of technique it is built with.
-- # Class: AicSystem_aic_system_fields
--     * Slot: AicSystem_aic_id Description: Autocreated FK slot
--     * Slot: aic_system_fields Description: The fields of AI it belongs to.
-- # Class: AicSystem_aic_system_steps
--     * Slot: AicSystem_aic_id Description: Autocreated FK slot
--     * Slot: aic_system_steps Description: The steps from data to action that it performs.
-- # Class: AicSystem_aic_system_components
--     * Slot: AicSystem_aic_id Description: Autocreated FK slot
--     * Slot: aic_system_components_aic_id Description: The parts it is made of.
-- # Class: AicSystem_aic_system_models
--     * Slot: AicSystem_aic_id Description: Autocreated FK slot
--     * Slot: aic_system_models_aic_id Description: The models it uses.
-- # Class: AicSystem_aic_system_datasets
--     * Slot: AicSystem_aic_id Description: Autocreated FK slot
--     * Slot: aic_system_datasets_aic_id Description: The datasets it uses.
-- # Class: AicSystem_aic_system_tasks
--     * Slot: AicSystem_aic_id Description: Autocreated FK slot
--     * Slot: aic_system_tasks_aic_id Description: The tasks it takes on.
-- # Class: AicSystem_aic_system_stakeholders
--     * Slot: AicSystem_aic_id Description: Autocreated FK slot
--     * Slot: aic_system_stakeholders_aic_id Description: The parties around it.
-- # Class: AicSystem_aic_system_resource_pools
--     * Slot: AicSystem_aic_id Description: Autocreated FK slot
--     * Slot: aic_system_resource_pools_aic_id Description: The computing resources it runs on.
-- # Class: AicSystem_aic_system_jurisdictional_issues
--     * Slot: AicSystem_aic_id Description: Autocreated FK slot
--     * Slot: aic_system_jurisdictional_issues Description: The legal questions that follow from where it is built, offered or used.
-- # Class: AicSystem_aic_system_societal_impacts
--     * Slot: AicSystem_aic_id Description: Autocreated FK slot
--     * Slot: aic_system_societal_impacts Description: The effects it may have on people and society beyond its users.
-- # Class: AicAgent_aic_agent_goals
--     * Slot: AicAgent_aic_id Description: Autocreated FK slot
--     * Slot: aic_agent_goals Description: The goals the agent pursues.
-- # Class: AicAgent_aic_system_approaches
--     * Slot: AicAgent_aic_id Description: Autocreated FK slot
--     * Slot: aic_system_approaches Description: Whether it works symbolically, subsymbolically or both ways.
-- # Class: AicAgent_aic_system_techniques
--     * Slot: AicAgent_aic_id Description: Autocreated FK slot
--     * Slot: aic_system_techniques Description: The families of technique it is built with.
-- # Class: AicAgent_aic_system_fields
--     * Slot: AicAgent_aic_id Description: Autocreated FK slot
--     * Slot: aic_system_fields Description: The fields of AI it belongs to.
-- # Class: AicAgent_aic_system_steps
--     * Slot: AicAgent_aic_id Description: Autocreated FK slot
--     * Slot: aic_system_steps Description: The steps from data to action that it performs.
-- # Class: AicAgent_aic_system_components
--     * Slot: AicAgent_aic_id Description: Autocreated FK slot
--     * Slot: aic_system_components_aic_id Description: The parts it is made of.
-- # Class: AicAgent_aic_system_models
--     * Slot: AicAgent_aic_id Description: Autocreated FK slot
--     * Slot: aic_system_models_aic_id Description: The models it uses.
-- # Class: AicAgent_aic_system_datasets
--     * Slot: AicAgent_aic_id Description: Autocreated FK slot
--     * Slot: aic_system_datasets_aic_id Description: The datasets it uses.
-- # Class: AicAgent_aic_system_tasks
--     * Slot: AicAgent_aic_id Description: Autocreated FK slot
--     * Slot: aic_system_tasks_aic_id Description: The tasks it takes on.
-- # Class: AicAgent_aic_system_stakeholders
--     * Slot: AicAgent_aic_id Description: Autocreated FK slot
--     * Slot: aic_system_stakeholders_aic_id Description: The parties around it.
-- # Class: AicAgent_aic_system_resource_pools
--     * Slot: AicAgent_aic_id Description: Autocreated FK slot
--     * Slot: aic_system_resource_pools_aic_id Description: The computing resources it runs on.
-- # Class: AicAgent_aic_system_jurisdictional_issues
--     * Slot: AicAgent_aic_id Description: Autocreated FK slot
--     * Slot: aic_system_jurisdictional_issues Description: The legal questions that follow from where it is built, offered or used.
-- # Class: AicAgent_aic_system_societal_impacts
--     * Slot: AicAgent_aic_id Description: Autocreated FK slot
--     * Slot: aic_system_societal_impacts Description: The effects it may have on people and society beyond its users.
-- # Class: AicExpertSystem_aic_expert_knowledge
--     * Slot: AicExpertSystem_aic_id Description: Autocreated FK slot
--     * Slot: aic_expert_knowledge_aic_id Description: The bodies of knowledge the system reasons with.
-- # Class: AicExpertSystem_aic_system_approaches
--     * Slot: AicExpertSystem_aic_id Description: Autocreated FK slot
--     * Slot: aic_system_approaches Description: Whether it works symbolically, subsymbolically or both ways.
-- # Class: AicExpertSystem_aic_system_techniques
--     * Slot: AicExpertSystem_aic_id Description: Autocreated FK slot
--     * Slot: aic_system_techniques Description: The families of technique it is built with.
-- # Class: AicExpertSystem_aic_system_fields
--     * Slot: AicExpertSystem_aic_id Description: Autocreated FK slot
--     * Slot: aic_system_fields Description: The fields of AI it belongs to.
-- # Class: AicExpertSystem_aic_system_steps
--     * Slot: AicExpertSystem_aic_id Description: Autocreated FK slot
--     * Slot: aic_system_steps Description: The steps from data to action that it performs.
-- # Class: AicExpertSystem_aic_system_components
--     * Slot: AicExpertSystem_aic_id Description: Autocreated FK slot
--     * Slot: aic_system_components_aic_id Description: The parts it is made of.
-- # Class: AicExpertSystem_aic_system_models
--     * Slot: AicExpertSystem_aic_id Description: Autocreated FK slot
--     * Slot: aic_system_models_aic_id Description: The models it uses.
-- # Class: AicExpertSystem_aic_system_datasets
--     * Slot: AicExpertSystem_aic_id Description: Autocreated FK slot
--     * Slot: aic_system_datasets_aic_id Description: The datasets it uses.
-- # Class: AicExpertSystem_aic_system_tasks
--     * Slot: AicExpertSystem_aic_id Description: Autocreated FK slot
--     * Slot: aic_system_tasks_aic_id Description: The tasks it takes on.
-- # Class: AicExpertSystem_aic_system_stakeholders
--     * Slot: AicExpertSystem_aic_id Description: Autocreated FK slot
--     * Slot: aic_system_stakeholders_aic_id Description: The parties around it.
-- # Class: AicExpertSystem_aic_system_resource_pools
--     * Slot: AicExpertSystem_aic_id Description: Autocreated FK slot
--     * Slot: aic_system_resource_pools_aic_id Description: The computing resources it runs on.
-- # Class: AicExpertSystem_aic_system_jurisdictional_issues
--     * Slot: AicExpertSystem_aic_id Description: Autocreated FK slot
--     * Slot: aic_system_jurisdictional_issues Description: The legal questions that follow from where it is built, offered or used.
-- # Class: AicExpertSystem_aic_system_societal_impacts
--     * Slot: AicExpertSystem_aic_id Description: Autocreated FK slot
--     * Slot: aic_system_societal_impacts Description: The effects it may have on people and society beyond its users.
-- # Class: AicRobot_aic_robot_actuators
--     * Slot: AicRobot_aic_id Description: Autocreated FK slot
--     * Slot: aic_robot_actuators Description: The actuators through which the robot acts.
-- # Class: AicRobot_aic_robot_sensors
--     * Slot: AicRobot_aic_id Description: Autocreated FK slot
--     * Slot: aic_robot_sensors Description: The sensors through which it perceives.
-- # Class: AicRobot_aic_system_approaches
--     * Slot: AicRobot_aic_id Description: Autocreated FK slot
--     * Slot: aic_system_approaches Description: Whether it works symbolically, subsymbolically or both ways.
-- # Class: AicRobot_aic_system_techniques
--     * Slot: AicRobot_aic_id Description: Autocreated FK slot
--     * Slot: aic_system_techniques Description: The families of technique it is built with.
-- # Class: AicRobot_aic_system_fields
--     * Slot: AicRobot_aic_id Description: Autocreated FK slot
--     * Slot: aic_system_fields Description: The fields of AI it belongs to.
-- # Class: AicRobot_aic_system_steps
--     * Slot: AicRobot_aic_id Description: Autocreated FK slot
--     * Slot: aic_system_steps Description: The steps from data to action that it performs.
-- # Class: AicRobot_aic_system_components
--     * Slot: AicRobot_aic_id Description: Autocreated FK slot
--     * Slot: aic_system_components_aic_id Description: The parts it is made of.
-- # Class: AicRobot_aic_system_models
--     * Slot: AicRobot_aic_id Description: Autocreated FK slot
--     * Slot: aic_system_models_aic_id Description: The models it uses.
-- # Class: AicRobot_aic_system_datasets
--     * Slot: AicRobot_aic_id Description: Autocreated FK slot
--     * Slot: aic_system_datasets_aic_id Description: The datasets it uses.
-- # Class: AicRobot_aic_system_tasks
--     * Slot: AicRobot_aic_id Description: Autocreated FK slot
--     * Slot: aic_system_tasks_aic_id Description: The tasks it takes on.
-- # Class: AicRobot_aic_system_stakeholders
--     * Slot: AicRobot_aic_id Description: Autocreated FK slot
--     * Slot: aic_system_stakeholders_aic_id Description: The parties around it.
-- # Class: AicRobot_aic_system_resource_pools
--     * Slot: AicRobot_aic_id Description: Autocreated FK slot
--     * Slot: aic_system_resource_pools_aic_id Description: The computing resources it runs on.
-- # Class: AicRobot_aic_system_jurisdictional_issues
--     * Slot: AicRobot_aic_id Description: Autocreated FK slot
--     * Slot: aic_system_jurisdictional_issues Description: The legal questions that follow from where it is built, offered or used.
-- # Class: AicRobot_aic_system_societal_impacts
--     * Slot: AicRobot_aic_id Description: Autocreated FK slot
--     * Slot: aic_system_societal_impacts Description: The effects it may have on people and society beyond its users.
-- # Class: AicComponent_aic_component_depends_on
--     * Slot: AicComponent_aic_id Description: Autocreated FK slot
--     * Slot: aic_component_depends_on_aic_id Description: The other parts this part needs.
-- # Class: AicTask_aic_task_languages
--     * Slot: AicTask_aic_id Description: Autocreated FK slot
--     * Slot: aic_task_languages Description: The human languages the task works in, as language tags such as en or fr-CA.
-- # Class: AicTask_aic_task_performance_measures
--     * Slot: AicTask_aic_id Description: Autocreated FK slot
--     * Slot: aic_task_performance_measures Description: What is measured to judge how well it is done, such as accuracy.
-- # Class: AicMachineLearningModel_aic_ml_datasets
--     * Slot: AicMachineLearningModel_aic_id Description: Autocreated FK slot
--     * Slot: aic_ml_datasets_aic_id Description: The datasets used to fit, tune and test it.
-- # Class: AicMachineLearningModel_aic_ml_hyperparameters
--     * Slot: AicMachineLearningModel_aic_id Description: Autocreated FK slot
--     * Slot: aic_ml_hyperparameters Description: The settings fixed before training, each as name=value.
-- # Class: AicNeuralNetworkModel_aic_network_activation_functions
--     * Slot: AicNeuralNetworkModel_aic_id Description: Autocreated FK slot
--     * Slot: aic_network_activation_functions Description: The functions its units use to turn their inputs into an output.
-- # Class: AicNeuralNetworkModel_aic_ml_datasets
--     * Slot: AicNeuralNetworkModel_aic_id Description: Autocreated FK slot
--     * Slot: aic_ml_datasets_aic_id Description: The datasets used to fit, tune and test it.
-- # Class: AicNeuralNetworkModel_aic_ml_hyperparameters
--     * Slot: AicNeuralNetworkModel_aic_id Description: Autocreated FK slot
--     * Slot: aic_ml_hyperparameters Description: The settings fixed before training, each as name=value.
-- # Class: AicDataset_aic_dataset_roles
--     * Slot: AicDataset_aic_id Description: Autocreated FK slot
--     * Slot: aic_dataset_roles Description: What the dataset is used for.
-- # Class: AicDataset_aic_dataset_labels
--     * Slot: AicDataset_aic_id Description: Autocreated FK slot
--     * Slot: aic_dataset_labels Description: The labels its samples can carry.
-- # Class: AicTrustworthinessClaim_aic_claim_evidence
--     * Slot: AicTrustworthinessClaim_aic_id Description: Autocreated FK slot
--     * Slot: aic_claim_evidence Description: What backs the claim.
-- # Class: AicLifecycleProcess_aic_lifecycle_inputs
--     * Slot: AicLifecycleProcess_aic_id Description: Autocreated FK slot
--     * Slot: aic_lifecycle_inputs Description: What the work starts from.
-- # Class: AicLifecycleProcess_aic_lifecycle_outputs
--     * Slot: AicLifecycleProcess_aic_id Description: Autocreated FK slot
--     * Slot: aic_lifecycle_outputs Description: What the work produces.
-- # Class: AicStakeholder_aic_stakeholder_sub_roles
--     * Slot: AicStakeholder_aic_id Description: Autocreated FK slot
--     * Slot: aic_stakeholder_sub_roles Description: The narrower parts it plays within that role.
-- # Class: AicStakeholder_aic_stakeholder_responsibilities
--     * Slot: AicStakeholder_aic_id Description: Autocreated FK slot
--     * Slot: aic_stakeholder_responsibilities Description: What the party answers for.
-- # Class: AicDecision_aic_decision_predictions
--     * Slot: AicDecision_aic_id Description: Autocreated FK slot
--     * Slot: aic_decision_predictions_aic_id Description: The predictions it rests on.
-- # Class: AicIotDevice_aic_device_senses
--     * Slot: AicIotDevice_aic_id Description: Autocreated FK slot
--     * Slot: aic_device_senses Description: What the device reads from its surroundings.
-- # Class: AicIotDevice_aic_device_actuates
--     * Slot: AicIotDevice_aic_id Description: Autocreated FK slot
--     * Slot: aic_device_actuates Description: What the device acts on.
-- # Class: AicIotSystem_aic_iot_devices
--     * Slot: AicIotSystem_aic_id Description: Autocreated FK slot
--     * Slot: aic_iot_devices_aic_id Description: The devices in it.
-- # Class: AicIotSystem_aic_iot_ai_systems
--     * Slot: AicIotSystem_aic_id Description: Autocreated FK slot
--     * Slot: aic_iot_ai_systems_aic_id Description: The AI systems that work with it.
-- # Class: AicCyberPhysicalSystem_aic_cps_physical_processes
--     * Slot: AicCyberPhysicalSystem_aic_id Description: Autocreated FK slot
--     * Slot: aic_cps_physical_processes Description: The physical processes it senses and controls.
-- # Class: AicCyberPhysicalSystem_aic_cps_ai_systems
--     * Slot: AicCyberPhysicalSystem_aic_id Description: Autocreated FK slot
--     * Slot: aic_cps_ai_systems_aic_id Description: The AI systems that work with it.

CREATE TABLE "AicRecordMixin" (
	aic_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	PRIMARY KEY (aic_id)
);
CREATE INDEX "ix_AicRecordMixin_aic_id" ON "AicRecordMixin" (aic_id);

CREATE TABLE "AicEcosystem" (
	aic_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	PRIMARY KEY (aic_id)
);
CREATE INDEX "ix_AicEcosystem_aic_id" ON "AicEcosystem" (aic_id);

CREATE TABLE "AicAgent" (
	aic_agent_environment TEXT,
	aic_system_type TEXT NOT NULL,
	aic_system_purpose TEXT,
	aic_system_scope VARCHAR(10),
	aic_system_automated BOOLEAN,
	aic_system_autonomy VARCHAR(12),
	aic_system_human_teaming TEXT,
	aic_system_stage VARCHAR(27),
	aic_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	PRIMARY KEY (aic_id)
);
CREATE INDEX "ix_AicAgent_aic_id" ON "AicAgent" (aic_id);

CREATE TABLE "AicExpertSystem" (
	aic_expert_inference TEXT,
	aic_system_type TEXT NOT NULL,
	aic_system_purpose TEXT,
	aic_system_scope VARCHAR(10),
	aic_system_automated BOOLEAN,
	aic_system_autonomy VARCHAR(12),
	aic_system_human_teaming TEXT,
	aic_system_stage VARCHAR(27),
	aic_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	PRIMARY KEY (aic_id)
);
CREATE INDEX "ix_AicExpertSystem_aic_id" ON "AicExpertSystem" (aic_id);

CREATE TABLE "AicRobot" (
	aic_system_type TEXT NOT NULL,
	aic_system_purpose TEXT,
	aic_system_scope VARCHAR(10),
	aic_system_automated BOOLEAN,
	aic_system_autonomy VARCHAR(12),
	aic_system_human_teaming TEXT,
	aic_system_stage VARCHAR(27),
	aic_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	PRIMARY KEY (aic_id)
);
CREATE INDEX "ix_AicRobot_aic_id" ON "AicRobot" (aic_id);

CREATE TABLE "AicMachineLearningModel" (
	aic_ml_paradigm VARCHAR(15),
	aic_ml_algorithm VARCHAR(22),
	aic_ml_parameter_count INTEGER,
	aic_ml_trained_on DATE,
	aic_ml_retrained_from TEXT,
	aic_ml_continuous_learning BOOLEAN,
	aic_model_type TEXT NOT NULL,
	aic_model_version TEXT,
	aic_model_represents TEXT,
	aic_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	PRIMARY KEY (aic_id),
	FOREIGN KEY(aic_ml_retrained_from) REFERENCES "AicMachineLearningModel" (aic_id)
);
CREATE INDEX "ix_AicMachineLearningModel_aic_id" ON "AicMachineLearningModel" (aic_id);

CREATE TABLE "AicSystem" (
	aic_system_type TEXT NOT NULL,
	aic_system_purpose TEXT,
	aic_system_scope VARCHAR(10),
	aic_system_automated BOOLEAN,
	aic_system_autonomy VARCHAR(12),
	aic_system_human_teaming TEXT,
	aic_system_stage VARCHAR(27),
	aic_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	"AicEcosystem_aic_id" TEXT,
	PRIMARY KEY (aic_id),
	FOREIGN KEY("AicEcosystem_aic_id") REFERENCES "AicEcosystem" (aic_id)
);
CREATE INDEX "ix_AicSystem_aic_id" ON "AicSystem" (aic_id);

CREATE TABLE "AicComponent" (
	aic_component_step VARCHAR(22),
	aic_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	"AicEcosystem_aic_id" TEXT,
	PRIMARY KEY (aic_id),
	FOREIGN KEY("AicEcosystem_aic_id") REFERENCES "AicEcosystem" (aic_id)
);
CREATE INDEX "ix_AicComponent_aic_id" ON "AicComponent" (aic_id);

CREATE TABLE "AicKnowledge" (
	aic_knowledge_kind VARCHAR(11),
	aic_knowledge_representation TEXT,
	aic_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	"AicEcosystem_aic_id" TEXT,
	PRIMARY KEY (aic_id),
	FOREIGN KEY("AicEcosystem_aic_id") REFERENCES "AicEcosystem" (aic_id)
);
CREATE INDEX "ix_AicKnowledge_aic_id" ON "AicKnowledge" (aic_id);

CREATE TABLE "AicTask" (
	aic_task_kind VARCHAR(30),
	aic_task_goal TEXT,
	aic_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	"AicEcosystem_aic_id" TEXT,
	PRIMARY KEY (aic_id),
	FOREIGN KEY("AicEcosystem_aic_id") REFERENCES "AicEcosystem" (aic_id)
);
CREATE INDEX "ix_AicTask_aic_id" ON "AicTask" (aic_id);

CREATE TABLE "AicModel" (
	aic_model_type TEXT NOT NULL,
	aic_model_version TEXT,
	aic_model_represents TEXT,
	aic_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	"AicEcosystem_aic_id" TEXT,
	PRIMARY KEY (aic_id),
	FOREIGN KEY("AicEcosystem_aic_id") REFERENCES "AicEcosystem" (aic_id)
);
CREATE INDEX "ix_AicModel_aic_id" ON "AicModel" (aic_id);

CREATE TABLE "AicNeuralNetworkModel" (
	aic_network_architecture VARCHAR(22),
	aic_network_layer_count INTEGER,
	aic_ml_paradigm VARCHAR(15),
	aic_ml_algorithm VARCHAR(22),
	aic_ml_parameter_count INTEGER,
	aic_ml_trained_on DATE,
	aic_ml_retrained_from TEXT,
	aic_ml_continuous_learning BOOLEAN,
	aic_model_type TEXT NOT NULL,
	aic_model_version TEXT,
	aic_model_represents TEXT,
	aic_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	PRIMARY KEY (aic_id),
	FOREIGN KEY(aic_ml_retrained_from) REFERENCES "AicMachineLearningModel" (aic_id)
);
CREATE INDEX "ix_AicNeuralNetworkModel_aic_id" ON "AicNeuralNetworkModel" (aic_id);

CREATE TABLE "AicDataset" (
	aic_dataset_source TEXT,
	aic_dataset_sample_count INTEGER,
	aic_dataset_ground_truth TEXT,
	aic_dataset_holds_pii BOOLEAN,
	aic_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	"AicEcosystem_aic_id" TEXT,
	PRIMARY KEY (aic_id),
	FOREIGN KEY("AicEcosystem_aic_id") REFERENCES "AicEcosystem" (aic_id)
);
CREATE INDEX "ix_AicDataset_aic_id" ON "AicDataset" (aic_id);

CREATE TABLE "AicStakeholder" (
	aic_stakeholder_role VARCHAR(18) NOT NULL,
	aic_stakeholder_organization TEXT,
	aic_stakeholder_contact TEXT,
	aic_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	"AicEcosystem_aic_id" TEXT,
	PRIMARY KEY (aic_id),
	FOREIGN KEY("AicEcosystem_aic_id") REFERENCES "AicEcosystem" (aic_id)
);
CREATE INDEX "ix_AicStakeholder_aic_id" ON "AicStakeholder" (aic_id);

CREATE TABLE "AicDecision" (
	aic_decision_outcome TEXT NOT NULL,
	aic_decision_criteria TEXT,
	aic_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	"AicEcosystem_aic_id" TEXT,
	PRIMARY KEY (aic_id),
	FOREIGN KEY("AicEcosystem_aic_id") REFERENCES "AicEcosystem" (aic_id)
);
CREATE INDEX "ix_AicDecision_aic_id" ON "AicDecision" (aic_id);

CREATE TABLE "AicResourcePool" (
	aic_pool_kind VARCHAR(39),
	aic_pool_hardware TEXT,
	aic_pool_capacity TEXT,
	aic_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	"AicEcosystem_aic_id" TEXT,
	PRIMARY KEY (aic_id),
	FOREIGN KEY("AicEcosystem_aic_id") REFERENCES "AicEcosystem" (aic_id)
);
CREATE INDEX "ix_AicResourcePool_aic_id" ON "AicResourcePool" (aic_id);

CREATE TABLE "AicIotDevice" (
	aic_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	"AicEcosystem_aic_id" TEXT,
	PRIMARY KEY (aic_id),
	FOREIGN KEY("AicEcosystem_aic_id") REFERENCES "AicEcosystem" (aic_id)
);
CREATE INDEX "ix_AicIotDevice_aic_id" ON "AicIotDevice" (aic_id);

CREATE TABLE "AicIotSystem" (
	aic_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	"AicEcosystem_aic_id" TEXT,
	PRIMARY KEY (aic_id),
	FOREIGN KEY("AicEcosystem_aic_id") REFERENCES "AicEcosystem" (aic_id)
);
CREATE INDEX "ix_AicIotSystem_aic_id" ON "AicIotSystem" (aic_id);

CREATE TABLE "AicAgent_aic_agent_goals" (
	"AicAgent_aic_id" TEXT,
	aic_agent_goals TEXT NOT NULL,
	PRIMARY KEY ("AicAgent_aic_id", aic_agent_goals),
	FOREIGN KEY("AicAgent_aic_id") REFERENCES "AicAgent" (aic_id)
);
CREATE INDEX "ix_AicAgent_aic_agent_goals_aic_agent_goals" ON "AicAgent_aic_agent_goals" (aic_agent_goals);
CREATE INDEX "ix_AicAgent_aic_agent_goals_AicAgent_aic_id" ON "AicAgent_aic_agent_goals" ("AicAgent_aic_id");

CREATE TABLE "AicAgent_aic_system_approaches" (
	"AicAgent_aic_id" TEXT,
	aic_system_approaches VARCHAR(11),
	PRIMARY KEY ("AicAgent_aic_id", aic_system_approaches),
	FOREIGN KEY("AicAgent_aic_id") REFERENCES "AicAgent" (aic_id)
);
CREATE INDEX "ix_AicAgent_aic_system_approaches_aic_system_approaches" ON "AicAgent_aic_system_approaches" (aic_system_approaches);
CREATE INDEX "ix_AicAgent_aic_system_approaches_AicAgent_aic_id" ON "AicAgent_aic_system_approaches" ("AicAgent_aic_id");

CREATE TABLE "AicAgent_aic_system_techniques" (
	"AicAgent_aic_id" TEXT,
	aic_system_techniques VARCHAR(19),
	PRIMARY KEY ("AicAgent_aic_id", aic_system_techniques),
	FOREIGN KEY("AicAgent_aic_id") REFERENCES "AicAgent" (aic_id)
);
CREATE INDEX "ix_AicAgent_aic_system_techniques_aic_system_techniques" ON "AicAgent_aic_system_techniques" (aic_system_techniques);
CREATE INDEX "ix_AicAgent_aic_system_techniques_AicAgent_aic_id" ON "AicAgent_aic_system_techniques" ("AicAgent_aic_id");

CREATE TABLE "AicAgent_aic_system_fields" (
	"AicAgent_aic_id" TEXT,
	aic_system_fields VARCHAR(27),
	PRIMARY KEY ("AicAgent_aic_id", aic_system_fields),
	FOREIGN KEY("AicAgent_aic_id") REFERENCES "AicAgent" (aic_id)
);
CREATE INDEX "ix_AicAgent_aic_system_fields_AicAgent_aic_id" ON "AicAgent_aic_system_fields" ("AicAgent_aic_id");
CREATE INDEX "ix_AicAgent_aic_system_fields_aic_system_fields" ON "AicAgent_aic_system_fields" (aic_system_fields);

CREATE TABLE "AicAgent_aic_system_steps" (
	"AicAgent_aic_id" TEXT,
	aic_system_steps VARCHAR(22),
	PRIMARY KEY ("AicAgent_aic_id", aic_system_steps),
	FOREIGN KEY("AicAgent_aic_id") REFERENCES "AicAgent" (aic_id)
);
CREATE INDEX "ix_AicAgent_aic_system_steps_AicAgent_aic_id" ON "AicAgent_aic_system_steps" ("AicAgent_aic_id");
CREATE INDEX "ix_AicAgent_aic_system_steps_aic_system_steps" ON "AicAgent_aic_system_steps" (aic_system_steps);

CREATE TABLE "AicAgent_aic_system_jurisdictional_issues" (
	"AicAgent_aic_id" TEXT,
	aic_system_jurisdictional_issues TEXT,
	PRIMARY KEY ("AicAgent_aic_id", aic_system_jurisdictional_issues),
	FOREIGN KEY("AicAgent_aic_id") REFERENCES "AicAgent" (aic_id)
);
CREATE INDEX "ix_AicAgent_aic_system_jurisdictional_issues_AicAgent_aic_id" ON "AicAgent_aic_system_jurisdictional_issues" ("AicAgent_aic_id");
CREATE INDEX "ix_AicAgent_aic_system_jurisdictional_issues_aic_system_jurisdictional_issues" ON "AicAgent_aic_system_jurisdictional_issues" (aic_system_jurisdictional_issues);

CREATE TABLE "AicAgent_aic_system_societal_impacts" (
	"AicAgent_aic_id" TEXT,
	aic_system_societal_impacts TEXT,
	PRIMARY KEY ("AicAgent_aic_id", aic_system_societal_impacts),
	FOREIGN KEY("AicAgent_aic_id") REFERENCES "AicAgent" (aic_id)
);
CREATE INDEX "ix_AicAgent_aic_system_societal_impacts_AicAgent_aic_id" ON "AicAgent_aic_system_societal_impacts" ("AicAgent_aic_id");
CREATE INDEX "ix_AicAgent_aic_system_societal_impacts_aic_system_societal_impacts" ON "AicAgent_aic_system_societal_impacts" (aic_system_societal_impacts);

CREATE TABLE "AicExpertSystem_aic_system_approaches" (
	"AicExpertSystem_aic_id" TEXT,
	aic_system_approaches VARCHAR(11),
	PRIMARY KEY ("AicExpertSystem_aic_id", aic_system_approaches),
	FOREIGN KEY("AicExpertSystem_aic_id") REFERENCES "AicExpertSystem" (aic_id)
);
CREATE INDEX "ix_AicExpertSystem_aic_system_approaches_aic_system_approaches" ON "AicExpertSystem_aic_system_approaches" (aic_system_approaches);
CREATE INDEX "ix_AicExpertSystem_aic_system_approaches_AicExpertSystem_aic_id" ON "AicExpertSystem_aic_system_approaches" ("AicExpertSystem_aic_id");

CREATE TABLE "AicExpertSystem_aic_system_techniques" (
	"AicExpertSystem_aic_id" TEXT,
	aic_system_techniques VARCHAR(19),
	PRIMARY KEY ("AicExpertSystem_aic_id", aic_system_techniques),
	FOREIGN KEY("AicExpertSystem_aic_id") REFERENCES "AicExpertSystem" (aic_id)
);
CREATE INDEX "ix_AicExpertSystem_aic_system_techniques_AicExpertSystem_aic_id" ON "AicExpertSystem_aic_system_techniques" ("AicExpertSystem_aic_id");
CREATE INDEX "ix_AicExpertSystem_aic_system_techniques_aic_system_techniques" ON "AicExpertSystem_aic_system_techniques" (aic_system_techniques);

CREATE TABLE "AicExpertSystem_aic_system_fields" (
	"AicExpertSystem_aic_id" TEXT,
	aic_system_fields VARCHAR(27),
	PRIMARY KEY ("AicExpertSystem_aic_id", aic_system_fields),
	FOREIGN KEY("AicExpertSystem_aic_id") REFERENCES "AicExpertSystem" (aic_id)
);
CREATE INDEX "ix_AicExpertSystem_aic_system_fields_AicExpertSystem_aic_id" ON "AicExpertSystem_aic_system_fields" ("AicExpertSystem_aic_id");
CREATE INDEX "ix_AicExpertSystem_aic_system_fields_aic_system_fields" ON "AicExpertSystem_aic_system_fields" (aic_system_fields);

CREATE TABLE "AicExpertSystem_aic_system_steps" (
	"AicExpertSystem_aic_id" TEXT,
	aic_system_steps VARCHAR(22),
	PRIMARY KEY ("AicExpertSystem_aic_id", aic_system_steps),
	FOREIGN KEY("AicExpertSystem_aic_id") REFERENCES "AicExpertSystem" (aic_id)
);
CREATE INDEX "ix_AicExpertSystem_aic_system_steps_aic_system_steps" ON "AicExpertSystem_aic_system_steps" (aic_system_steps);
CREATE INDEX "ix_AicExpertSystem_aic_system_steps_AicExpertSystem_aic_id" ON "AicExpertSystem_aic_system_steps" ("AicExpertSystem_aic_id");

CREATE TABLE "AicExpertSystem_aic_system_jurisdictional_issues" (
	"AicExpertSystem_aic_id" TEXT,
	aic_system_jurisdictional_issues TEXT,
	PRIMARY KEY ("AicExpertSystem_aic_id", aic_system_jurisdictional_issues),
	FOREIGN KEY("AicExpertSystem_aic_id") REFERENCES "AicExpertSystem" (aic_id)
);
CREATE INDEX "ix_AicExpertSystem_aic_system_jurisdictional_issues_aic_system_jurisdictional_issues" ON "AicExpertSystem_aic_system_jurisdictional_issues" (aic_system_jurisdictional_issues);
CREATE INDEX "ix_AicExpertSystem_aic_system_jurisdictional_issues_AicExpertSystem_aic_id" ON "AicExpertSystem_aic_system_jurisdictional_issues" ("AicExpertSystem_aic_id");

CREATE TABLE "AicExpertSystem_aic_system_societal_impacts" (
	"AicExpertSystem_aic_id" TEXT,
	aic_system_societal_impacts TEXT,
	PRIMARY KEY ("AicExpertSystem_aic_id", aic_system_societal_impacts),
	FOREIGN KEY("AicExpertSystem_aic_id") REFERENCES "AicExpertSystem" (aic_id)
);
CREATE INDEX "ix_AicExpertSystem_aic_system_societal_impacts_aic_system_societal_impacts" ON "AicExpertSystem_aic_system_societal_impacts" (aic_system_societal_impacts);
CREATE INDEX "ix_AicExpertSystem_aic_system_societal_impacts_AicExpertSystem_aic_id" ON "AicExpertSystem_aic_system_societal_impacts" ("AicExpertSystem_aic_id");

CREATE TABLE "AicRobot_aic_robot_actuators" (
	"AicRobot_aic_id" TEXT,
	aic_robot_actuators TEXT NOT NULL,
	PRIMARY KEY ("AicRobot_aic_id", aic_robot_actuators),
	FOREIGN KEY("AicRobot_aic_id") REFERENCES "AicRobot" (aic_id)
);
CREATE INDEX "ix_AicRobot_aic_robot_actuators_aic_robot_actuators" ON "AicRobot_aic_robot_actuators" (aic_robot_actuators);
CREATE INDEX "ix_AicRobot_aic_robot_actuators_AicRobot_aic_id" ON "AicRobot_aic_robot_actuators" ("AicRobot_aic_id");

CREATE TABLE "AicRobot_aic_robot_sensors" (
	"AicRobot_aic_id" TEXT,
	aic_robot_sensors TEXT,
	PRIMARY KEY ("AicRobot_aic_id", aic_robot_sensors),
	FOREIGN KEY("AicRobot_aic_id") REFERENCES "AicRobot" (aic_id)
);
CREATE INDEX "ix_AicRobot_aic_robot_sensors_aic_robot_sensors" ON "AicRobot_aic_robot_sensors" (aic_robot_sensors);
CREATE INDEX "ix_AicRobot_aic_robot_sensors_AicRobot_aic_id" ON "AicRobot_aic_robot_sensors" ("AicRobot_aic_id");

CREATE TABLE "AicRobot_aic_system_approaches" (
	"AicRobot_aic_id" TEXT,
	aic_system_approaches VARCHAR(11),
	PRIMARY KEY ("AicRobot_aic_id", aic_system_approaches),
	FOREIGN KEY("AicRobot_aic_id") REFERENCES "AicRobot" (aic_id)
);
CREATE INDEX "ix_AicRobot_aic_system_approaches_AicRobot_aic_id" ON "AicRobot_aic_system_approaches" ("AicRobot_aic_id");
CREATE INDEX "ix_AicRobot_aic_system_approaches_aic_system_approaches" ON "AicRobot_aic_system_approaches" (aic_system_approaches);

CREATE TABLE "AicRobot_aic_system_techniques" (
	"AicRobot_aic_id" TEXT,
	aic_system_techniques VARCHAR(19),
	PRIMARY KEY ("AicRobot_aic_id", aic_system_techniques),
	FOREIGN KEY("AicRobot_aic_id") REFERENCES "AicRobot" (aic_id)
);
CREATE INDEX "ix_AicRobot_aic_system_techniques_aic_system_techniques" ON "AicRobot_aic_system_techniques" (aic_system_techniques);
CREATE INDEX "ix_AicRobot_aic_system_techniques_AicRobot_aic_id" ON "AicRobot_aic_system_techniques" ("AicRobot_aic_id");

CREATE TABLE "AicRobot_aic_system_fields" (
	"AicRobot_aic_id" TEXT,
	aic_system_fields VARCHAR(27),
	PRIMARY KEY ("AicRobot_aic_id", aic_system_fields),
	FOREIGN KEY("AicRobot_aic_id") REFERENCES "AicRobot" (aic_id)
);
CREATE INDEX "ix_AicRobot_aic_system_fields_aic_system_fields" ON "AicRobot_aic_system_fields" (aic_system_fields);
CREATE INDEX "ix_AicRobot_aic_system_fields_AicRobot_aic_id" ON "AicRobot_aic_system_fields" ("AicRobot_aic_id");

CREATE TABLE "AicRobot_aic_system_steps" (
	"AicRobot_aic_id" TEXT,
	aic_system_steps VARCHAR(22),
	PRIMARY KEY ("AicRobot_aic_id", aic_system_steps),
	FOREIGN KEY("AicRobot_aic_id") REFERENCES "AicRobot" (aic_id)
);
CREATE INDEX "ix_AicRobot_aic_system_steps_aic_system_steps" ON "AicRobot_aic_system_steps" (aic_system_steps);
CREATE INDEX "ix_AicRobot_aic_system_steps_AicRobot_aic_id" ON "AicRobot_aic_system_steps" ("AicRobot_aic_id");

CREATE TABLE "AicRobot_aic_system_jurisdictional_issues" (
	"AicRobot_aic_id" TEXT,
	aic_system_jurisdictional_issues TEXT,
	PRIMARY KEY ("AicRobot_aic_id", aic_system_jurisdictional_issues),
	FOREIGN KEY("AicRobot_aic_id") REFERENCES "AicRobot" (aic_id)
);
CREATE INDEX "ix_AicRobot_aic_system_jurisdictional_issues_aic_system_jurisdictional_issues" ON "AicRobot_aic_system_jurisdictional_issues" (aic_system_jurisdictional_issues);
CREATE INDEX "ix_AicRobot_aic_system_jurisdictional_issues_AicRobot_aic_id" ON "AicRobot_aic_system_jurisdictional_issues" ("AicRobot_aic_id");

CREATE TABLE "AicRobot_aic_system_societal_impacts" (
	"AicRobot_aic_id" TEXT,
	aic_system_societal_impacts TEXT,
	PRIMARY KEY ("AicRobot_aic_id", aic_system_societal_impacts),
	FOREIGN KEY("AicRobot_aic_id") REFERENCES "AicRobot" (aic_id)
);
CREATE INDEX "ix_AicRobot_aic_system_societal_impacts_aic_system_societal_impacts" ON "AicRobot_aic_system_societal_impacts" (aic_system_societal_impacts);
CREATE INDEX "ix_AicRobot_aic_system_societal_impacts_AicRobot_aic_id" ON "AicRobot_aic_system_societal_impacts" ("AicRobot_aic_id");

CREATE TABLE "AicMachineLearningModel_aic_ml_hyperparameters" (
	"AicMachineLearningModel_aic_id" TEXT,
	aic_ml_hyperparameters TEXT,
	PRIMARY KEY ("AicMachineLearningModel_aic_id", aic_ml_hyperparameters),
	FOREIGN KEY("AicMachineLearningModel_aic_id") REFERENCES "AicMachineLearningModel" (aic_id)
);
CREATE INDEX "ix_AicMachineLearningModel_aic_ml_hyperparameters_AicMachineLearningModel_aic_id" ON "AicMachineLearningModel_aic_ml_hyperparameters" ("AicMachineLearningModel_aic_id");
CREATE INDEX "ix_AicMachineLearningModel_aic_ml_hyperparameters_aic_ml_hyperparameters" ON "AicMachineLearningModel_aic_ml_hyperparameters" (aic_ml_hyperparameters);

CREATE TABLE "AicDataProcess" (
	id INTEGER NOT NULL,
	aic_data_process_kind VARCHAR(25) NOT NULL,
	aic_data_process_method TEXT,
	aic_data_process_date DATE,
	"AicDataset_aic_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("AicDataset_aic_id") REFERENCES "AicDataset" (aic_id)
);
CREATE INDEX "ix_AicDataProcess_id" ON "AicDataProcess" (id);

CREATE TABLE "AicTrustworthinessClaim" (
	aic_claim_system TEXT NOT NULL,
	aic_claim_property VARCHAR(27) NOT NULL,
	aic_claim_measure TEXT,
	aic_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	"AicEcosystem_aic_id" TEXT,
	PRIMARY KEY (aic_id),
	FOREIGN KEY(aic_claim_system) REFERENCES "AicSystem" (aic_id),
	FOREIGN KEY("AicEcosystem_aic_id") REFERENCES "AicEcosystem" (aic_id)
);
CREATE INDEX "ix_AicTrustworthinessClaim_aic_id" ON "AicTrustworthinessClaim" (aic_id);

CREATE TABLE "AicAssessment" (
	aic_assessment_kind VARCHAR(12) NOT NULL,
	aic_assessment_system TEXT NOT NULL,
	aic_assessment_method TEXT,
	aic_assessment_result TEXT,
	aic_assessment_date DATE,
	aic_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	"AicEcosystem_aic_id" TEXT,
	PRIMARY KEY (aic_id),
	FOREIGN KEY(aic_assessment_system) REFERENCES "AicSystem" (aic_id),
	FOREIGN KEY("AicEcosystem_aic_id") REFERENCES "AicEcosystem" (aic_id)
);
CREATE INDEX "ix_AicAssessment_aic_id" ON "AicAssessment" (aic_id);

CREATE TABLE "AicLifecycleProcess" (
	aic_lifecycle_stage VARCHAR(27) NOT NULL,
	aic_lifecycle_system TEXT,
	aic_lifecycle_responsible TEXT,
	aic_lifecycle_start DATE,
	aic_lifecycle_end DATE,
	aic_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	"AicEcosystem_aic_id" TEXT,
	PRIMARY KEY (aic_id),
	FOREIGN KEY(aic_lifecycle_system) REFERENCES "AicSystem" (aic_id),
	FOREIGN KEY(aic_lifecycle_responsible) REFERENCES "AicStakeholder" (aic_id),
	FOREIGN KEY("AicEcosystem_aic_id") REFERENCES "AicEcosystem" (aic_id)
);
CREATE INDEX "ix_AicLifecycleProcess_aic_id" ON "AicLifecycleProcess" (aic_id);

CREATE TABLE "AicPrediction" (
	aic_prediction_system TEXT NOT NULL,
	aic_prediction_value TEXT NOT NULL,
	aic_prediction_confidence FLOAT,
	aic_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	"AicEcosystem_aic_id" TEXT,
	PRIMARY KEY (aic_id),
	FOREIGN KEY(aic_prediction_system) REFERENCES "AicSystem" (aic_id),
	FOREIGN KEY("AicEcosystem_aic_id") REFERENCES "AicEcosystem" (aic_id)
);
CREATE INDEX "ix_AicPrediction_aic_id" ON "AicPrediction" (aic_id);

CREATE TABLE "AicAction" (
	aic_action_decision TEXT NOT NULL,
	aic_action_target TEXT,
	aic_action_time DATETIME,
	aic_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	"AicEcosystem_aic_id" TEXT,
	PRIMARY KEY (aic_id),
	FOREIGN KEY(aic_action_decision) REFERENCES "AicDecision" (aic_id),
	FOREIGN KEY("AicEcosystem_aic_id") REFERENCES "AicEcosystem" (aic_id)
);
CREATE INDEX "ix_AicAction_aic_id" ON "AicAction" (aic_id);

CREATE TABLE "AicApplication" (
	aic_application_system TEXT NOT NULL,
	aic_application_domain VARCHAR(22),
	aic_application_sector TEXT,
	aic_application_purpose TEXT,
	aic_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	"AicEcosystem_aic_id" TEXT,
	PRIMARY KEY (aic_id),
	FOREIGN KEY(aic_application_system) REFERENCES "AicSystem" (aic_id),
	FOREIGN KEY("AicEcosystem_aic_id") REFERENCES "AicEcosystem" (aic_id)
);
CREATE INDEX "ix_AicApplication_aic_id" ON "AicApplication" (aic_id);

CREATE TABLE "AicCyberPhysicalSystem" (
	aic_cps_iot_system TEXT,
	aic_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	"AicEcosystem_aic_id" TEXT,
	PRIMARY KEY (aic_id),
	FOREIGN KEY(aic_cps_iot_system) REFERENCES "AicIotSystem" (aic_id),
	FOREIGN KEY("AicEcosystem_aic_id") REFERENCES "AicEcosystem" (aic_id)
);
CREATE INDEX "ix_AicCyberPhysicalSystem_aic_id" ON "AicCyberPhysicalSystem" (aic_id);

CREATE TABLE "AicSystem_aic_system_approaches" (
	"AicSystem_aic_id" TEXT,
	aic_system_approaches VARCHAR(11),
	PRIMARY KEY ("AicSystem_aic_id", aic_system_approaches),
	FOREIGN KEY("AicSystem_aic_id") REFERENCES "AicSystem" (aic_id)
);
CREATE INDEX "ix_AicSystem_aic_system_approaches_aic_system_approaches" ON "AicSystem_aic_system_approaches" (aic_system_approaches);
CREATE INDEX "ix_AicSystem_aic_system_approaches_AicSystem_aic_id" ON "AicSystem_aic_system_approaches" ("AicSystem_aic_id");

CREATE TABLE "AicSystem_aic_system_techniques" (
	"AicSystem_aic_id" TEXT,
	aic_system_techniques VARCHAR(19),
	PRIMARY KEY ("AicSystem_aic_id", aic_system_techniques),
	FOREIGN KEY("AicSystem_aic_id") REFERENCES "AicSystem" (aic_id)
);
CREATE INDEX "ix_AicSystem_aic_system_techniques_aic_system_techniques" ON "AicSystem_aic_system_techniques" (aic_system_techniques);
CREATE INDEX "ix_AicSystem_aic_system_techniques_AicSystem_aic_id" ON "AicSystem_aic_system_techniques" ("AicSystem_aic_id");

CREATE TABLE "AicSystem_aic_system_fields" (
	"AicSystem_aic_id" TEXT,
	aic_system_fields VARCHAR(27),
	PRIMARY KEY ("AicSystem_aic_id", aic_system_fields),
	FOREIGN KEY("AicSystem_aic_id") REFERENCES "AicSystem" (aic_id)
);
CREATE INDEX "ix_AicSystem_aic_system_fields_aic_system_fields" ON "AicSystem_aic_system_fields" (aic_system_fields);
CREATE INDEX "ix_AicSystem_aic_system_fields_AicSystem_aic_id" ON "AicSystem_aic_system_fields" ("AicSystem_aic_id");

CREATE TABLE "AicSystem_aic_system_steps" (
	"AicSystem_aic_id" TEXT,
	aic_system_steps VARCHAR(22),
	PRIMARY KEY ("AicSystem_aic_id", aic_system_steps),
	FOREIGN KEY("AicSystem_aic_id") REFERENCES "AicSystem" (aic_id)
);
CREATE INDEX "ix_AicSystem_aic_system_steps_AicSystem_aic_id" ON "AicSystem_aic_system_steps" ("AicSystem_aic_id");
CREATE INDEX "ix_AicSystem_aic_system_steps_aic_system_steps" ON "AicSystem_aic_system_steps" (aic_system_steps);

CREATE TABLE "AicSystem_aic_system_components" (
	"AicSystem_aic_id" TEXT,
	aic_system_components_aic_id TEXT,
	PRIMARY KEY ("AicSystem_aic_id", aic_system_components_aic_id),
	FOREIGN KEY("AicSystem_aic_id") REFERENCES "AicSystem" (aic_id),
	FOREIGN KEY(aic_system_components_aic_id) REFERENCES "AicComponent" (aic_id)
);
CREATE INDEX "ix_AicSystem_aic_system_components_aic_system_components_aic_id" ON "AicSystem_aic_system_components" (aic_system_components_aic_id);
CREATE INDEX "ix_AicSystem_aic_system_components_AicSystem_aic_id" ON "AicSystem_aic_system_components" ("AicSystem_aic_id");

CREATE TABLE "AicSystem_aic_system_models" (
	"AicSystem_aic_id" TEXT,
	aic_system_models_aic_id TEXT,
	PRIMARY KEY ("AicSystem_aic_id", aic_system_models_aic_id),
	FOREIGN KEY("AicSystem_aic_id") REFERENCES "AicSystem" (aic_id),
	FOREIGN KEY(aic_system_models_aic_id) REFERENCES "AicModel" (aic_id)
);
CREATE INDEX "ix_AicSystem_aic_system_models_AicSystem_aic_id" ON "AicSystem_aic_system_models" ("AicSystem_aic_id");
CREATE INDEX "ix_AicSystem_aic_system_models_aic_system_models_aic_id" ON "AicSystem_aic_system_models" (aic_system_models_aic_id);

CREATE TABLE "AicSystem_aic_system_datasets" (
	"AicSystem_aic_id" TEXT,
	aic_system_datasets_aic_id TEXT,
	PRIMARY KEY ("AicSystem_aic_id", aic_system_datasets_aic_id),
	FOREIGN KEY("AicSystem_aic_id") REFERENCES "AicSystem" (aic_id),
	FOREIGN KEY(aic_system_datasets_aic_id) REFERENCES "AicDataset" (aic_id)
);
CREATE INDEX "ix_AicSystem_aic_system_datasets_AicSystem_aic_id" ON "AicSystem_aic_system_datasets" ("AicSystem_aic_id");
CREATE INDEX "ix_AicSystem_aic_system_datasets_aic_system_datasets_aic_id" ON "AicSystem_aic_system_datasets" (aic_system_datasets_aic_id);

CREATE TABLE "AicSystem_aic_system_tasks" (
	"AicSystem_aic_id" TEXT,
	aic_system_tasks_aic_id TEXT,
	PRIMARY KEY ("AicSystem_aic_id", aic_system_tasks_aic_id),
	FOREIGN KEY("AicSystem_aic_id") REFERENCES "AicSystem" (aic_id),
	FOREIGN KEY(aic_system_tasks_aic_id) REFERENCES "AicTask" (aic_id)
);
CREATE INDEX "ix_AicSystem_aic_system_tasks_aic_system_tasks_aic_id" ON "AicSystem_aic_system_tasks" (aic_system_tasks_aic_id);
CREATE INDEX "ix_AicSystem_aic_system_tasks_AicSystem_aic_id" ON "AicSystem_aic_system_tasks" ("AicSystem_aic_id");

CREATE TABLE "AicSystem_aic_system_stakeholders" (
	"AicSystem_aic_id" TEXT,
	aic_system_stakeholders_aic_id TEXT,
	PRIMARY KEY ("AicSystem_aic_id", aic_system_stakeholders_aic_id),
	FOREIGN KEY("AicSystem_aic_id") REFERENCES "AicSystem" (aic_id),
	FOREIGN KEY(aic_system_stakeholders_aic_id) REFERENCES "AicStakeholder" (aic_id)
);
CREATE INDEX "ix_AicSystem_aic_system_stakeholders_AicSystem_aic_id" ON "AicSystem_aic_system_stakeholders" ("AicSystem_aic_id");
CREATE INDEX "ix_AicSystem_aic_system_stakeholders_aic_system_stakeholders_aic_id" ON "AicSystem_aic_system_stakeholders" (aic_system_stakeholders_aic_id);

CREATE TABLE "AicSystem_aic_system_resource_pools" (
	"AicSystem_aic_id" TEXT,
	aic_system_resource_pools_aic_id TEXT,
	PRIMARY KEY ("AicSystem_aic_id", aic_system_resource_pools_aic_id),
	FOREIGN KEY("AicSystem_aic_id") REFERENCES "AicSystem" (aic_id),
	FOREIGN KEY(aic_system_resource_pools_aic_id) REFERENCES "AicResourcePool" (aic_id)
);
CREATE INDEX "ix_AicSystem_aic_system_resource_pools_AicSystem_aic_id" ON "AicSystem_aic_system_resource_pools" ("AicSystem_aic_id");
CREATE INDEX "ix_AicSystem_aic_system_resource_pools_aic_system_resource_pools_aic_id" ON "AicSystem_aic_system_resource_pools" (aic_system_resource_pools_aic_id);

CREATE TABLE "AicSystem_aic_system_jurisdictional_issues" (
	"AicSystem_aic_id" TEXT,
	aic_system_jurisdictional_issues TEXT,
	PRIMARY KEY ("AicSystem_aic_id", aic_system_jurisdictional_issues),
	FOREIGN KEY("AicSystem_aic_id") REFERENCES "AicSystem" (aic_id)
);
CREATE INDEX "ix_AicSystem_aic_system_jurisdictional_issues_AicSystem_aic_id" ON "AicSystem_aic_system_jurisdictional_issues" ("AicSystem_aic_id");
CREATE INDEX "ix_AicSystem_aic_system_jurisdictional_issues_aic_system_jurisdictional_issues" ON "AicSystem_aic_system_jurisdictional_issues" (aic_system_jurisdictional_issues);

CREATE TABLE "AicSystem_aic_system_societal_impacts" (
	"AicSystem_aic_id" TEXT,
	aic_system_societal_impacts TEXT,
	PRIMARY KEY ("AicSystem_aic_id", aic_system_societal_impacts),
	FOREIGN KEY("AicSystem_aic_id") REFERENCES "AicSystem" (aic_id)
);
CREATE INDEX "ix_AicSystem_aic_system_societal_impacts_AicSystem_aic_id" ON "AicSystem_aic_system_societal_impacts" ("AicSystem_aic_id");
CREATE INDEX "ix_AicSystem_aic_system_societal_impacts_aic_system_societal_impacts" ON "AicSystem_aic_system_societal_impacts" (aic_system_societal_impacts);

CREATE TABLE "AicAgent_aic_system_components" (
	"AicAgent_aic_id" TEXT,
	aic_system_components_aic_id TEXT,
	PRIMARY KEY ("AicAgent_aic_id", aic_system_components_aic_id),
	FOREIGN KEY("AicAgent_aic_id") REFERENCES "AicAgent" (aic_id),
	FOREIGN KEY(aic_system_components_aic_id) REFERENCES "AicComponent" (aic_id)
);
CREATE INDEX "ix_AicAgent_aic_system_components_AicAgent_aic_id" ON "AicAgent_aic_system_components" ("AicAgent_aic_id");
CREATE INDEX "ix_AicAgent_aic_system_components_aic_system_components_aic_id" ON "AicAgent_aic_system_components" (aic_system_components_aic_id);

CREATE TABLE "AicAgent_aic_system_models" (
	"AicAgent_aic_id" TEXT,
	aic_system_models_aic_id TEXT,
	PRIMARY KEY ("AicAgent_aic_id", aic_system_models_aic_id),
	FOREIGN KEY("AicAgent_aic_id") REFERENCES "AicAgent" (aic_id),
	FOREIGN KEY(aic_system_models_aic_id) REFERENCES "AicModel" (aic_id)
);
CREATE INDEX "ix_AicAgent_aic_system_models_aic_system_models_aic_id" ON "AicAgent_aic_system_models" (aic_system_models_aic_id);
CREATE INDEX "ix_AicAgent_aic_system_models_AicAgent_aic_id" ON "AicAgent_aic_system_models" ("AicAgent_aic_id");

CREATE TABLE "AicAgent_aic_system_datasets" (
	"AicAgent_aic_id" TEXT,
	aic_system_datasets_aic_id TEXT,
	PRIMARY KEY ("AicAgent_aic_id", aic_system_datasets_aic_id),
	FOREIGN KEY("AicAgent_aic_id") REFERENCES "AicAgent" (aic_id),
	FOREIGN KEY(aic_system_datasets_aic_id) REFERENCES "AicDataset" (aic_id)
);
CREATE INDEX "ix_AicAgent_aic_system_datasets_AicAgent_aic_id" ON "AicAgent_aic_system_datasets" ("AicAgent_aic_id");
CREATE INDEX "ix_AicAgent_aic_system_datasets_aic_system_datasets_aic_id" ON "AicAgent_aic_system_datasets" (aic_system_datasets_aic_id);

CREATE TABLE "AicAgent_aic_system_tasks" (
	"AicAgent_aic_id" TEXT,
	aic_system_tasks_aic_id TEXT,
	PRIMARY KEY ("AicAgent_aic_id", aic_system_tasks_aic_id),
	FOREIGN KEY("AicAgent_aic_id") REFERENCES "AicAgent" (aic_id),
	FOREIGN KEY(aic_system_tasks_aic_id) REFERENCES "AicTask" (aic_id)
);
CREATE INDEX "ix_AicAgent_aic_system_tasks_AicAgent_aic_id" ON "AicAgent_aic_system_tasks" ("AicAgent_aic_id");
CREATE INDEX "ix_AicAgent_aic_system_tasks_aic_system_tasks_aic_id" ON "AicAgent_aic_system_tasks" (aic_system_tasks_aic_id);

CREATE TABLE "AicAgent_aic_system_stakeholders" (
	"AicAgent_aic_id" TEXT,
	aic_system_stakeholders_aic_id TEXT,
	PRIMARY KEY ("AicAgent_aic_id", aic_system_stakeholders_aic_id),
	FOREIGN KEY("AicAgent_aic_id") REFERENCES "AicAgent" (aic_id),
	FOREIGN KEY(aic_system_stakeholders_aic_id) REFERENCES "AicStakeholder" (aic_id)
);
CREATE INDEX "ix_AicAgent_aic_system_stakeholders_AicAgent_aic_id" ON "AicAgent_aic_system_stakeholders" ("AicAgent_aic_id");
CREATE INDEX "ix_AicAgent_aic_system_stakeholders_aic_system_stakeholders_aic_id" ON "AicAgent_aic_system_stakeholders" (aic_system_stakeholders_aic_id);

CREATE TABLE "AicAgent_aic_system_resource_pools" (
	"AicAgent_aic_id" TEXT,
	aic_system_resource_pools_aic_id TEXT,
	PRIMARY KEY ("AicAgent_aic_id", aic_system_resource_pools_aic_id),
	FOREIGN KEY("AicAgent_aic_id") REFERENCES "AicAgent" (aic_id),
	FOREIGN KEY(aic_system_resource_pools_aic_id) REFERENCES "AicResourcePool" (aic_id)
);
CREATE INDEX "ix_AicAgent_aic_system_resource_pools_AicAgent_aic_id" ON "AicAgent_aic_system_resource_pools" ("AicAgent_aic_id");
CREATE INDEX "ix_AicAgent_aic_system_resource_pools_aic_system_resource_pools_aic_id" ON "AicAgent_aic_system_resource_pools" (aic_system_resource_pools_aic_id);

CREATE TABLE "AicExpertSystem_aic_expert_knowledge" (
	"AicExpertSystem_aic_id" TEXT,
	aic_expert_knowledge_aic_id TEXT NOT NULL,
	PRIMARY KEY ("AicExpertSystem_aic_id", aic_expert_knowledge_aic_id),
	FOREIGN KEY("AicExpertSystem_aic_id") REFERENCES "AicExpertSystem" (aic_id),
	FOREIGN KEY(aic_expert_knowledge_aic_id) REFERENCES "AicKnowledge" (aic_id)
);
CREATE INDEX "ix_AicExpertSystem_aic_expert_knowledge_aic_expert_knowledge_aic_id" ON "AicExpertSystem_aic_expert_knowledge" (aic_expert_knowledge_aic_id);
CREATE INDEX "ix_AicExpertSystem_aic_expert_knowledge_AicExpertSystem_aic_id" ON "AicExpertSystem_aic_expert_knowledge" ("AicExpertSystem_aic_id");

CREATE TABLE "AicExpertSystem_aic_system_components" (
	"AicExpertSystem_aic_id" TEXT,
	aic_system_components_aic_id TEXT,
	PRIMARY KEY ("AicExpertSystem_aic_id", aic_system_components_aic_id),
	FOREIGN KEY("AicExpertSystem_aic_id") REFERENCES "AicExpertSystem" (aic_id),
	FOREIGN KEY(aic_system_components_aic_id) REFERENCES "AicComponent" (aic_id)
);
CREATE INDEX "ix_AicExpertSystem_aic_system_components_AicExpertSystem_aic_id" ON "AicExpertSystem_aic_system_components" ("AicExpertSystem_aic_id");
CREATE INDEX "ix_AicExpertSystem_aic_system_components_aic_system_components_aic_id" ON "AicExpertSystem_aic_system_components" (aic_system_components_aic_id);

CREATE TABLE "AicExpertSystem_aic_system_models" (
	"AicExpertSystem_aic_id" TEXT,
	aic_system_models_aic_id TEXT,
	PRIMARY KEY ("AicExpertSystem_aic_id", aic_system_models_aic_id),
	FOREIGN KEY("AicExpertSystem_aic_id") REFERENCES "AicExpertSystem" (aic_id),
	FOREIGN KEY(aic_system_models_aic_id) REFERENCES "AicModel" (aic_id)
);
CREATE INDEX "ix_AicExpertSystem_aic_system_models_aic_system_models_aic_id" ON "AicExpertSystem_aic_system_models" (aic_system_models_aic_id);
CREATE INDEX "ix_AicExpertSystem_aic_system_models_AicExpertSystem_aic_id" ON "AicExpertSystem_aic_system_models" ("AicExpertSystem_aic_id");

CREATE TABLE "AicExpertSystem_aic_system_datasets" (
	"AicExpertSystem_aic_id" TEXT,
	aic_system_datasets_aic_id TEXT,
	PRIMARY KEY ("AicExpertSystem_aic_id", aic_system_datasets_aic_id),
	FOREIGN KEY("AicExpertSystem_aic_id") REFERENCES "AicExpertSystem" (aic_id),
	FOREIGN KEY(aic_system_datasets_aic_id) REFERENCES "AicDataset" (aic_id)
);
CREATE INDEX "ix_AicExpertSystem_aic_system_datasets_AicExpertSystem_aic_id" ON "AicExpertSystem_aic_system_datasets" ("AicExpertSystem_aic_id");
CREATE INDEX "ix_AicExpertSystem_aic_system_datasets_aic_system_datasets_aic_id" ON "AicExpertSystem_aic_system_datasets" (aic_system_datasets_aic_id);

CREATE TABLE "AicExpertSystem_aic_system_tasks" (
	"AicExpertSystem_aic_id" TEXT,
	aic_system_tasks_aic_id TEXT,
	PRIMARY KEY ("AicExpertSystem_aic_id", aic_system_tasks_aic_id),
	FOREIGN KEY("AicExpertSystem_aic_id") REFERENCES "AicExpertSystem" (aic_id),
	FOREIGN KEY(aic_system_tasks_aic_id) REFERENCES "AicTask" (aic_id)
);
CREATE INDEX "ix_AicExpertSystem_aic_system_tasks_aic_system_tasks_aic_id" ON "AicExpertSystem_aic_system_tasks" (aic_system_tasks_aic_id);
CREATE INDEX "ix_AicExpertSystem_aic_system_tasks_AicExpertSystem_aic_id" ON "AicExpertSystem_aic_system_tasks" ("AicExpertSystem_aic_id");

CREATE TABLE "AicExpertSystem_aic_system_stakeholders" (
	"AicExpertSystem_aic_id" TEXT,
	aic_system_stakeholders_aic_id TEXT,
	PRIMARY KEY ("AicExpertSystem_aic_id", aic_system_stakeholders_aic_id),
	FOREIGN KEY("AicExpertSystem_aic_id") REFERENCES "AicExpertSystem" (aic_id),
	FOREIGN KEY(aic_system_stakeholders_aic_id) REFERENCES "AicStakeholder" (aic_id)
);
CREATE INDEX "ix_AicExpertSystem_aic_system_stakeholders_aic_system_stakeholders_aic_id" ON "AicExpertSystem_aic_system_stakeholders" (aic_system_stakeholders_aic_id);
CREATE INDEX "ix_AicExpertSystem_aic_system_stakeholders_AicExpertSystem_aic_id" ON "AicExpertSystem_aic_system_stakeholders" ("AicExpertSystem_aic_id");

CREATE TABLE "AicExpertSystem_aic_system_resource_pools" (
	"AicExpertSystem_aic_id" TEXT,
	aic_system_resource_pools_aic_id TEXT,
	PRIMARY KEY ("AicExpertSystem_aic_id", aic_system_resource_pools_aic_id),
	FOREIGN KEY("AicExpertSystem_aic_id") REFERENCES "AicExpertSystem" (aic_id),
	FOREIGN KEY(aic_system_resource_pools_aic_id) REFERENCES "AicResourcePool" (aic_id)
);
CREATE INDEX "ix_AicExpertSystem_aic_system_resource_pools_AicExpertSystem_aic_id" ON "AicExpertSystem_aic_system_resource_pools" ("AicExpertSystem_aic_id");
CREATE INDEX "ix_AicExpertSystem_aic_system_resource_pools_aic_system_resource_pools_aic_id" ON "AicExpertSystem_aic_system_resource_pools" (aic_system_resource_pools_aic_id);

CREATE TABLE "AicRobot_aic_system_components" (
	"AicRobot_aic_id" TEXT,
	aic_system_components_aic_id TEXT,
	PRIMARY KEY ("AicRobot_aic_id", aic_system_components_aic_id),
	FOREIGN KEY("AicRobot_aic_id") REFERENCES "AicRobot" (aic_id),
	FOREIGN KEY(aic_system_components_aic_id) REFERENCES "AicComponent" (aic_id)
);
CREATE INDEX "ix_AicRobot_aic_system_components_aic_system_components_aic_id" ON "AicRobot_aic_system_components" (aic_system_components_aic_id);
CREATE INDEX "ix_AicRobot_aic_system_components_AicRobot_aic_id" ON "AicRobot_aic_system_components" ("AicRobot_aic_id");

CREATE TABLE "AicRobot_aic_system_models" (
	"AicRobot_aic_id" TEXT,
	aic_system_models_aic_id TEXT,
	PRIMARY KEY ("AicRobot_aic_id", aic_system_models_aic_id),
	FOREIGN KEY("AicRobot_aic_id") REFERENCES "AicRobot" (aic_id),
	FOREIGN KEY(aic_system_models_aic_id) REFERENCES "AicModel" (aic_id)
);
CREATE INDEX "ix_AicRobot_aic_system_models_aic_system_models_aic_id" ON "AicRobot_aic_system_models" (aic_system_models_aic_id);
CREATE INDEX "ix_AicRobot_aic_system_models_AicRobot_aic_id" ON "AicRobot_aic_system_models" ("AicRobot_aic_id");

CREATE TABLE "AicRobot_aic_system_datasets" (
	"AicRobot_aic_id" TEXT,
	aic_system_datasets_aic_id TEXT,
	PRIMARY KEY ("AicRobot_aic_id", aic_system_datasets_aic_id),
	FOREIGN KEY("AicRobot_aic_id") REFERENCES "AicRobot" (aic_id),
	FOREIGN KEY(aic_system_datasets_aic_id) REFERENCES "AicDataset" (aic_id)
);
CREATE INDEX "ix_AicRobot_aic_system_datasets_aic_system_datasets_aic_id" ON "AicRobot_aic_system_datasets" (aic_system_datasets_aic_id);
CREATE INDEX "ix_AicRobot_aic_system_datasets_AicRobot_aic_id" ON "AicRobot_aic_system_datasets" ("AicRobot_aic_id");

CREATE TABLE "AicRobot_aic_system_tasks" (
	"AicRobot_aic_id" TEXT,
	aic_system_tasks_aic_id TEXT,
	PRIMARY KEY ("AicRobot_aic_id", aic_system_tasks_aic_id),
	FOREIGN KEY("AicRobot_aic_id") REFERENCES "AicRobot" (aic_id),
	FOREIGN KEY(aic_system_tasks_aic_id) REFERENCES "AicTask" (aic_id)
);
CREATE INDEX "ix_AicRobot_aic_system_tasks_aic_system_tasks_aic_id" ON "AicRobot_aic_system_tasks" (aic_system_tasks_aic_id);
CREATE INDEX "ix_AicRobot_aic_system_tasks_AicRobot_aic_id" ON "AicRobot_aic_system_tasks" ("AicRobot_aic_id");

CREATE TABLE "AicRobot_aic_system_stakeholders" (
	"AicRobot_aic_id" TEXT,
	aic_system_stakeholders_aic_id TEXT,
	PRIMARY KEY ("AicRobot_aic_id", aic_system_stakeholders_aic_id),
	FOREIGN KEY("AicRobot_aic_id") REFERENCES "AicRobot" (aic_id),
	FOREIGN KEY(aic_system_stakeholders_aic_id) REFERENCES "AicStakeholder" (aic_id)
);
CREATE INDEX "ix_AicRobot_aic_system_stakeholders_AicRobot_aic_id" ON "AicRobot_aic_system_stakeholders" ("AicRobot_aic_id");
CREATE INDEX "ix_AicRobot_aic_system_stakeholders_aic_system_stakeholders_aic_id" ON "AicRobot_aic_system_stakeholders" (aic_system_stakeholders_aic_id);

CREATE TABLE "AicRobot_aic_system_resource_pools" (
	"AicRobot_aic_id" TEXT,
	aic_system_resource_pools_aic_id TEXT,
	PRIMARY KEY ("AicRobot_aic_id", aic_system_resource_pools_aic_id),
	FOREIGN KEY("AicRobot_aic_id") REFERENCES "AicRobot" (aic_id),
	FOREIGN KEY(aic_system_resource_pools_aic_id) REFERENCES "AicResourcePool" (aic_id)
);
CREATE INDEX "ix_AicRobot_aic_system_resource_pools_aic_system_resource_pools_aic_id" ON "AicRobot_aic_system_resource_pools" (aic_system_resource_pools_aic_id);
CREATE INDEX "ix_AicRobot_aic_system_resource_pools_AicRobot_aic_id" ON "AicRobot_aic_system_resource_pools" ("AicRobot_aic_id");

CREATE TABLE "AicComponent_aic_component_depends_on" (
	"AicComponent_aic_id" TEXT,
	aic_component_depends_on_aic_id TEXT,
	PRIMARY KEY ("AicComponent_aic_id", aic_component_depends_on_aic_id),
	FOREIGN KEY("AicComponent_aic_id") REFERENCES "AicComponent" (aic_id),
	FOREIGN KEY(aic_component_depends_on_aic_id) REFERENCES "AicComponent" (aic_id)
);
CREATE INDEX "ix_AicComponent_aic_component_depends_on_AicComponent_aic_id" ON "AicComponent_aic_component_depends_on" ("AicComponent_aic_id");
CREATE INDEX "ix_AicComponent_aic_component_depends_on_aic_component_depends_on_aic_id" ON "AicComponent_aic_component_depends_on" (aic_component_depends_on_aic_id);

CREATE TABLE "AicTask_aic_task_languages" (
	"AicTask_aic_id" TEXT,
	aic_task_languages TEXT,
	PRIMARY KEY ("AicTask_aic_id", aic_task_languages),
	FOREIGN KEY("AicTask_aic_id") REFERENCES "AicTask" (aic_id)
);
CREATE INDEX "ix_AicTask_aic_task_languages_AicTask_aic_id" ON "AicTask_aic_task_languages" ("AicTask_aic_id");
CREATE INDEX "ix_AicTask_aic_task_languages_aic_task_languages" ON "AicTask_aic_task_languages" (aic_task_languages);

CREATE TABLE "AicTask_aic_task_performance_measures" (
	"AicTask_aic_id" TEXT,
	aic_task_performance_measures TEXT,
	PRIMARY KEY ("AicTask_aic_id", aic_task_performance_measures),
	FOREIGN KEY("AicTask_aic_id") REFERENCES "AicTask" (aic_id)
);
CREATE INDEX "ix_AicTask_aic_task_performance_measures_AicTask_aic_id" ON "AicTask_aic_task_performance_measures" ("AicTask_aic_id");
CREATE INDEX "ix_AicTask_aic_task_performance_measures_aic_task_performance_measures" ON "AicTask_aic_task_performance_measures" (aic_task_performance_measures);

CREATE TABLE "AicMachineLearningModel_aic_ml_datasets" (
	"AicMachineLearningModel_aic_id" TEXT,
	aic_ml_datasets_aic_id TEXT,
	PRIMARY KEY ("AicMachineLearningModel_aic_id", aic_ml_datasets_aic_id),
	FOREIGN KEY("AicMachineLearningModel_aic_id") REFERENCES "AicMachineLearningModel" (aic_id),
	FOREIGN KEY(aic_ml_datasets_aic_id) REFERENCES "AicDataset" (aic_id)
);
CREATE INDEX "ix_AicMachineLearningModel_aic_ml_datasets_aic_ml_datasets_aic_id" ON "AicMachineLearningModel_aic_ml_datasets" (aic_ml_datasets_aic_id);
CREATE INDEX "ix_AicMachineLearningModel_aic_ml_datasets_AicMachineLearningModel_aic_id" ON "AicMachineLearningModel_aic_ml_datasets" ("AicMachineLearningModel_aic_id");

CREATE TABLE "AicNeuralNetworkModel_aic_network_activation_functions" (
	"AicNeuralNetworkModel_aic_id" TEXT,
	aic_network_activation_functions TEXT,
	PRIMARY KEY ("AicNeuralNetworkModel_aic_id", aic_network_activation_functions),
	FOREIGN KEY("AicNeuralNetworkModel_aic_id") REFERENCES "AicNeuralNetworkModel" (aic_id)
);
CREATE INDEX "ix_AicNeuralNetworkModel_aic_network_activation_functions_AicNeuralNetworkModel_aic_id" ON "AicNeuralNetworkModel_aic_network_activation_functions" ("AicNeuralNetworkModel_aic_id");
CREATE INDEX "ix_AicNeuralNetworkModel_aic_network_activation_functions_aic_network_activation_functions" ON "AicNeuralNetworkModel_aic_network_activation_functions" (aic_network_activation_functions);

CREATE TABLE "AicNeuralNetworkModel_aic_ml_datasets" (
	"AicNeuralNetworkModel_aic_id" TEXT,
	aic_ml_datasets_aic_id TEXT,
	PRIMARY KEY ("AicNeuralNetworkModel_aic_id", aic_ml_datasets_aic_id),
	FOREIGN KEY("AicNeuralNetworkModel_aic_id") REFERENCES "AicNeuralNetworkModel" (aic_id),
	FOREIGN KEY(aic_ml_datasets_aic_id) REFERENCES "AicDataset" (aic_id)
);
CREATE INDEX "ix_AicNeuralNetworkModel_aic_ml_datasets_AicNeuralNetworkModel_aic_id" ON "AicNeuralNetworkModel_aic_ml_datasets" ("AicNeuralNetworkModel_aic_id");
CREATE INDEX "ix_AicNeuralNetworkModel_aic_ml_datasets_aic_ml_datasets_aic_id" ON "AicNeuralNetworkModel_aic_ml_datasets" (aic_ml_datasets_aic_id);

CREATE TABLE "AicNeuralNetworkModel_aic_ml_hyperparameters" (
	"AicNeuralNetworkModel_aic_id" TEXT,
	aic_ml_hyperparameters TEXT,
	PRIMARY KEY ("AicNeuralNetworkModel_aic_id", aic_ml_hyperparameters),
	FOREIGN KEY("AicNeuralNetworkModel_aic_id") REFERENCES "AicNeuralNetworkModel" (aic_id)
);
CREATE INDEX "ix_AicNeuralNetworkModel_aic_ml_hyperparameters_aic_ml_hyperparameters" ON "AicNeuralNetworkModel_aic_ml_hyperparameters" (aic_ml_hyperparameters);
CREATE INDEX "ix_AicNeuralNetworkModel_aic_ml_hyperparameters_AicNeuralNetworkModel_aic_id" ON "AicNeuralNetworkModel_aic_ml_hyperparameters" ("AicNeuralNetworkModel_aic_id");

CREATE TABLE "AicDataset_aic_dataset_roles" (
	"AicDataset_aic_id" TEXT,
	aic_dataset_roles VARCHAR(10),
	PRIMARY KEY ("AicDataset_aic_id", aic_dataset_roles),
	FOREIGN KEY("AicDataset_aic_id") REFERENCES "AicDataset" (aic_id)
);
CREATE INDEX "ix_AicDataset_aic_dataset_roles_aic_dataset_roles" ON "AicDataset_aic_dataset_roles" (aic_dataset_roles);
CREATE INDEX "ix_AicDataset_aic_dataset_roles_AicDataset_aic_id" ON "AicDataset_aic_dataset_roles" ("AicDataset_aic_id");

CREATE TABLE "AicDataset_aic_dataset_labels" (
	"AicDataset_aic_id" TEXT,
	aic_dataset_labels TEXT,
	PRIMARY KEY ("AicDataset_aic_id", aic_dataset_labels),
	FOREIGN KEY("AicDataset_aic_id") REFERENCES "AicDataset" (aic_id)
);
CREATE INDEX "ix_AicDataset_aic_dataset_labels_AicDataset_aic_id" ON "AicDataset_aic_dataset_labels" ("AicDataset_aic_id");
CREATE INDEX "ix_AicDataset_aic_dataset_labels_aic_dataset_labels" ON "AicDataset_aic_dataset_labels" (aic_dataset_labels);

CREATE TABLE "AicStakeholder_aic_stakeholder_sub_roles" (
	"AicStakeholder_aic_id" TEXT,
	aic_stakeholder_sub_roles VARCHAR(30),
	PRIMARY KEY ("AicStakeholder_aic_id", aic_stakeholder_sub_roles),
	FOREIGN KEY("AicStakeholder_aic_id") REFERENCES "AicStakeholder" (aic_id)
);
CREATE INDEX "ix_AicStakeholder_aic_stakeholder_sub_roles_aic_stakeholder_sub_roles" ON "AicStakeholder_aic_stakeholder_sub_roles" (aic_stakeholder_sub_roles);
CREATE INDEX "ix_AicStakeholder_aic_stakeholder_sub_roles_AicStakeholder_aic_id" ON "AicStakeholder_aic_stakeholder_sub_roles" ("AicStakeholder_aic_id");

CREATE TABLE "AicStakeholder_aic_stakeholder_responsibilities" (
	"AicStakeholder_aic_id" TEXT,
	aic_stakeholder_responsibilities TEXT,
	PRIMARY KEY ("AicStakeholder_aic_id", aic_stakeholder_responsibilities),
	FOREIGN KEY("AicStakeholder_aic_id") REFERENCES "AicStakeholder" (aic_id)
);
CREATE INDEX "ix_AicStakeholder_aic_stakeholder_responsibilities_aic_stakeholder_responsibilities" ON "AicStakeholder_aic_stakeholder_responsibilities" (aic_stakeholder_responsibilities);
CREATE INDEX "ix_AicStakeholder_aic_stakeholder_responsibilities_AicStakeholder_aic_id" ON "AicStakeholder_aic_stakeholder_responsibilities" ("AicStakeholder_aic_id");

CREATE TABLE "AicIotDevice_aic_device_senses" (
	"AicIotDevice_aic_id" TEXT,
	aic_device_senses TEXT,
	PRIMARY KEY ("AicIotDevice_aic_id", aic_device_senses),
	FOREIGN KEY("AicIotDevice_aic_id") REFERENCES "AicIotDevice" (aic_id)
);
CREATE INDEX "ix_AicIotDevice_aic_device_senses_AicIotDevice_aic_id" ON "AicIotDevice_aic_device_senses" ("AicIotDevice_aic_id");
CREATE INDEX "ix_AicIotDevice_aic_device_senses_aic_device_senses" ON "AicIotDevice_aic_device_senses" (aic_device_senses);

CREATE TABLE "AicIotDevice_aic_device_actuates" (
	"AicIotDevice_aic_id" TEXT,
	aic_device_actuates TEXT,
	PRIMARY KEY ("AicIotDevice_aic_id", aic_device_actuates),
	FOREIGN KEY("AicIotDevice_aic_id") REFERENCES "AicIotDevice" (aic_id)
);
CREATE INDEX "ix_AicIotDevice_aic_device_actuates_AicIotDevice_aic_id" ON "AicIotDevice_aic_device_actuates" ("AicIotDevice_aic_id");
CREATE INDEX "ix_AicIotDevice_aic_device_actuates_aic_device_actuates" ON "AicIotDevice_aic_device_actuates" (aic_device_actuates);

CREATE TABLE "AicIotSystem_aic_iot_devices" (
	"AicIotSystem_aic_id" TEXT,
	aic_iot_devices_aic_id TEXT NOT NULL,
	PRIMARY KEY ("AicIotSystem_aic_id", aic_iot_devices_aic_id),
	FOREIGN KEY("AicIotSystem_aic_id") REFERENCES "AicIotSystem" (aic_id),
	FOREIGN KEY(aic_iot_devices_aic_id) REFERENCES "AicIotDevice" (aic_id)
);
CREATE INDEX "ix_AicIotSystem_aic_iot_devices_aic_iot_devices_aic_id" ON "AicIotSystem_aic_iot_devices" (aic_iot_devices_aic_id);
CREATE INDEX "ix_AicIotSystem_aic_iot_devices_AicIotSystem_aic_id" ON "AicIotSystem_aic_iot_devices" ("AicIotSystem_aic_id");

CREATE TABLE "AicIotSystem_aic_iot_ai_systems" (
	"AicIotSystem_aic_id" TEXT,
	aic_iot_ai_systems_aic_id TEXT,
	PRIMARY KEY ("AicIotSystem_aic_id", aic_iot_ai_systems_aic_id),
	FOREIGN KEY("AicIotSystem_aic_id") REFERENCES "AicIotSystem" (aic_id),
	FOREIGN KEY(aic_iot_ai_systems_aic_id) REFERENCES "AicSystem" (aic_id)
);
CREATE INDEX "ix_AicIotSystem_aic_iot_ai_systems_AicIotSystem_aic_id" ON "AicIotSystem_aic_iot_ai_systems" ("AicIotSystem_aic_id");
CREATE INDEX "ix_AicIotSystem_aic_iot_ai_systems_aic_iot_ai_systems_aic_id" ON "AicIotSystem_aic_iot_ai_systems" (aic_iot_ai_systems_aic_id);

CREATE TABLE "AicTrustworthinessClaim_aic_claim_evidence" (
	"AicTrustworthinessClaim_aic_id" TEXT,
	aic_claim_evidence TEXT,
	PRIMARY KEY ("AicTrustworthinessClaim_aic_id", aic_claim_evidence),
	FOREIGN KEY("AicTrustworthinessClaim_aic_id") REFERENCES "AicTrustworthinessClaim" (aic_id)
);
CREATE INDEX "ix_AicTrustworthinessClaim_aic_claim_evidence_aic_claim_evidence" ON "AicTrustworthinessClaim_aic_claim_evidence" (aic_claim_evidence);
CREATE INDEX "ix_AicTrustworthinessClaim_aic_claim_evidence_AicTrustworthinessClaim_aic_id" ON "AicTrustworthinessClaim_aic_claim_evidence" ("AicTrustworthinessClaim_aic_id");

CREATE TABLE "AicLifecycleProcess_aic_lifecycle_inputs" (
	"AicLifecycleProcess_aic_id" TEXT,
	aic_lifecycle_inputs TEXT,
	PRIMARY KEY ("AicLifecycleProcess_aic_id", aic_lifecycle_inputs),
	FOREIGN KEY("AicLifecycleProcess_aic_id") REFERENCES "AicLifecycleProcess" (aic_id)
);
CREATE INDEX "ix_AicLifecycleProcess_aic_lifecycle_inputs_AicLifecycleProcess_aic_id" ON "AicLifecycleProcess_aic_lifecycle_inputs" ("AicLifecycleProcess_aic_id");
CREATE INDEX "ix_AicLifecycleProcess_aic_lifecycle_inputs_aic_lifecycle_inputs" ON "AicLifecycleProcess_aic_lifecycle_inputs" (aic_lifecycle_inputs);

CREATE TABLE "AicLifecycleProcess_aic_lifecycle_outputs" (
	"AicLifecycleProcess_aic_id" TEXT,
	aic_lifecycle_outputs TEXT,
	PRIMARY KEY ("AicLifecycleProcess_aic_id", aic_lifecycle_outputs),
	FOREIGN KEY("AicLifecycleProcess_aic_id") REFERENCES "AicLifecycleProcess" (aic_id)
);
CREATE INDEX "ix_AicLifecycleProcess_aic_lifecycle_outputs_AicLifecycleProcess_aic_id" ON "AicLifecycleProcess_aic_lifecycle_outputs" ("AicLifecycleProcess_aic_id");
CREATE INDEX "ix_AicLifecycleProcess_aic_lifecycle_outputs_aic_lifecycle_outputs" ON "AicLifecycleProcess_aic_lifecycle_outputs" (aic_lifecycle_outputs);

CREATE TABLE "AicDecision_aic_decision_predictions" (
	"AicDecision_aic_id" TEXT,
	aic_decision_predictions_aic_id TEXT,
	PRIMARY KEY ("AicDecision_aic_id", aic_decision_predictions_aic_id),
	FOREIGN KEY("AicDecision_aic_id") REFERENCES "AicDecision" (aic_id),
	FOREIGN KEY(aic_decision_predictions_aic_id) REFERENCES "AicPrediction" (aic_id)
);
CREATE INDEX "ix_AicDecision_aic_decision_predictions_AicDecision_aic_id" ON "AicDecision_aic_decision_predictions" ("AicDecision_aic_id");
CREATE INDEX "ix_AicDecision_aic_decision_predictions_aic_decision_predictions_aic_id" ON "AicDecision_aic_decision_predictions" (aic_decision_predictions_aic_id);

CREATE TABLE "AicCyberPhysicalSystem_aic_cps_physical_processes" (
	"AicCyberPhysicalSystem_aic_id" TEXT,
	aic_cps_physical_processes TEXT NOT NULL,
	PRIMARY KEY ("AicCyberPhysicalSystem_aic_id", aic_cps_physical_processes),
	FOREIGN KEY("AicCyberPhysicalSystem_aic_id") REFERENCES "AicCyberPhysicalSystem" (aic_id)
);
CREATE INDEX "ix_AicCyberPhysicalSystem_aic_cps_physical_processes_AicCyberPhysicalSystem_aic_id" ON "AicCyberPhysicalSystem_aic_cps_physical_processes" ("AicCyberPhysicalSystem_aic_id");
CREATE INDEX "ix_AicCyberPhysicalSystem_aic_cps_physical_processes_aic_cps_physical_processes" ON "AicCyberPhysicalSystem_aic_cps_physical_processes" (aic_cps_physical_processes);

CREATE TABLE "AicCyberPhysicalSystem_aic_cps_ai_systems" (
	"AicCyberPhysicalSystem_aic_id" TEXT,
	aic_cps_ai_systems_aic_id TEXT,
	PRIMARY KEY ("AicCyberPhysicalSystem_aic_id", aic_cps_ai_systems_aic_id),
	FOREIGN KEY("AicCyberPhysicalSystem_aic_id") REFERENCES "AicCyberPhysicalSystem" (aic_id),
	FOREIGN KEY(aic_cps_ai_systems_aic_id) REFERENCES "AicSystem" (aic_id)
);
CREATE INDEX "ix_AicCyberPhysicalSystem_aic_cps_ai_systems_AicCyberPhysicalSystem_aic_id" ON "AicCyberPhysicalSystem_aic_cps_ai_systems" ("AicCyberPhysicalSystem_aic_id");
CREATE INDEX "ix_AicCyberPhysicalSystem_aic_cps_ai_systems_aic_cps_ai_systems_aic_id" ON "AicCyberPhysicalSystem_aic_cps_ai_systems" (aic_cps_ai_systems_aic_id);
