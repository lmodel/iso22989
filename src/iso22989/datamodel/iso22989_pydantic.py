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


metamodel_version = "1.12.0"
version = "2022"


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


linkml_meta = LinkMLMeta({'annotations': {'edition': {'tag': 'edition', 'value': '1'},
                     'iso_open_data_date': {'tag': 'iso_open_data_date',
                                            'value': '2026-11-05'},
                     'publication_date': {'tag': 'publication_date',
                                          'value': '2022-07-19'},
                     'standard': {'tag': 'standard',
                                  'value': 'ISO/IEC 22989:2022'}},
     'comments': ['The version is the edition the schema models, and source is '
                  "ISO's page for that edition. ISO Open Data's records of it and "
                  'of the two amendments in progress are copied to '
                  'src/iso22989/schema/iso-open-data/ as of the date in the '
                  'annotations, and scripts/check_upstream_release.py reports when '
                  'ISO publishes one of them or another edition. The release tags '
                  "are the schema's own versions.",
                  'ISO/IEC 22989 is copyright ISO and IEC, and none of its text is '
                  'reproduced here. Each element cites what it renders by number, '
                  'in the iso22989_term annotation for a term of Clause 3 and the '
                  'iso22989_clause annotation for a clause, and its description is '
                  "this project's own words. A reader with a licensed copy looks "
                  "the standard's wording up there by those numbers.",
                  'tests/iso22989_numbers.yaml lists every term number and says '
                  'which element renders it, or why none does.',
                  'Every record that other records refer to has an aic_id, and a '
                  'reference holds that identifier. AicEcosystem holds each kind '
                  'of record in a list of its own.'],
     'default_prefix': 'iso22989',
     'default_range': 'string',
     'description': 'A LinkML vocabulary for describing an AI system in the terms '
                    'of ISO/IEC 22989:2022: the system and its kinds, its models, '
                    'data and tasks, its place in the life cycle, the parties '
                    'around it, the trustworthiness claims made for it, and the '
                    'fields and applications it belongs to.',
     'id': 'https://w3id.org/lmodel/iso22989',
     'imports': ['linkml:types'],
     'license': 'Apache-2.0',
     'name': 'iso22989',
     'prefixes': {'gist_ontology': {'prefix_prefix': 'gist_ontology',
                                    'prefix_reference': 'https://w3id.org/semanticarts/ns/ontology/gist/'},
                  'iso22989': {'prefix_prefix': 'iso22989',
                               'prefix_reference': 'https://w3id.org/lmodel/iso22989/'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'schema': {'prefix_prefix': 'schema',
                             'prefix_reference': 'http://schema.org/'},
                  'spdx_ai': {'prefix_prefix': 'spdx_ai',
                              'prefix_reference': 'https://spdx.org/rdf/3.0.1/terms/AI/'},
                  'spdx_dataset': {'prefix_prefix': 'spdx_dataset',
                                   'prefix_reference': 'https://spdx.org/rdf/3.0.1/terms/Dataset/'},
                  'uco-observable': {'prefix_prefix': 'uco-observable',
                                     'prefix_reference': 'https://ontology.unifiedcyberontology.org/uco/observable/'},
                  'uco-role': {'prefix_prefix': 'uco-role',
                               'prefix_reference': 'https://ontology.unifiedcyberontology.org/uco/role/'}},
     'see_also': ['https://lmodel.github.io/iso22989',
                  'https://www.iso.org/standard/74296.html'],
     'source': 'https://www.iso.org/standard/74296.html',
     'source_file': 'src/iso22989/schema/iso22989.yaml',
     'subsets': {'aic_data': {'description': 'Datasets and the work done on them '
                                             '(clauses 5.10 and 8.6).',
                              'from_schema': 'https://w3id.org/lmodel/iso22989',
                              'name': 'aic_data'},
                 'aic_ecosystem': {'description': 'What surrounds AI systems, such '
                                                  'as computing resources (clause '
                                                  '8).',
                                   'from_schema': 'https://w3id.org/lmodel/iso22989',
                                   'name': 'aic_ecosystem'},
                 'aic_fields_and_applications': {'description': 'The fields of AI '
                                                                'and where systems '
                                                                'are applied '
                                                                '(clauses 9 and '
                                                                '10).',
                                                 'from_schema': 'https://w3id.org/lmodel/iso22989',
                                                 'name': 'aic_fields_and_applications'},
                 'aic_functional_view': {'description': 'How a system moves from '
                                                        'data to acting on its '
                                                        'results (clause 7).',
                                         'from_schema': 'https://w3id.org/lmodel/iso22989',
                                         'name': 'aic_functional_view'},
                 'aic_iot': {'description': 'Connected devices and physical '
                                            'systems (clause 5.14).',
                             'from_schema': 'https://w3id.org/lmodel/iso22989',
                             'name': 'aic_iot'},
                 'aic_lifecycle': {'description': "The stages of an AI system's "
                                                  'life and the work in each '
                                                  '(clause 6).',
                                   'from_schema': 'https://w3id.org/lmodel/iso22989',
                                   'name': 'aic_lifecycle'},
                 'aic_machine_learning': {'description': 'Models and how they '
                                                         'learn (clauses 5.11, '
                                                         '5.12 and 8.4).',
                                          'from_schema': 'https://w3id.org/lmodel/iso22989',
                                          'name': 'aic_machine_learning'},
                 'aic_stakeholders': {'description': 'The parties around an AI '
                                                     'system (clause 5.19).',
                                      'from_schema': 'https://w3id.org/lmodel/iso22989',
                                      'name': 'aic_stakeholders'},
                 'aic_systems': {'description': 'AI systems, their kinds and their '
                                                'parts (clauses 5.1 to 5.9, 5.13 '
                                                'and 8.2).',
                                 'from_schema': 'https://w3id.org/lmodel/iso22989',
                                 'name': 'aic_systems'},
                 'aic_trustworthiness': {'description': 'Claims about an AI system '
                                                        'and checks on it (clauses '
                                                        '5.15 and 5.16).',
                                         'from_schema': 'https://w3id.org/lmodel/iso22989',
                                         'name': 'aic_trustworthiness'}},
     'title': 'ISO/IEC 22989:2022 AI concepts and terminology'} )

class AicSystemScope(str, Enum):
    """
    How wide a range of problems a system can take on.
    """
    narrow_ai = "narrow_ai"
    """
    Built for a bounded set of problems, and cannot move beyond them.
    """
    general_ai = "general_ai"
    """
    Able to take on problems of many kinds, including ones it was not built for.
    """


class AicApproach(str, Enum):
    """
    Whether a system works on explicit symbols or on learned numeric encodings.
    """
    symbolic = "symbolic"
    """
    Works by manipulating explicit symbols and the rules that relate them.
    """
    subsymbolic = "subsymbolic"
    """
    Works on numeric encodings that carry meaning only as a whole, such as the weights of a network.
    """


class AicTechnique(str, Enum):
    """
    A family of techniques a system is built with.
    """
    machine_learning = "machine_learning"
    """
    Fits a model's numbers to data rather than having a person write the logic.
    """
    deep_learning = "deep_learning"
    """
    Machine learning that stacks many layers of a network.
    """
    cognitive_computing = "cognitive_computing"
    """
    Aims at interaction with people that feels closer to how people deal with one another.
    """
    semantic_computing = "semantic_computing"
    """
    Works out what content and requests mean, so that it can act on the meaning.
    """
    soft_computing = "soft_computing"
    """
    Accepts inexact or uncertain reasoning where an exact answer would cost too much.
    """
    genetic_algorithm = "genetic_algorithm"
    """
    Searches by breeding and selecting candidate answers over many generations.
    """
    logic_programming = "logic_programming"
    """
    States facts and rules in logic, and lets a solver reach the conclusions.
    """


class AicAutonomy(str, Enum):
    """
    Whether a system can change its own remit or stays under outside direction.
    """
    autonomous = "autonomous"
    """
    Can change what it is for or where it applies with nobody directing it.
    """
    heteronomous = "heteronomous"
    """
    Stays under the direction of a person or another system.
    """


class AicKnowledgeKind(str, Enum):
    """
    Whether a body of knowledge states facts or steps.
    """
    declarative = "declarative"
    """
    States what is the case.
    """
    procedural = "procedural"
    """
    States what to do, step by step.
    """


class AicFunctionalStep(str, Enum):
    """
    A step in how a system gets from data to acting on its results.
    """
    data_and_information = "data_and_information"
    """
    Taking in data and giving it meaning.
    """
    knowledge_and_learning = "knowledge_and_learning"
    """
    Building up what the system knows, and learning from more data.
    """
    prediction = "prediction"
    """
    Working out a likely result for the case in hand.
    """
    decision = "decision"
    """
    Choosing what to do, given the results so far.
    """
    action = "action"
    """
    Carrying out what was chosen.
    """


class AicLearningParadigm(str, Enum):
    """
    How a model learns from its data.
    """
    supervised = "supervised"
    """
    Every example comes with the answer it should give.
    """
    unsupervised = "unsupervised"
    """
    No example comes with an answer, so the model looks for structure.
    """
    semi_supervised = "semi_supervised"
    """
    Some examples come with answers and the rest do not.
    """
    reinforcement = "reinforcement"
    """
    The model acts, gets a reward or penalty, and adjusts to earn more reward.
    """
    transfer = "transfer"
    """
    What was learned on one problem gives a start on another.
    """


class AicAlgorithmFamily(str, Enum):
    """
    A family of algorithms that fit machine learning models.
    """
    neural_network = "neural_network"
    """
    Layers of simple units whose connection weights are tuned to the data.
    """
    bayesian_network = "bayesian_network"
    """
    A graph of variables and how the probability of one depends on others.
    """
    decision_tree = "decision_tree"
    """
    A series of branching tests that end in a result.
    """
    support_vector_machine = "support_vector_machine"
    """
    Finds the widest gap that separates the classes of example.
    """


class AicNetworkArchitecture(str, Enum):
    """
    How the layers of a neural network are connected.
    """
    feed_forward = "feed_forward"
    """
    Signals pass one way, from first layer to last, with no loops.
    """
    recurrent = "recurrent"
    """
    Outputs feed back as inputs, so the network can follow a sequence.
    """
    long_short_term_memory = "long_short_term_memory"
    """
    A recurrent design whose gates let it carry a signal across long sequences.
    """
    convolutional = "convolutional"
    """
    Layers slide small filters across the input, as is usual for images.
    """


class AicDatasetRole(str, Enum):
    """
    What a dataset is used for.
    """
    training = "training"
    """
    Used to fit a model.
    """
    validation = "validation"
    """
    Used while developing a model, to compare versions and tune settings.
    """
    test = "test"
    """
    Held back from development, to judge the finished model.
    """
    production = "production"
    """
    Gathered while the system runs, when it is deployed and in real use.
    """
    input = "input"
    """
    What a system is given so that it can work out a result.
    """


class AicDataProcessKind(str, Enum):
    """
    A kind of work done on data before or while a model uses it.
    """
    data_annotation = "data_annotation"
    """
    Adds descriptive notes to data and leaves the data itself as it was.
    """
    data_quality_checking = "data_quality_checking"
    """
    Looks for gaps, skew and whatever else would limit the data's use.
    """
    data_augmentation = "data_augmentation"
    """
    Makes new samples out of existing ones by altering them.
    """
    data_sampling = "data_sampling"
    """
    Picks a smaller part of the data that behaves like the whole.
    """
    exploratory_data_analysis = "exploratory_data_analysis"
    """
    A first look at data to learn its shape and what it may hold.
    """
    imputation = "imputation"
    """
    Fills gaps with values worked out from what is there.
    """


class AicTrustworthinessProperty(str, Enum):
    """
    A property a trustworthiness claim is about.
    """
    robustness = "robustness"
    """
    Keeps performing well when conditions turn hostile or unusual.
    """
    reliability = "reliability"
    """
    Behaves and delivers as intended, time after time.
    """
    resilience = "resilience"
    """
    Gets back to working order soon after something goes wrong.
    """
    controllability = "controllability"
    """
    A person or another system can step in and steer it.
    """
    explainability = "explainability"
    """
    Can say, in terms people follow, what drove a result.
    """
    predictability = "predictability"
    """
    Lets people form sound expectations of what it will produce.
    """
    organizational_transparency = "organizational_transparency"
    """
    The organization tells those concerned what it does and decides.
    """
    system_transparency = "system_transparency"
    """
    Those concerned can learn what they need to know about the system.
    """
    bias_and_fairness = "bias_and_fairness"
    """
    Whether the system treats some people or things worse than others, as a pattern.
    """
    accountability = "accountability"
    """
    Someone answers for what the system does and decides.
    """
    availability = "availability"
    """
    Those entitled to use it can reach it and use it when they ask.
    """


class AicAssessmentKind(str, Enum):
    """
    Which question an assessment answers.
    """
    verification = "verification"
    """
    Evidence shows that the system meets what was specified for it.
    """
    validation = "validation"
    """
    Evidence shows that the system suits the use it is meant for.
    """


class AicStakeholderRole(str, Enum):
    """
    The part a party plays around an AI system.
    """
    ai_provider = "ai_provider"
    """
    Offers AI products or services, or the platform for them.
    """
    ai_producer = "ai_producer"
    """
    Designs, builds, tests or runs AI systems.
    """
    ai_customer = "ai_customer"
    """
    Takes an AI product or service for its own use.
    """
    ai_partner = "ai_partner"
    """
    Helps others in the ecosystem, by integrating systems or supplying data.
    """
    ai_subject = "ai_subject"
    """
    Is affected by an AI system, or has data about them used in it.
    """
    relevant_authority = "relevant_authority"
    """
    Sets policy for AI or holds others to the rules on it.
    """


class AicStakeholderSubRole(str, Enum):
    """
    A narrower part within one of the roles.
    """
    ai_platform_provider = "ai_platform_provider"
    """
    Offers the platform that others run AI on.
    """
    ai_product_or_service_provider = "ai_product_or_service_provider"
    """
    Offers a finished AI product or a service built on AI.
    """
    ai_developer = "ai_developer"
    """
    Writes and builds the system.
    """
    ai_user = "ai_user"
    """
    Uses the system directly.
    """
    ai_system_integrator = "ai_system_integrator"
    """
    Fits AI parts into a larger system.
    """
    data_provider = "data_provider"
    """
    Supplies data that others build or run on.
    """
    data_subject = "data_subject"
    """
    A person the data is about.
    """
    other_subject = "other_subject"
    """
    Anyone else a system affects.
    """
    policy_maker = "policy_maker"
    """
    Decides policy on AI.
    """
    regulator = "regulator"
    """
    Holds others to the rules on AI.
    """


class AicLifecycleStage(str, Enum):
    """
    A stage in an AI system's life.
    """
    inception = "inception"
    """
    Deciding that a system is wanted, what it is for and whether it can be done.
    """
    design_and_development = "design_and_development"
    """
    Making the system, from its architecture through its data work to its models.
    """
    verification_and_validation = "verification_and_validation"
    """
    Checking what was made against its specification and against its purpose.
    """
    deployment = "deployment"
    """
    Installing the system where it is to run, and making it ready for use.
    """
    operation_and_monitoring = "operation_and_monitoring"
    """
    Running the system and keeping an eye on how it behaves.
    """
    continuous_validation = "continuous_validation"
    """
    Repeating the checks on a system that goes on learning as it runs.
    """
    re_evaluation = "re_evaluation"
    """
    Looking again at whether the running system still meets its aims.
    """
    retirement = "retirement"
    """
    Taking the system out of use.
    """


class AicOecdLifecycleStage(str, Enum):
    """
    A phase of the OECD's account of an AI system's life, which Annex A sets beside the standard's.
    """
    plan_and_design = "plan_and_design"
    """
    Setting out what the system is for and how it will work.
    """
    collect_and_process_data = "collect_and_process_data"
    """
    Gathering and readying the data.
    """
    build_and_use_model = "build_and_use_model"
    """
    Making the model, or adapting one that exists, and trying it on the task.
    """
    verify_and_validate = "verify_and_validate"
    """
    Testing and evaluating the system, and checking it against what was specified and what it is for.
    """
    deploy = "deploy"
    """
    Making the system available for use.
    """
    operate_and_monitor = "operate_and_monitor"
    """
    Running the system and watching how it behaves.
    """
    retire_or_decommission = "retire_or_decommission"
    """
    Taking the system out of service, a step that may come at any point while it runs.
    """


class AicResourceKind(str, Enum):
    """
    A kind of computing resource AI work runs on.
    """
    cloud = "cloud"
    """
    Computing bought as a shared service, in someone else's data centre.
    """
    edge = "edge"
    """
    Computing close to where data arises, rather than in a far data centre.
    """
    application_specific_integrated_circuit = "application_specific_integrated_circuit"
    """
    A chip made for one kind of work, such as training or running a model.
    """


class AicField(str, Enum):
    """
    A field of AI a system belongs to.
    """
    computer_vision = "computer_vision"
    """
    Making sense of pictures and video.
    """
    natural_language_processing = "natural_language_processing"
    """
    Making sense of, or producing, human language.
    """
    data_mining = "data_mining"
    """
    Finding patterns in large amounts of numbers.
    """
    planning = "planning"
    """
    Working out a sequence of steps that reaches an aim.
    """


class AicTaskKind(str, Enum):
    """
    A named kind of task from the fields of language and vision.
    """
    automatic_summarization = "automatic_summarization"
    """
    Cuts a text down to its main points.
    """
    dialogue_management = "dialogue_management"
    """
    Decides what to say next in a conversation.
    """
    emotion_recognition = "emotion_recognition"
    """
    Works out the feeling a text or voice conveys.
    """
    information_retrieval = "information_retrieval"
    """
    Finds stored documents that answer a need.
    """
    machine_translation = "machine_translation"
    """
    Renders text from one language in another.
    """
    named_entity_recognition = "named_entity_recognition"
    """
    Spots the people, places and other named things in a text.
    """
    natural_language_generation = "natural_language_generation"
    """
    Writes text from data or from an internal form.
    """
    natural_language_understanding = "natural_language_understanding"
    """
    Takes a text and draws out what it means.
    """
    optical_character_recognition = "optical_character_recognition"
    """
    Reads printed or written characters from a picture.
    """
    part_of_speech_tagging = "part_of_speech_tagging"
    """
    Marks each word as a noun, a verb and so on.
    """
    question_answering = "question_answering"
    """
    Replies to a question put in everyday words.
    """
    relationship_extraction = "relationship_extraction"
    """
    Finds how the things a text names relate to one another.
    """
    sentiment_analysis = "sentiment_analysis"
    """
    Works out the opinion a text expresses.
    """
    speech_recognition = "speech_recognition"
    """
    Turns spoken words into text.
    """
    speech_synthesis = "speech_synthesis"
    """
    Turns text into spoken words.
    """
    face_recognition = "face_recognition"
    """
    Matches a face in a picture against stored faces.
    """
    image_recognition = "image_recognition"
    """
    Says what a picture shows.
    """


class AicApplicationDomain(str, Enum):
    """
    A domain the standard works through as an application of AI.
    """
    fraud_detection = "fraud_detection"
    """
    Spotting dishonest transactions or claims.
    """
    automated_vehicles = "automated_vehicles"
    """
    Vehicles that drive part or all of the way without a driver.
    """
    predictive_maintenance = "predictive_maintenance"
    """
    Forecasting when equipment needs attention, before it fails.
    """



class AicRecordMixin(ConfiguredBaseModel):
    """
    What every record has, so that other records can refer to it: an identifier, a title and a description.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'comments': ['It is a mixin, not a base class, so that the adapt copy can '
                      "re-root some record classes on LOKF's Concept and leave the "
                      "others as they are. lokf adapt replaces aic_id with LOKF's id, "
                      'and a class that declares id itself must descend from Concept.'],
         'from_schema': 'https://w3id.org/lmodel/iso22989',
         'mixin': True,
         'slot_usage': {'title': {'name': 'title',
                                  'pattern': '^\\s*\\S',
                                  'required': True}}})

    aic_id: str = Field(default=..., description="""The record's identifier, unique among the records it sits with, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicRecordMixin']} })
    title: str = Field(default=..., description="""The name the record's author gives it.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['AicRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record describes, in its author's words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['AicRecordMixin'],
         'slot_uri': 'schema:description'} })

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class AicEcosystem(AicRecordMixin):
    """
    The AI systems around one context of use, with the data, resources and parties that surround them, each kind of record in a list of its own.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso22989_clause': {'tag': 'iso22989_clause', 'value': '8'}},
         'from_schema': 'https://w3id.org/lmodel/iso22989',
         'in_subset': ['aic_ecosystem'],
         'mixins': ['AicRecordMixin'],
         'tree_root': True})

    aic_ecosystem_systems: Optional[list[Union[AicSystem,AicAgent,AicExpertSystem,AicRobot]]] = Field(default=None, description="""The AI systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicEcosystem']} })
    aic_ecosystem_components: Optional[list[AicComponent]] = Field(default=None, description="""The parts of those systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicEcosystem']} })
    aic_ecosystem_knowledge: Optional[list[AicKnowledge]] = Field(default=None, description="""The bodies of knowledge those systems draw on.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicEcosystem']} })
    aic_ecosystem_tasks: Optional[list[AicTask]] = Field(default=None, description="""The tasks those systems take on.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicEcosystem']} })
    aic_ecosystem_models: Optional[list[Union[AicModel,AicMachineLearningModel,AicNeuralNetworkModel]]] = Field(default=None, description="""The models those systems use.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicEcosystem']} })
    aic_ecosystem_datasets: Optional[list[AicDataset]] = Field(default=None, description="""The datasets those systems and models use.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicEcosystem']} })
    aic_ecosystem_stakeholders: Optional[list[AicStakeholder]] = Field(default=None, description="""The parties around those systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicEcosystem']} })
    aic_ecosystem_lifecycle_processes: Optional[list[AicLifecycleProcess]] = Field(default=None, description="""The work done at each stage of those systems' lives.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicEcosystem']} })
    aic_ecosystem_claims: Optional[list[AicTrustworthinessClaim]] = Field(default=None, description="""The trustworthiness claims made for those systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicEcosystem']} })
    aic_ecosystem_assessments: Optional[list[AicAssessment]] = Field(default=None, description="""The verification and validation of those systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicEcosystem']} })
    aic_ecosystem_predictions: Optional[list[AicPrediction]] = Field(default=None, description="""The predictions those systems produced.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicEcosystem']} })
    aic_ecosystem_decisions: Optional[list[AicDecision]] = Field(default=None, description="""The decisions taken on those predictions.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicEcosystem']} })
    aic_ecosystem_actions: Optional[list[AicAction]] = Field(default=None, description="""The actions taken on those decisions.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicEcosystem']} })
    aic_ecosystem_applications: Optional[list[AicApplication]] = Field(default=None, description="""Where those systems are applied.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicEcosystem']} })
    aic_ecosystem_resource_pools: Optional[list[AicResourcePool]] = Field(default=None, description="""The computing resources those systems run on.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicEcosystem']} })
    aic_ecosystem_iot_devices: Optional[list[AicIotDevice]] = Field(default=None, description="""The connected devices in the ecosystem.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicEcosystem']} })
    aic_ecosystem_iot_systems: Optional[list[AicIotSystem]] = Field(default=None, description="""The connected systems in the ecosystem.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicEcosystem']} })
    aic_ecosystem_cyber_physical_systems: Optional[list[AicCyberPhysicalSystem]] = Field(default=None, description="""The cyber-physical systems in the ecosystem.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicEcosystem']} })
    aic_id: str = Field(default=..., description="""The record's identifier, unique among the records it sits with, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicRecordMixin']} })
    title: str = Field(default=..., description="""The name the record's author gives it.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['AicRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record describes, in its author's words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['AicRecordMixin'],
         'slot_uri': 'schema:description'} })

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class AicSystem(AicRecordMixin):
    """
    A system built to produce results for goals set by people, using AI techniques, whatever else it is made of.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso22989_clause': {'tag': 'iso22989_clause', 'value': '8.2'},
                         'iso22989_term': {'tag': 'iso22989_term', 'value': '3.1.4'}},
         'broad_mappings': ['gist_ontology:System'],
         'comments': ["gist's System is any composite whose parts work as a whole, so "
                      "it is the wider term. SPDX's AIPackage describes a system as a "
                      'distributed package.'],
         'from_schema': 'https://w3id.org/lmodel/iso22989',
         'in_subset': ['aic_systems'],
         'mixins': ['AicRecordMixin'],
         'related_mappings': ['spdx_ai:AIPackage']})

    aic_system_type: Literal["AicSystem"] = Field(default="AicSystem", description="""Which class this record is: AicSystem or a kind of it.""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['AicSystem']} })
    aic_system_purpose: Optional[str] = Field(default=None, description="""What the system is meant to do.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicSystem']} })
    aic_system_scope: Optional[AicSystemScope] = Field(default=None, description="""How wide a range of problems the system can take on.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicSystem']} })
    aic_system_approaches: Optional[list[AicApproach]] = Field(default=None, description="""Whether it works symbolically, subsymbolically or both ways.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicSystem']} })
    aic_system_techniques: Optional[list[AicTechnique]] = Field(default=None, description="""The families of technique it is built with.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicSystem']} })
    aic_system_automated: Optional[bool] = Field(default=None, description="""Whether it runs without a person acting at each step, under the conditions given.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso22989_clause': {'tag': 'iso22989_clause', 'value': '5.13'},
                         'iso22989_term': {'tag': 'iso22989_term', 'value': '3.1.7'}},
         'domain_of': ['AicSystem']} })
    aic_system_autonomy: Optional[AicAutonomy] = Field(default=None, description="""Whether it can change its own remit or stays under outside direction.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicSystem']} })
    aic_system_human_teaming: Optional[str] = Field(default=None, description="""How people and the system share the work, if they do.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso22989_term': {'tag': 'iso22989_term', 'value': '3.3.3'}},
         'domain_of': ['AicSystem']} })
    aic_system_stage: Optional[AicLifecycleStage] = Field(default=None, description="""The stage of its life the system is in now.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicSystem']} })
    aic_system_fields: Optional[list[AicField]] = Field(default=None, description="""The fields of AI it belongs to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicSystem']} })
    aic_system_steps: Optional[list[AicFunctionalStep]] = Field(default=None, description="""The steps from data to action that it performs.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicSystem']} })
    aic_system_components: Optional[list[str]] = Field(default=None, description="""The parts it is made of.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicSystem']} })
    aic_system_models: Optional[list[str]] = Field(default=None, description="""The models it uses.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicSystem']} })
    aic_system_datasets: Optional[list[str]] = Field(default=None, description="""The datasets it uses.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicSystem']} })
    aic_system_tasks: Optional[list[str]] = Field(default=None, description="""The tasks it takes on.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicSystem']} })
    aic_system_stakeholders: Optional[list[str]] = Field(default=None, description="""The parties around it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicSystem']} })
    aic_system_resource_pools: Optional[list[str]] = Field(default=None, description="""The computing resources it runs on.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicSystem']} })
    aic_system_jurisdictional_issues: Optional[list[str]] = Field(default=None, description="""The legal questions that follow from where it is built, offered or used.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso22989_clause': {'tag': 'iso22989_clause',
                                             'value': '5.17'}},
         'domain_of': ['AicSystem']} })
    aic_system_societal_impacts: Optional[list[str]] = Field(default=None, description="""The effects it may have on people and society beyond its users.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso22989_clause': {'tag': 'iso22989_clause',
                                             'value': '5.18'}},
         'domain_of': ['AicSystem']} })
    aic_id: str = Field(default=..., description="""The record's identifier, unique among the records it sits with, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicRecordMixin']} })
    title: str = Field(default=..., description="""The name the record's author gives it.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['AicRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record describes, in its author's words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['AicRecordMixin'],
         'slot_uri': 'schema:description'} })

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class AicAgent(AicSystem):
    """
    A system that perceives its surroundings and acts on them in pursuit of goals.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso22989_clause': {'tag': 'iso22989_clause', 'value': '5.3'},
                         'iso22989_term': {'tag': 'iso22989_term', 'value': '3.1.1'}},
         'from_schema': 'https://w3id.org/lmodel/iso22989',
         'in_subset': ['aic_systems']})

    aic_agent_goals: list[str] = Field(default=..., description="""The goals the agent pursues.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicAgent']} })
    aic_agent_environment: Optional[str] = Field(default=None, description="""The surroundings the agent perceives and acts on.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicAgent']} })
    aic_system_type: Literal["AicAgent"] = Field(default="AicAgent", description="""Which class this record is: AicSystem or a kind of it.""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['AicSystem']} })
    aic_system_purpose: Optional[str] = Field(default=None, description="""What the system is meant to do.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicSystem']} })
    aic_system_scope: Optional[AicSystemScope] = Field(default=None, description="""How wide a range of problems the system can take on.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicSystem']} })
    aic_system_approaches: Optional[list[AicApproach]] = Field(default=None, description="""Whether it works symbolically, subsymbolically or both ways.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicSystem']} })
    aic_system_techniques: Optional[list[AicTechnique]] = Field(default=None, description="""The families of technique it is built with.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicSystem']} })
    aic_system_automated: Optional[bool] = Field(default=None, description="""Whether it runs without a person acting at each step, under the conditions given.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso22989_clause': {'tag': 'iso22989_clause', 'value': '5.13'},
                         'iso22989_term': {'tag': 'iso22989_term', 'value': '3.1.7'}},
         'domain_of': ['AicSystem']} })
    aic_system_autonomy: Optional[AicAutonomy] = Field(default=None, description="""Whether it can change its own remit or stays under outside direction.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicSystem']} })
    aic_system_human_teaming: Optional[str] = Field(default=None, description="""How people and the system share the work, if they do.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso22989_term': {'tag': 'iso22989_term', 'value': '3.3.3'}},
         'domain_of': ['AicSystem']} })
    aic_system_stage: Optional[AicLifecycleStage] = Field(default=None, description="""The stage of its life the system is in now.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicSystem']} })
    aic_system_fields: Optional[list[AicField]] = Field(default=None, description="""The fields of AI it belongs to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicSystem']} })
    aic_system_steps: Optional[list[AicFunctionalStep]] = Field(default=None, description="""The steps from data to action that it performs.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicSystem']} })
    aic_system_components: Optional[list[str]] = Field(default=None, description="""The parts it is made of.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicSystem']} })
    aic_system_models: Optional[list[str]] = Field(default=None, description="""The models it uses.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicSystem']} })
    aic_system_datasets: Optional[list[str]] = Field(default=None, description="""The datasets it uses.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicSystem']} })
    aic_system_tasks: Optional[list[str]] = Field(default=None, description="""The tasks it takes on.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicSystem']} })
    aic_system_stakeholders: Optional[list[str]] = Field(default=None, description="""The parties around it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicSystem']} })
    aic_system_resource_pools: Optional[list[str]] = Field(default=None, description="""The computing resources it runs on.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicSystem']} })
    aic_system_jurisdictional_issues: Optional[list[str]] = Field(default=None, description="""The legal questions that follow from where it is built, offered or used.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso22989_clause': {'tag': 'iso22989_clause',
                                             'value': '5.17'}},
         'domain_of': ['AicSystem']} })
    aic_system_societal_impacts: Optional[list[str]] = Field(default=None, description="""The effects it may have on people and society beyond its users.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso22989_clause': {'tag': 'iso22989_clause',
                                             'value': '5.18'}},
         'domain_of': ['AicSystem']} })
    aic_id: str = Field(default=..., description="""The record's identifier, unique among the records it sits with, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicRecordMixin']} })
    title: str = Field(default=..., description="""The name the record's author gives it.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['AicRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record describes, in its author's words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['AicRecordMixin'],
         'slot_uri': 'schema:description'} })

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class AicExpertSystem(AicSystem):
    """
    A system that puts what human specialists know into a form it can reason with.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso22989_clause': {'tag': 'iso22989_clause',
                                             'value': '8.5.2'},
                         'iso22989_term': {'tag': 'iso22989_term', 'value': '3.1.13'}},
         'from_schema': 'https://w3id.org/lmodel/iso22989',
         'in_subset': ['aic_systems']})

    aic_expert_knowledge: list[str] = Field(default=..., description="""The bodies of knowledge the system reasons with.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicExpertSystem']} })
    aic_expert_inference: Optional[str] = Field(default=None, description="""How the system draws conclusions from that knowledge.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso22989_term': {'tag': 'iso22989_term', 'value': '3.1.17'}},
         'domain_of': ['AicExpertSystem']} })
    aic_system_type: Literal["AicExpertSystem"] = Field(default="AicExpertSystem", description="""Which class this record is: AicSystem or a kind of it.""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['AicSystem']} })
    aic_system_purpose: Optional[str] = Field(default=None, description="""What the system is meant to do.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicSystem']} })
    aic_system_scope: Optional[AicSystemScope] = Field(default=None, description="""How wide a range of problems the system can take on.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicSystem']} })
    aic_system_approaches: Optional[list[AicApproach]] = Field(default=None, description="""Whether it works symbolically, subsymbolically or both ways.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicSystem']} })
    aic_system_techniques: Optional[list[AicTechnique]] = Field(default=None, description="""The families of technique it is built with.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicSystem']} })
    aic_system_automated: Optional[bool] = Field(default=None, description="""Whether it runs without a person acting at each step, under the conditions given.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso22989_clause': {'tag': 'iso22989_clause', 'value': '5.13'},
                         'iso22989_term': {'tag': 'iso22989_term', 'value': '3.1.7'}},
         'domain_of': ['AicSystem']} })
    aic_system_autonomy: Optional[AicAutonomy] = Field(default=None, description="""Whether it can change its own remit or stays under outside direction.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicSystem']} })
    aic_system_human_teaming: Optional[str] = Field(default=None, description="""How people and the system share the work, if they do.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso22989_term': {'tag': 'iso22989_term', 'value': '3.3.3'}},
         'domain_of': ['AicSystem']} })
    aic_system_stage: Optional[AicLifecycleStage] = Field(default=None, description="""The stage of its life the system is in now.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicSystem']} })
    aic_system_fields: Optional[list[AicField]] = Field(default=None, description="""The fields of AI it belongs to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicSystem']} })
    aic_system_steps: Optional[list[AicFunctionalStep]] = Field(default=None, description="""The steps from data to action that it performs.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicSystem']} })
    aic_system_components: Optional[list[str]] = Field(default=None, description="""The parts it is made of.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicSystem']} })
    aic_system_models: Optional[list[str]] = Field(default=None, description="""The models it uses.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicSystem']} })
    aic_system_datasets: Optional[list[str]] = Field(default=None, description="""The datasets it uses.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicSystem']} })
    aic_system_tasks: Optional[list[str]] = Field(default=None, description="""The tasks it takes on.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicSystem']} })
    aic_system_stakeholders: Optional[list[str]] = Field(default=None, description="""The parties around it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicSystem']} })
    aic_system_resource_pools: Optional[list[str]] = Field(default=None, description="""The computing resources it runs on.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicSystem']} })
    aic_system_jurisdictional_issues: Optional[list[str]] = Field(default=None, description="""The legal questions that follow from where it is built, offered or used.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso22989_clause': {'tag': 'iso22989_clause',
                                             'value': '5.17'}},
         'domain_of': ['AicSystem']} })
    aic_system_societal_impacts: Optional[list[str]] = Field(default=None, description="""The effects it may have on people and society beyond its users.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso22989_clause': {'tag': 'iso22989_clause',
                                             'value': '5.18'}},
         'domain_of': ['AicSystem']} })
    aic_id: str = Field(default=..., description="""The record's identifier, unique among the records it sits with, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicRecordMixin']} })
    title: str = Field(default=..., description="""The name the record's author gives it.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['AicRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record describes, in its author's words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['AicRecordMixin'],
         'slot_uri': 'schema:description'} })

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class AicRobot(AicSystem):
    """
    A system that moves or acts on physical things through its own actuators.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso22989_term': {'tag': 'iso22989_term', 'value': '3.1.29'}},
         'broad_mappings': ['gist_ontology:Equipment'],
         'comments': ["gist's Equipment is any tangible, human-made thing used for a "
                      'task, so it is the wider term.'],
         'from_schema': 'https://w3id.org/lmodel/iso22989',
         'in_subset': ['aic_systems']})

    aic_robot_actuators: list[str] = Field(default=..., description="""The actuators through which the robot acts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicRobot']} })
    aic_robot_sensors: Optional[list[str]] = Field(default=None, description="""The sensors through which it perceives.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicRobot']} })
    aic_system_type: Literal["AicRobot"] = Field(default="AicRobot", description="""Which class this record is: AicSystem or a kind of it.""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['AicSystem']} })
    aic_system_purpose: Optional[str] = Field(default=None, description="""What the system is meant to do.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicSystem']} })
    aic_system_scope: Optional[AicSystemScope] = Field(default=None, description="""How wide a range of problems the system can take on.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicSystem']} })
    aic_system_approaches: Optional[list[AicApproach]] = Field(default=None, description="""Whether it works symbolically, subsymbolically or both ways.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicSystem']} })
    aic_system_techniques: Optional[list[AicTechnique]] = Field(default=None, description="""The families of technique it is built with.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicSystem']} })
    aic_system_automated: Optional[bool] = Field(default=None, description="""Whether it runs without a person acting at each step, under the conditions given.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso22989_clause': {'tag': 'iso22989_clause', 'value': '5.13'},
                         'iso22989_term': {'tag': 'iso22989_term', 'value': '3.1.7'}},
         'domain_of': ['AicSystem']} })
    aic_system_autonomy: Optional[AicAutonomy] = Field(default=None, description="""Whether it can change its own remit or stays under outside direction.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicSystem']} })
    aic_system_human_teaming: Optional[str] = Field(default=None, description="""How people and the system share the work, if they do.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso22989_term': {'tag': 'iso22989_term', 'value': '3.3.3'}},
         'domain_of': ['AicSystem']} })
    aic_system_stage: Optional[AicLifecycleStage] = Field(default=None, description="""The stage of its life the system is in now.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicSystem']} })
    aic_system_fields: Optional[list[AicField]] = Field(default=None, description="""The fields of AI it belongs to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicSystem']} })
    aic_system_steps: Optional[list[AicFunctionalStep]] = Field(default=None, description="""The steps from data to action that it performs.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicSystem']} })
    aic_system_components: Optional[list[str]] = Field(default=None, description="""The parts it is made of.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicSystem']} })
    aic_system_models: Optional[list[str]] = Field(default=None, description="""The models it uses.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicSystem']} })
    aic_system_datasets: Optional[list[str]] = Field(default=None, description="""The datasets it uses.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicSystem']} })
    aic_system_tasks: Optional[list[str]] = Field(default=None, description="""The tasks it takes on.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicSystem']} })
    aic_system_stakeholders: Optional[list[str]] = Field(default=None, description="""The parties around it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicSystem']} })
    aic_system_resource_pools: Optional[list[str]] = Field(default=None, description="""The computing resources it runs on.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicSystem']} })
    aic_system_jurisdictional_issues: Optional[list[str]] = Field(default=None, description="""The legal questions that follow from where it is built, offered or used.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso22989_clause': {'tag': 'iso22989_clause',
                                             'value': '5.17'}},
         'domain_of': ['AicSystem']} })
    aic_system_societal_impacts: Optional[list[str]] = Field(default=None, description="""The effects it may have on people and society beyond its users.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso22989_clause': {'tag': 'iso22989_clause',
                                             'value': '5.18'}},
         'domain_of': ['AicSystem']} })
    aic_id: str = Field(default=..., description="""The record's identifier, unique among the records it sits with, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicRecordMixin']} })
    title: str = Field(default=..., description="""The name the record's author gives it.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['AicRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record describes, in its author's words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['AicRecordMixin'],
         'slot_uri': 'schema:description'} })

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class AicComponent(AicRecordMixin):
    """
    A part of a system that does one job in it.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso22989_term': {'tag': 'iso22989_term', 'value': '3.1.2'}},
         'from_schema': 'https://w3id.org/lmodel/iso22989',
         'in_subset': ['aic_systems'],
         'mixins': ['AicRecordMixin']})

    aic_component_step: Optional[AicFunctionalStep] = Field(default=None, description="""The step from data to action this part performs.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicComponent']} })
    aic_component_depends_on: Optional[list[str]] = Field(default=None, description="""The other parts this part needs.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicComponent']} })
    aic_id: str = Field(default=..., description="""The record's identifier, unique among the records it sits with, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicRecordMixin']} })
    title: str = Field(default=..., description="""The name the record's author gives it.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['AicRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record describes, in its author's words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['AicRecordMixin'],
         'slot_uri': 'schema:description'} })

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class AicKnowledge(AicRecordMixin):
    """
    A body of what a system knows, in a form it can use.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso22989_clause': {'tag': 'iso22989_clause', 'value': '5.4'},
                         'iso22989_term': {'tag': 'iso22989_term', 'value': '3.1.21'}},
         'from_schema': 'https://w3id.org/lmodel/iso22989',
         'in_subset': ['aic_systems'],
         'mixins': ['AicRecordMixin']})

    aic_knowledge_kind: Optional[AicKnowledgeKind] = Field(default=None, description="""Whether it states what is the case or what to do.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicKnowledge']} })
    aic_knowledge_representation: Optional[str] = Field(default=None, description="""The form it is held in, such as rules, a graph or an ontology.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicKnowledge']} })
    aic_id: str = Field(default=..., description="""The record's identifier, unique among the records it sits with, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicRecordMixin']} })
    title: str = Field(default=..., description="""The name the record's author gives it.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['AicRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record describes, in its author's words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['AicRecordMixin'],
         'slot_uri': 'schema:description'} })

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class AicTask(AicRecordMixin):
    """
    Something a system is asked to get done.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso22989_term': {'tag': 'iso22989_term', 'value': '3.1.35'}},
         'comments': ["gist's Task is a piece of work that is planned or under way, "
                      'where this is what a system is asked to do.'],
         'from_schema': 'https://w3id.org/lmodel/iso22989',
         'in_subset': ['aic_systems'],
         'mixins': ['AicRecordMixin'],
         'related_mappings': ['gist_ontology:Task']})

    aic_task_kind: Optional[AicTaskKind] = Field(default=None, description="""The named kind of task it is, where it is one.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicTask']} })
    aic_task_goal: Optional[str] = Field(default=None, description="""What getting the task done achieves.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicTask']} })
    aic_task_languages: Optional[list[str]] = Field(default=None, description="""The human languages the task works in, as language tags such as en or fr-CA.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso22989_term': {'tag': 'iso22989_term', 'value': '3.6.7'}},
         'domain_of': ['AicTask']} })
    aic_task_performance_measures: Optional[list[str]] = Field(default=None, description="""What is measured to judge how well it is done, such as accuracy.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso22989_term': {'tag': 'iso22989_term', 'value': '3.1.25'}},
         'domain_of': ['AicTask']} })
    aic_id: str = Field(default=..., description="""The record's identifier, unique among the records it sits with, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicRecordMixin']} })
    title: str = Field(default=..., description="""The name the record's author gives it.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['AicRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record describes, in its author's words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['AicRecordMixin'],
         'slot_uri': 'schema:description'} })

    @field_validator('aic_task_languages')
    def pattern_aic_task_languages(cls, v):
        pattern=re.compile(r"^[A-Za-z]{2,8}(-[A-Za-z0-9]{1,8})*$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid aic_task_languages format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid aic_task_languages format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class AicModel(AicRecordMixin):
    """
    A representation of something, made so that a system can compute with it.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso22989_term': {'tag': 'iso22989_term', 'value': '3.1.23'}},
         'from_schema': 'https://w3id.org/lmodel/iso22989',
         'in_subset': ['aic_machine_learning'],
         'mixins': ['AicRecordMixin']})

    aic_model_type: Literal["AicModel"] = Field(default="AicModel", description="""Which class this record is: AicModel or a kind of it.""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['AicModel']} })
    aic_model_version: Optional[str] = Field(default=None, description="""The version of the model, as its makers number it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicModel']} })
    aic_model_represents: Optional[str] = Field(default=None, description="""What the model stands for, such as a process or a body of data.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicModel']} })
    aic_id: str = Field(default=..., description="""The record's identifier, unique among the records it sits with, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicRecordMixin']} })
    title: str = Field(default=..., description="""The name the record's author gives it.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['AicRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record describes, in its author's words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['AicRecordMixin'],
         'slot_uri': 'schema:description'} })

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class AicMachineLearningModel(AicModel):
    """
    A model whose numbers were fitted to data by a training run.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso22989_clause': {'tag': 'iso22989_clause',
                                             'value': '5.11.7'},
                         'iso22989_term': {'tag': 'iso22989_term',
                                           'value': '3.3.7, 3.3.14'}},
         'from_schema': 'https://w3id.org/lmodel/iso22989',
         'in_subset': ['aic_machine_learning']})

    aic_ml_paradigm: Optional[AicLearningParadigm] = Field(default=None, description="""How the model learned from its data.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicMachineLearningModel']} })
    aic_ml_algorithm: Optional[AicAlgorithmFamily] = Field(default=None, description="""The family of algorithm that fitted it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicMachineLearningModel']} })
    aic_ml_datasets: Optional[list[str]] = Field(default=None, description="""The datasets used to fit, tune and test it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicMachineLearningModel']} })
    aic_ml_hyperparameters: Optional[list[str]] = Field(default=None, description="""The settings fixed before training, each as name=value.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso22989_term': {'tag': 'iso22989_term', 'value': '3.3.4'}},
         'domain_of': ['AicMachineLearningModel']} })
    aic_ml_parameter_count: Optional[int] = Field(default=None, description="""How many numbers training fitted.""", ge=0, json_schema_extra = { "linkml_meta": {'annotations': {'iso22989_term': {'tag': 'iso22989_term', 'value': '3.3.8'}},
         'domain_of': ['AicMachineLearningModel']} })
    aic_ml_trained_on: Optional[date] = Field(default=None, description="""When the last training run ended.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso22989_term': {'tag': 'iso22989_term', 'value': '3.3.15'}},
         'domain_of': ['AicMachineLearningModel']} })
    aic_ml_retrained_from: Optional[str] = Field(default=None, description="""The earlier model that this one updates by training it again on other data.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso22989_clause': {'tag': 'iso22989_clause',
                                             'value': '5.11.9'},
                         'iso22989_term': {'tag': 'iso22989_term', 'value': '3.3.10'}},
         'domain_of': ['AicMachineLearningModel']} })
    aic_ml_continuous_learning: Optional[bool] = Field(default=None, description="""Whether it goes on learning in small steps while in use.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso22989_term': {'tag': 'iso22989_term', 'value': '3.1.9'}},
         'domain_of': ['AicMachineLearningModel']} })
    aic_model_type: Literal["AicMachineLearningModel"] = Field(default="AicMachineLearningModel", description="""Which class this record is: AicModel or a kind of it.""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['AicModel']} })
    aic_model_version: Optional[str] = Field(default=None, description="""The version of the model, as its makers number it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicModel']} })
    aic_model_represents: Optional[str] = Field(default=None, description="""What the model stands for, such as a process or a body of data.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicModel']} })
    aic_id: str = Field(default=..., description="""The record's identifier, unique among the records it sits with, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicRecordMixin']} })
    title: str = Field(default=..., description="""The name the record's author gives it.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['AicRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record describes, in its author's words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['AicRecordMixin'],
         'slot_uri': 'schema:description'} })

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class AicNeuralNetworkModel(AicMachineLearningModel):
    """
    A kind of machine learning model built from layers of simple connected units.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso22989_clause': {'tag': 'iso22989_clause',
                                             'value': '5.12.1'},
                         'iso22989_term': {'tag': 'iso22989_term', 'value': '3.4.8'}},
         'from_schema': 'https://w3id.org/lmodel/iso22989',
         'in_subset': ['aic_machine_learning']})

    aic_network_architecture: Optional[AicNetworkArchitecture] = Field(default=None, description="""How its layers are connected.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicNeuralNetworkModel']} })
    aic_network_layer_count: Optional[int] = Field(default=None, description="""How many layers it has.""", ge=1, json_schema_extra = { "linkml_meta": {'domain_of': ['AicNeuralNetworkModel']} })
    aic_network_activation_functions: Optional[list[str]] = Field(default=None, description="""The functions its units use to turn their inputs into an output.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso22989_term': {'tag': 'iso22989_term', 'value': '3.4.1'}},
         'domain_of': ['AicNeuralNetworkModel']} })
    aic_ml_paradigm: Optional[AicLearningParadigm] = Field(default=None, description="""How the model learned from its data.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicMachineLearningModel']} })
    aic_ml_algorithm: Optional[AicAlgorithmFamily] = Field(default=None, description="""The family of algorithm that fitted it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicMachineLearningModel']} })
    aic_ml_datasets: Optional[list[str]] = Field(default=None, description="""The datasets used to fit, tune and test it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicMachineLearningModel']} })
    aic_ml_hyperparameters: Optional[list[str]] = Field(default=None, description="""The settings fixed before training, each as name=value.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso22989_term': {'tag': 'iso22989_term', 'value': '3.3.4'}},
         'domain_of': ['AicMachineLearningModel']} })
    aic_ml_parameter_count: Optional[int] = Field(default=None, description="""How many numbers training fitted.""", ge=0, json_schema_extra = { "linkml_meta": {'annotations': {'iso22989_term': {'tag': 'iso22989_term', 'value': '3.3.8'}},
         'domain_of': ['AicMachineLearningModel']} })
    aic_ml_trained_on: Optional[date] = Field(default=None, description="""When the last training run ended.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso22989_term': {'tag': 'iso22989_term', 'value': '3.3.15'}},
         'domain_of': ['AicMachineLearningModel']} })
    aic_ml_retrained_from: Optional[str] = Field(default=None, description="""The earlier model that this one updates by training it again on other data.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso22989_clause': {'tag': 'iso22989_clause',
                                             'value': '5.11.9'},
                         'iso22989_term': {'tag': 'iso22989_term', 'value': '3.3.10'}},
         'domain_of': ['AicMachineLearningModel']} })
    aic_ml_continuous_learning: Optional[bool] = Field(default=None, description="""Whether it goes on learning in small steps while in use.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso22989_term': {'tag': 'iso22989_term', 'value': '3.1.9'}},
         'domain_of': ['AicMachineLearningModel']} })
    aic_model_type: Literal["AicNeuralNetworkModel"] = Field(default="AicNeuralNetworkModel", description="""Which class this record is: AicModel or a kind of it.""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['AicModel']} })
    aic_model_version: Optional[str] = Field(default=None, description="""The version of the model, as its makers number it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicModel']} })
    aic_model_represents: Optional[str] = Field(default=None, description="""What the model stands for, such as a process or a body of data.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicModel']} })
    aic_id: str = Field(default=..., description="""The record's identifier, unique among the records it sits with, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicRecordMixin']} })
    title: str = Field(default=..., description="""The name the record's author gives it.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['AicRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record describes, in its author's words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['AicRecordMixin'],
         'slot_uri': 'schema:description'} })

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class AicDataset(AicRecordMixin):
    """
    A set of data kept together in one format.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso22989_term': {'tag': 'iso22989_term', 'value': '3.2.5'}},
         'comments': ["SPDX's DatasetPackage describes a dataset as a distributed "
                      'package.'],
         'from_schema': 'https://w3id.org/lmodel/iso22989',
         'in_subset': ['aic_data'],
         'mixins': ['AicRecordMixin'],
         'related_mappings': ['spdx_dataset:DatasetPackage']})

    aic_dataset_roles: Optional[list[AicDatasetRole]] = Field(default=None, description="""What the dataset is used for.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicDataset']} })
    aic_dataset_source: Optional[str] = Field(default=None, description="""Where the data comes from.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso22989_clause': {'tag': 'iso22989_clause',
                                             'value': '8.6.1'}},
         'domain_of': ['AicDataset']} })
    aic_dataset_sample_count: Optional[int] = Field(default=None, description="""How many samples it holds.""", ge=0, json_schema_extra = { "linkml_meta": {'annotations': {'iso22989_term': {'tag': 'iso22989_term', 'value': '3.2.13'}},
         'domain_of': ['AicDataset']} })
    aic_dataset_labels: Optional[list[str]] = Field(default=None, description="""The labels its samples can carry.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso22989_term': {'tag': 'iso22989_term', 'value': '3.2.10'}},
         'domain_of': ['AicDataset']} })
    aic_dataset_ground_truth: Optional[str] = Field(default=None, description="""Where the correct answers for its samples come from.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso22989_term': {'tag': 'iso22989_term', 'value': '3.2.7'}},
         'domain_of': ['AicDataset']} })
    aic_dataset_holds_pii: Optional[bool] = Field(default=None, description="""Whether it holds data that can identify a person.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso22989_term': {'tag': 'iso22989_term', 'value': '3.2.11'}},
         'domain_of': ['AicDataset']} })
    aic_dataset_processes: Optional[list[AicDataProcess]] = Field(default=None, description="""The work done on the data.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicDataset']} })
    aic_id: str = Field(default=..., description="""The record's identifier, unique among the records it sits with, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicRecordMixin']} })
    title: str = Field(default=..., description="""The name the record's author gives it.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['AicRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record describes, in its author's words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['AicRecordMixin'],
         'slot_uri': 'schema:description'} })

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class AicDataProcess(ConfiguredBaseModel):
    """
    One piece of work done on a dataset.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso22989_clause': {'tag': 'iso22989_clause',
                                             'value': '5.10'}},
         'from_schema': 'https://w3id.org/lmodel/iso22989',
         'in_subset': ['aic_data']})

    aic_data_process_kind: AicDataProcessKind = Field(default=..., description="""The kind of work.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicDataProcess']} })
    aic_data_process_method: Optional[str] = Field(default=None, description="""How it was done, such as the tool used.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicDataProcess']} })
    aic_data_process_date: Optional[date] = Field(default=None, description="""When it was done.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicDataProcess']} })


class AicTrustworthinessClaim(AicRecordMixin):
    """
    A claim that a system has a property people can rely on, with what backs it.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso22989_clause': {'tag': 'iso22989_clause',
                                             'value': '5.15.1'},
                         'iso22989_term': {'tag': 'iso22989_term', 'value': '3.5.16'}},
         'from_schema': 'https://w3id.org/lmodel/iso22989',
         'in_subset': ['aic_trustworthiness'],
         'mixins': ['AicRecordMixin']})

    aic_claim_system: str = Field(default=..., description="""The system the claim is about.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicTrustworthinessClaim']} })
    aic_claim_property: AicTrustworthinessProperty = Field(default=..., description="""The property claimed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicTrustworthinessClaim']} })
    aic_claim_evidence: Optional[list[str]] = Field(default=None, description="""What backs the claim.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicTrustworthinessClaim']} })
    aic_claim_measure: Optional[str] = Field(default=None, description="""How the property was measured, if it was.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicTrustworthinessClaim']} })
    aic_id: str = Field(default=..., description="""The record's identifier, unique among the records it sits with, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicRecordMixin']} })
    title: str = Field(default=..., description="""The name the record's author gives it.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['AicRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record describes, in its author's words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['AicRecordMixin'],
         'slot_uri': 'schema:description'} })

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class AicAssessment(AicRecordMixin):
    """
    One verification or validation of a system.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso22989_clause': {'tag': 'iso22989_clause',
                                             'value': '5.16'}},
         'from_schema': 'https://w3id.org/lmodel/iso22989',
         'in_subset': ['aic_trustworthiness'],
         'mixins': ['AicRecordMixin']})

    aic_assessment_kind: AicAssessmentKind = Field(default=..., description="""Whether it checks the system against its specification or against its purpose.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicAssessment']} })
    aic_assessment_system: str = Field(default=..., description="""The system assessed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicAssessment']} })
    aic_assessment_method: Optional[str] = Field(default=None, description="""How the system was assessed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicAssessment']} })
    aic_assessment_result: Optional[str] = Field(default=None, description="""What the assessment found.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicAssessment']} })
    aic_assessment_date: Optional[date] = Field(default=None, description="""When it was done.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicAssessment']} })
    aic_id: str = Field(default=..., description="""The record's identifier, unique among the records it sits with, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicRecordMixin']} })
    title: str = Field(default=..., description="""The name the record's author gives it.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['AicRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record describes, in its author's words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['AicRecordMixin'],
         'slot_uri': 'schema:description'} })

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class AicLifecycleProcess(AicRecordMixin):
    """
    A piece of work done at one stage of a system's life.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso22989_clause': {'tag': 'iso22989_clause', 'value': '6.2'}},
         'from_schema': 'https://w3id.org/lmodel/iso22989',
         'in_subset': ['aic_lifecycle'],
         'mixins': ['AicRecordMixin']})

    aic_lifecycle_stage: AicLifecycleStage = Field(default=..., description="""The stage the work belongs to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicLifecycleProcess']} })
    aic_lifecycle_system: Optional[str] = Field(default=None, description="""The system the work is for.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicLifecycleProcess']} })
    aic_lifecycle_inputs: Optional[list[str]] = Field(default=None, description="""What the work starts from.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicLifecycleProcess']} })
    aic_lifecycle_outputs: Optional[list[str]] = Field(default=None, description="""What the work produces.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicLifecycleProcess']} })
    aic_lifecycle_responsible: Optional[str] = Field(default=None, description="""The party that answers for the work.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicLifecycleProcess']} })
    aic_lifecycle_start: Optional[date] = Field(default=None, description="""When the work began.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicLifecycleProcess']} })
    aic_lifecycle_end: Optional[date] = Field(default=None, description="""When the work ended.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicLifecycleProcess']} })
    aic_id: str = Field(default=..., description="""The record's identifier, unique among the records it sits with, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicRecordMixin']} })
    title: str = Field(default=..., description="""The name the record's author gives it.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['AicRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record describes, in its author's words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['AicRecordMixin'],
         'slot_uri': 'schema:description'} })

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class AicStakeholder(AicRecordMixin):
    """
    A person, group or organization with a part in an AI system or an interest in it.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso22989_clause': {'tag': 'iso22989_clause',
                                             'value': '5.19.1'},
                         'iso22989_term': {'tag': 'iso22989_term', 'value': '3.5.13'}},
         'comments': ["UCO's Role is the function something has in context, which this "
                      'record states for one party. A party with two roles has a '
                      'record for each.',
                      'The rules hold each sub-role to the role its role annotation '
                      'names, so a validator refuses a sub-role of another role. '
                      'tests/test_data.py holds the rules and the annotations equal.'],
         'from_schema': 'https://w3id.org/lmodel/iso22989',
         'in_subset': ['aic_stakeholders'],
         'mixins': ['AicRecordMixin'],
         'related_mappings': ['uco-role:Role'],
         'rules': [{'description': 'A party in the ai_provider role takes only that '
                                   "role's sub-roles.",
                    'postconditions': {'slot_conditions': {'aic_stakeholder_sub_roles': {'any_of': [{'equals_string': 'ai_platform_provider'},
                                                                                                    {'equals_string': 'ai_product_or_service_provider'}],
                                                                                         'name': 'aic_stakeholder_sub_roles'}}},
                    'preconditions': {'slot_conditions': {'aic_stakeholder_role': {'equals_string': 'ai_provider',
                                                                                   'name': 'aic_stakeholder_role'},
                                                          'aic_stakeholder_sub_roles': {'name': 'aic_stakeholder_sub_roles',
                                                                                        'value_presence': 'PRESENT'}}}},
                   {'description': 'A party in the ai_producer role takes only that '
                                   "role's sub-roles.",
                    'postconditions': {'slot_conditions': {'aic_stakeholder_sub_roles': {'any_of': [{'equals_string': 'ai_developer'}],
                                                                                         'name': 'aic_stakeholder_sub_roles'}}},
                    'preconditions': {'slot_conditions': {'aic_stakeholder_role': {'equals_string': 'ai_producer',
                                                                                   'name': 'aic_stakeholder_role'},
                                                          'aic_stakeholder_sub_roles': {'name': 'aic_stakeholder_sub_roles',
                                                                                        'value_presence': 'PRESENT'}}}},
                   {'description': 'A party in the ai_customer role takes only that '
                                   "role's sub-roles.",
                    'postconditions': {'slot_conditions': {'aic_stakeholder_sub_roles': {'any_of': [{'equals_string': 'ai_user'}],
                                                                                         'name': 'aic_stakeholder_sub_roles'}}},
                    'preconditions': {'slot_conditions': {'aic_stakeholder_role': {'equals_string': 'ai_customer',
                                                                                   'name': 'aic_stakeholder_role'},
                                                          'aic_stakeholder_sub_roles': {'name': 'aic_stakeholder_sub_roles',
                                                                                        'value_presence': 'PRESENT'}}}},
                   {'description': 'A party in the ai_partner role takes only that '
                                   "role's sub-roles.",
                    'postconditions': {'slot_conditions': {'aic_stakeholder_sub_roles': {'any_of': [{'equals_string': 'ai_system_integrator'},
                                                                                                    {'equals_string': 'data_provider'}],
                                                                                         'name': 'aic_stakeholder_sub_roles'}}},
                    'preconditions': {'slot_conditions': {'aic_stakeholder_role': {'equals_string': 'ai_partner',
                                                                                   'name': 'aic_stakeholder_role'},
                                                          'aic_stakeholder_sub_roles': {'name': 'aic_stakeholder_sub_roles',
                                                                                        'value_presence': 'PRESENT'}}}},
                   {'description': 'A party in the ai_subject role takes only that '
                                   "role's sub-roles.",
                    'postconditions': {'slot_conditions': {'aic_stakeholder_sub_roles': {'any_of': [{'equals_string': 'data_subject'},
                                                                                                    {'equals_string': 'other_subject'}],
                                                                                         'name': 'aic_stakeholder_sub_roles'}}},
                    'preconditions': {'slot_conditions': {'aic_stakeholder_role': {'equals_string': 'ai_subject',
                                                                                   'name': 'aic_stakeholder_role'},
                                                          'aic_stakeholder_sub_roles': {'name': 'aic_stakeholder_sub_roles',
                                                                                        'value_presence': 'PRESENT'}}}},
                   {'description': 'A party in the relevant_authority role takes only '
                                   "that role's sub-roles.",
                    'postconditions': {'slot_conditions': {'aic_stakeholder_sub_roles': {'any_of': [{'equals_string': 'policy_maker'},
                                                                                                    {'equals_string': 'regulator'}],
                                                                                         'name': 'aic_stakeholder_sub_roles'}}},
                    'preconditions': {'slot_conditions': {'aic_stakeholder_role': {'equals_string': 'relevant_authority',
                                                                                   'name': 'aic_stakeholder_role'},
                                                          'aic_stakeholder_sub_roles': {'name': 'aic_stakeholder_sub_roles',
                                                                                        'value_presence': 'PRESENT'}}}}]})

    aic_stakeholder_role: AicStakeholderRole = Field(default=..., description="""The part the party plays.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicStakeholder']} })
    aic_stakeholder_sub_roles: Optional[list[AicStakeholderSubRole]] = Field(default=None, description="""The narrower parts it plays within that role.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicStakeholder']} })
    aic_stakeholder_organization: Optional[str] = Field(default=None, description="""The organization the party is or belongs to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicStakeholder']} })
    aic_stakeholder_contact: Optional[str] = Field(default=None, description="""How to reach the party.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicStakeholder']} })
    aic_stakeholder_responsibilities: Optional[list[str]] = Field(default=None, description="""What the party answers for.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicStakeholder']} })
    aic_id: str = Field(default=..., description="""The record's identifier, unique among the records it sits with, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicRecordMixin']} })
    title: str = Field(default=..., description="""The name the record's author gives it.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['AicRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record describes, in its author's words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['AicRecordMixin'],
         'slot_uri': 'schema:description'} })

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class AicPrediction(AicRecordMixin):
    """
    A result a system worked out for one case.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso22989_clause': {'tag': 'iso22989_clause',
                                             'value': '7.4.2'},
                         'iso22989_term': {'tag': 'iso22989_term', 'value': '3.1.27'}},
         'from_schema': 'https://w3id.org/lmodel/iso22989',
         'in_subset': ['aic_functional_view'],
         'mixins': ['AicRecordMixin']})

    aic_prediction_system: str = Field(default=..., description="""The system that produced it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicPrediction']} })
    aic_prediction_value: str = Field(default=..., description="""What it says.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicPrediction']} })
    aic_prediction_confidence: Optional[float] = Field(default=None, description="""How sure the system was, from 0 to 1.""", ge=0, le=1, json_schema_extra = { "linkml_meta": {'domain_of': ['AicPrediction']} })
    aic_id: str = Field(default=..., description="""The record's identifier, unique among the records it sits with, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicRecordMixin']} })
    title: str = Field(default=..., description="""The name the record's author gives it.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['AicRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record describes, in its author's words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['AicRecordMixin'],
         'slot_uri': 'schema:description'} })

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class AicDecision(AicRecordMixin):
    """
    A choice made on the strength of some predictions.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso22989_clause': {'tag': 'iso22989_clause',
                                             'value': '7.4.3'}},
         'from_schema': 'https://w3id.org/lmodel/iso22989',
         'in_subset': ['aic_functional_view'],
         'mixins': ['AicRecordMixin']})

    aic_decision_outcome: str = Field(default=..., description="""What was chosen.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicDecision']} })
    aic_decision_predictions: Optional[list[str]] = Field(default=None, description="""The predictions it rests on.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicDecision']} })
    aic_decision_criteria: Optional[str] = Field(default=None, description="""How the choice was made, such as a threshold or a rule.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicDecision']} })
    aic_id: str = Field(default=..., description="""The record's identifier, unique among the records it sits with, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicRecordMixin']} })
    title: str = Field(default=..., description="""The name the record's author gives it.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['AicRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record describes, in its author's words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['AicRecordMixin'],
         'slot_uri': 'schema:description'} })

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class AicAction(AicRecordMixin):
    """
    What was done because of a decision.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso22989_clause': {'tag': 'iso22989_clause',
                                             'value': '7.4.4'}},
         'from_schema': 'https://w3id.org/lmodel/iso22989',
         'in_subset': ['aic_functional_view'],
         'mixins': ['AicRecordMixin']})

    aic_action_decision: str = Field(default=..., description="""The decision it carries out.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicAction']} })
    aic_action_target: Optional[str] = Field(default=None, description="""What it acted on.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicAction']} })
    aic_action_time: Optional[datetime ] = Field(default=None, description="""When it was done.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicAction']} })
    aic_id: str = Field(default=..., description="""The record's identifier, unique among the records it sits with, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicRecordMixin']} })
    title: str = Field(default=..., description="""The name the record's author gives it.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['AicRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record describes, in its author's words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['AicRecordMixin'],
         'slot_uri': 'schema:description'} })

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class AicApplication(AicRecordMixin):
    """
    One use of a system in a line of work.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso22989_clause': {'tag': 'iso22989_clause', 'value': '10'}},
         'from_schema': 'https://w3id.org/lmodel/iso22989',
         'in_subset': ['aic_fields_and_applications'],
         'mixins': ['AicRecordMixin']})

    aic_application_system: str = Field(default=..., description="""The system applied.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicApplication']} })
    aic_application_domain: Optional[AicApplicationDomain] = Field(default=None, description="""The domain, where it is one the standard works through.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicApplication']} })
    aic_application_sector: Optional[str] = Field(default=None, description="""The sector, in the words of whoever keeps the record.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicApplication']} })
    aic_application_purpose: Optional[str] = Field(default=None, description="""What this use is for.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicApplication']} })
    aic_id: str = Field(default=..., description="""The record's identifier, unique among the records it sits with, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicRecordMixin']} })
    title: str = Field(default=..., description="""The name the record's author gives it.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['AicRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record describes, in its author's words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['AicRecordMixin'],
         'slot_uri': 'schema:description'} })

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class AicResourcePool(AicRecordMixin):
    """
    A body of computing resource that AI work can draw on.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso22989_clause': {'tag': 'iso22989_clause', 'value': '8.7'}},
         'from_schema': 'https://w3id.org/lmodel/iso22989',
         'in_subset': ['aic_ecosystem'],
         'mixins': ['AicRecordMixin']})

    aic_pool_kind: Optional[AicResourceKind] = Field(default=None, description="""The kind of resource.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicResourcePool']} })
    aic_pool_hardware: Optional[str] = Field(default=None, description="""The hardware in it, such as a model of accelerator.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicResourcePool']} })
    aic_pool_capacity: Optional[str] = Field(default=None, description="""How much it offers, in units its owner uses.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicResourcePool']} })
    aic_id: str = Field(default=..., description="""The record's identifier, unique among the records it sits with, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicRecordMixin']} })
    title: str = Field(default=..., description="""The name the record's author gives it.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['AicRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record describes, in its author's words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['AicRecordMixin'],
         'slot_uri': 'schema:description'} })

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class AicIotDevice(AicRecordMixin):
    """
    A connected device that reads from or acts on its physical surroundings.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso22989_clause': {'tag': 'iso22989_clause',
                                             'value': '5.14.2'},
                         'iso22989_term': {'tag': 'iso22989_term', 'value': '3.1.19'}},
         'any_of': [{'slot_conditions': {'aic_device_senses': {'name': 'aic_device_senses',
                                                               'required': True}}},
                    {'slot_conditions': {'aic_device_actuates': {'name': 'aic_device_actuates',
                                                                 'required': True}}}],
         'broad_mappings': ['uco-observable:Device'],
         'comments': ["UCO's Device is any piece of equipment made for a purpose, so "
                      'it is the wider term. Its SmartDevice is the narrower one, a '
                      'device tied directly to cloud networks or a phone.'],
         'from_schema': 'https://w3id.org/lmodel/iso22989',
         'in_subset': ['aic_iot'],
         'mixins': ['AicRecordMixin'],
         'narrow_mappings': ['uco-observable:SmartDevice']})

    aic_device_senses: Optional[list[str]] = Field(default=None, description="""What the device reads from its surroundings.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicIotDevice']} })
    aic_device_actuates: Optional[list[str]] = Field(default=None, description="""What the device acts on.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicIotDevice']} })
    aic_id: str = Field(default=..., description="""The record's identifier, unique among the records it sits with, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicRecordMixin']} })
    title: str = Field(default=..., description="""The name the record's author gives it.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['AicRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record describes, in its author's words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['AicRecordMixin'],
         'slot_uri': 'schema:description'} })

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class AicIotSystem(AicRecordMixin):
    """
    A networked system that links devices and offers services built on them.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso22989_clause': {'tag': 'iso22989_clause',
                                             'value': '5.14.2'},
                         'iso22989_term': {'tag': 'iso22989_term',
                                           'value': '3.1.18, 3.1.20'}},
         'from_schema': 'https://w3id.org/lmodel/iso22989',
         'in_subset': ['aic_iot'],
         'mixins': ['AicRecordMixin']})

    aic_iot_devices: list[str] = Field(default=..., description="""The devices in it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicIotSystem']} })
    aic_iot_ai_systems: Optional[list[str]] = Field(default=None, description="""The AI systems that work with it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicIotSystem']} })
    aic_id: str = Field(default=..., description="""The record's identifier, unique among the records it sits with, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicRecordMixin']} })
    title: str = Field(default=..., description="""The name the record's author gives it.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['AicRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record describes, in its author's words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['AicRecordMixin'],
         'slot_uri': 'schema:description'} })

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class AicCyberPhysicalSystem(AicRecordMixin):
    """
    Computing and physical processes tied in a loop, each affecting the other.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso22989_clause': {'tag': 'iso22989_clause',
                                             'value': '5.14.3'}},
         'from_schema': 'https://w3id.org/lmodel/iso22989',
         'in_subset': ['aic_iot'],
         'mixins': ['AicRecordMixin']})

    aic_cps_physical_processes: list[str] = Field(default=..., description="""The physical processes it senses and controls.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicCyberPhysicalSystem']} })
    aic_cps_iot_system: Optional[str] = Field(default=None, description="""The connected system it runs on, if it does.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicCyberPhysicalSystem']} })
    aic_cps_ai_systems: Optional[list[str]] = Field(default=None, description="""The AI systems that work with it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicCyberPhysicalSystem']} })
    aic_id: str = Field(default=..., description="""The record's identifier, unique among the records it sits with, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AicRecordMixin']} })
    title: str = Field(default=..., description="""The name the record's author gives it.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['AicRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record describes, in its author's words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['AicRecordMixin'],
         'slot_uri': 'schema:description'} })

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
AicRecordMixin.model_rebuild()
AicEcosystem.model_rebuild()
AicSystem.model_rebuild()
AicAgent.model_rebuild()
AicExpertSystem.model_rebuild()
AicRobot.model_rebuild()
AicComponent.model_rebuild()
AicKnowledge.model_rebuild()
AicTask.model_rebuild()
AicModel.model_rebuild()
AicMachineLearningModel.model_rebuild()
AicNeuralNetworkModel.model_rebuild()
AicDataset.model_rebuild()
AicDataProcess.model_rebuild()
AicTrustworthinessClaim.model_rebuild()
AicAssessment.model_rebuild()
AicLifecycleProcess.model_rebuild()
AicStakeholder.model_rebuild()
AicPrediction.model_rebuild()
AicDecision.model_rebuild()
AicAction.model_rebuild()
AicApplication.model_rebuild()
AicResourcePool.model_rebuild()
AicIotDevice.model_rebuild()
AicIotSystem.model_rebuild()
AicCyberPhysicalSystem.model_rebuild()
