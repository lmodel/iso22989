# Auto generated from iso22989.yaml by pythongen.py version: 0.0.1
# Schema: iso22989
#
# id: https://w3id.org/lmodel/iso22989
# description: A LinkML vocabulary for describing an AI system in the terms of ISO/IEC 22989:2022: the system and its kinds, its models, data and tasks, its place in the life cycle, the parties around it, the trustworthiness claims made for it, and the fields and applications it belongs to.
# license: Apache-2.0

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import Boolean, Date, Datetime, Float, Integer, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import Bool, URIorCURIE, XSDDate, XSDDateTime

metamodel_version = "1.12.0"
version = "2022"

# Namespaces
GIST_ONTOLOGY = CurieNamespace('gist_ontology', 'https://w3id.org/semanticarts/ns/ontology/gist/')
ISO22989 = CurieNamespace('iso22989', 'https://w3id.org/lmodel/iso22989/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
SPDX_AI = CurieNamespace('spdx_ai', 'https://spdx.org/rdf/3.0.1/terms/AI/')
SPDX_DATASET = CurieNamespace('spdx_dataset', 'https://spdx.org/rdf/3.0.1/terms/Dataset/')
UCO_OBSERVABLE = CurieNamespace('uco-observable', 'https://ontology.unifiedcyberontology.org/uco/observable/')
UCO_ROLE = CurieNamespace('uco-role', 'https://ontology.unifiedcyberontology.org/uco/role/')
DEFAULT_ = ISO22989


# Types

# Class references
class AicRecordMixinAicId(URIorCURIE):
    pass


class AicEcosystemAicId(URIorCURIE):
    pass


class AicSystemAicId(URIorCURIE):
    pass


class AicAgentAicId(AicSystemAicId):
    pass


class AicExpertSystemAicId(AicSystemAicId):
    pass


class AicRobotAicId(AicSystemAicId):
    pass


class AicComponentAicId(URIorCURIE):
    pass


class AicKnowledgeAicId(URIorCURIE):
    pass


class AicTaskAicId(URIorCURIE):
    pass


class AicModelAicId(URIorCURIE):
    pass


class AicMachineLearningModelAicId(AicModelAicId):
    pass


class AicNeuralNetworkModelAicId(AicMachineLearningModelAicId):
    pass


class AicDatasetAicId(URIorCURIE):
    pass


class AicTrustworthinessClaimAicId(URIorCURIE):
    pass


class AicAssessmentAicId(URIorCURIE):
    pass


class AicLifecycleProcessAicId(URIorCURIE):
    pass


class AicStakeholderAicId(URIorCURIE):
    pass


class AicPredictionAicId(URIorCURIE):
    pass


class AicDecisionAicId(URIorCURIE):
    pass


class AicActionAicId(URIorCURIE):
    pass


class AicApplicationAicId(URIorCURIE):
    pass


class AicResourcePoolAicId(URIorCURIE):
    pass


class AicIotDeviceAicId(URIorCURIE):
    pass


class AicIotSystemAicId(URIorCURIE):
    pass


class AicCyberPhysicalSystemAicId(URIorCURIE):
    pass


@dataclass(repr=False)
class AicRecordMixin(YAMLRoot):
    """
    What every record has, so that other records can refer to it: an identifier, a title and a description.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO22989["AicRecordMixin"]
    class_class_curie: ClassVar[str] = "iso22989:AicRecordMixin"
    class_name: ClassVar[str] = "AicRecordMixin"
    class_model_uri: ClassVar[URIRef] = ISO22989.AicRecordMixin

    aic_id: Union[str, AicRecordMixinAicId] = None
    title: str = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.aic_id):
            self.MissingRequiredField("aic_id")
        if not isinstance(self.aic_id, AicRecordMixinAicId):
            self.aic_id = AicRecordMixinAicId(self.aic_id)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AicEcosystem(YAMLRoot):
    """
    The AI systems around one context of use, with the data, resources and parties that surround them, each kind of
    record in a list of its own.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO22989["AicEcosystem"]
    class_class_curie: ClassVar[str] = "iso22989:AicEcosystem"
    class_name: ClassVar[str] = "AicEcosystem"
    class_model_uri: ClassVar[URIRef] = ISO22989.AicEcosystem

    aic_id: Union[str, AicEcosystemAicId] = None
    title: str = None
    aic_ecosystem_systems: Optional[Union[dict[Union[str, AicSystemAicId], Union[dict, "AicSystem"]], list[Union[dict, "AicSystem"]]]] = empty_dict()
    aic_ecosystem_components: Optional[Union[dict[Union[str, AicComponentAicId], Union[dict, "AicComponent"]], list[Union[dict, "AicComponent"]]]] = empty_dict()
    aic_ecosystem_knowledge: Optional[Union[dict[Union[str, AicKnowledgeAicId], Union[dict, "AicKnowledge"]], list[Union[dict, "AicKnowledge"]]]] = empty_dict()
    aic_ecosystem_tasks: Optional[Union[dict[Union[str, AicTaskAicId], Union[dict, "AicTask"]], list[Union[dict, "AicTask"]]]] = empty_dict()
    aic_ecosystem_models: Optional[Union[dict[Union[str, AicModelAicId], Union[dict, "AicModel"]], list[Union[dict, "AicModel"]]]] = empty_dict()
    aic_ecosystem_datasets: Optional[Union[dict[Union[str, AicDatasetAicId], Union[dict, "AicDataset"]], list[Union[dict, "AicDataset"]]]] = empty_dict()
    aic_ecosystem_stakeholders: Optional[Union[dict[Union[str, AicStakeholderAicId], Union[dict, "AicStakeholder"]], list[Union[dict, "AicStakeholder"]]]] = empty_dict()
    aic_ecosystem_lifecycle_processes: Optional[Union[dict[Union[str, AicLifecycleProcessAicId], Union[dict, "AicLifecycleProcess"]], list[Union[dict, "AicLifecycleProcess"]]]] = empty_dict()
    aic_ecosystem_claims: Optional[Union[dict[Union[str, AicTrustworthinessClaimAicId], Union[dict, "AicTrustworthinessClaim"]], list[Union[dict, "AicTrustworthinessClaim"]]]] = empty_dict()
    aic_ecosystem_assessments: Optional[Union[dict[Union[str, AicAssessmentAicId], Union[dict, "AicAssessment"]], list[Union[dict, "AicAssessment"]]]] = empty_dict()
    aic_ecosystem_predictions: Optional[Union[dict[Union[str, AicPredictionAicId], Union[dict, "AicPrediction"]], list[Union[dict, "AicPrediction"]]]] = empty_dict()
    aic_ecosystem_decisions: Optional[Union[dict[Union[str, AicDecisionAicId], Union[dict, "AicDecision"]], list[Union[dict, "AicDecision"]]]] = empty_dict()
    aic_ecosystem_actions: Optional[Union[dict[Union[str, AicActionAicId], Union[dict, "AicAction"]], list[Union[dict, "AicAction"]]]] = empty_dict()
    aic_ecosystem_applications: Optional[Union[dict[Union[str, AicApplicationAicId], Union[dict, "AicApplication"]], list[Union[dict, "AicApplication"]]]] = empty_dict()
    aic_ecosystem_resource_pools: Optional[Union[dict[Union[str, AicResourcePoolAicId], Union[dict, "AicResourcePool"]], list[Union[dict, "AicResourcePool"]]]] = empty_dict()
    aic_ecosystem_iot_devices: Optional[Union[dict[Union[str, AicIotDeviceAicId], Union[dict, "AicIotDevice"]], list[Union[dict, "AicIotDevice"]]]] = empty_dict()
    aic_ecosystem_iot_systems: Optional[Union[dict[Union[str, AicIotSystemAicId], Union[dict, "AicIotSystem"]], list[Union[dict, "AicIotSystem"]]]] = empty_dict()
    aic_ecosystem_cyber_physical_systems: Optional[Union[dict[Union[str, AicCyberPhysicalSystemAicId], Union[dict, "AicCyberPhysicalSystem"]], list[Union[dict, "AicCyberPhysicalSystem"]]]] = empty_dict()
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.aic_id):
            self.MissingRequiredField("aic_id")
        if not isinstance(self.aic_id, AicEcosystemAicId):
            self.aic_id = AicEcosystemAicId(self.aic_id)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        self._normalize_inlined_as_list(slot_name="aic_ecosystem_systems", slot_type=AicSystem, key_name="aic_id", keyed=True)

        self._normalize_inlined_as_list(slot_name="aic_ecosystem_components", slot_type=AicComponent, key_name="aic_id", keyed=True)

        self._normalize_inlined_as_list(slot_name="aic_ecosystem_knowledge", slot_type=AicKnowledge, key_name="aic_id", keyed=True)

        self._normalize_inlined_as_list(slot_name="aic_ecosystem_tasks", slot_type=AicTask, key_name="aic_id", keyed=True)

        self._normalize_inlined_as_list(slot_name="aic_ecosystem_models", slot_type=AicModel, key_name="aic_id", keyed=True)

        self._normalize_inlined_as_list(slot_name="aic_ecosystem_datasets", slot_type=AicDataset, key_name="aic_id", keyed=True)

        self._normalize_inlined_as_list(slot_name="aic_ecosystem_stakeholders", slot_type=AicStakeholder, key_name="aic_id", keyed=True)

        self._normalize_inlined_as_list(slot_name="aic_ecosystem_lifecycle_processes", slot_type=AicLifecycleProcess, key_name="aic_id", keyed=True)

        self._normalize_inlined_as_list(slot_name="aic_ecosystem_claims", slot_type=AicTrustworthinessClaim, key_name="aic_id", keyed=True)

        self._normalize_inlined_as_list(slot_name="aic_ecosystem_assessments", slot_type=AicAssessment, key_name="aic_id", keyed=True)

        self._normalize_inlined_as_list(slot_name="aic_ecosystem_predictions", slot_type=AicPrediction, key_name="aic_id", keyed=True)

        self._normalize_inlined_as_list(slot_name="aic_ecosystem_decisions", slot_type=AicDecision, key_name="aic_id", keyed=True)

        self._normalize_inlined_as_list(slot_name="aic_ecosystem_actions", slot_type=AicAction, key_name="aic_id", keyed=True)

        self._normalize_inlined_as_list(slot_name="aic_ecosystem_applications", slot_type=AicApplication, key_name="aic_id", keyed=True)

        self._normalize_inlined_as_list(slot_name="aic_ecosystem_resource_pools", slot_type=AicResourcePool, key_name="aic_id", keyed=True)

        self._normalize_inlined_as_list(slot_name="aic_ecosystem_iot_devices", slot_type=AicIotDevice, key_name="aic_id", keyed=True)

        self._normalize_inlined_as_list(slot_name="aic_ecosystem_iot_systems", slot_type=AicIotSystem, key_name="aic_id", keyed=True)

        self._normalize_inlined_as_list(slot_name="aic_ecosystem_cyber_physical_systems", slot_type=AicCyberPhysicalSystem, key_name="aic_id", keyed=True)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AicSystem(YAMLRoot):
    """
    A system built to produce results for goals set by people, using AI techniques, whatever else it is made of.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO22989["AicSystem"]
    class_class_curie: ClassVar[str] = "iso22989:AicSystem"
    class_name: ClassVar[str] = "AicSystem"
    class_model_uri: ClassVar[URIRef] = ISO22989.AicSystem

    aic_id: Union[str, AicSystemAicId] = None
    aic_system_type: str = None
    title: str = None
    aic_system_purpose: Optional[str] = None
    aic_system_scope: Optional[Union[str, "AicSystemScope"]] = None
    aic_system_approaches: Optional[Union[Union[str, "AicApproach"], list[Union[str, "AicApproach"]]]] = empty_list()
    aic_system_techniques: Optional[Union[Union[str, "AicTechnique"], list[Union[str, "AicTechnique"]]]] = empty_list()
    aic_system_automated: Optional[Union[bool, Bool]] = None
    aic_system_autonomy: Optional[Union[str, "AicAutonomy"]] = None
    aic_system_human_teaming: Optional[str] = None
    aic_system_stage: Optional[Union[str, "AicLifecycleStage"]] = None
    aic_system_fields: Optional[Union[Union[str, "AicField"], list[Union[str, "AicField"]]]] = empty_list()
    aic_system_steps: Optional[Union[Union[str, "AicFunctionalStep"], list[Union[str, "AicFunctionalStep"]]]] = empty_list()
    aic_system_components: Optional[Union[Union[str, AicComponentAicId], list[Union[str, AicComponentAicId]]]] = empty_list()
    aic_system_models: Optional[Union[Union[str, AicModelAicId], list[Union[str, AicModelAicId]]]] = empty_list()
    aic_system_datasets: Optional[Union[Union[str, AicDatasetAicId], list[Union[str, AicDatasetAicId]]]] = empty_list()
    aic_system_tasks: Optional[Union[Union[str, AicTaskAicId], list[Union[str, AicTaskAicId]]]] = empty_list()
    aic_system_stakeholders: Optional[Union[Union[str, AicStakeholderAicId], list[Union[str, AicStakeholderAicId]]]] = empty_list()
    aic_system_resource_pools: Optional[Union[Union[str, AicResourcePoolAicId], list[Union[str, AicResourcePoolAicId]]]] = empty_list()
    aic_system_jurisdictional_issues: Optional[Union[str, list[str]]] = empty_list()
    aic_system_societal_impacts: Optional[Union[str, list[str]]] = empty_list()
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.aic_id):
            self.MissingRequiredField("aic_id")
        if not isinstance(self.aic_id, AicSystemAicId):
            self.aic_id = AicSystemAicId(self.aic_id)

        if self._is_empty(self.aic_system_type):
            self.MissingRequiredField("aic_system_type")
        self.aic_system_type = str(self.class_name)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self.aic_system_purpose is not None and not isinstance(self.aic_system_purpose, str):
            self.aic_system_purpose = str(self.aic_system_purpose)

        if self.aic_system_scope is not None and not isinstance(self.aic_system_scope, AicSystemScope):
            self.aic_system_scope = AicSystemScope(self.aic_system_scope)

        if not isinstance(self.aic_system_approaches, list):
            self.aic_system_approaches = [self.aic_system_approaches] if self.aic_system_approaches is not None else []
        self.aic_system_approaches = [v if isinstance(v, AicApproach) else AicApproach(v) for v in self.aic_system_approaches]

        if not isinstance(self.aic_system_techniques, list):
            self.aic_system_techniques = [self.aic_system_techniques] if self.aic_system_techniques is not None else []
        self.aic_system_techniques = [v if isinstance(v, AicTechnique) else AicTechnique(v) for v in self.aic_system_techniques]

        if self.aic_system_automated is not None and not isinstance(self.aic_system_automated, Bool):
            self.aic_system_automated = Bool(self.aic_system_automated)

        if self.aic_system_autonomy is not None and not isinstance(self.aic_system_autonomy, AicAutonomy):
            self.aic_system_autonomy = AicAutonomy(self.aic_system_autonomy)

        if self.aic_system_human_teaming is not None and not isinstance(self.aic_system_human_teaming, str):
            self.aic_system_human_teaming = str(self.aic_system_human_teaming)

        if self.aic_system_stage is not None and not isinstance(self.aic_system_stage, AicLifecycleStage):
            self.aic_system_stage = AicLifecycleStage(self.aic_system_stage)

        if not isinstance(self.aic_system_fields, list):
            self.aic_system_fields = [self.aic_system_fields] if self.aic_system_fields is not None else []
        self.aic_system_fields = [v if isinstance(v, AicField) else AicField(v) for v in self.aic_system_fields]

        if not isinstance(self.aic_system_steps, list):
            self.aic_system_steps = [self.aic_system_steps] if self.aic_system_steps is not None else []
        self.aic_system_steps = [v if isinstance(v, AicFunctionalStep) else AicFunctionalStep(v) for v in self.aic_system_steps]

        if not isinstance(self.aic_system_components, list):
            self.aic_system_components = [self.aic_system_components] if self.aic_system_components is not None else []
        self.aic_system_components = [v if isinstance(v, AicComponentAicId) else AicComponentAicId(v) for v in self.aic_system_components]

        if not isinstance(self.aic_system_models, list):
            self.aic_system_models = [self.aic_system_models] if self.aic_system_models is not None else []
        self.aic_system_models = [v if isinstance(v, AicModelAicId) else AicModelAicId(v) for v in self.aic_system_models]

        if not isinstance(self.aic_system_datasets, list):
            self.aic_system_datasets = [self.aic_system_datasets] if self.aic_system_datasets is not None else []
        self.aic_system_datasets = [v if isinstance(v, AicDatasetAicId) else AicDatasetAicId(v) for v in self.aic_system_datasets]

        if not isinstance(self.aic_system_tasks, list):
            self.aic_system_tasks = [self.aic_system_tasks] if self.aic_system_tasks is not None else []
        self.aic_system_tasks = [v if isinstance(v, AicTaskAicId) else AicTaskAicId(v) for v in self.aic_system_tasks]

        if not isinstance(self.aic_system_stakeholders, list):
            self.aic_system_stakeholders = [self.aic_system_stakeholders] if self.aic_system_stakeholders is not None else []
        self.aic_system_stakeholders = [v if isinstance(v, AicStakeholderAicId) else AicStakeholderAicId(v) for v in self.aic_system_stakeholders]

        if not isinstance(self.aic_system_resource_pools, list):
            self.aic_system_resource_pools = [self.aic_system_resource_pools] if self.aic_system_resource_pools is not None else []
        self.aic_system_resource_pools = [v if isinstance(v, AicResourcePoolAicId) else AicResourcePoolAicId(v) for v in self.aic_system_resource_pools]

        if not isinstance(self.aic_system_jurisdictional_issues, list):
            self.aic_system_jurisdictional_issues = [self.aic_system_jurisdictional_issues] if self.aic_system_jurisdictional_issues is not None else []
        self.aic_system_jurisdictional_issues = [v if isinstance(v, str) else str(v) for v in self.aic_system_jurisdictional_issues]

        if not isinstance(self.aic_system_societal_impacts, list):
            self.aic_system_societal_impacts = [self.aic_system_societal_impacts] if self.aic_system_societal_impacts is not None else []
        self.aic_system_societal_impacts = [v if isinstance(v, str) else str(v) for v in self.aic_system_societal_impacts]

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


    def __new__(cls, *args, **kwargs):

        type_designator = "aic_system_type"
        if not type_designator in kwargs:
            return super().__new__(cls,*args,**kwargs)
        else:
            type_designator_value = kwargs[type_designator]
            target_cls = cls._class_for("class_name", type_designator_value)


            if target_cls is None:
                raise ValueError(f"Wrong type designator value: class {cls.__name__} "
                                 f"has no subclass with ['class_name']='{kwargs[type_designator]}'")
            return super().__new__(target_cls,*args,**kwargs)



@dataclass(repr=False)
class AicAgent(AicSystem):
    """
    A system that perceives its surroundings and acts on them in pursuit of goals.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO22989["AicAgent"]
    class_class_curie: ClassVar[str] = "iso22989:AicAgent"
    class_name: ClassVar[str] = "AicAgent"
    class_model_uri: ClassVar[URIRef] = ISO22989.AicAgent

    aic_id: Union[str, AicAgentAicId] = None
    aic_system_type: str = None
    title: str = None
    aic_agent_goals: Union[str, list[str]] = None
    aic_agent_environment: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.aic_id):
            self.MissingRequiredField("aic_id")
        if not isinstance(self.aic_id, AicAgentAicId):
            self.aic_id = AicAgentAicId(self.aic_id)

        if self._is_empty(self.aic_agent_goals):
            self.MissingRequiredField("aic_agent_goals")
        if not isinstance(self.aic_agent_goals, list):
            self.aic_agent_goals = [self.aic_agent_goals] if self.aic_agent_goals is not None else []
        self.aic_agent_goals = [v if isinstance(v, str) else str(v) for v in self.aic_agent_goals]

        if self.aic_agent_environment is not None and not isinstance(self.aic_agent_environment, str):
            self.aic_agent_environment = str(self.aic_agent_environment)

        super().__post_init__(**kwargs)
        if self._is_empty(self.aic_system_type):
            self.MissingRequiredField("aic_system_type")
        self.aic_system_type = str(self.class_name)


@dataclass(repr=False)
class AicExpertSystem(AicSystem):
    """
    A system that puts what human specialists know into a form it can reason with.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO22989["AicExpertSystem"]
    class_class_curie: ClassVar[str] = "iso22989:AicExpertSystem"
    class_name: ClassVar[str] = "AicExpertSystem"
    class_model_uri: ClassVar[URIRef] = ISO22989.AicExpertSystem

    aic_id: Union[str, AicExpertSystemAicId] = None
    aic_system_type: str = None
    title: str = None
    aic_expert_knowledge: Union[Union[str, AicKnowledgeAicId], list[Union[str, AicKnowledgeAicId]]] = None
    aic_expert_inference: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.aic_id):
            self.MissingRequiredField("aic_id")
        if not isinstance(self.aic_id, AicExpertSystemAicId):
            self.aic_id = AicExpertSystemAicId(self.aic_id)

        if self._is_empty(self.aic_expert_knowledge):
            self.MissingRequiredField("aic_expert_knowledge")
        if not isinstance(self.aic_expert_knowledge, list):
            self.aic_expert_knowledge = [self.aic_expert_knowledge] if self.aic_expert_knowledge is not None else []
        self.aic_expert_knowledge = [v if isinstance(v, AicKnowledgeAicId) else AicKnowledgeAicId(v) for v in self.aic_expert_knowledge]

        if self.aic_expert_inference is not None and not isinstance(self.aic_expert_inference, str):
            self.aic_expert_inference = str(self.aic_expert_inference)

        super().__post_init__(**kwargs)
        if self._is_empty(self.aic_system_type):
            self.MissingRequiredField("aic_system_type")
        self.aic_system_type = str(self.class_name)


@dataclass(repr=False)
class AicRobot(AicSystem):
    """
    A system that moves or acts on physical things through its own actuators.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO22989["AicRobot"]
    class_class_curie: ClassVar[str] = "iso22989:AicRobot"
    class_name: ClassVar[str] = "AicRobot"
    class_model_uri: ClassVar[URIRef] = ISO22989.AicRobot

    aic_id: Union[str, AicRobotAicId] = None
    aic_system_type: str = None
    title: str = None
    aic_robot_actuators: Union[str, list[str]] = None
    aic_robot_sensors: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.aic_id):
            self.MissingRequiredField("aic_id")
        if not isinstance(self.aic_id, AicRobotAicId):
            self.aic_id = AicRobotAicId(self.aic_id)

        if self._is_empty(self.aic_robot_actuators):
            self.MissingRequiredField("aic_robot_actuators")
        if not isinstance(self.aic_robot_actuators, list):
            self.aic_robot_actuators = [self.aic_robot_actuators] if self.aic_robot_actuators is not None else []
        self.aic_robot_actuators = [v if isinstance(v, str) else str(v) for v in self.aic_robot_actuators]

        if not isinstance(self.aic_robot_sensors, list):
            self.aic_robot_sensors = [self.aic_robot_sensors] if self.aic_robot_sensors is not None else []
        self.aic_robot_sensors = [v if isinstance(v, str) else str(v) for v in self.aic_robot_sensors]

        super().__post_init__(**kwargs)
        if self._is_empty(self.aic_system_type):
            self.MissingRequiredField("aic_system_type")
        self.aic_system_type = str(self.class_name)


@dataclass(repr=False)
class AicComponent(YAMLRoot):
    """
    A part of a system that does one job in it.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO22989["AicComponent"]
    class_class_curie: ClassVar[str] = "iso22989:AicComponent"
    class_name: ClassVar[str] = "AicComponent"
    class_model_uri: ClassVar[URIRef] = ISO22989.AicComponent

    aic_id: Union[str, AicComponentAicId] = None
    title: str = None
    aic_component_step: Optional[Union[str, "AicFunctionalStep"]] = None
    aic_component_depends_on: Optional[Union[Union[str, AicComponentAicId], list[Union[str, AicComponentAicId]]]] = empty_list()
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.aic_id):
            self.MissingRequiredField("aic_id")
        if not isinstance(self.aic_id, AicComponentAicId):
            self.aic_id = AicComponentAicId(self.aic_id)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self.aic_component_step is not None and not isinstance(self.aic_component_step, AicFunctionalStep):
            self.aic_component_step = AicFunctionalStep(self.aic_component_step)

        if not isinstance(self.aic_component_depends_on, list):
            self.aic_component_depends_on = [self.aic_component_depends_on] if self.aic_component_depends_on is not None else []
        self.aic_component_depends_on = [v if isinstance(v, AicComponentAicId) else AicComponentAicId(v) for v in self.aic_component_depends_on]

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AicKnowledge(YAMLRoot):
    """
    A body of what a system knows, in a form it can use.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO22989["AicKnowledge"]
    class_class_curie: ClassVar[str] = "iso22989:AicKnowledge"
    class_name: ClassVar[str] = "AicKnowledge"
    class_model_uri: ClassVar[URIRef] = ISO22989.AicKnowledge

    aic_id: Union[str, AicKnowledgeAicId] = None
    title: str = None
    aic_knowledge_kind: Optional[Union[str, "AicKnowledgeKind"]] = None
    aic_knowledge_representation: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.aic_id):
            self.MissingRequiredField("aic_id")
        if not isinstance(self.aic_id, AicKnowledgeAicId):
            self.aic_id = AicKnowledgeAicId(self.aic_id)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self.aic_knowledge_kind is not None and not isinstance(self.aic_knowledge_kind, AicKnowledgeKind):
            self.aic_knowledge_kind = AicKnowledgeKind(self.aic_knowledge_kind)

        if self.aic_knowledge_representation is not None and not isinstance(self.aic_knowledge_representation, str):
            self.aic_knowledge_representation = str(self.aic_knowledge_representation)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AicTask(YAMLRoot):
    """
    Something a system is asked to get done.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO22989["AicTask"]
    class_class_curie: ClassVar[str] = "iso22989:AicTask"
    class_name: ClassVar[str] = "AicTask"
    class_model_uri: ClassVar[URIRef] = ISO22989.AicTask

    aic_id: Union[str, AicTaskAicId] = None
    title: str = None
    aic_task_kind: Optional[Union[str, "AicTaskKind"]] = None
    aic_task_goal: Optional[str] = None
    aic_task_languages: Optional[Union[str, list[str]]] = empty_list()
    aic_task_performance_measures: Optional[Union[str, list[str]]] = empty_list()
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.aic_id):
            self.MissingRequiredField("aic_id")
        if not isinstance(self.aic_id, AicTaskAicId):
            self.aic_id = AicTaskAicId(self.aic_id)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self.aic_task_kind is not None and not isinstance(self.aic_task_kind, AicTaskKind):
            self.aic_task_kind = AicTaskKind(self.aic_task_kind)

        if self.aic_task_goal is not None and not isinstance(self.aic_task_goal, str):
            self.aic_task_goal = str(self.aic_task_goal)

        if not isinstance(self.aic_task_languages, list):
            self.aic_task_languages = [self.aic_task_languages] if self.aic_task_languages is not None else []
        self.aic_task_languages = [v if isinstance(v, str) else str(v) for v in self.aic_task_languages]

        if not isinstance(self.aic_task_performance_measures, list):
            self.aic_task_performance_measures = [self.aic_task_performance_measures] if self.aic_task_performance_measures is not None else []
        self.aic_task_performance_measures = [v if isinstance(v, str) else str(v) for v in self.aic_task_performance_measures]

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AicModel(YAMLRoot):
    """
    A representation of something, made so that a system can compute with it.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO22989["AicModel"]
    class_class_curie: ClassVar[str] = "iso22989:AicModel"
    class_name: ClassVar[str] = "AicModel"
    class_model_uri: ClassVar[URIRef] = ISO22989.AicModel

    aic_id: Union[str, AicModelAicId] = None
    aic_model_type: str = None
    title: str = None
    aic_model_version: Optional[str] = None
    aic_model_represents: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.aic_id):
            self.MissingRequiredField("aic_id")
        if not isinstance(self.aic_id, AicModelAicId):
            self.aic_id = AicModelAicId(self.aic_id)

        if self._is_empty(self.aic_model_type):
            self.MissingRequiredField("aic_model_type")
        self.aic_model_type = str(self.class_name)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self.aic_model_version is not None and not isinstance(self.aic_model_version, str):
            self.aic_model_version = str(self.aic_model_version)

        if self.aic_model_represents is not None and not isinstance(self.aic_model_represents, str):
            self.aic_model_represents = str(self.aic_model_represents)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


    def __new__(cls, *args, **kwargs):

        type_designator = "aic_model_type"
        if not type_designator in kwargs:
            return super().__new__(cls,*args,**kwargs)
        else:
            type_designator_value = kwargs[type_designator]
            target_cls = cls._class_for("class_name", type_designator_value)


            if target_cls is None:
                raise ValueError(f"Wrong type designator value: class {cls.__name__} "
                                 f"has no subclass with ['class_name']='{kwargs[type_designator]}'")
            return super().__new__(target_cls,*args,**kwargs)



@dataclass(repr=False)
class AicMachineLearningModel(AicModel):
    """
    A model whose numbers were fitted to data by a training run.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO22989["AicMachineLearningModel"]
    class_class_curie: ClassVar[str] = "iso22989:AicMachineLearningModel"
    class_name: ClassVar[str] = "AicMachineLearningModel"
    class_model_uri: ClassVar[URIRef] = ISO22989.AicMachineLearningModel

    aic_id: Union[str, AicMachineLearningModelAicId] = None
    aic_model_type: str = None
    title: str = None
    aic_ml_paradigm: Optional[Union[str, "AicLearningParadigm"]] = None
    aic_ml_algorithm: Optional[Union[str, "AicAlgorithmFamily"]] = None
    aic_ml_datasets: Optional[Union[Union[str, AicDatasetAicId], list[Union[str, AicDatasetAicId]]]] = empty_list()
    aic_ml_hyperparameters: Optional[Union[str, list[str]]] = empty_list()
    aic_ml_parameter_count: Optional[int] = None
    aic_ml_trained_on: Optional[Union[str, XSDDate]] = None
    aic_ml_retrained_from: Optional[Union[str, AicMachineLearningModelAicId]] = None
    aic_ml_continuous_learning: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.aic_id):
            self.MissingRequiredField("aic_id")
        if not isinstance(self.aic_id, AicMachineLearningModelAicId):
            self.aic_id = AicMachineLearningModelAicId(self.aic_id)

        if self.aic_ml_paradigm is not None and not isinstance(self.aic_ml_paradigm, AicLearningParadigm):
            self.aic_ml_paradigm = AicLearningParadigm(self.aic_ml_paradigm)

        if self.aic_ml_algorithm is not None and not isinstance(self.aic_ml_algorithm, AicAlgorithmFamily):
            self.aic_ml_algorithm = AicAlgorithmFamily(self.aic_ml_algorithm)

        if not isinstance(self.aic_ml_datasets, list):
            self.aic_ml_datasets = [self.aic_ml_datasets] if self.aic_ml_datasets is not None else []
        self.aic_ml_datasets = [v if isinstance(v, AicDatasetAicId) else AicDatasetAicId(v) for v in self.aic_ml_datasets]

        if not isinstance(self.aic_ml_hyperparameters, list):
            self.aic_ml_hyperparameters = [self.aic_ml_hyperparameters] if self.aic_ml_hyperparameters is not None else []
        self.aic_ml_hyperparameters = [v if isinstance(v, str) else str(v) for v in self.aic_ml_hyperparameters]

        if self.aic_ml_parameter_count is not None and not isinstance(self.aic_ml_parameter_count, int):
            self.aic_ml_parameter_count = int(self.aic_ml_parameter_count)

        if self.aic_ml_trained_on is not None and not isinstance(self.aic_ml_trained_on, XSDDate):
            self.aic_ml_trained_on = XSDDate(self.aic_ml_trained_on)

        if self.aic_ml_retrained_from is not None and not isinstance(self.aic_ml_retrained_from, AicMachineLearningModelAicId):
            self.aic_ml_retrained_from = AicMachineLearningModelAicId(self.aic_ml_retrained_from)

        if self.aic_ml_continuous_learning is not None and not isinstance(self.aic_ml_continuous_learning, Bool):
            self.aic_ml_continuous_learning = Bool(self.aic_ml_continuous_learning)

        super().__post_init__(**kwargs)
        if self._is_empty(self.aic_model_type):
            self.MissingRequiredField("aic_model_type")
        self.aic_model_type = str(self.class_name)


@dataclass(repr=False)
class AicNeuralNetworkModel(AicMachineLearningModel):
    """
    A kind of machine learning model built from layers of simple connected units.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO22989["AicNeuralNetworkModel"]
    class_class_curie: ClassVar[str] = "iso22989:AicNeuralNetworkModel"
    class_name: ClassVar[str] = "AicNeuralNetworkModel"
    class_model_uri: ClassVar[URIRef] = ISO22989.AicNeuralNetworkModel

    aic_id: Union[str, AicNeuralNetworkModelAicId] = None
    aic_model_type: str = None
    title: str = None
    aic_network_architecture: Optional[Union[str, "AicNetworkArchitecture"]] = None
    aic_network_layer_count: Optional[int] = None
    aic_network_activation_functions: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.aic_id):
            self.MissingRequiredField("aic_id")
        if not isinstance(self.aic_id, AicNeuralNetworkModelAicId):
            self.aic_id = AicNeuralNetworkModelAicId(self.aic_id)

        if self.aic_network_architecture is not None and not isinstance(self.aic_network_architecture, AicNetworkArchitecture):
            self.aic_network_architecture = AicNetworkArchitecture(self.aic_network_architecture)

        if self.aic_network_layer_count is not None and not isinstance(self.aic_network_layer_count, int):
            self.aic_network_layer_count = int(self.aic_network_layer_count)

        if not isinstance(self.aic_network_activation_functions, list):
            self.aic_network_activation_functions = [self.aic_network_activation_functions] if self.aic_network_activation_functions is not None else []
        self.aic_network_activation_functions = [v if isinstance(v, str) else str(v) for v in self.aic_network_activation_functions]

        super().__post_init__(**kwargs)
        if self._is_empty(self.aic_model_type):
            self.MissingRequiredField("aic_model_type")
        self.aic_model_type = str(self.class_name)


@dataclass(repr=False)
class AicDataset(YAMLRoot):
    """
    A set of data kept together in one format.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO22989["AicDataset"]
    class_class_curie: ClassVar[str] = "iso22989:AicDataset"
    class_name: ClassVar[str] = "AicDataset"
    class_model_uri: ClassVar[URIRef] = ISO22989.AicDataset

    aic_id: Union[str, AicDatasetAicId] = None
    title: str = None
    aic_dataset_roles: Optional[Union[Union[str, "AicDatasetRole"], list[Union[str, "AicDatasetRole"]]]] = empty_list()
    aic_dataset_source: Optional[str] = None
    aic_dataset_sample_count: Optional[int] = None
    aic_dataset_labels: Optional[Union[str, list[str]]] = empty_list()
    aic_dataset_ground_truth: Optional[str] = None
    aic_dataset_holds_pii: Optional[Union[bool, Bool]] = None
    aic_dataset_processes: Optional[Union[Union[dict, "AicDataProcess"], list[Union[dict, "AicDataProcess"]]]] = empty_list()
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.aic_id):
            self.MissingRequiredField("aic_id")
        if not isinstance(self.aic_id, AicDatasetAicId):
            self.aic_id = AicDatasetAicId(self.aic_id)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if not isinstance(self.aic_dataset_roles, list):
            self.aic_dataset_roles = [self.aic_dataset_roles] if self.aic_dataset_roles is not None else []
        self.aic_dataset_roles = [v if isinstance(v, AicDatasetRole) else AicDatasetRole(v) for v in self.aic_dataset_roles]

        if self.aic_dataset_source is not None and not isinstance(self.aic_dataset_source, str):
            self.aic_dataset_source = str(self.aic_dataset_source)

        if self.aic_dataset_sample_count is not None and not isinstance(self.aic_dataset_sample_count, int):
            self.aic_dataset_sample_count = int(self.aic_dataset_sample_count)

        if not isinstance(self.aic_dataset_labels, list):
            self.aic_dataset_labels = [self.aic_dataset_labels] if self.aic_dataset_labels is not None else []
        self.aic_dataset_labels = [v if isinstance(v, str) else str(v) for v in self.aic_dataset_labels]

        if self.aic_dataset_ground_truth is not None and not isinstance(self.aic_dataset_ground_truth, str):
            self.aic_dataset_ground_truth = str(self.aic_dataset_ground_truth)

        if self.aic_dataset_holds_pii is not None and not isinstance(self.aic_dataset_holds_pii, Bool):
            self.aic_dataset_holds_pii = Bool(self.aic_dataset_holds_pii)

        self._normalize_inlined_as_list(slot_name="aic_dataset_processes", slot_type=AicDataProcess, key_name="aic_data_process_kind", keyed=False)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AicDataProcess(YAMLRoot):
    """
    One piece of work done on a dataset.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO22989["AicDataProcess"]
    class_class_curie: ClassVar[str] = "iso22989:AicDataProcess"
    class_name: ClassVar[str] = "AicDataProcess"
    class_model_uri: ClassVar[URIRef] = ISO22989.AicDataProcess

    aic_data_process_kind: Union[str, "AicDataProcessKind"] = None
    aic_data_process_method: Optional[str] = None
    aic_data_process_date: Optional[Union[str, XSDDate]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.aic_data_process_kind):
            self.MissingRequiredField("aic_data_process_kind")
        if not isinstance(self.aic_data_process_kind, AicDataProcessKind):
            self.aic_data_process_kind = AicDataProcessKind(self.aic_data_process_kind)

        if self.aic_data_process_method is not None and not isinstance(self.aic_data_process_method, str):
            self.aic_data_process_method = str(self.aic_data_process_method)

        if self.aic_data_process_date is not None and not isinstance(self.aic_data_process_date, XSDDate):
            self.aic_data_process_date = XSDDate(self.aic_data_process_date)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AicTrustworthinessClaim(YAMLRoot):
    """
    A claim that a system has a property people can rely on, with what backs it.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO22989["AicTrustworthinessClaim"]
    class_class_curie: ClassVar[str] = "iso22989:AicTrustworthinessClaim"
    class_name: ClassVar[str] = "AicTrustworthinessClaim"
    class_model_uri: ClassVar[URIRef] = ISO22989.AicTrustworthinessClaim

    aic_id: Union[str, AicTrustworthinessClaimAicId] = None
    aic_claim_system: Union[str, AicSystemAicId] = None
    aic_claim_property: Union[str, "AicTrustworthinessProperty"] = None
    title: str = None
    aic_claim_evidence: Optional[Union[str, list[str]]] = empty_list()
    aic_claim_measure: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.aic_id):
            self.MissingRequiredField("aic_id")
        if not isinstance(self.aic_id, AicTrustworthinessClaimAicId):
            self.aic_id = AicTrustworthinessClaimAicId(self.aic_id)

        if self._is_empty(self.aic_claim_system):
            self.MissingRequiredField("aic_claim_system")
        if not isinstance(self.aic_claim_system, AicSystemAicId):
            self.aic_claim_system = AicSystemAicId(self.aic_claim_system)

        if self._is_empty(self.aic_claim_property):
            self.MissingRequiredField("aic_claim_property")
        if not isinstance(self.aic_claim_property, AicTrustworthinessProperty):
            self.aic_claim_property = AicTrustworthinessProperty(self.aic_claim_property)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if not isinstance(self.aic_claim_evidence, list):
            self.aic_claim_evidence = [self.aic_claim_evidence] if self.aic_claim_evidence is not None else []
        self.aic_claim_evidence = [v if isinstance(v, str) else str(v) for v in self.aic_claim_evidence]

        if self.aic_claim_measure is not None and not isinstance(self.aic_claim_measure, str):
            self.aic_claim_measure = str(self.aic_claim_measure)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AicAssessment(YAMLRoot):
    """
    One verification or validation of a system.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO22989["AicAssessment"]
    class_class_curie: ClassVar[str] = "iso22989:AicAssessment"
    class_name: ClassVar[str] = "AicAssessment"
    class_model_uri: ClassVar[URIRef] = ISO22989.AicAssessment

    aic_id: Union[str, AicAssessmentAicId] = None
    aic_assessment_kind: Union[str, "AicAssessmentKind"] = None
    aic_assessment_system: Union[str, AicSystemAicId] = None
    title: str = None
    aic_assessment_method: Optional[str] = None
    aic_assessment_result: Optional[str] = None
    aic_assessment_date: Optional[Union[str, XSDDate]] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.aic_id):
            self.MissingRequiredField("aic_id")
        if not isinstance(self.aic_id, AicAssessmentAicId):
            self.aic_id = AicAssessmentAicId(self.aic_id)

        if self._is_empty(self.aic_assessment_kind):
            self.MissingRequiredField("aic_assessment_kind")
        if not isinstance(self.aic_assessment_kind, AicAssessmentKind):
            self.aic_assessment_kind = AicAssessmentKind(self.aic_assessment_kind)

        if self._is_empty(self.aic_assessment_system):
            self.MissingRequiredField("aic_assessment_system")
        if not isinstance(self.aic_assessment_system, AicSystemAicId):
            self.aic_assessment_system = AicSystemAicId(self.aic_assessment_system)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self.aic_assessment_method is not None and not isinstance(self.aic_assessment_method, str):
            self.aic_assessment_method = str(self.aic_assessment_method)

        if self.aic_assessment_result is not None and not isinstance(self.aic_assessment_result, str):
            self.aic_assessment_result = str(self.aic_assessment_result)

        if self.aic_assessment_date is not None and not isinstance(self.aic_assessment_date, XSDDate):
            self.aic_assessment_date = XSDDate(self.aic_assessment_date)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AicLifecycleProcess(YAMLRoot):
    """
    A piece of work done at one stage of a system's life.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO22989["AicLifecycleProcess"]
    class_class_curie: ClassVar[str] = "iso22989:AicLifecycleProcess"
    class_name: ClassVar[str] = "AicLifecycleProcess"
    class_model_uri: ClassVar[URIRef] = ISO22989.AicLifecycleProcess

    aic_id: Union[str, AicLifecycleProcessAicId] = None
    aic_lifecycle_stage: Union[str, "AicLifecycleStage"] = None
    title: str = None
    aic_lifecycle_system: Optional[Union[str, AicSystemAicId]] = None
    aic_lifecycle_inputs: Optional[Union[str, list[str]]] = empty_list()
    aic_lifecycle_outputs: Optional[Union[str, list[str]]] = empty_list()
    aic_lifecycle_responsible: Optional[Union[str, AicStakeholderAicId]] = None
    aic_lifecycle_start: Optional[Union[str, XSDDate]] = None
    aic_lifecycle_end: Optional[Union[str, XSDDate]] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.aic_id):
            self.MissingRequiredField("aic_id")
        if not isinstance(self.aic_id, AicLifecycleProcessAicId):
            self.aic_id = AicLifecycleProcessAicId(self.aic_id)

        if self._is_empty(self.aic_lifecycle_stage):
            self.MissingRequiredField("aic_lifecycle_stage")
        if not isinstance(self.aic_lifecycle_stage, AicLifecycleStage):
            self.aic_lifecycle_stage = AicLifecycleStage(self.aic_lifecycle_stage)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self.aic_lifecycle_system is not None and not isinstance(self.aic_lifecycle_system, AicSystemAicId):
            self.aic_lifecycle_system = AicSystemAicId(self.aic_lifecycle_system)

        if not isinstance(self.aic_lifecycle_inputs, list):
            self.aic_lifecycle_inputs = [self.aic_lifecycle_inputs] if self.aic_lifecycle_inputs is not None else []
        self.aic_lifecycle_inputs = [v if isinstance(v, str) else str(v) for v in self.aic_lifecycle_inputs]

        if not isinstance(self.aic_lifecycle_outputs, list):
            self.aic_lifecycle_outputs = [self.aic_lifecycle_outputs] if self.aic_lifecycle_outputs is not None else []
        self.aic_lifecycle_outputs = [v if isinstance(v, str) else str(v) for v in self.aic_lifecycle_outputs]

        if self.aic_lifecycle_responsible is not None and not isinstance(self.aic_lifecycle_responsible, AicStakeholderAicId):
            self.aic_lifecycle_responsible = AicStakeholderAicId(self.aic_lifecycle_responsible)

        if self.aic_lifecycle_start is not None and not isinstance(self.aic_lifecycle_start, XSDDate):
            self.aic_lifecycle_start = XSDDate(self.aic_lifecycle_start)

        if self.aic_lifecycle_end is not None and not isinstance(self.aic_lifecycle_end, XSDDate):
            self.aic_lifecycle_end = XSDDate(self.aic_lifecycle_end)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AicStakeholder(YAMLRoot):
    """
    A person, group or organization with a part in an AI system or an interest in it.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO22989["AicStakeholder"]
    class_class_curie: ClassVar[str] = "iso22989:AicStakeholder"
    class_name: ClassVar[str] = "AicStakeholder"
    class_model_uri: ClassVar[URIRef] = ISO22989.AicStakeholder

    aic_id: Union[str, AicStakeholderAicId] = None
    aic_stakeholder_role: Union[str, "AicStakeholderRole"] = None
    title: str = None
    aic_stakeholder_sub_roles: Optional[Union[Union[str, "AicStakeholderSubRole"], list[Union[str, "AicStakeholderSubRole"]]]] = empty_list()
    aic_stakeholder_organization: Optional[str] = None
    aic_stakeholder_contact: Optional[str] = None
    aic_stakeholder_responsibilities: Optional[Union[str, list[str]]] = empty_list()
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.aic_id):
            self.MissingRequiredField("aic_id")
        if not isinstance(self.aic_id, AicStakeholderAicId):
            self.aic_id = AicStakeholderAicId(self.aic_id)

        if self._is_empty(self.aic_stakeholder_role):
            self.MissingRequiredField("aic_stakeholder_role")
        if not isinstance(self.aic_stakeholder_role, AicStakeholderRole):
            self.aic_stakeholder_role = AicStakeholderRole(self.aic_stakeholder_role)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if not isinstance(self.aic_stakeholder_sub_roles, list):
            self.aic_stakeholder_sub_roles = [self.aic_stakeholder_sub_roles] if self.aic_stakeholder_sub_roles is not None else []
        self.aic_stakeholder_sub_roles = [v if isinstance(v, AicStakeholderSubRole) else AicStakeholderSubRole(v) for v in self.aic_stakeholder_sub_roles]

        if self.aic_stakeholder_organization is not None and not isinstance(self.aic_stakeholder_organization, str):
            self.aic_stakeholder_organization = str(self.aic_stakeholder_organization)

        if self.aic_stakeholder_contact is not None and not isinstance(self.aic_stakeholder_contact, str):
            self.aic_stakeholder_contact = str(self.aic_stakeholder_contact)

        if not isinstance(self.aic_stakeholder_responsibilities, list):
            self.aic_stakeholder_responsibilities = [self.aic_stakeholder_responsibilities] if self.aic_stakeholder_responsibilities is not None else []
        self.aic_stakeholder_responsibilities = [v if isinstance(v, str) else str(v) for v in self.aic_stakeholder_responsibilities]

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AicPrediction(YAMLRoot):
    """
    A result a system worked out for one case.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO22989["AicPrediction"]
    class_class_curie: ClassVar[str] = "iso22989:AicPrediction"
    class_name: ClassVar[str] = "AicPrediction"
    class_model_uri: ClassVar[URIRef] = ISO22989.AicPrediction

    aic_id: Union[str, AicPredictionAicId] = None
    aic_prediction_system: Union[str, AicSystemAicId] = None
    aic_prediction_value: str = None
    title: str = None
    aic_prediction_confidence: Optional[float] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.aic_id):
            self.MissingRequiredField("aic_id")
        if not isinstance(self.aic_id, AicPredictionAicId):
            self.aic_id = AicPredictionAicId(self.aic_id)

        if self._is_empty(self.aic_prediction_system):
            self.MissingRequiredField("aic_prediction_system")
        if not isinstance(self.aic_prediction_system, AicSystemAicId):
            self.aic_prediction_system = AicSystemAicId(self.aic_prediction_system)

        if self._is_empty(self.aic_prediction_value):
            self.MissingRequiredField("aic_prediction_value")
        if not isinstance(self.aic_prediction_value, str):
            self.aic_prediction_value = str(self.aic_prediction_value)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self.aic_prediction_confidence is not None and not isinstance(self.aic_prediction_confidence, float):
            self.aic_prediction_confidence = float(self.aic_prediction_confidence)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AicDecision(YAMLRoot):
    """
    A choice made on the strength of some predictions.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO22989["AicDecision"]
    class_class_curie: ClassVar[str] = "iso22989:AicDecision"
    class_name: ClassVar[str] = "AicDecision"
    class_model_uri: ClassVar[URIRef] = ISO22989.AicDecision

    aic_id: Union[str, AicDecisionAicId] = None
    aic_decision_outcome: str = None
    title: str = None
    aic_decision_predictions: Optional[Union[Union[str, AicPredictionAicId], list[Union[str, AicPredictionAicId]]]] = empty_list()
    aic_decision_criteria: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.aic_id):
            self.MissingRequiredField("aic_id")
        if not isinstance(self.aic_id, AicDecisionAicId):
            self.aic_id = AicDecisionAicId(self.aic_id)

        if self._is_empty(self.aic_decision_outcome):
            self.MissingRequiredField("aic_decision_outcome")
        if not isinstance(self.aic_decision_outcome, str):
            self.aic_decision_outcome = str(self.aic_decision_outcome)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if not isinstance(self.aic_decision_predictions, list):
            self.aic_decision_predictions = [self.aic_decision_predictions] if self.aic_decision_predictions is not None else []
        self.aic_decision_predictions = [v if isinstance(v, AicPredictionAicId) else AicPredictionAicId(v) for v in self.aic_decision_predictions]

        if self.aic_decision_criteria is not None and not isinstance(self.aic_decision_criteria, str):
            self.aic_decision_criteria = str(self.aic_decision_criteria)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AicAction(YAMLRoot):
    """
    What was done because of a decision.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO22989["AicAction"]
    class_class_curie: ClassVar[str] = "iso22989:AicAction"
    class_name: ClassVar[str] = "AicAction"
    class_model_uri: ClassVar[URIRef] = ISO22989.AicAction

    aic_id: Union[str, AicActionAicId] = None
    aic_action_decision: Union[str, AicDecisionAicId] = None
    title: str = None
    aic_action_target: Optional[str] = None
    aic_action_time: Optional[Union[str, XSDDateTime]] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.aic_id):
            self.MissingRequiredField("aic_id")
        if not isinstance(self.aic_id, AicActionAicId):
            self.aic_id = AicActionAicId(self.aic_id)

        if self._is_empty(self.aic_action_decision):
            self.MissingRequiredField("aic_action_decision")
        if not isinstance(self.aic_action_decision, AicDecisionAicId):
            self.aic_action_decision = AicDecisionAicId(self.aic_action_decision)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self.aic_action_target is not None and not isinstance(self.aic_action_target, str):
            self.aic_action_target = str(self.aic_action_target)

        if self.aic_action_time is not None and not isinstance(self.aic_action_time, XSDDateTime):
            self.aic_action_time = XSDDateTime(self.aic_action_time)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AicApplication(YAMLRoot):
    """
    One use of a system in a line of work.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO22989["AicApplication"]
    class_class_curie: ClassVar[str] = "iso22989:AicApplication"
    class_name: ClassVar[str] = "AicApplication"
    class_model_uri: ClassVar[URIRef] = ISO22989.AicApplication

    aic_id: Union[str, AicApplicationAicId] = None
    aic_application_system: Union[str, AicSystemAicId] = None
    title: str = None
    aic_application_domain: Optional[Union[str, "AicApplicationDomain"]] = None
    aic_application_sector: Optional[str] = None
    aic_application_purpose: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.aic_id):
            self.MissingRequiredField("aic_id")
        if not isinstance(self.aic_id, AicApplicationAicId):
            self.aic_id = AicApplicationAicId(self.aic_id)

        if self._is_empty(self.aic_application_system):
            self.MissingRequiredField("aic_application_system")
        if not isinstance(self.aic_application_system, AicSystemAicId):
            self.aic_application_system = AicSystemAicId(self.aic_application_system)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self.aic_application_domain is not None and not isinstance(self.aic_application_domain, AicApplicationDomain):
            self.aic_application_domain = AicApplicationDomain(self.aic_application_domain)

        if self.aic_application_sector is not None and not isinstance(self.aic_application_sector, str):
            self.aic_application_sector = str(self.aic_application_sector)

        if self.aic_application_purpose is not None and not isinstance(self.aic_application_purpose, str):
            self.aic_application_purpose = str(self.aic_application_purpose)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AicResourcePool(YAMLRoot):
    """
    A body of computing resource that AI work can draw on.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO22989["AicResourcePool"]
    class_class_curie: ClassVar[str] = "iso22989:AicResourcePool"
    class_name: ClassVar[str] = "AicResourcePool"
    class_model_uri: ClassVar[URIRef] = ISO22989.AicResourcePool

    aic_id: Union[str, AicResourcePoolAicId] = None
    title: str = None
    aic_pool_kind: Optional[Union[str, "AicResourceKind"]] = None
    aic_pool_hardware: Optional[str] = None
    aic_pool_capacity: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.aic_id):
            self.MissingRequiredField("aic_id")
        if not isinstance(self.aic_id, AicResourcePoolAicId):
            self.aic_id = AicResourcePoolAicId(self.aic_id)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self.aic_pool_kind is not None and not isinstance(self.aic_pool_kind, AicResourceKind):
            self.aic_pool_kind = AicResourceKind(self.aic_pool_kind)

        if self.aic_pool_hardware is not None and not isinstance(self.aic_pool_hardware, str):
            self.aic_pool_hardware = str(self.aic_pool_hardware)

        if self.aic_pool_capacity is not None and not isinstance(self.aic_pool_capacity, str):
            self.aic_pool_capacity = str(self.aic_pool_capacity)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AicIotDevice(YAMLRoot):
    """
    A connected device that reads from or acts on its physical surroundings.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO22989["AicIotDevice"]
    class_class_curie: ClassVar[str] = "iso22989:AicIotDevice"
    class_name: ClassVar[str] = "AicIotDevice"
    class_model_uri: ClassVar[URIRef] = ISO22989.AicIotDevice

    aic_id: Union[str, AicIotDeviceAicId] = None
    title: str = None
    aic_device_senses: Optional[Union[str, list[str]]] = empty_list()
    aic_device_actuates: Optional[Union[str, list[str]]] = empty_list()
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.aic_id):
            self.MissingRequiredField("aic_id")
        if not isinstance(self.aic_id, AicIotDeviceAicId):
            self.aic_id = AicIotDeviceAicId(self.aic_id)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if not isinstance(self.aic_device_senses, list):
            self.aic_device_senses = [self.aic_device_senses] if self.aic_device_senses is not None else []
        self.aic_device_senses = [v if isinstance(v, str) else str(v) for v in self.aic_device_senses]

        if not isinstance(self.aic_device_actuates, list):
            self.aic_device_actuates = [self.aic_device_actuates] if self.aic_device_actuates is not None else []
        self.aic_device_actuates = [v if isinstance(v, str) else str(v) for v in self.aic_device_actuates]

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AicIotSystem(YAMLRoot):
    """
    A networked system that links devices and offers services built on them.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO22989["AicIotSystem"]
    class_class_curie: ClassVar[str] = "iso22989:AicIotSystem"
    class_name: ClassVar[str] = "AicIotSystem"
    class_model_uri: ClassVar[URIRef] = ISO22989.AicIotSystem

    aic_id: Union[str, AicIotSystemAicId] = None
    aic_iot_devices: Union[Union[str, AicIotDeviceAicId], list[Union[str, AicIotDeviceAicId]]] = None
    title: str = None
    aic_iot_ai_systems: Optional[Union[Union[str, AicSystemAicId], list[Union[str, AicSystemAicId]]]] = empty_list()
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.aic_id):
            self.MissingRequiredField("aic_id")
        if not isinstance(self.aic_id, AicIotSystemAicId):
            self.aic_id = AicIotSystemAicId(self.aic_id)

        if self._is_empty(self.aic_iot_devices):
            self.MissingRequiredField("aic_iot_devices")
        if not isinstance(self.aic_iot_devices, list):
            self.aic_iot_devices = [self.aic_iot_devices] if self.aic_iot_devices is not None else []
        self.aic_iot_devices = [v if isinstance(v, AicIotDeviceAicId) else AicIotDeviceAicId(v) for v in self.aic_iot_devices]

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if not isinstance(self.aic_iot_ai_systems, list):
            self.aic_iot_ai_systems = [self.aic_iot_ai_systems] if self.aic_iot_ai_systems is not None else []
        self.aic_iot_ai_systems = [v if isinstance(v, AicSystemAicId) else AicSystemAicId(v) for v in self.aic_iot_ai_systems]

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AicCyberPhysicalSystem(YAMLRoot):
    """
    Computing and physical processes tied in a loop, each affecting the other.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO22989["AicCyberPhysicalSystem"]
    class_class_curie: ClassVar[str] = "iso22989:AicCyberPhysicalSystem"
    class_name: ClassVar[str] = "AicCyberPhysicalSystem"
    class_model_uri: ClassVar[URIRef] = ISO22989.AicCyberPhysicalSystem

    aic_id: Union[str, AicCyberPhysicalSystemAicId] = None
    aic_cps_physical_processes: Union[str, list[str]] = None
    title: str = None
    aic_cps_iot_system: Optional[Union[str, AicIotSystemAicId]] = None
    aic_cps_ai_systems: Optional[Union[Union[str, AicSystemAicId], list[Union[str, AicSystemAicId]]]] = empty_list()
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.aic_id):
            self.MissingRequiredField("aic_id")
        if not isinstance(self.aic_id, AicCyberPhysicalSystemAicId):
            self.aic_id = AicCyberPhysicalSystemAicId(self.aic_id)

        if self._is_empty(self.aic_cps_physical_processes):
            self.MissingRequiredField("aic_cps_physical_processes")
        if not isinstance(self.aic_cps_physical_processes, list):
            self.aic_cps_physical_processes = [self.aic_cps_physical_processes] if self.aic_cps_physical_processes is not None else []
        self.aic_cps_physical_processes = [v if isinstance(v, str) else str(v) for v in self.aic_cps_physical_processes]

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self.aic_cps_iot_system is not None and not isinstance(self.aic_cps_iot_system, AicIotSystemAicId):
            self.aic_cps_iot_system = AicIotSystemAicId(self.aic_cps_iot_system)

        if not isinstance(self.aic_cps_ai_systems, list):
            self.aic_cps_ai_systems = [self.aic_cps_ai_systems] if self.aic_cps_ai_systems is not None else []
        self.aic_cps_ai_systems = [v if isinstance(v, AicSystemAicId) else AicSystemAicId(v) for v in self.aic_cps_ai_systems]

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


# Enumerations
class AicSystemScope(EnumDefinitionImpl):
    """
    How wide a range of problems a system can take on.
    """
    narrow_ai = PermissibleValue(
        text="narrow_ai",
        description="Built for a bounded set of problems, and cannot move beyond them.")
    general_ai = PermissibleValue(
        text="general_ai",
        description="Able to take on problems of many kinds, including ones it was not built for.")

    _defn = EnumDefinition(
        name="AicSystemScope",
        description="How wide a range of problems a system can take on.",
    )

class AicApproach(EnumDefinitionImpl):
    """
    Whether a system works on explicit symbols or on learned numeric encodings.
    """
    symbolic = PermissibleValue(
        text="symbolic",
        description="Works by manipulating explicit symbols and the rules that relate them.")
    subsymbolic = PermissibleValue(
        text="subsymbolic",
        description="""Works on numeric encodings that carry meaning only as a whole, such as the weights of a network.""")

    _defn = EnumDefinition(
        name="AicApproach",
        description="Whether a system works on explicit symbols or on learned numeric encodings.",
    )

class AicTechnique(EnumDefinitionImpl):
    """
    A family of techniques a system is built with.
    """
    machine_learning = PermissibleValue(
        text="machine_learning",
        description="Fits a model's numbers to data rather than having a person write the logic.")
    deep_learning = PermissibleValue(
        text="deep_learning",
        description="Machine learning that stacks many layers of a network.")
    cognitive_computing = PermissibleValue(
        text="cognitive_computing",
        description="Aims at interaction with people that feels closer to how people deal with one another.")
    semantic_computing = PermissibleValue(
        text="semantic_computing",
        description="Works out what content and requests mean, so that it can act on the meaning.")
    soft_computing = PermissibleValue(
        text="soft_computing",
        description="Accepts inexact or uncertain reasoning where an exact answer would cost too much.")
    genetic_algorithm = PermissibleValue(
        text="genetic_algorithm",
        description="Searches by breeding and selecting candidate answers over many generations.")
    logic_programming = PermissibleValue(
        text="logic_programming",
        description="States facts and rules in logic, and lets a solver reach the conclusions.")

    _defn = EnumDefinition(
        name="AicTechnique",
        description="A family of techniques a system is built with.",
    )

class AicAutonomy(EnumDefinitionImpl):
    """
    Whether a system can change its own remit or stays under outside direction.
    """
    autonomous = PermissibleValue(
        text="autonomous",
        description="Can change what it is for or where it applies with nobody directing it.")
    heteronomous = PermissibleValue(
        text="heteronomous",
        description="Stays under the direction of a person or another system.")

    _defn = EnumDefinition(
        name="AicAutonomy",
        description="Whether a system can change its own remit or stays under outside direction.",
    )

class AicKnowledgeKind(EnumDefinitionImpl):
    """
    How a body of knowledge is put.
    """
    declarative = PermissibleValue(
        text="declarative",
        description="States what is the case.")
    procedural = PermissibleValue(
        text="procedural",
        description="States what to do, step by step.")

    _defn = EnumDefinition(
        name="AicKnowledgeKind",
        description="How a body of knowledge is put.",
    )

class AicFunctionalStep(EnumDefinitionImpl):
    """
    A step in how a system gets from data to acting on its results.
    """
    data_and_information = PermissibleValue(
        text="data_and_information",
        description="Taking in data and giving it meaning.")
    knowledge_and_learning = PermissibleValue(
        text="knowledge_and_learning",
        description="Building up what the system knows, and learning from more data.")
    prediction = PermissibleValue(
        text="prediction",
        description="Working out a likely result for the case in hand.")
    decision = PermissibleValue(
        text="decision",
        description="Choosing what to do, given the results so far.")
    action = PermissibleValue(
        text="action",
        description="Carrying out what was chosen.")

    _defn = EnumDefinition(
        name="AicFunctionalStep",
        description="A step in how a system gets from data to acting on its results.",
    )

class AicLearningParadigm(EnumDefinitionImpl):
    """
    How a model learns from its data.
    """
    supervised = PermissibleValue(
        text="supervised",
        description="Every example comes with the answer it should give.")
    unsupervised = PermissibleValue(
        text="unsupervised",
        description="No example comes with an answer, so the model looks for structure.")
    semi_supervised = PermissibleValue(
        text="semi_supervised",
        description="Some examples come with answers and the rest do not.")
    reinforcement = PermissibleValue(
        text="reinforcement",
        description="The model acts, gets a reward or penalty, and adjusts to earn more reward.")
    transfer = PermissibleValue(
        text="transfer",
        description="What was learned on one problem gives a start on another.")

    _defn = EnumDefinition(
        name="AicLearningParadigm",
        description="How a model learns from its data.",
    )

class AicAlgorithmFamily(EnumDefinitionImpl):
    """
    A family of algorithms that fit machine learning models.
    """
    neural_network = PermissibleValue(
        text="neural_network",
        description="Layers of simple units whose connection weights are tuned to the data.")
    bayesian_network = PermissibleValue(
        text="bayesian_network",
        description="A graph of variables and how the probability of one depends on others.")
    decision_tree = PermissibleValue(
        text="decision_tree",
        description="A series of branching tests that end in a result.")
    support_vector_machine = PermissibleValue(
        text="support_vector_machine",
        description="Finds the widest gap that separates the classes of example.")

    _defn = EnumDefinition(
        name="AicAlgorithmFamily",
        description="A family of algorithms that fit machine learning models.",
    )

class AicNetworkArchitecture(EnumDefinitionImpl):
    """
    How the layers of a neural network are connected.
    """
    feed_forward = PermissibleValue(
        text="feed_forward",
        description="Signals pass one way, from first layer to last, with no loops.")
    recurrent = PermissibleValue(
        text="recurrent",
        description="Outputs feed back as inputs, so the network can follow a sequence.")
    long_short_term_memory = PermissibleValue(
        text="long_short_term_memory",
        description="A recurrent design whose gates let it carry a signal across long sequences.")
    convolutional = PermissibleValue(
        text="convolutional",
        description="Layers slide small filters across the input, as is usual for images.")

    _defn = EnumDefinition(
        name="AicNetworkArchitecture",
        description="How the layers of a neural network are connected.",
    )

class AicDatasetRole(EnumDefinitionImpl):
    """
    What a dataset is used for.
    """
    training = PermissibleValue(
        text="training",
        description="Used to fit a model.")
    validation = PermissibleValue(
        text="validation",
        description="Used while developing a model, to compare versions and tune settings.")
    test = PermissibleValue(
        text="test",
        description="Held back from development, to judge the finished model.")
    production = PermissibleValue(
        text="production",
        description="Gathered while the system runs, when it is deployed and in real use.")
    input = PermissibleValue(
        text="input",
        description="What a system is given so that it can work out a result.")

    _defn = EnumDefinition(
        name="AicDatasetRole",
        description="What a dataset is used for.",
    )

class AicDataProcessKind(EnumDefinitionImpl):
    """
    A kind of work done on data before or while a model uses it.
    """
    data_annotation = PermissibleValue(
        text="data_annotation",
        description="Adds descriptive notes to data and leaves the data itself as it was.")
    data_quality_checking = PermissibleValue(
        text="data_quality_checking",
        description="Looks for gaps, skew and whatever else would limit the data's use.")
    data_augmentation = PermissibleValue(
        text="data_augmentation",
        description="Makes new samples out of existing ones by altering them.")
    data_sampling = PermissibleValue(
        text="data_sampling",
        description="Picks a smaller part of the data that behaves like the whole.")
    exploratory_data_analysis = PermissibleValue(
        text="exploratory_data_analysis",
        description="A first look at data to learn its shape and what it may hold.")
    imputation = PermissibleValue(
        text="imputation",
        description="Fills gaps with values worked out from what is there.")

    _defn = EnumDefinition(
        name="AicDataProcessKind",
        description="A kind of work done on data before or while a model uses it.",
    )

class AicTrustworthinessProperty(EnumDefinitionImpl):
    """
    A property a trustworthiness claim is about.
    """
    robustness = PermissibleValue(
        text="robustness",
        description="Keeps performing well when conditions turn hostile or unusual.")
    reliability = PermissibleValue(
        text="reliability",
        description="Behaves and delivers as intended, time after time.")
    resilience = PermissibleValue(
        text="resilience",
        description="Gets back to working order soon after something goes wrong.")
    controllability = PermissibleValue(
        text="controllability",
        description="A person or another system can step in and steer it.")
    explainability = PermissibleValue(
        text="explainability",
        description="Can say, in terms people follow, what drove a result.")
    predictability = PermissibleValue(
        text="predictability",
        description="Lets people form sound expectations of what it will produce.")
    organizational_transparency = PermissibleValue(
        text="organizational_transparency",
        description="The organization tells those concerned what it does and decides.")
    system_transparency = PermissibleValue(
        text="system_transparency",
        description="Those concerned can learn what they need to know about the system.")
    bias_and_fairness = PermissibleValue(
        text="bias_and_fairness",
        description="Whether the system treats some people or things worse than others, as a pattern.")
    accountability = PermissibleValue(
        text="accountability",
        description="Someone answers for what the system does and decides.")
    availability = PermissibleValue(
        text="availability",
        description="Those entitled to use it can reach it and use it when they ask.")

    _defn = EnumDefinition(
        name="AicTrustworthinessProperty",
        description="A property a trustworthiness claim is about.",
    )

class AicAssessmentKind(EnumDefinitionImpl):
    """
    Which question an assessment answers.
    """
    verification = PermissibleValue(
        text="verification",
        description="Evidence shows that the system meets what was specified for it.")
    validation = PermissibleValue(
        text="validation",
        description="Evidence shows that the system suits the use it is meant for.")

    _defn = EnumDefinition(
        name="AicAssessmentKind",
        description="Which question an assessment answers.",
    )

class AicStakeholderRole(EnumDefinitionImpl):
    """
    The part a party plays around an AI system.
    """
    ai_provider = PermissibleValue(
        text="ai_provider",
        description="Offers AI products or services, or the platform for them.")
    ai_producer = PermissibleValue(
        text="ai_producer",
        description="Designs, builds, tests or runs AI systems.")
    ai_customer = PermissibleValue(
        text="ai_customer",
        description="Takes an AI product or service for its own use.")
    ai_partner = PermissibleValue(
        text="ai_partner",
        description="Helps others in the ecosystem, by integrating systems or supplying data.")
    ai_subject = PermissibleValue(
        text="ai_subject",
        description="Is affected by an AI system, or has data about them used in it.")
    relevant_authority = PermissibleValue(
        text="relevant_authority",
        description="Sets policy for AI or holds others to the rules on it.")

    _defn = EnumDefinition(
        name="AicStakeholderRole",
        description="The part a party plays around an AI system.",
    )

class AicStakeholderSubRole(EnumDefinitionImpl):
    """
    A narrower part within one of the roles.
    """
    ai_platform_provider = PermissibleValue(
        text="ai_platform_provider",
        description="Offers the platform that others run AI on.")
    ai_product_or_service_provider = PermissibleValue(
        text="ai_product_or_service_provider",
        description="Offers a finished AI product or a service built on AI.")
    ai_developer = PermissibleValue(
        text="ai_developer",
        description="Writes and builds the system.")
    ai_user = PermissibleValue(
        text="ai_user",
        description="Uses the system directly.")
    ai_system_integrator = PermissibleValue(
        text="ai_system_integrator",
        description="Fits AI parts into a larger system.")
    data_provider = PermissibleValue(
        text="data_provider",
        description="Supplies data that others build or run on.")
    data_subject = PermissibleValue(
        text="data_subject",
        description="A person the data is about.")
    other_subject = PermissibleValue(
        text="other_subject",
        description="Anyone else a system affects.")
    policy_maker = PermissibleValue(
        text="policy_maker",
        description="Decides policy on AI.")
    regulator = PermissibleValue(
        text="regulator",
        description="Holds others to the rules on AI.")

    _defn = EnumDefinition(
        name="AicStakeholderSubRole",
        description="A narrower part within one of the roles.",
    )

class AicLifecycleStage(EnumDefinitionImpl):
    """
    A stage in an AI system's life.
    """
    inception = PermissibleValue(
        text="inception",
        description="Deciding that a system is wanted, what it is for and whether it can be done.")
    design_and_development = PermissibleValue(
        text="design_and_development",
        description="Making the system, from its architecture through its data work to its models.")
    verification_and_validation = PermissibleValue(
        text="verification_and_validation",
        description="Checking what was made against its specification and against its purpose.")
    deployment = PermissibleValue(
        text="deployment",
        description="Installing the system where it is to run, and making it ready for use.")
    operation_and_monitoring = PermissibleValue(
        text="operation_and_monitoring",
        description="Running the system and keeping an eye on how it behaves.")
    continuous_validation = PermissibleValue(
        text="continuous_validation",
        description="Repeating the checks on a system that goes on learning as it runs.")
    re_evaluation = PermissibleValue(
        text="re_evaluation",
        description="Looking again at whether the running system still meets its aims.")
    retirement = PermissibleValue(
        text="retirement",
        description="Taking the system out of use.")

    _defn = EnumDefinition(
        name="AicLifecycleStage",
        description="A stage in an AI system's life.",
    )

class AicOecdLifecycleStage(EnumDefinitionImpl):
    """
    A stage of the OECD's account of an AI system's life, which Annex A sets beside the standard's.
    """
    plan_and_design = PermissibleValue(
        text="plan_and_design",
        description="Setting out what the system is for and how it will work.")
    collect_and_process_data = PermissibleValue(
        text="collect_and_process_data",
        description="Gathering and readying the data.")
    build_and_use_model = PermissibleValue(
        text="build_and_use_model",
        description="Making the model and trying it.")
    verify_and_validate = PermissibleValue(
        text="verify_and_validate",
        description="Checking the model.")
    deploy = PermissibleValue(
        text="deploy",
        description="Putting the system into use.")
    operate_and_monitor = PermissibleValue(
        text="operate_and_monitor",
        description="Running the system and watching it.")

    _defn = EnumDefinition(
        name="AicOecdLifecycleStage",
        description="A stage of the OECD's account of an AI system's life, which Annex A sets beside the standard's.",
    )

class AicResourceKind(EnumDefinitionImpl):
    """
    A kind of computing resource AI work runs on.
    """
    cloud = PermissibleValue(
        text="cloud",
        description="Computing bought as a shared service, in someone else's data centre.")
    edge = PermissibleValue(
        text="edge",
        description="Computing close to where data arises, rather than in a far data centre.")
    application_specific_integrated_circuit = PermissibleValue(
        text="application_specific_integrated_circuit",
        description="A chip made for one kind of work, such as training or running a model.")

    _defn = EnumDefinition(
        name="AicResourceKind",
        description="A kind of computing resource AI work runs on.",
    )

class AicField(EnumDefinitionImpl):
    """
    A field of AI a system belongs to.
    """
    computer_vision = PermissibleValue(
        text="computer_vision",
        description="Making sense of pictures and video.")
    natural_language_processing = PermissibleValue(
        text="natural_language_processing",
        description="Making sense of, or producing, human language.")
    data_mining = PermissibleValue(
        text="data_mining",
        description="Finding patterns in large amounts of numbers.")
    planning = PermissibleValue(
        text="planning",
        description="Working out a sequence of steps that reaches an aim.")

    _defn = EnumDefinition(
        name="AicField",
        description="A field of AI a system belongs to.",
    )

class AicTaskKind(EnumDefinitionImpl):
    """
    A named kind of task from the fields of language and vision.
    """
    automatic_summarization = PermissibleValue(
        text="automatic_summarization",
        description="Cuts a text down to its main points.")
    dialogue_management = PermissibleValue(
        text="dialogue_management",
        description="Decides what to say next in a conversation.")
    emotion_recognition = PermissibleValue(
        text="emotion_recognition",
        description="Works out the feeling a text or voice conveys.")
    information_retrieval = PermissibleValue(
        text="information_retrieval",
        description="Finds stored documents that answer a need.")
    machine_translation = PermissibleValue(
        text="machine_translation",
        description="Renders text from one language in another.")
    named_entity_recognition = PermissibleValue(
        text="named_entity_recognition",
        description="Spots the people, places and other named things in a text.")
    natural_language_generation = PermissibleValue(
        text="natural_language_generation",
        description="Writes text from data or from an internal form.")
    natural_language_understanding = PermissibleValue(
        text="natural_language_understanding",
        description="Takes a text and draws out what it means.")
    optical_character_recognition = PermissibleValue(
        text="optical_character_recognition",
        description="Reads printed or written characters from a picture.")
    part_of_speech_tagging = PermissibleValue(
        text="part_of_speech_tagging",
        description="Marks each word as a noun, a verb and so on.")
    question_answering = PermissibleValue(
        text="question_answering",
        description="Replies to a question put in everyday words.")
    relationship_extraction = PermissibleValue(
        text="relationship_extraction",
        description="Finds how the things a text names relate to one another.")
    sentiment_analysis = PermissibleValue(
        text="sentiment_analysis",
        description="Works out the opinion a text expresses.")
    speech_recognition = PermissibleValue(
        text="speech_recognition",
        description="Turns spoken words into text.")
    speech_synthesis = PermissibleValue(
        text="speech_synthesis",
        description="Turns text into spoken words.")
    face_recognition = PermissibleValue(
        text="face_recognition",
        description="Matches a face in a picture against stored faces.")
    image_recognition = PermissibleValue(
        text="image_recognition",
        description="Says what a picture shows.")

    _defn = EnumDefinition(
        name="AicTaskKind",
        description="A named kind of task from the fields of language and vision.",
    )

class AicApplicationDomain(EnumDefinitionImpl):
    """
    A domain the standard works through as an application of AI.
    """
    fraud_detection = PermissibleValue(
        text="fraud_detection",
        description="Spotting dishonest transactions or claims.")
    automated_vehicles = PermissibleValue(
        text="automated_vehicles",
        description="Vehicles that drive part or all of the way without a driver.")
    predictive_maintenance = PermissibleValue(
        text="predictive_maintenance",
        description="Forecasting when equipment needs attention, before it fails.")

    _defn = EnumDefinition(
        name="AicApplicationDomain",
        description="A domain the standard works through as an application of AI.",
    )

# Slots
class slots:
    pass

slots.aic_id = Slot(uri=ISO22989.aic_id, name="aic_id", curie=ISO22989.curie('aic_id'),
                   model_uri=ISO22989.aic_id, domain=None, range=URIRef)

slots.title = Slot(uri=SCHEMA.name, name="title", curie=SCHEMA.curie('name'),
                   model_uri=ISO22989.title, domain=None, range=Optional[str])

slots.description = Slot(uri=SCHEMA.description, name="description", curie=SCHEMA.curie('description'),
                   model_uri=ISO22989.description, domain=None, range=Optional[str])

slots.aic_system_type = Slot(uri=ISO22989.aic_system_type, name="aic_system_type", curie=ISO22989.curie('aic_system_type'),
                   model_uri=ISO22989.aic_system_type, domain=None, range=str)

slots.aic_model_type = Slot(uri=ISO22989.aic_model_type, name="aic_model_type", curie=ISO22989.curie('aic_model_type'),
                   model_uri=ISO22989.aic_model_type, domain=None, range=str)

slots.aicEcosystem__aic_ecosystem_systems = Slot(uri=ISO22989.aic_ecosystem_systems, name="aicEcosystem__aic_ecosystem_systems", curie=ISO22989.curie('aic_ecosystem_systems'),
                   model_uri=ISO22989.aicEcosystem__aic_ecosystem_systems, domain=None, range=Optional[Union[dict[Union[str, AicSystemAicId], Union[dict, AicSystem]], list[Union[dict, AicSystem]]]])

slots.aicEcosystem__aic_ecosystem_components = Slot(uri=ISO22989.aic_ecosystem_components, name="aicEcosystem__aic_ecosystem_components", curie=ISO22989.curie('aic_ecosystem_components'),
                   model_uri=ISO22989.aicEcosystem__aic_ecosystem_components, domain=None, range=Optional[Union[dict[Union[str, AicComponentAicId], Union[dict, AicComponent]], list[Union[dict, AicComponent]]]])

slots.aicEcosystem__aic_ecosystem_knowledge = Slot(uri=ISO22989.aic_ecosystem_knowledge, name="aicEcosystem__aic_ecosystem_knowledge", curie=ISO22989.curie('aic_ecosystem_knowledge'),
                   model_uri=ISO22989.aicEcosystem__aic_ecosystem_knowledge, domain=None, range=Optional[Union[dict[Union[str, AicKnowledgeAicId], Union[dict, AicKnowledge]], list[Union[dict, AicKnowledge]]]])

slots.aicEcosystem__aic_ecosystem_tasks = Slot(uri=ISO22989.aic_ecosystem_tasks, name="aicEcosystem__aic_ecosystem_tasks", curie=ISO22989.curie('aic_ecosystem_tasks'),
                   model_uri=ISO22989.aicEcosystem__aic_ecosystem_tasks, domain=None, range=Optional[Union[dict[Union[str, AicTaskAicId], Union[dict, AicTask]], list[Union[dict, AicTask]]]])

slots.aicEcosystem__aic_ecosystem_models = Slot(uri=ISO22989.aic_ecosystem_models, name="aicEcosystem__aic_ecosystem_models", curie=ISO22989.curie('aic_ecosystem_models'),
                   model_uri=ISO22989.aicEcosystem__aic_ecosystem_models, domain=None, range=Optional[Union[dict[Union[str, AicModelAicId], Union[dict, AicModel]], list[Union[dict, AicModel]]]])

slots.aicEcosystem__aic_ecosystem_datasets = Slot(uri=ISO22989.aic_ecosystem_datasets, name="aicEcosystem__aic_ecosystem_datasets", curie=ISO22989.curie('aic_ecosystem_datasets'),
                   model_uri=ISO22989.aicEcosystem__aic_ecosystem_datasets, domain=None, range=Optional[Union[dict[Union[str, AicDatasetAicId], Union[dict, AicDataset]], list[Union[dict, AicDataset]]]])

slots.aicEcosystem__aic_ecosystem_stakeholders = Slot(uri=ISO22989.aic_ecosystem_stakeholders, name="aicEcosystem__aic_ecosystem_stakeholders", curie=ISO22989.curie('aic_ecosystem_stakeholders'),
                   model_uri=ISO22989.aicEcosystem__aic_ecosystem_stakeholders, domain=None, range=Optional[Union[dict[Union[str, AicStakeholderAicId], Union[dict, AicStakeholder]], list[Union[dict, AicStakeholder]]]])

slots.aicEcosystem__aic_ecosystem_lifecycle_processes = Slot(uri=ISO22989.aic_ecosystem_lifecycle_processes, name="aicEcosystem__aic_ecosystem_lifecycle_processes", curie=ISO22989.curie('aic_ecosystem_lifecycle_processes'),
                   model_uri=ISO22989.aicEcosystem__aic_ecosystem_lifecycle_processes, domain=None, range=Optional[Union[dict[Union[str, AicLifecycleProcessAicId], Union[dict, AicLifecycleProcess]], list[Union[dict, AicLifecycleProcess]]]])

slots.aicEcosystem__aic_ecosystem_claims = Slot(uri=ISO22989.aic_ecosystem_claims, name="aicEcosystem__aic_ecosystem_claims", curie=ISO22989.curie('aic_ecosystem_claims'),
                   model_uri=ISO22989.aicEcosystem__aic_ecosystem_claims, domain=None, range=Optional[Union[dict[Union[str, AicTrustworthinessClaimAicId], Union[dict, AicTrustworthinessClaim]], list[Union[dict, AicTrustworthinessClaim]]]])

slots.aicEcosystem__aic_ecosystem_assessments = Slot(uri=ISO22989.aic_ecosystem_assessments, name="aicEcosystem__aic_ecosystem_assessments", curie=ISO22989.curie('aic_ecosystem_assessments'),
                   model_uri=ISO22989.aicEcosystem__aic_ecosystem_assessments, domain=None, range=Optional[Union[dict[Union[str, AicAssessmentAicId], Union[dict, AicAssessment]], list[Union[dict, AicAssessment]]]])

slots.aicEcosystem__aic_ecosystem_predictions = Slot(uri=ISO22989.aic_ecosystem_predictions, name="aicEcosystem__aic_ecosystem_predictions", curie=ISO22989.curie('aic_ecosystem_predictions'),
                   model_uri=ISO22989.aicEcosystem__aic_ecosystem_predictions, domain=None, range=Optional[Union[dict[Union[str, AicPredictionAicId], Union[dict, AicPrediction]], list[Union[dict, AicPrediction]]]])

slots.aicEcosystem__aic_ecosystem_decisions = Slot(uri=ISO22989.aic_ecosystem_decisions, name="aicEcosystem__aic_ecosystem_decisions", curie=ISO22989.curie('aic_ecosystem_decisions'),
                   model_uri=ISO22989.aicEcosystem__aic_ecosystem_decisions, domain=None, range=Optional[Union[dict[Union[str, AicDecisionAicId], Union[dict, AicDecision]], list[Union[dict, AicDecision]]]])

slots.aicEcosystem__aic_ecosystem_actions = Slot(uri=ISO22989.aic_ecosystem_actions, name="aicEcosystem__aic_ecosystem_actions", curie=ISO22989.curie('aic_ecosystem_actions'),
                   model_uri=ISO22989.aicEcosystem__aic_ecosystem_actions, domain=None, range=Optional[Union[dict[Union[str, AicActionAicId], Union[dict, AicAction]], list[Union[dict, AicAction]]]])

slots.aicEcosystem__aic_ecosystem_applications = Slot(uri=ISO22989.aic_ecosystem_applications, name="aicEcosystem__aic_ecosystem_applications", curie=ISO22989.curie('aic_ecosystem_applications'),
                   model_uri=ISO22989.aicEcosystem__aic_ecosystem_applications, domain=None, range=Optional[Union[dict[Union[str, AicApplicationAicId], Union[dict, AicApplication]], list[Union[dict, AicApplication]]]])

slots.aicEcosystem__aic_ecosystem_resource_pools = Slot(uri=ISO22989.aic_ecosystem_resource_pools, name="aicEcosystem__aic_ecosystem_resource_pools", curie=ISO22989.curie('aic_ecosystem_resource_pools'),
                   model_uri=ISO22989.aicEcosystem__aic_ecosystem_resource_pools, domain=None, range=Optional[Union[dict[Union[str, AicResourcePoolAicId], Union[dict, AicResourcePool]], list[Union[dict, AicResourcePool]]]])

slots.aicEcosystem__aic_ecosystem_iot_devices = Slot(uri=ISO22989.aic_ecosystem_iot_devices, name="aicEcosystem__aic_ecosystem_iot_devices", curie=ISO22989.curie('aic_ecosystem_iot_devices'),
                   model_uri=ISO22989.aicEcosystem__aic_ecosystem_iot_devices, domain=None, range=Optional[Union[dict[Union[str, AicIotDeviceAicId], Union[dict, AicIotDevice]], list[Union[dict, AicIotDevice]]]])

slots.aicEcosystem__aic_ecosystem_iot_systems = Slot(uri=ISO22989.aic_ecosystem_iot_systems, name="aicEcosystem__aic_ecosystem_iot_systems", curie=ISO22989.curie('aic_ecosystem_iot_systems'),
                   model_uri=ISO22989.aicEcosystem__aic_ecosystem_iot_systems, domain=None, range=Optional[Union[dict[Union[str, AicIotSystemAicId], Union[dict, AicIotSystem]], list[Union[dict, AicIotSystem]]]])

slots.aicEcosystem__aic_ecosystem_cyber_physical_systems = Slot(uri=ISO22989.aic_ecosystem_cyber_physical_systems, name="aicEcosystem__aic_ecosystem_cyber_physical_systems", curie=ISO22989.curie('aic_ecosystem_cyber_physical_systems'),
                   model_uri=ISO22989.aicEcosystem__aic_ecosystem_cyber_physical_systems, domain=None, range=Optional[Union[dict[Union[str, AicCyberPhysicalSystemAicId], Union[dict, AicCyberPhysicalSystem]], list[Union[dict, AicCyberPhysicalSystem]]]])

slots.aicSystem__aic_system_purpose = Slot(uri=ISO22989.aic_system_purpose, name="aicSystem__aic_system_purpose", curie=ISO22989.curie('aic_system_purpose'),
                   model_uri=ISO22989.aicSystem__aic_system_purpose, domain=None, range=Optional[str])

slots.aicSystem__aic_system_scope = Slot(uri=ISO22989.aic_system_scope, name="aicSystem__aic_system_scope", curie=ISO22989.curie('aic_system_scope'),
                   model_uri=ISO22989.aicSystem__aic_system_scope, domain=None, range=Optional[Union[str, "AicSystemScope"]])

slots.aicSystem__aic_system_approaches = Slot(uri=ISO22989.aic_system_approaches, name="aicSystem__aic_system_approaches", curie=ISO22989.curie('aic_system_approaches'),
                   model_uri=ISO22989.aicSystem__aic_system_approaches, domain=None, range=Optional[Union[Union[str, "AicApproach"], list[Union[str, "AicApproach"]]]])

slots.aicSystem__aic_system_techniques = Slot(uri=ISO22989.aic_system_techniques, name="aicSystem__aic_system_techniques", curie=ISO22989.curie('aic_system_techniques'),
                   model_uri=ISO22989.aicSystem__aic_system_techniques, domain=None, range=Optional[Union[Union[str, "AicTechnique"], list[Union[str, "AicTechnique"]]]])

slots.aicSystem__aic_system_automated = Slot(uri=ISO22989.aic_system_automated, name="aicSystem__aic_system_automated", curie=ISO22989.curie('aic_system_automated'),
                   model_uri=ISO22989.aicSystem__aic_system_automated, domain=None, range=Optional[Union[bool, Bool]])

slots.aicSystem__aic_system_autonomy = Slot(uri=ISO22989.aic_system_autonomy, name="aicSystem__aic_system_autonomy", curie=ISO22989.curie('aic_system_autonomy'),
                   model_uri=ISO22989.aicSystem__aic_system_autonomy, domain=None, range=Optional[Union[str, "AicAutonomy"]])

slots.aicSystem__aic_system_human_teaming = Slot(uri=ISO22989.aic_system_human_teaming, name="aicSystem__aic_system_human_teaming", curie=ISO22989.curie('aic_system_human_teaming'),
                   model_uri=ISO22989.aicSystem__aic_system_human_teaming, domain=None, range=Optional[str])

slots.aicSystem__aic_system_stage = Slot(uri=ISO22989.aic_system_stage, name="aicSystem__aic_system_stage", curie=ISO22989.curie('aic_system_stage'),
                   model_uri=ISO22989.aicSystem__aic_system_stage, domain=None, range=Optional[Union[str, "AicLifecycleStage"]])

slots.aicSystem__aic_system_fields = Slot(uri=ISO22989.aic_system_fields, name="aicSystem__aic_system_fields", curie=ISO22989.curie('aic_system_fields'),
                   model_uri=ISO22989.aicSystem__aic_system_fields, domain=None, range=Optional[Union[Union[str, "AicField"], list[Union[str, "AicField"]]]])

slots.aicSystem__aic_system_steps = Slot(uri=ISO22989.aic_system_steps, name="aicSystem__aic_system_steps", curie=ISO22989.curie('aic_system_steps'),
                   model_uri=ISO22989.aicSystem__aic_system_steps, domain=None, range=Optional[Union[Union[str, "AicFunctionalStep"], list[Union[str, "AicFunctionalStep"]]]])

slots.aicSystem__aic_system_components = Slot(uri=ISO22989.aic_system_components, name="aicSystem__aic_system_components", curie=ISO22989.curie('aic_system_components'),
                   model_uri=ISO22989.aicSystem__aic_system_components, domain=None, range=Optional[Union[Union[str, AicComponentAicId], list[Union[str, AicComponentAicId]]]])

slots.aicSystem__aic_system_models = Slot(uri=ISO22989.aic_system_models, name="aicSystem__aic_system_models", curie=ISO22989.curie('aic_system_models'),
                   model_uri=ISO22989.aicSystem__aic_system_models, domain=None, range=Optional[Union[Union[str, AicModelAicId], list[Union[str, AicModelAicId]]]])

slots.aicSystem__aic_system_datasets = Slot(uri=ISO22989.aic_system_datasets, name="aicSystem__aic_system_datasets", curie=ISO22989.curie('aic_system_datasets'),
                   model_uri=ISO22989.aicSystem__aic_system_datasets, domain=None, range=Optional[Union[Union[str, AicDatasetAicId], list[Union[str, AicDatasetAicId]]]])

slots.aicSystem__aic_system_tasks = Slot(uri=ISO22989.aic_system_tasks, name="aicSystem__aic_system_tasks", curie=ISO22989.curie('aic_system_tasks'),
                   model_uri=ISO22989.aicSystem__aic_system_tasks, domain=None, range=Optional[Union[Union[str, AicTaskAicId], list[Union[str, AicTaskAicId]]]])

slots.aicSystem__aic_system_stakeholders = Slot(uri=ISO22989.aic_system_stakeholders, name="aicSystem__aic_system_stakeholders", curie=ISO22989.curie('aic_system_stakeholders'),
                   model_uri=ISO22989.aicSystem__aic_system_stakeholders, domain=None, range=Optional[Union[Union[str, AicStakeholderAicId], list[Union[str, AicStakeholderAicId]]]])

slots.aicSystem__aic_system_resource_pools = Slot(uri=ISO22989.aic_system_resource_pools, name="aicSystem__aic_system_resource_pools", curie=ISO22989.curie('aic_system_resource_pools'),
                   model_uri=ISO22989.aicSystem__aic_system_resource_pools, domain=None, range=Optional[Union[Union[str, AicResourcePoolAicId], list[Union[str, AicResourcePoolAicId]]]])

slots.aicSystem__aic_system_jurisdictional_issues = Slot(uri=ISO22989.aic_system_jurisdictional_issues, name="aicSystem__aic_system_jurisdictional_issues", curie=ISO22989.curie('aic_system_jurisdictional_issues'),
                   model_uri=ISO22989.aicSystem__aic_system_jurisdictional_issues, domain=None, range=Optional[Union[str, list[str]]])

slots.aicSystem__aic_system_societal_impacts = Slot(uri=ISO22989.aic_system_societal_impacts, name="aicSystem__aic_system_societal_impacts", curie=ISO22989.curie('aic_system_societal_impacts'),
                   model_uri=ISO22989.aicSystem__aic_system_societal_impacts, domain=None, range=Optional[Union[str, list[str]]])

slots.aicAgent__aic_agent_goals = Slot(uri=ISO22989.aic_agent_goals, name="aicAgent__aic_agent_goals", curie=ISO22989.curie('aic_agent_goals'),
                   model_uri=ISO22989.aicAgent__aic_agent_goals, domain=None, range=Union[str, list[str]])

slots.aicAgent__aic_agent_environment = Slot(uri=ISO22989.aic_agent_environment, name="aicAgent__aic_agent_environment", curie=ISO22989.curie('aic_agent_environment'),
                   model_uri=ISO22989.aicAgent__aic_agent_environment, domain=None, range=Optional[str])

slots.aicExpertSystem__aic_expert_knowledge = Slot(uri=ISO22989.aic_expert_knowledge, name="aicExpertSystem__aic_expert_knowledge", curie=ISO22989.curie('aic_expert_knowledge'),
                   model_uri=ISO22989.aicExpertSystem__aic_expert_knowledge, domain=None, range=Union[Union[str, AicKnowledgeAicId], list[Union[str, AicKnowledgeAicId]]])

slots.aicExpertSystem__aic_expert_inference = Slot(uri=ISO22989.aic_expert_inference, name="aicExpertSystem__aic_expert_inference", curie=ISO22989.curie('aic_expert_inference'),
                   model_uri=ISO22989.aicExpertSystem__aic_expert_inference, domain=None, range=Optional[str])

slots.aicRobot__aic_robot_actuators = Slot(uri=ISO22989.aic_robot_actuators, name="aicRobot__aic_robot_actuators", curie=ISO22989.curie('aic_robot_actuators'),
                   model_uri=ISO22989.aicRobot__aic_robot_actuators, domain=None, range=Union[str, list[str]])

slots.aicRobot__aic_robot_sensors = Slot(uri=ISO22989.aic_robot_sensors, name="aicRobot__aic_robot_sensors", curie=ISO22989.curie('aic_robot_sensors'),
                   model_uri=ISO22989.aicRobot__aic_robot_sensors, domain=None, range=Optional[Union[str, list[str]]])

slots.aicComponent__aic_component_step = Slot(uri=ISO22989.aic_component_step, name="aicComponent__aic_component_step", curie=ISO22989.curie('aic_component_step'),
                   model_uri=ISO22989.aicComponent__aic_component_step, domain=None, range=Optional[Union[str, "AicFunctionalStep"]])

slots.aicComponent__aic_component_depends_on = Slot(uri=ISO22989.aic_component_depends_on, name="aicComponent__aic_component_depends_on", curie=ISO22989.curie('aic_component_depends_on'),
                   model_uri=ISO22989.aicComponent__aic_component_depends_on, domain=None, range=Optional[Union[Union[str, AicComponentAicId], list[Union[str, AicComponentAicId]]]])

slots.aicKnowledge__aic_knowledge_kind = Slot(uri=ISO22989.aic_knowledge_kind, name="aicKnowledge__aic_knowledge_kind", curie=ISO22989.curie('aic_knowledge_kind'),
                   model_uri=ISO22989.aicKnowledge__aic_knowledge_kind, domain=None, range=Optional[Union[str, "AicKnowledgeKind"]])

slots.aicKnowledge__aic_knowledge_representation = Slot(uri=ISO22989.aic_knowledge_representation, name="aicKnowledge__aic_knowledge_representation", curie=ISO22989.curie('aic_knowledge_representation'),
                   model_uri=ISO22989.aicKnowledge__aic_knowledge_representation, domain=None, range=Optional[str])

slots.aicTask__aic_task_kind = Slot(uri=ISO22989.aic_task_kind, name="aicTask__aic_task_kind", curie=ISO22989.curie('aic_task_kind'),
                   model_uri=ISO22989.aicTask__aic_task_kind, domain=None, range=Optional[Union[str, "AicTaskKind"]])

slots.aicTask__aic_task_goal = Slot(uri=ISO22989.aic_task_goal, name="aicTask__aic_task_goal", curie=ISO22989.curie('aic_task_goal'),
                   model_uri=ISO22989.aicTask__aic_task_goal, domain=None, range=Optional[str])

slots.aicTask__aic_task_languages = Slot(uri=ISO22989.aic_task_languages, name="aicTask__aic_task_languages", curie=ISO22989.curie('aic_task_languages'),
                   model_uri=ISO22989.aicTask__aic_task_languages, domain=None, range=Optional[Union[str, list[str]]],
                   pattern=re.compile(r'^[A-Za-z]{2,8}(-[A-Za-z0-9]{1,8})*$'))

slots.aicTask__aic_task_performance_measures = Slot(uri=ISO22989.aic_task_performance_measures, name="aicTask__aic_task_performance_measures", curie=ISO22989.curie('aic_task_performance_measures'),
                   model_uri=ISO22989.aicTask__aic_task_performance_measures, domain=None, range=Optional[Union[str, list[str]]])

slots.aicModel__aic_model_version = Slot(uri=ISO22989.aic_model_version, name="aicModel__aic_model_version", curie=ISO22989.curie('aic_model_version'),
                   model_uri=ISO22989.aicModel__aic_model_version, domain=None, range=Optional[str])

slots.aicModel__aic_model_represents = Slot(uri=ISO22989.aic_model_represents, name="aicModel__aic_model_represents", curie=ISO22989.curie('aic_model_represents'),
                   model_uri=ISO22989.aicModel__aic_model_represents, domain=None, range=Optional[str])

slots.aicMachineLearningModel__aic_ml_paradigm = Slot(uri=ISO22989.aic_ml_paradigm, name="aicMachineLearningModel__aic_ml_paradigm", curie=ISO22989.curie('aic_ml_paradigm'),
                   model_uri=ISO22989.aicMachineLearningModel__aic_ml_paradigm, domain=None, range=Optional[Union[str, "AicLearningParadigm"]])

slots.aicMachineLearningModel__aic_ml_algorithm = Slot(uri=ISO22989.aic_ml_algorithm, name="aicMachineLearningModel__aic_ml_algorithm", curie=ISO22989.curie('aic_ml_algorithm'),
                   model_uri=ISO22989.aicMachineLearningModel__aic_ml_algorithm, domain=None, range=Optional[Union[str, "AicAlgorithmFamily"]])

slots.aicMachineLearningModel__aic_ml_datasets = Slot(uri=ISO22989.aic_ml_datasets, name="aicMachineLearningModel__aic_ml_datasets", curie=ISO22989.curie('aic_ml_datasets'),
                   model_uri=ISO22989.aicMachineLearningModel__aic_ml_datasets, domain=None, range=Optional[Union[Union[str, AicDatasetAicId], list[Union[str, AicDatasetAicId]]]])

slots.aicMachineLearningModel__aic_ml_hyperparameters = Slot(uri=ISO22989.aic_ml_hyperparameters, name="aicMachineLearningModel__aic_ml_hyperparameters", curie=ISO22989.curie('aic_ml_hyperparameters'),
                   model_uri=ISO22989.aicMachineLearningModel__aic_ml_hyperparameters, domain=None, range=Optional[Union[str, list[str]]])

slots.aicMachineLearningModel__aic_ml_parameter_count = Slot(uri=ISO22989.aic_ml_parameter_count, name="aicMachineLearningModel__aic_ml_parameter_count", curie=ISO22989.curie('aic_ml_parameter_count'),
                   model_uri=ISO22989.aicMachineLearningModel__aic_ml_parameter_count, domain=None, range=Optional[int])

slots.aicMachineLearningModel__aic_ml_trained_on = Slot(uri=ISO22989.aic_ml_trained_on, name="aicMachineLearningModel__aic_ml_trained_on", curie=ISO22989.curie('aic_ml_trained_on'),
                   model_uri=ISO22989.aicMachineLearningModel__aic_ml_trained_on, domain=None, range=Optional[Union[str, XSDDate]])

slots.aicMachineLearningModel__aic_ml_retrained_from = Slot(uri=ISO22989.aic_ml_retrained_from, name="aicMachineLearningModel__aic_ml_retrained_from", curie=ISO22989.curie('aic_ml_retrained_from'),
                   model_uri=ISO22989.aicMachineLearningModel__aic_ml_retrained_from, domain=None, range=Optional[Union[str, AicMachineLearningModelAicId]])

slots.aicMachineLearningModel__aic_ml_continuous_learning = Slot(uri=ISO22989.aic_ml_continuous_learning, name="aicMachineLearningModel__aic_ml_continuous_learning", curie=ISO22989.curie('aic_ml_continuous_learning'),
                   model_uri=ISO22989.aicMachineLearningModel__aic_ml_continuous_learning, domain=None, range=Optional[Union[bool, Bool]])

slots.aicNeuralNetworkModel__aic_network_architecture = Slot(uri=ISO22989.aic_network_architecture, name="aicNeuralNetworkModel__aic_network_architecture", curie=ISO22989.curie('aic_network_architecture'),
                   model_uri=ISO22989.aicNeuralNetworkModel__aic_network_architecture, domain=None, range=Optional[Union[str, "AicNetworkArchitecture"]])

slots.aicNeuralNetworkModel__aic_network_layer_count = Slot(uri=ISO22989.aic_network_layer_count, name="aicNeuralNetworkModel__aic_network_layer_count", curie=ISO22989.curie('aic_network_layer_count'),
                   model_uri=ISO22989.aicNeuralNetworkModel__aic_network_layer_count, domain=None, range=Optional[int])

slots.aicNeuralNetworkModel__aic_network_activation_functions = Slot(uri=ISO22989.aic_network_activation_functions, name="aicNeuralNetworkModel__aic_network_activation_functions", curie=ISO22989.curie('aic_network_activation_functions'),
                   model_uri=ISO22989.aicNeuralNetworkModel__aic_network_activation_functions, domain=None, range=Optional[Union[str, list[str]]])

slots.aicDataset__aic_dataset_roles = Slot(uri=ISO22989.aic_dataset_roles, name="aicDataset__aic_dataset_roles", curie=ISO22989.curie('aic_dataset_roles'),
                   model_uri=ISO22989.aicDataset__aic_dataset_roles, domain=None, range=Optional[Union[Union[str, "AicDatasetRole"], list[Union[str, "AicDatasetRole"]]]])

slots.aicDataset__aic_dataset_source = Slot(uri=ISO22989.aic_dataset_source, name="aicDataset__aic_dataset_source", curie=ISO22989.curie('aic_dataset_source'),
                   model_uri=ISO22989.aicDataset__aic_dataset_source, domain=None, range=Optional[str])

slots.aicDataset__aic_dataset_sample_count = Slot(uri=ISO22989.aic_dataset_sample_count, name="aicDataset__aic_dataset_sample_count", curie=ISO22989.curie('aic_dataset_sample_count'),
                   model_uri=ISO22989.aicDataset__aic_dataset_sample_count, domain=None, range=Optional[int])

slots.aicDataset__aic_dataset_labels = Slot(uri=ISO22989.aic_dataset_labels, name="aicDataset__aic_dataset_labels", curie=ISO22989.curie('aic_dataset_labels'),
                   model_uri=ISO22989.aicDataset__aic_dataset_labels, domain=None, range=Optional[Union[str, list[str]]])

slots.aicDataset__aic_dataset_ground_truth = Slot(uri=ISO22989.aic_dataset_ground_truth, name="aicDataset__aic_dataset_ground_truth", curie=ISO22989.curie('aic_dataset_ground_truth'),
                   model_uri=ISO22989.aicDataset__aic_dataset_ground_truth, domain=None, range=Optional[str])

slots.aicDataset__aic_dataset_holds_pii = Slot(uri=ISO22989.aic_dataset_holds_pii, name="aicDataset__aic_dataset_holds_pii", curie=ISO22989.curie('aic_dataset_holds_pii'),
                   model_uri=ISO22989.aicDataset__aic_dataset_holds_pii, domain=None, range=Optional[Union[bool, Bool]])

slots.aicDataset__aic_dataset_processes = Slot(uri=ISO22989.aic_dataset_processes, name="aicDataset__aic_dataset_processes", curie=ISO22989.curie('aic_dataset_processes'),
                   model_uri=ISO22989.aicDataset__aic_dataset_processes, domain=None, range=Optional[Union[Union[dict, AicDataProcess], list[Union[dict, AicDataProcess]]]])

slots.aicDataProcess__aic_data_process_kind = Slot(uri=ISO22989.aic_data_process_kind, name="aicDataProcess__aic_data_process_kind", curie=ISO22989.curie('aic_data_process_kind'),
                   model_uri=ISO22989.aicDataProcess__aic_data_process_kind, domain=None, range=Union[str, "AicDataProcessKind"])

slots.aicDataProcess__aic_data_process_method = Slot(uri=ISO22989.aic_data_process_method, name="aicDataProcess__aic_data_process_method", curie=ISO22989.curie('aic_data_process_method'),
                   model_uri=ISO22989.aicDataProcess__aic_data_process_method, domain=None, range=Optional[str])

slots.aicDataProcess__aic_data_process_date = Slot(uri=ISO22989.aic_data_process_date, name="aicDataProcess__aic_data_process_date", curie=ISO22989.curie('aic_data_process_date'),
                   model_uri=ISO22989.aicDataProcess__aic_data_process_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.aicTrustworthinessClaim__aic_claim_system = Slot(uri=ISO22989.aic_claim_system, name="aicTrustworthinessClaim__aic_claim_system", curie=ISO22989.curie('aic_claim_system'),
                   model_uri=ISO22989.aicTrustworthinessClaim__aic_claim_system, domain=None, range=Union[str, AicSystemAicId])

slots.aicTrustworthinessClaim__aic_claim_property = Slot(uri=ISO22989.aic_claim_property, name="aicTrustworthinessClaim__aic_claim_property", curie=ISO22989.curie('aic_claim_property'),
                   model_uri=ISO22989.aicTrustworthinessClaim__aic_claim_property, domain=None, range=Union[str, "AicTrustworthinessProperty"])

slots.aicTrustworthinessClaim__aic_claim_evidence = Slot(uri=ISO22989.aic_claim_evidence, name="aicTrustworthinessClaim__aic_claim_evidence", curie=ISO22989.curie('aic_claim_evidence'),
                   model_uri=ISO22989.aicTrustworthinessClaim__aic_claim_evidence, domain=None, range=Optional[Union[str, list[str]]])

slots.aicTrustworthinessClaim__aic_claim_measure = Slot(uri=ISO22989.aic_claim_measure, name="aicTrustworthinessClaim__aic_claim_measure", curie=ISO22989.curie('aic_claim_measure'),
                   model_uri=ISO22989.aicTrustworthinessClaim__aic_claim_measure, domain=None, range=Optional[str])

slots.aicAssessment__aic_assessment_kind = Slot(uri=ISO22989.aic_assessment_kind, name="aicAssessment__aic_assessment_kind", curie=ISO22989.curie('aic_assessment_kind'),
                   model_uri=ISO22989.aicAssessment__aic_assessment_kind, domain=None, range=Union[str, "AicAssessmentKind"])

slots.aicAssessment__aic_assessment_system = Slot(uri=ISO22989.aic_assessment_system, name="aicAssessment__aic_assessment_system", curie=ISO22989.curie('aic_assessment_system'),
                   model_uri=ISO22989.aicAssessment__aic_assessment_system, domain=None, range=Union[str, AicSystemAicId])

slots.aicAssessment__aic_assessment_method = Slot(uri=ISO22989.aic_assessment_method, name="aicAssessment__aic_assessment_method", curie=ISO22989.curie('aic_assessment_method'),
                   model_uri=ISO22989.aicAssessment__aic_assessment_method, domain=None, range=Optional[str])

slots.aicAssessment__aic_assessment_result = Slot(uri=ISO22989.aic_assessment_result, name="aicAssessment__aic_assessment_result", curie=ISO22989.curie('aic_assessment_result'),
                   model_uri=ISO22989.aicAssessment__aic_assessment_result, domain=None, range=Optional[str])

slots.aicAssessment__aic_assessment_date = Slot(uri=ISO22989.aic_assessment_date, name="aicAssessment__aic_assessment_date", curie=ISO22989.curie('aic_assessment_date'),
                   model_uri=ISO22989.aicAssessment__aic_assessment_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.aicLifecycleProcess__aic_lifecycle_stage = Slot(uri=ISO22989.aic_lifecycle_stage, name="aicLifecycleProcess__aic_lifecycle_stage", curie=ISO22989.curie('aic_lifecycle_stage'),
                   model_uri=ISO22989.aicLifecycleProcess__aic_lifecycle_stage, domain=None, range=Union[str, "AicLifecycleStage"])

slots.aicLifecycleProcess__aic_lifecycle_system = Slot(uri=ISO22989.aic_lifecycle_system, name="aicLifecycleProcess__aic_lifecycle_system", curie=ISO22989.curie('aic_lifecycle_system'),
                   model_uri=ISO22989.aicLifecycleProcess__aic_lifecycle_system, domain=None, range=Optional[Union[str, AicSystemAicId]])

slots.aicLifecycleProcess__aic_lifecycle_inputs = Slot(uri=ISO22989.aic_lifecycle_inputs, name="aicLifecycleProcess__aic_lifecycle_inputs", curie=ISO22989.curie('aic_lifecycle_inputs'),
                   model_uri=ISO22989.aicLifecycleProcess__aic_lifecycle_inputs, domain=None, range=Optional[Union[str, list[str]]])

slots.aicLifecycleProcess__aic_lifecycle_outputs = Slot(uri=ISO22989.aic_lifecycle_outputs, name="aicLifecycleProcess__aic_lifecycle_outputs", curie=ISO22989.curie('aic_lifecycle_outputs'),
                   model_uri=ISO22989.aicLifecycleProcess__aic_lifecycle_outputs, domain=None, range=Optional[Union[str, list[str]]])

slots.aicLifecycleProcess__aic_lifecycle_responsible = Slot(uri=ISO22989.aic_lifecycle_responsible, name="aicLifecycleProcess__aic_lifecycle_responsible", curie=ISO22989.curie('aic_lifecycle_responsible'),
                   model_uri=ISO22989.aicLifecycleProcess__aic_lifecycle_responsible, domain=None, range=Optional[Union[str, AicStakeholderAicId]])

slots.aicLifecycleProcess__aic_lifecycle_start = Slot(uri=ISO22989.aic_lifecycle_start, name="aicLifecycleProcess__aic_lifecycle_start", curie=ISO22989.curie('aic_lifecycle_start'),
                   model_uri=ISO22989.aicLifecycleProcess__aic_lifecycle_start, domain=None, range=Optional[Union[str, XSDDate]])

slots.aicLifecycleProcess__aic_lifecycle_end = Slot(uri=ISO22989.aic_lifecycle_end, name="aicLifecycleProcess__aic_lifecycle_end", curie=ISO22989.curie('aic_lifecycle_end'),
                   model_uri=ISO22989.aicLifecycleProcess__aic_lifecycle_end, domain=None, range=Optional[Union[str, XSDDate]])

slots.aicStakeholder__aic_stakeholder_role = Slot(uri=ISO22989.aic_stakeholder_role, name="aicStakeholder__aic_stakeholder_role", curie=ISO22989.curie('aic_stakeholder_role'),
                   model_uri=ISO22989.aicStakeholder__aic_stakeholder_role, domain=None, range=Union[str, "AicStakeholderRole"])

slots.aicStakeholder__aic_stakeholder_sub_roles = Slot(uri=ISO22989.aic_stakeholder_sub_roles, name="aicStakeholder__aic_stakeholder_sub_roles", curie=ISO22989.curie('aic_stakeholder_sub_roles'),
                   model_uri=ISO22989.aicStakeholder__aic_stakeholder_sub_roles, domain=None, range=Optional[Union[Union[str, "AicStakeholderSubRole"], list[Union[str, "AicStakeholderSubRole"]]]])

slots.aicStakeholder__aic_stakeholder_organization = Slot(uri=ISO22989.aic_stakeholder_organization, name="aicStakeholder__aic_stakeholder_organization", curie=ISO22989.curie('aic_stakeholder_organization'),
                   model_uri=ISO22989.aicStakeholder__aic_stakeholder_organization, domain=None, range=Optional[str])

slots.aicStakeholder__aic_stakeholder_contact = Slot(uri=ISO22989.aic_stakeholder_contact, name="aicStakeholder__aic_stakeholder_contact", curie=ISO22989.curie('aic_stakeholder_contact'),
                   model_uri=ISO22989.aicStakeholder__aic_stakeholder_contact, domain=None, range=Optional[str])

slots.aicStakeholder__aic_stakeholder_responsibilities = Slot(uri=ISO22989.aic_stakeholder_responsibilities, name="aicStakeholder__aic_stakeholder_responsibilities", curie=ISO22989.curie('aic_stakeholder_responsibilities'),
                   model_uri=ISO22989.aicStakeholder__aic_stakeholder_responsibilities, domain=None, range=Optional[Union[str, list[str]]])

slots.aicPrediction__aic_prediction_system = Slot(uri=ISO22989.aic_prediction_system, name="aicPrediction__aic_prediction_system", curie=ISO22989.curie('aic_prediction_system'),
                   model_uri=ISO22989.aicPrediction__aic_prediction_system, domain=None, range=Union[str, AicSystemAicId])

slots.aicPrediction__aic_prediction_value = Slot(uri=ISO22989.aic_prediction_value, name="aicPrediction__aic_prediction_value", curie=ISO22989.curie('aic_prediction_value'),
                   model_uri=ISO22989.aicPrediction__aic_prediction_value, domain=None, range=str)

slots.aicPrediction__aic_prediction_confidence = Slot(uri=ISO22989.aic_prediction_confidence, name="aicPrediction__aic_prediction_confidence", curie=ISO22989.curie('aic_prediction_confidence'),
                   model_uri=ISO22989.aicPrediction__aic_prediction_confidence, domain=None, range=Optional[float])

slots.aicDecision__aic_decision_outcome = Slot(uri=ISO22989.aic_decision_outcome, name="aicDecision__aic_decision_outcome", curie=ISO22989.curie('aic_decision_outcome'),
                   model_uri=ISO22989.aicDecision__aic_decision_outcome, domain=None, range=str)

slots.aicDecision__aic_decision_predictions = Slot(uri=ISO22989.aic_decision_predictions, name="aicDecision__aic_decision_predictions", curie=ISO22989.curie('aic_decision_predictions'),
                   model_uri=ISO22989.aicDecision__aic_decision_predictions, domain=None, range=Optional[Union[Union[str, AicPredictionAicId], list[Union[str, AicPredictionAicId]]]])

slots.aicDecision__aic_decision_criteria = Slot(uri=ISO22989.aic_decision_criteria, name="aicDecision__aic_decision_criteria", curie=ISO22989.curie('aic_decision_criteria'),
                   model_uri=ISO22989.aicDecision__aic_decision_criteria, domain=None, range=Optional[str])

slots.aicAction__aic_action_decision = Slot(uri=ISO22989.aic_action_decision, name="aicAction__aic_action_decision", curie=ISO22989.curie('aic_action_decision'),
                   model_uri=ISO22989.aicAction__aic_action_decision, domain=None, range=Union[str, AicDecisionAicId])

slots.aicAction__aic_action_target = Slot(uri=ISO22989.aic_action_target, name="aicAction__aic_action_target", curie=ISO22989.curie('aic_action_target'),
                   model_uri=ISO22989.aicAction__aic_action_target, domain=None, range=Optional[str])

slots.aicAction__aic_action_time = Slot(uri=ISO22989.aic_action_time, name="aicAction__aic_action_time", curie=ISO22989.curie('aic_action_time'),
                   model_uri=ISO22989.aicAction__aic_action_time, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.aicApplication__aic_application_system = Slot(uri=ISO22989.aic_application_system, name="aicApplication__aic_application_system", curie=ISO22989.curie('aic_application_system'),
                   model_uri=ISO22989.aicApplication__aic_application_system, domain=None, range=Union[str, AicSystemAicId])

slots.aicApplication__aic_application_domain = Slot(uri=ISO22989.aic_application_domain, name="aicApplication__aic_application_domain", curie=ISO22989.curie('aic_application_domain'),
                   model_uri=ISO22989.aicApplication__aic_application_domain, domain=None, range=Optional[Union[str, "AicApplicationDomain"]])

slots.aicApplication__aic_application_sector = Slot(uri=ISO22989.aic_application_sector, name="aicApplication__aic_application_sector", curie=ISO22989.curie('aic_application_sector'),
                   model_uri=ISO22989.aicApplication__aic_application_sector, domain=None, range=Optional[str])

slots.aicApplication__aic_application_purpose = Slot(uri=ISO22989.aic_application_purpose, name="aicApplication__aic_application_purpose", curie=ISO22989.curie('aic_application_purpose'),
                   model_uri=ISO22989.aicApplication__aic_application_purpose, domain=None, range=Optional[str])

slots.aicResourcePool__aic_pool_kind = Slot(uri=ISO22989.aic_pool_kind, name="aicResourcePool__aic_pool_kind", curie=ISO22989.curie('aic_pool_kind'),
                   model_uri=ISO22989.aicResourcePool__aic_pool_kind, domain=None, range=Optional[Union[str, "AicResourceKind"]])

slots.aicResourcePool__aic_pool_hardware = Slot(uri=ISO22989.aic_pool_hardware, name="aicResourcePool__aic_pool_hardware", curie=ISO22989.curie('aic_pool_hardware'),
                   model_uri=ISO22989.aicResourcePool__aic_pool_hardware, domain=None, range=Optional[str])

slots.aicResourcePool__aic_pool_capacity = Slot(uri=ISO22989.aic_pool_capacity, name="aicResourcePool__aic_pool_capacity", curie=ISO22989.curie('aic_pool_capacity'),
                   model_uri=ISO22989.aicResourcePool__aic_pool_capacity, domain=None, range=Optional[str])

slots.aicIotDevice__aic_device_senses = Slot(uri=ISO22989.aic_device_senses, name="aicIotDevice__aic_device_senses", curie=ISO22989.curie('aic_device_senses'),
                   model_uri=ISO22989.aicIotDevice__aic_device_senses, domain=None, range=Optional[Union[str, list[str]]])

slots.aicIotDevice__aic_device_actuates = Slot(uri=ISO22989.aic_device_actuates, name="aicIotDevice__aic_device_actuates", curie=ISO22989.curie('aic_device_actuates'),
                   model_uri=ISO22989.aicIotDevice__aic_device_actuates, domain=None, range=Optional[Union[str, list[str]]])

slots.aicIotSystem__aic_iot_devices = Slot(uri=ISO22989.aic_iot_devices, name="aicIotSystem__aic_iot_devices", curie=ISO22989.curie('aic_iot_devices'),
                   model_uri=ISO22989.aicIotSystem__aic_iot_devices, domain=None, range=Union[Union[str, AicIotDeviceAicId], list[Union[str, AicIotDeviceAicId]]])

slots.aicIotSystem__aic_iot_ai_systems = Slot(uri=ISO22989.aic_iot_ai_systems, name="aicIotSystem__aic_iot_ai_systems", curie=ISO22989.curie('aic_iot_ai_systems'),
                   model_uri=ISO22989.aicIotSystem__aic_iot_ai_systems, domain=None, range=Optional[Union[Union[str, AicSystemAicId], list[Union[str, AicSystemAicId]]]])

slots.aicCyberPhysicalSystem__aic_cps_physical_processes = Slot(uri=ISO22989.aic_cps_physical_processes, name="aicCyberPhysicalSystem__aic_cps_physical_processes", curie=ISO22989.curie('aic_cps_physical_processes'),
                   model_uri=ISO22989.aicCyberPhysicalSystem__aic_cps_physical_processes, domain=None, range=Union[str, list[str]])

slots.aicCyberPhysicalSystem__aic_cps_iot_system = Slot(uri=ISO22989.aic_cps_iot_system, name="aicCyberPhysicalSystem__aic_cps_iot_system", curie=ISO22989.curie('aic_cps_iot_system'),
                   model_uri=ISO22989.aicCyberPhysicalSystem__aic_cps_iot_system, domain=None, range=Optional[Union[str, AicIotSystemAicId]])

slots.aicCyberPhysicalSystem__aic_cps_ai_systems = Slot(uri=ISO22989.aic_cps_ai_systems, name="aicCyberPhysicalSystem__aic_cps_ai_systems", curie=ISO22989.curie('aic_cps_ai_systems'),
                   model_uri=ISO22989.aicCyberPhysicalSystem__aic_cps_ai_systems, domain=None, range=Optional[Union[Union[str, AicSystemAicId], list[Union[str, AicSystemAicId]]]])

slots.AicRecordMixin_title = Slot(uri=SCHEMA.name, name="AicRecordMixin_title", curie=SCHEMA.curie('name'),
                   model_uri=ISO22989.AicRecordMixin_title, domain=None, range=str,
                   pattern=re.compile(r'^\s*\S'))
