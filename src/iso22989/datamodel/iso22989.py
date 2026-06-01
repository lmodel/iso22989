# Auto generated from iso22989.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-06-01T17:22:22
# Schema: iso22989
#
# id: https://w3id.org/lmodel/iso22989
# description: A LinkML schema modelling the artificial-intelligence concepts, terminology, life-cycle stages, stakeholder roles, ecosystem components and application domains defined in ISO/IEC 22989:2022. The schema supplies the controlled vocabulary referenced by sibling lmodel schemas (iso42001 AIMS, iso23894 AI risk management) and supports SSSOM mappings to adjacent AI taxonomies.
# license: https://www.apache.org/licenses/LICENSE-2.0

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

from linkml_runtime.linkml_model.types import Boolean, Date, Float, Integer, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import Bool, URIorCURIE, XSDDate

metamodel_version = "1.11.0"
version = "0.1.0"

# Namespaces
DCTERMS = CurieNamespace('dcterms', 'http://purl.org/dc/terms/')
EU_AI_ACT = CurieNamespace('eu_ai_act', 'https://w3id.org/lmodel/eu-ai-act/')
GIST_LINKML = CurieNamespace('gist_linkml', 'https://w3id.org/lmodel/gist/')
ISO22989 = CurieNamespace('iso22989', 'https://w3id.org/lmodel/iso22989/')
ISO23894 = CurieNamespace('iso23894', 'https://w3id.org/lmodel/iso23894/')
ISO27001 = CurieNamespace('iso27001', 'https://w3id.org/lmodel/iso27001/')
ISO29100 = CurieNamespace('iso29100', 'https://w3id.org/lmodel/iso29100/')
ISO42001 = CurieNamespace('iso42001', 'https://w3id.org/lmodel/iso42001/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
NIST_AI_100_1 = CurieNamespace('nist_ai_100_1', 'https://w3id.org/lmodel/nist-ai-100-1/')
NIST_AI_600_1 = CurieNamespace('nist_ai_600_1', 'https://w3id.org/lmodel/nist-ai-600-1/')
NIST_AI_RMF = CurieNamespace('nist_ai_rmf', 'https://w3id.org/lmodel/nist-ai-100-1/')
NIST_AI_RMF_COMMON = CurieNamespace('nist_ai_rmf_common', 'https://w3id.org/lmodel/nist-ai-100-1/schema/nist_ai_rmf_common/')
OECD_AI = CurieNamespace('oecd_ai', 'https://oecd.ai/en/ai-principles#')
PROV = CurieNamespace('prov', 'http://www.w3.org/ns/prov#')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
SEMAPV = CurieNamespace('semapv', 'https://w3id.org/semapv/vocab/')
SKOS = CurieNamespace('skos', 'http://www.w3.org/2004/02/skos/core#')
UCO_CORE = CurieNamespace('uco_core', 'https://w3id.org/lmodel/uco-core/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = ISO22989


# Types
class DurationType(str):
    """ ISO 8601 duration value such as P1Y, P30D or PT4H. """
    type_class_uri = XSD["duration"]
    type_class_curie = "xsd:duration"
    type_name = "DurationType"
    type_model_uri = ISO22989.DurationType


class ConfidenceScore(Float):
    """ Numeric confidence score expressed as a value in the closed interval [0.0, 1.0]. Used for model prediction confidence, trust scores and similar normalised quality indicators. """
    type_class_uri = XSD["float"]
    type_class_curie = "xsd:float"
    type_name = "ConfidenceScore"
    type_model_uri = ISO22989.ConfidenceScore


# Class references
class NamedEntityId(URIorCURIE):
    pass


class TermId(NamedEntityId):
    pass


class AITermId(TermId):
    pass


class DataTermId(TermId):
    pass


class MachineLearningTermId(TermId):
    pass


class NeuralNetworkTermId(TermId):
    pass


class TrustworthinessTermId(TermId):
    pass


class NLPTermId(TermId):
    pass


class ComputerVisionTermId(TermId):
    pass


class AbbreviatedTermId(NamedEntityId):
    pass


class AIConceptId(NamedEntityId):
    pass


class AIAgentId(AIConceptId):
    pass


class KnowledgeRepresentationId(AIConceptId):
    pass


class AISystemId(NamedEntityId):
    pass


class AIComponentId(NamedEntityId):
    pass


class AIModelId(NamedEntityId):
    pass


class NeuralNetworkModelId(AIModelId):
    pass


class DatasetId(NamedEntityId):
    pass


class TrustworthinessPropertyId(NamedEntityId):
    pass


class AILifecycleProcessId(NamedEntityId):
    pass


class AIStakeholderRoleId(NamedEntityId):
    pass


class AIProviderId(AIStakeholderRoleId):
    pass


class AIProducerId(AIStakeholderRoleId):
    pass


class AICustomerId(AIStakeholderRoleId):
    pass


class AIPartnerId(AIStakeholderRoleId):
    pass


class AISubjectId(AIStakeholderRoleId):
    pass


class RelevantAuthorityId(AIStakeholderRoleId):
    pass


class AIEcosystemId(NamedEntityId):
    pass


class ResourcePoolId(NamedEntityId):
    pass


class NLPComponentId(NamedEntityId):
    pass


class ComputerVisionFunctionId(NamedEntityId):
    pass


class AIApplicationId(NamedEntityId):
    pass


class TaskId(NamedEntityId):
    pass


class PredictionId(NamedEntityId):
    pass


class DecisionId(NamedEntityId):
    pass


class ActionId(NamedEntityId):
    pass


class InferenceEngineId(NamedEntityId):
    pass


class KnowledgeGraphId(KnowledgeRepresentationId):
    pass


class ExpertSystemId(NamedEntityId):
    pass


class CognitiveComputingSystemId(AIConceptId):
    pass


class SemanticComputingSystemId(AIConceptId):
    pass


class SoftComputingSystemId(AIConceptId):
    pass


class DataProcessId(NamedEntityId):
    pass


class DataSampleId(NamedEntityId):
    pass


class DataLabelId(NamedEntityId):
    pass


class GroundTruthRecordId(NamedEntityId):
    pass


class RobotId(NamedEntityId):
    pass


class IoTDeviceId(NamedEntityId):
    pass


class IoTSystemId(NamedEntityId):
    pass


class CyberPhysicalSystemId(NamedEntityId):
    pass


class AbbreviationEntryId(NamedEntityId):
    pass


class AIPlatformProviderId(AIProviderId):
    pass


class AIServiceProductProviderId(AIProviderId):
    pass


class ModelDesignerId(AIProducerId):
    pass


class ModelImplementerId(AIProducerId):
    pass


class ComputationVerifierId(AIProducerId):
    pass


class ModelVerifierId(AIProducerId):
    pass


class AIUserId(AICustomerId):
    pass


class AISystemIntegratorId(AIPartnerId):
    pass


class DataProviderId(AIPartnerId):
    pass


class AIAuditorId(AIPartnerId):
    pass


class AIEvaluatorId(AIPartnerId):
    pass


class DataSubjectId(AISubjectId):
    pass


class PolicyMakerId(RelevantAuthorityId):
    pass


class RegulatorId(RelevantAuthorityId):
    pass


class AutonomyAssessmentId(NamedEntityId):
    pass


class VerificationValidationFrameworkId(NamedEntityId):
    pass


class HumanMachineTeamId(AIConceptId):
    pass


class IntelligenceAugmentationId(AIConceptId):
    pass


class RecommendationId(NamedEntityId):
    pass


class EvaluationMetricId(NamedEntityId):
    pass


class ThresholdId(NamedEntityId):
    pass


class NeuronId(AIConceptId):
    pass


class ConvolutionOperationId(AIConceptId):
    pass


class DataDriftId(NamedEntityId):
    pass


class CatastrophicForgettingId(NamedEntityId):
    pass


class FaultToleranceMechanismId(NamedEntityId):
    pass


class NaturalLanguageId(AIConceptId):
    pass


class RiskItemId(NamedEntityId):
    pass


class InputDataId(NamedEntityId):
    pass


class InferenceId(NamedEntityId):
    pass


class OECDLifecycleMappingId(NamedEntityId):
    pass


class OrganizationId(NamedEntityId):
    pass


class InterestedPartyId(NamedEntityId):
    pass


@dataclass(repr=False)
class NamedEntity(YAMLRoot):
    """
    Abstract base class for any addressable entity in the schema, carrying identity, label and clause-reference
    metadata.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["Thing"]
    class_class_curie: ClassVar[str] = "schema:Thing"
    class_name: ClassVar[str] = "NamedEntity"
    class_model_uri: ClassVar[URIRef] = ISO22989.NamedEntity

    id: Union[str, NamedEntityId] = None
    name: str = None
    description: Optional[str] = None
    clause_reference: Optional[str] = None
    aliases: Optional[Union[str, list[str]]] = empty_list()
    preferred_label: Optional[str] = None
    see_also_uri: Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NamedEntityId):
            self.id = NamedEntityId(self.id)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.clause_reference is not None and not isinstance(self.clause_reference, str):
            self.clause_reference = str(self.clause_reference)

        if not isinstance(self.aliases, list):
            self.aliases = [self.aliases] if self.aliases is not None else []
        self.aliases = [v if isinstance(v, str) else str(v) for v in self.aliases]

        if self.preferred_label is not None and not isinstance(self.preferred_label, str):
            self.preferred_label = str(self.preferred_label)

        if not isinstance(self.see_also_uri, list):
            self.see_also_uri = [self.see_also_uri] if self.see_also_uri is not None else []
        self.see_also_uri = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.see_also_uri]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Term(NamedEntity):
    """
    Abstract base class for a glossary term defined in Clause 3. Concrete subclasses partition the terminology along
    Clauses 3.1–3.7.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO22989["Term"]
    class_class_curie: ClassVar[str] = "iso22989:Term"
    class_name: ClassVar[str] = "Term"
    class_model_uri: ClassVar[URIRef] = ISO22989.Term

    id: Union[str, TermId] = None
    name: str = None

@dataclass(repr=False)
class AITerm(Term):
    """
    Term defined in Clause 3.1 (terms related to AI).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO22989["AITerm"]
    class_class_curie: ClassVar[str] = "iso22989:AITerm"
    class_name: ClassVar[str] = "AITerm"
    class_model_uri: ClassVar[URIRef] = ISO22989.AITerm

    id: Union[str, AITermId] = None
    name: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AITermId):
            self.id = AITermId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DataTerm(Term):
    """
    Term defined in Clause 3.2 (terms related to data).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO22989["DataTerm"]
    class_class_curie: ClassVar[str] = "iso22989:DataTerm"
    class_name: ClassVar[str] = "DataTerm"
    class_model_uri: ClassVar[URIRef] = ISO22989.DataTerm

    id: Union[str, DataTermId] = None
    name: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DataTermId):
            self.id = DataTermId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MachineLearningTerm(Term):
    """
    Term defined in Clause 3.3 (terms related to machine learning).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO22989["MachineLearningTerm"]
    class_class_curie: ClassVar[str] = "iso22989:MachineLearningTerm"
    class_name: ClassVar[str] = "MachineLearningTerm"
    class_model_uri: ClassVar[URIRef] = ISO22989.MachineLearningTerm

    id: Union[str, MachineLearningTermId] = None
    name: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MachineLearningTermId):
            self.id = MachineLearningTermId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NeuralNetworkTerm(Term):
    """
    Term defined in Clause 3.4 (terms related to neural networks).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO22989["NeuralNetworkTerm"]
    class_class_curie: ClassVar[str] = "iso22989:NeuralNetworkTerm"
    class_name: ClassVar[str] = "NeuralNetworkTerm"
    class_model_uri: ClassVar[URIRef] = ISO22989.NeuralNetworkTerm

    id: Union[str, NeuralNetworkTermId] = None
    name: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NeuralNetworkTermId):
            self.id = NeuralNetworkTermId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TrustworthinessTerm(Term):
    """
    Term defined in Clause 3.5 (terms related to trustworthiness).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO22989["TrustworthinessTerm"]
    class_class_curie: ClassVar[str] = "iso22989:TrustworthinessTerm"
    class_name: ClassVar[str] = "TrustworthinessTerm"
    class_model_uri: ClassVar[URIRef] = ISO22989.TrustworthinessTerm

    id: Union[str, TrustworthinessTermId] = None
    name: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TrustworthinessTermId):
            self.id = TrustworthinessTermId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NLPTerm(Term):
    """
    Term defined in Clause 3.6 (terms related to natural-language processing).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO22989["NLPTerm"]
    class_class_curie: ClassVar[str] = "iso22989:NLPTerm"
    class_name: ClassVar[str] = "NLPTerm"
    class_model_uri: ClassVar[URIRef] = ISO22989.NLPTerm

    id: Union[str, NLPTermId] = None
    name: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NLPTermId):
            self.id = NLPTermId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ComputerVisionTerm(Term):
    """
    Term defined in Clause 3.7 (terms related to computer vision).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO22989["ComputerVisionTerm"]
    class_class_curie: ClassVar[str] = "iso22989:ComputerVisionTerm"
    class_name: ClassVar[str] = "ComputerVisionTerm"
    class_model_uri: ClassVar[URIRef] = ISO22989.ComputerVisionTerm

    id: Union[str, ComputerVisionTermId] = None
    name: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ComputerVisionTermId):
            self.id = ComputerVisionTermId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AbbreviatedTerm(NamedEntity):
    """
    Abbreviation or acronym listed in Clause 4 with its expansion and optional definition reference.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO22989["AbbreviatedTerm"]
    class_class_curie: ClassVar[str] = "iso22989:AbbreviatedTerm"
    class_name: ClassVar[str] = "AbbreviatedTerm"
    class_model_uri: ClassVar[URIRef] = ISO22989.AbbreviatedTerm

    id: Union[str, AbbreviatedTermId] = None
    name: str = None
    expansion: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AbbreviatedTermId):
            self.id = AbbreviatedTermId(self.id)

        if self._is_empty(self.expansion):
            self.MissingRequiredField("expansion")
        if not isinstance(self.expansion, str):
            self.expansion = str(self.expansion)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AIConcept(NamedEntity):
    """
    Abstract base for Clause 5 conceptual entities (agent, knowledge, cognition, autonomy, etc.).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO22989["AIConcept"]
    class_class_curie: ClassVar[str] = "iso22989:AIConcept"
    class_name: ClassVar[str] = "AIConcept"
    class_model_uri: ClassVar[URIRef] = ISO22989.AIConcept

    id: Union[str, AIConceptId] = None
    name: str = None

@dataclass(repr=False)
class AIAgent(AIConcept):
    """
    Entity that perceives its environment and acts upon it to achieve goals (Clause 5.3).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO22989["AIAgent"]
    class_class_curie: ClassVar[str] = "iso22989:AIAgent"
    class_name: ClassVar[str] = "AIAgent"
    class_model_uri: ClassVar[URIRef] = ISO22989.AIAgent

    id: Union[str, AIAgentId] = None
    name: str = None
    autonomy_level: Optional[Union[str, "AutonomyLevel"]] = None
    symbolic_approach: Optional[Union[str, "SymbolicApproach"]] = None
    agent_architecture: Optional[Union[str, "AgentArchitectureType"]] = None
    goal_set: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AIAgentId):
            self.id = AIAgentId(self.id)

        if self.autonomy_level is not None and not isinstance(self.autonomy_level, AutonomyLevel):
            self.autonomy_level = AutonomyLevel(self.autonomy_level)

        if self.symbolic_approach is not None and not isinstance(self.symbolic_approach, SymbolicApproach):
            self.symbolic_approach = SymbolicApproach(self.symbolic_approach)

        if self.agent_architecture is not None and not isinstance(self.agent_architecture, AgentArchitectureType):
            self.agent_architecture = AgentArchitectureType(self.agent_architecture)

        if not isinstance(self.goal_set, list):
            self.goal_set = [self.goal_set] if self.goal_set is not None else []
        self.goal_set = [v if isinstance(v, str) else str(v) for v in self.goal_set]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class KnowledgeRepresentation(AIConcept):
    """
    Representation of knowledge usable by an AI system (Clause 5.4), including knowledge graphs, ontologies and rule
    bases.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO22989["KnowledgeRepresentation"]
    class_class_curie: ClassVar[str] = "iso22989:KnowledgeRepresentation"
    class_name: ClassVar[str] = "KnowledgeRepresentation"
    class_model_uri: ClassVar[URIRef] = ISO22989.KnowledgeRepresentation

    id: Union[str, KnowledgeRepresentationId] = None
    name: str = None
    symbolic_approach: Optional[Union[str, "SymbolicApproach"]] = None
    knowledge_type: Optional[Union[str, "KnowledgeType"]] = None
    representation_form: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, KnowledgeRepresentationId):
            self.id = KnowledgeRepresentationId(self.id)

        if self.symbolic_approach is not None and not isinstance(self.symbolic_approach, SymbolicApproach):
            self.symbolic_approach = SymbolicApproach(self.symbolic_approach)

        if self.knowledge_type is not None and not isinstance(self.knowledge_type, KnowledgeType):
            self.knowledge_type = KnowledgeType(self.knowledge_type)

        if self.representation_form is not None and not isinstance(self.representation_form, str):
            self.representation_form = str(self.representation_form)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AISystem(NamedEntity):
    """
    Engineered system that uses AI techniques to perform tasks delegated to it. Aggregates lifecycle, functional,
    model and stakeholder data.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO22989["AISystem"]
    class_class_curie: ClassVar[str] = "iso22989:AISystem"
    class_name: ClassVar[str] = "AISystem"
    class_model_uri: ClassVar[URIRef] = ISO22989.AISystem

    id: Union[str, AISystemId] = None
    name: str = None
    ai_system_type: Optional[Union[str, "AISystemType"]] = None
    symbolic_approach: Optional[Union[str, "SymbolicApproach"]] = None
    autonomy_level: Optional[Union[str, "AutonomyLevel"]] = None
    intended_purpose: Optional[str] = None
    application_domain: Optional[Union[Union[str, "AIApplicationDomain"], list[Union[str, "AIApplicationDomain"]]]] = empty_list()
    ai_field: Optional[Union[Union[str, "AIField"], list[Union[str, "AIField"]]]] = empty_list()
    functional_components: Optional[Union[Union[str, "AIFunctionalComponent"], list[Union[str, "AIFunctionalComponent"]]]] = empty_list()
    lifecycle_stage: Optional[Union[str, "AILifecycleStage"]] = None
    stakeholders: Optional[Union[dict[Union[str, AIStakeholderRoleId], Union[dict, "AIStakeholderRole"]], list[Union[dict, "AIStakeholderRole"]]]] = empty_dict()
    components: Optional[Union[dict[Union[str, AIComponentId], Union[dict, "AIComponent"]], list[Union[dict, "AIComponent"]]]] = empty_dict()
    models: Optional[Union[dict[Union[str, AIModelId], Union[dict, "AIModel"]], list[Union[dict, "AIModel"]]]] = empty_dict()
    datasets: Optional[Union[dict[Union[str, DatasetId], Union[dict, "Dataset"]], list[Union[dict, "Dataset"]]]] = empty_dict()
    trustworthiness_properties: Optional[Union[dict[Union[str, TrustworthinessPropertyId], Union[dict, "TrustworthinessProperty"]], list[Union[dict, "TrustworthinessProperty"]]]] = empty_dict()
    jurisdictional_issues: Optional[Union[Union[str, "JurisdictionalIssueType"], list[Union[str, "JurisdictionalIssueType"]]]] = empty_list()
    societal_impacts: Optional[Union[Union[str, "SocietalImpactCategory"], list[Union[str, "SocietalImpactCategory"]]]] = empty_list()
    system_characteristics: Optional[Union[Union[str, "AISystemCharacteristic"], list[Union[str, "AISystemCharacteristic"]]]] = empty_list()
    task_categories: Optional[Union[Union[str, "TaskCategory"], list[Union[str, "TaskCategory"]]]] = empty_list()
    agent_architecture: Optional[Union[str, "AgentArchitectureType"]] = None
    data_processes: Optional[Union[dict[Union[str, DataProcessId], Union[dict, "DataProcess"]], list[Union[dict, "DataProcess"]]]] = empty_dict()
    iot_integration: Optional[Union[str, IoTSystemId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AISystemId):
            self.id = AISystemId(self.id)

        if self.ai_system_type is not None and not isinstance(self.ai_system_type, AISystemType):
            self.ai_system_type = AISystemType(self.ai_system_type)

        if self.symbolic_approach is not None and not isinstance(self.symbolic_approach, SymbolicApproach):
            self.symbolic_approach = SymbolicApproach(self.symbolic_approach)

        if self.autonomy_level is not None and not isinstance(self.autonomy_level, AutonomyLevel):
            self.autonomy_level = AutonomyLevel(self.autonomy_level)

        if self.intended_purpose is not None and not isinstance(self.intended_purpose, str):
            self.intended_purpose = str(self.intended_purpose)

        if not isinstance(self.application_domain, list):
            self.application_domain = [self.application_domain] if self.application_domain is not None else []
        self.application_domain = [v if isinstance(v, AIApplicationDomain) else AIApplicationDomain(v) for v in self.application_domain]

        if not isinstance(self.ai_field, list):
            self.ai_field = [self.ai_field] if self.ai_field is not None else []
        self.ai_field = [v if isinstance(v, AIField) else AIField(v) for v in self.ai_field]

        if not isinstance(self.functional_components, list):
            self.functional_components = [self.functional_components] if self.functional_components is not None else []
        self.functional_components = [v if isinstance(v, AIFunctionalComponent) else AIFunctionalComponent(v) for v in self.functional_components]

        if self.lifecycle_stage is not None and not isinstance(self.lifecycle_stage, AILifecycleStage):
            self.lifecycle_stage = AILifecycleStage(self.lifecycle_stage)

        self._normalize_inlined_as_list(slot_name="stakeholders", slot_type=AIStakeholderRole, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="components", slot_type=AIComponent, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="models", slot_type=AIModel, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="datasets", slot_type=Dataset, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="trustworthiness_properties", slot_type=TrustworthinessProperty, key_name="id", keyed=True)

        if not isinstance(self.jurisdictional_issues, list):
            self.jurisdictional_issues = [self.jurisdictional_issues] if self.jurisdictional_issues is not None else []
        self.jurisdictional_issues = [v if isinstance(v, JurisdictionalIssueType) else JurisdictionalIssueType(v) for v in self.jurisdictional_issues]

        if not isinstance(self.societal_impacts, list):
            self.societal_impacts = [self.societal_impacts] if self.societal_impacts is not None else []
        self.societal_impacts = [v if isinstance(v, SocietalImpactCategory) else SocietalImpactCategory(v) for v in self.societal_impacts]

        if not isinstance(self.system_characteristics, list):
            self.system_characteristics = [self.system_characteristics] if self.system_characteristics is not None else []
        self.system_characteristics = [v if isinstance(v, AISystemCharacteristic) else AISystemCharacteristic(v) for v in self.system_characteristics]

        if not isinstance(self.task_categories, list):
            self.task_categories = [self.task_categories] if self.task_categories is not None else []
        self.task_categories = [v if isinstance(v, TaskCategory) else TaskCategory(v) for v in self.task_categories]

        if self.agent_architecture is not None and not isinstance(self.agent_architecture, AgentArchitectureType):
            self.agent_architecture = AgentArchitectureType(self.agent_architecture)

        self._normalize_inlined_as_list(slot_name="data_processes", slot_type=DataProcess, key_name="id", keyed=True)

        if self.iot_integration is not None and not isinstance(self.iot_integration, IoTSystemId):
            self.iot_integration = IoTSystemId(self.iot_integration)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AIComponent(NamedEntity):
    """
    Functional component of an AI system, such as a data pipeline, preprocessor, model server, or post-processing
    module.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO22989["AIComponent"]
    class_class_curie: ClassVar[str] = "iso22989:AIComponent"
    class_name: ClassVar[str] = "AIComponent"
    class_model_uri: ClassVar[URIRef] = ISO22989.AIComponent

    id: Union[str, AIComponentId] = None
    name: str = None
    component_function: Optional[Union[str, "AIFunctionalComponent"]] = None
    depends_on: Optional[Union[Union[str, AIComponentId], list[Union[str, AIComponentId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AIComponentId):
            self.id = AIComponentId(self.id)

        if self.component_function is not None and not isinstance(self.component_function, AIFunctionalComponent):
            self.component_function = AIFunctionalComponent(self.component_function)

        if not isinstance(self.depends_on, list):
            self.depends_on = [self.depends_on] if self.depends_on is not None else []
        self.depends_on = [v if isinstance(v, AIComponentId) else AIComponentId(v) for v in self.depends_on]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AIModel(NamedEntity):
    """
    Trained or rule-based model embedded in an AI system. Carries paradigm, algorithm family, dataset references and
    version metadata.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO22989["AIModel"]
    class_class_curie: ClassVar[str] = "iso22989:AIModel"
    class_name: ClassVar[str] = "AIModel"
    class_model_uri: ClassVar[URIRef] = ISO22989.AIModel

    id: Union[str, AIModelId] = None
    name: str = None
    model_paradigm: Optional[Union[str, "MachineLearningParadigm"]] = None
    algorithm_family: Optional[Union[str, "MLAlgorithmFamily"]] = None
    engineering_approach: Optional[Union[str, "EngineeringApproach"]] = None
    training_dataset: Optional[Union[str, DatasetId]] = None
    validation_dataset: Optional[Union[str, DatasetId]] = None
    test_dataset: Optional[Union[str, DatasetId]] = None
    hyperparameters: Optional[Union[str, list[str]]] = empty_list()
    model_version: Optional[str] = None
    trained_on: Optional[str] = None
    supports_continuous_learning: Optional[Union[bool, Bool]] = None
    catastrophic_forgetting_risk: Optional[Union[float, ConfidenceScore]] = None
    parameter_count: Optional[int] = None
    training_duration: Optional[str] = None
    inference_latency_ms: Optional[float] = None
    model_compression_applied: Optional[Union[bool, Bool]] = None
    neural_network_architecture: Optional[Union[str, "NeuralNetworkArchitecture"]] = None
    activation_function: Optional[Union[str, "ActivationFunctionType"]] = None
    training_phenomena: Optional[Union[Union[str, "NeuralNetworkPhenomenon"], list[Union[str, "NeuralNetworkPhenomenon"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AIModelId):
            self.id = AIModelId(self.id)

        if self.model_paradigm is not None and not isinstance(self.model_paradigm, MachineLearningParadigm):
            self.model_paradigm = MachineLearningParadigm(self.model_paradigm)

        if self.algorithm_family is not None and not isinstance(self.algorithm_family, MLAlgorithmFamily):
            self.algorithm_family = MLAlgorithmFamily(self.algorithm_family)

        if self.engineering_approach is not None and not isinstance(self.engineering_approach, EngineeringApproach):
            self.engineering_approach = EngineeringApproach(self.engineering_approach)

        if self.training_dataset is not None and not isinstance(self.training_dataset, DatasetId):
            self.training_dataset = DatasetId(self.training_dataset)

        if self.validation_dataset is not None and not isinstance(self.validation_dataset, DatasetId):
            self.validation_dataset = DatasetId(self.validation_dataset)

        if self.test_dataset is not None and not isinstance(self.test_dataset, DatasetId):
            self.test_dataset = DatasetId(self.test_dataset)

        if not isinstance(self.hyperparameters, list):
            self.hyperparameters = [self.hyperparameters] if self.hyperparameters is not None else []
        self.hyperparameters = [v if isinstance(v, str) else str(v) for v in self.hyperparameters]

        if self.model_version is not None and not isinstance(self.model_version, str):
            self.model_version = str(self.model_version)

        if self.trained_on is not None and not isinstance(self.trained_on, str):
            self.trained_on = str(self.trained_on)

        if self.supports_continuous_learning is not None and not isinstance(self.supports_continuous_learning, Bool):
            self.supports_continuous_learning = Bool(self.supports_continuous_learning)

        if self.catastrophic_forgetting_risk is not None and not isinstance(self.catastrophic_forgetting_risk, ConfidenceScore):
            self.catastrophic_forgetting_risk = ConfidenceScore(self.catastrophic_forgetting_risk)

        if self.parameter_count is not None and not isinstance(self.parameter_count, int):
            self.parameter_count = int(self.parameter_count)

        if self.training_duration is not None and not isinstance(self.training_duration, str):
            self.training_duration = str(self.training_duration)

        if self.inference_latency_ms is not None and not isinstance(self.inference_latency_ms, float):
            self.inference_latency_ms = float(self.inference_latency_ms)

        if self.model_compression_applied is not None and not isinstance(self.model_compression_applied, Bool):
            self.model_compression_applied = Bool(self.model_compression_applied)

        if self.neural_network_architecture is not None and not isinstance(self.neural_network_architecture, NeuralNetworkArchitecture):
            self.neural_network_architecture = NeuralNetworkArchitecture(self.neural_network_architecture)

        if self.activation_function is not None and not isinstance(self.activation_function, ActivationFunctionType):
            self.activation_function = ActivationFunctionType(self.activation_function)

        if not isinstance(self.training_phenomena, list):
            self.training_phenomena = [self.training_phenomena] if self.training_phenomena is not None else []
        self.training_phenomena = [v if isinstance(v, NeuralNetworkPhenomenon) else NeuralNetworkPhenomenon(v) for v in self.training_phenomena]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NeuralNetworkModel(AIModel):
    """
    AIModel realised as a neural network (Clause 5.12.1, Clause 3.4 terms).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO22989["NeuralNetworkModel"]
    class_class_curie: ClassVar[str] = "iso22989:NeuralNetworkModel"
    class_name: ClassVar[str] = "NeuralNetworkModel"
    class_model_uri: ClassVar[URIRef] = ISO22989.NeuralNetworkModel

    id: Union[str, NeuralNetworkModelId] = None
    name: str = None
    number_of_layers: Optional[int] = None
    number_of_parameters: Optional[int] = None
    algorithm_family: Optional[Union[str, "MLAlgorithmFamily"]] = 'neural_network'

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NeuralNetworkModelId):
            self.id = NeuralNetworkModelId(self.id)

        if self.number_of_layers is not None and not isinstance(self.number_of_layers, int):
            self.number_of_layers = int(self.number_of_layers)

        if self.number_of_parameters is not None and not isinstance(self.number_of_parameters, int):
            self.number_of_parameters = int(self.number_of_parameters)

        if self.algorithm_family is not None and not isinstance(self.algorithm_family, MLAlgorithmFamily):
            self.algorithm_family = MLAlgorithmFamily(self.algorithm_family)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Dataset(NamedEntity):
    """
    Collection of data items used by an AI system in a training, validation, test, reference or production role.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO22989["Dataset"]
    class_class_curie: ClassVar[str] = "iso22989:Dataset"
    class_name: ClassVar[str] = "Dataset"
    class_model_uri: ClassVar[URIRef] = ISO22989.Dataset

    id: Union[str, DatasetId] = None
    name: str = None
    data_modality: Optional[Union[Union[str, "DataModality"], list[Union[str, "DataModality"]]]] = empty_list()
    dataset_role: Optional[Union[str, "DatasetRole"]] = None
    data_provenance: Optional[str] = None
    record_count: Optional[int] = None
    data_quality_notes: Optional[str] = None
    contains_personal_data: Optional[Union[bool, Bool]] = None
    label_type: Optional[Union[str, "DataLabelType"]] = None
    ground_truth_available: Optional[Union[bool, Bool]] = None
    feature_count: Optional[int] = None
    data_processes_applied: Optional[Union[dict[Union[str, DataProcessId], Union[dict, "DataProcess"]], list[Union[dict, "DataProcess"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DatasetId):
            self.id = DatasetId(self.id)

        if not isinstance(self.data_modality, list):
            self.data_modality = [self.data_modality] if self.data_modality is not None else []
        self.data_modality = [v if isinstance(v, DataModality) else DataModality(v) for v in self.data_modality]

        if self.dataset_role is not None and not isinstance(self.dataset_role, DatasetRole):
            self.dataset_role = DatasetRole(self.dataset_role)

        if self.data_provenance is not None and not isinstance(self.data_provenance, str):
            self.data_provenance = str(self.data_provenance)

        if self.record_count is not None and not isinstance(self.record_count, int):
            self.record_count = int(self.record_count)

        if self.data_quality_notes is not None and not isinstance(self.data_quality_notes, str):
            self.data_quality_notes = str(self.data_quality_notes)

        if self.contains_personal_data is not None and not isinstance(self.contains_personal_data, Bool):
            self.contains_personal_data = Bool(self.contains_personal_data)

        if self.label_type is not None and not isinstance(self.label_type, DataLabelType):
            self.label_type = DataLabelType(self.label_type)

        if self.ground_truth_available is not None and not isinstance(self.ground_truth_available, Bool):
            self.ground_truth_available = Bool(self.ground_truth_available)

        if self.feature_count is not None and not isinstance(self.feature_count, int):
            self.feature_count = int(self.feature_count)

        self._normalize_inlined_as_list(slot_name="data_processes_applied", slot_type=DataProcess, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TrustworthinessProperty(NamedEntity):
    """
    Claim about a trustworthiness property of an AI system or model, with evidence and measurement metadata.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO22989["TrustworthinessProperty"]
    class_class_curie: ClassVar[str] = "iso22989:TrustworthinessProperty"
    class_name: ClassVar[str] = "TrustworthinessProperty"
    class_model_uri: ClassVar[URIRef] = ISO22989.TrustworthinessProperty

    id: Union[str, TrustworthinessPropertyId] = None
    name: str = None
    trustworthiness_property_type: Union[str, "TrustworthinessPropertyType"] = None
    property_evidence: Optional[Union[str, list[str]]] = empty_list()
    measurement_method: Optional[str] = None
    applicable_biases: Optional[Union[Union[str, "BiasType"], list[Union[str, "BiasType"]]]] = empty_list()
    confidence_score: Optional[Union[float, ConfidenceScore]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TrustworthinessPropertyId):
            self.id = TrustworthinessPropertyId(self.id)

        if self._is_empty(self.trustworthiness_property_type):
            self.MissingRequiredField("trustworthiness_property_type")
        if not isinstance(self.trustworthiness_property_type, TrustworthinessPropertyType):
            self.trustworthiness_property_type = TrustworthinessPropertyType(self.trustworthiness_property_type)

        if not isinstance(self.property_evidence, list):
            self.property_evidence = [self.property_evidence] if self.property_evidence is not None else []
        self.property_evidence = [v if isinstance(v, str) else str(v) for v in self.property_evidence]

        if self.measurement_method is not None and not isinstance(self.measurement_method, str):
            self.measurement_method = str(self.measurement_method)

        if not isinstance(self.applicable_biases, list):
            self.applicable_biases = [self.applicable_biases] if self.applicable_biases is not None else []
        self.applicable_biases = [v if isinstance(v, BiasType) else BiasType(v) for v in self.applicable_biases]

        if self.confidence_score is not None and not isinstance(self.confidence_score, ConfidenceScore):
            self.confidence_score = ConfidenceScore(self.confidence_score)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AILifecycleProcess(NamedEntity):
    """
    Process or activity associated with a stage of the AI system life cycle (Clause 6).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO22989["AILifecycleProcess"]
    class_class_curie: ClassVar[str] = "iso22989:AILifecycleProcess"
    class_name: ClassVar[str] = "AILifecycleProcess"
    class_model_uri: ClassVar[URIRef] = ISO22989.AILifecycleProcess

    id: Union[str, AILifecycleProcessId] = None
    name: str = None
    process_stage: Union[str, "AILifecycleStage"] = None
    process_inputs: Optional[Union[str, list[str]]] = empty_list()
    process_outputs: Optional[Union[str, list[str]]] = empty_list()
    responsible_role: Optional[Union[str, "AIStakeholderRoleType"]] = None
    start_date: Optional[Union[str, XSDDate]] = None
    end_date: Optional[Union[str, XSDDate]] = None
    risk_items: Optional[Union[str, list[str]]] = empty_list()
    approval_criteria: Optional[Union[str, list[str]]] = empty_list()
    process_sub_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AILifecycleProcessId):
            self.id = AILifecycleProcessId(self.id)

        if self._is_empty(self.process_stage):
            self.MissingRequiredField("process_stage")
        if not isinstance(self.process_stage, AILifecycleStage):
            self.process_stage = AILifecycleStage(self.process_stage)

        if not isinstance(self.process_inputs, list):
            self.process_inputs = [self.process_inputs] if self.process_inputs is not None else []
        self.process_inputs = [v if isinstance(v, str) else str(v) for v in self.process_inputs]

        if not isinstance(self.process_outputs, list):
            self.process_outputs = [self.process_outputs] if self.process_outputs is not None else []
        self.process_outputs = [v if isinstance(v, str) else str(v) for v in self.process_outputs]

        if self.responsible_role is not None and not isinstance(self.responsible_role, AIStakeholderRoleType):
            self.responsible_role = AIStakeholderRoleType(self.responsible_role)

        if self.start_date is not None and not isinstance(self.start_date, XSDDate):
            self.start_date = XSDDate(self.start_date)

        if self.end_date is not None and not isinstance(self.end_date, XSDDate):
            self.end_date = XSDDate(self.end_date)

        if not isinstance(self.risk_items, list):
            self.risk_items = [self.risk_items] if self.risk_items is not None else []
        self.risk_items = [v if isinstance(v, str) else str(v) for v in self.risk_items]

        if not isinstance(self.approval_criteria, list):
            self.approval_criteria = [self.approval_criteria] if self.approval_criteria is not None else []
        self.approval_criteria = [v if isinstance(v, str) else str(v) for v in self.approval_criteria]

        if self.process_sub_type is not None and not isinstance(self.process_sub_type, str):
            self.process_sub_type = str(self.process_sub_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AIStakeholderRole(NamedEntity):
    """
    Stakeholder role enacted by an organisation or individual in relation to an AI system (Clause 5.19).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO22989["AIStakeholderRole"]
    class_class_curie: ClassVar[str] = "iso22989:AIStakeholderRole"
    class_name: ClassVar[str] = "AIStakeholderRole"
    class_model_uri: ClassVar[URIRef] = ISO22989.AIStakeholderRole

    id: Union[str, AIStakeholderRoleId] = None
    name: str = None
    stakeholder_role_type: Union[str, "AIStakeholderRoleType"] = None
    organization_name: Optional[str] = None
    contact: Optional[str] = None
    responsibilities: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AIStakeholderRoleId):
            self.id = AIStakeholderRoleId(self.id)

        if self._is_empty(self.stakeholder_role_type):
            self.MissingRequiredField("stakeholder_role_type")
        if not isinstance(self.stakeholder_role_type, AIStakeholderRoleType):
            self.stakeholder_role_type = AIStakeholderRoleType(self.stakeholder_role_type)

        if self.organization_name is not None and not isinstance(self.organization_name, str):
            self.organization_name = str(self.organization_name)

        if self.contact is not None and not isinstance(self.contact, str):
            self.contact = str(self.contact)

        if not isinstance(self.responsibilities, list):
            self.responsibilities = [self.responsibilities] if self.responsibilities is not None else []
        self.responsibilities = [v if isinstance(v, str) else str(v) for v in self.responsibilities]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AIProvider(AIStakeholderRole):
    """
    Stakeholder making an AI system available to customers (Clause 5.19.2).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO22989["AIProvider"]
    class_class_curie: ClassVar[str] = "iso22989:AIProvider"
    class_name: ClassVar[str] = "AIProvider"
    class_model_uri: ClassVar[URIRef] = ISO22989.AIProvider

    id: Union[str, AIProviderId] = None
    name: str = None
    stakeholder_role_type: Union[str, "AIStakeholderRoleType"] = 'ai_provider'

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AIProviderId):
            self.id = AIProviderId(self.id)

        if self._is_empty(self.stakeholder_role_type):
            self.MissingRequiredField("stakeholder_role_type")
        if not isinstance(self.stakeholder_role_type, AIStakeholderRoleType):
            self.stakeholder_role_type = AIStakeholderRoleType(self.stakeholder_role_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AIProducer(AIStakeholderRole):
    """
    Stakeholder designing, developing or assembling AI systems (Clause 5.19.3).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO22989["AIProducer"]
    class_class_curie: ClassVar[str] = "iso22989:AIProducer"
    class_name: ClassVar[str] = "AIProducer"
    class_model_uri: ClassVar[URIRef] = ISO22989.AIProducer

    id: Union[str, AIProducerId] = None
    name: str = None
    stakeholder_role_type: Union[str, "AIStakeholderRoleType"] = 'ai_producer'

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AIProducerId):
            self.id = AIProducerId(self.id)

        if self._is_empty(self.stakeholder_role_type):
            self.MissingRequiredField("stakeholder_role_type")
        if not isinstance(self.stakeholder_role_type, AIStakeholderRoleType):
            self.stakeholder_role_type = AIStakeholderRoleType(self.stakeholder_role_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AICustomer(AIStakeholderRole):
    """
    Stakeholder using an AI system or AI-backed service (Clause 5.19.4).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO22989["AICustomer"]
    class_class_curie: ClassVar[str] = "iso22989:AICustomer"
    class_name: ClassVar[str] = "AICustomer"
    class_model_uri: ClassVar[URIRef] = ISO22989.AICustomer

    id: Union[str, AICustomerId] = None
    name: str = None
    stakeholder_role_type: Union[str, "AIStakeholderRoleType"] = 'ai_customer'

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AICustomerId):
            self.id = AICustomerId(self.id)

        if self._is_empty(self.stakeholder_role_type):
            self.MissingRequiredField("stakeholder_role_type")
        if not isinstance(self.stakeholder_role_type, AIStakeholderRoleType):
            self.stakeholder_role_type = AIStakeholderRoleType(self.stakeholder_role_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AIPartner(AIStakeholderRole):
    """
    Stakeholder providing supporting services across the AI life cycle (Clause 5.19.5).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO22989["AIPartner"]
    class_class_curie: ClassVar[str] = "iso22989:AIPartner"
    class_name: ClassVar[str] = "AIPartner"
    class_model_uri: ClassVar[URIRef] = ISO22989.AIPartner

    id: Union[str, AIPartnerId] = None
    name: str = None
    stakeholder_role_type: Union[str, "AIStakeholderRoleType"] = 'ai_partner'

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AIPartnerId):
            self.id = AIPartnerId(self.id)

        if self._is_empty(self.stakeholder_role_type):
            self.MissingRequiredField("stakeholder_role_type")
        if not isinstance(self.stakeholder_role_type, AIStakeholderRoleType):
            self.stakeholder_role_type = AIStakeholderRoleType(self.stakeholder_role_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AISubject(AIStakeholderRole):
    """
    Person or group affected by an AI system (Clause 5.19.6).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO22989["AISubject"]
    class_class_curie: ClassVar[str] = "iso22989:AISubject"
    class_name: ClassVar[str] = "AISubject"
    class_model_uri: ClassVar[URIRef] = ISO22989.AISubject

    id: Union[str, AISubjectId] = None
    name: str = None
    stakeholder_role_type: Union[str, "AIStakeholderRoleType"] = 'ai_subject'

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AISubjectId):
            self.id = AISubjectId(self.id)

        if self._is_empty(self.stakeholder_role_type):
            self.MissingRequiredField("stakeholder_role_type")
        if not isinstance(self.stakeholder_role_type, AIStakeholderRoleType):
            self.stakeholder_role_type = AIStakeholderRoleType(self.stakeholder_role_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RelevantAuthority(AIStakeholderRole):
    """
    Regulator or standards-setting body with oversight responsibilities (Clause 5.19.7).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO22989["RelevantAuthority"]
    class_class_curie: ClassVar[str] = "iso22989:RelevantAuthority"
    class_name: ClassVar[str] = "RelevantAuthority"
    class_model_uri: ClassVar[URIRef] = ISO22989.RelevantAuthority

    id: Union[str, RelevantAuthorityId] = None
    name: str = None
    stakeholder_role_type: Union[str, "AIStakeholderRoleType"] = 'relevant_authority'

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RelevantAuthorityId):
            self.id = RelevantAuthorityId(self.id)

        if self._is_empty(self.stakeholder_role_type):
            self.MissingRequiredField("stakeholder_role_type")
        if not isinstance(self.stakeholder_role_type, AIStakeholderRoleType):
            self.stakeholder_role_type = AIStakeholderRoleType(self.stakeholder_role_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AIEcosystem(NamedEntity):
    """
    Aggregation of the AI systems, data sources, computing resources and stakeholder roles that surround a deployment
    context (Clause 8).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO22989["AIEcosystem"]
    class_class_curie: ClassVar[str] = "iso22989:AIEcosystem"
    class_name: ClassVar[str] = "AIEcosystem"
    class_model_uri: ClassVar[URIRef] = ISO22989.AIEcosystem

    id: Union[str, AIEcosystemId] = None
    name: str = None
    computing_resources: Optional[Union[Union[str, "ComputingResourceType"], list[Union[str, "ComputingResourceType"]]]] = empty_list()
    data_sources: Optional[Union[str, list[str]]] = empty_list()
    ecosystem_components: Optional[Union[str, list[str]]] = empty_list()
    ai_systems: Optional[Union[dict[Union[str, AISystemId], Union[dict, AISystem]], list[Union[dict, AISystem]]]] = empty_dict()
    ai_stakeholder_roles: Optional[Union[dict[Union[str, AIStakeholderRoleId], Union[dict, AIStakeholderRole]], list[Union[dict, AIStakeholderRole]]]] = empty_dict()
    big_data_characteristics: Optional[Union[Union[str, "BigDataCharacteristic"], list[Union[str, "BigDataCharacteristic"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AIEcosystemId):
            self.id = AIEcosystemId(self.id)

        if not isinstance(self.computing_resources, list):
            self.computing_resources = [self.computing_resources] if self.computing_resources is not None else []
        self.computing_resources = [v if isinstance(v, ComputingResourceType) else ComputingResourceType(v) for v in self.computing_resources]

        if not isinstance(self.data_sources, list):
            self.data_sources = [self.data_sources] if self.data_sources is not None else []
        self.data_sources = [v if isinstance(v, str) else str(v) for v in self.data_sources]

        if not isinstance(self.ecosystem_components, list):
            self.ecosystem_components = [self.ecosystem_components] if self.ecosystem_components is not None else []
        self.ecosystem_components = [v if isinstance(v, str) else str(v) for v in self.ecosystem_components]

        self._normalize_inlined_as_list(slot_name="ai_systems", slot_type=AISystem, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="ai_stakeholder_roles", slot_type=AIStakeholderRole, key_name="id", keyed=True)

        if not isinstance(self.big_data_characteristics, list):
            self.big_data_characteristics = [self.big_data_characteristics] if self.big_data_characteristics is not None else []
        self.big_data_characteristics = [v if isinstance(v, BigDataCharacteristic) else BigDataCharacteristic(v) for v in self.big_data_characteristics]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ResourcePool(NamedEntity):
    """
    Pool of computing resources (CPU/GPU/TPU/ASIC/FPGA) available to AI workloads (Clause 8.7).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO22989["ResourcePool"]
    class_class_curie: ClassVar[str] = "iso22989:ResourcePool"
    class_name: ClassVar[str] = "ResourcePool"
    class_model_uri: ClassVar[URIRef] = ISO22989.ResourcePool

    id: Union[str, ResourcePoolId] = None
    name: str = None
    resource_type: Union[str, "ComputingResourceType"] = None
    capacity_units: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ResourcePoolId):
            self.id = ResourcePoolId(self.id)

        if self._is_empty(self.resource_type):
            self.MissingRequiredField("resource_type")
        if not isinstance(self.resource_type, ComputingResourceType):
            self.resource_type = ComputingResourceType(self.resource_type)

        if self.capacity_units is not None and not isinstance(self.capacity_units, str):
            self.capacity_units = str(self.capacity_units)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NLPComponent(NamedEntity):
    """
    Component of a natural-language-processing pipeline (Clause 9.2).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO22989["NLPComponent"]
    class_class_curie: ClassVar[str] = "iso22989:NLPComponent"
    class_name: ClassVar[str] = "NLPComponent"
    class_model_uri: ClassVar[URIRef] = ISO22989.NLPComponent

    id: Union[str, NLPComponentId] = None
    name: str = None
    nlp_component_type: Union[str, "NLPComponentType"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NLPComponentId):
            self.id = NLPComponentId(self.id)

        if self._is_empty(self.nlp_component_type):
            self.MissingRequiredField("nlp_component_type")
        if not isinstance(self.nlp_component_type, NLPComponentType):
            self.nlp_component_type = NLPComponentType(self.nlp_component_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ComputerVisionFunction(NamedEntity):
    """
    Computer-vision capability provided by an AI system (Clause 9.1).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO22989["ComputerVisionFunction"]
    class_class_curie: ClassVar[str] = "iso22989:ComputerVisionFunction"
    class_name: ClassVar[str] = "ComputerVisionFunction"
    class_model_uri: ClassVar[URIRef] = ISO22989.ComputerVisionFunction

    id: Union[str, ComputerVisionFunctionId] = None
    name: str = None
    cv_task: Union[str, "ComputerVisionTask"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ComputerVisionFunctionId):
            self.id = ComputerVisionFunctionId(self.id)

        if self._is_empty(self.cv_task):
            self.MissingRequiredField("cv_task")
        if not isinstance(self.cv_task, ComputerVisionTask):
            self.cv_task = ComputerVisionTask(self.cv_task)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AIApplication(NamedEntity):
    """
    Description of an AI application instance situated in a domain (Clause 10).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO22989["AIApplication"]
    class_class_curie: ClassVar[str] = "iso22989:AIApplication"
    class_name: ClassVar[str] = "AIApplication"
    class_model_uri: ClassVar[URIRef] = ISO22989.AIApplication

    id: Union[str, AIApplicationId] = None
    name: str = None
    application_domain: Optional[Union[Union[str, "AIApplicationDomain"], list[Union[str, "AIApplicationDomain"]]]] = empty_list()
    intended_purpose: Optional[str] = None
    jurisdictional_issues: Optional[Union[Union[str, "JurisdictionalIssueType"], list[Union[str, "JurisdictionalIssueType"]]]] = empty_list()
    societal_impacts: Optional[Union[Union[str, "SocietalImpactCategory"], list[Union[str, "SocietalImpactCategory"]]]] = empty_list()
    hosting_system: Optional[Union[str, AISystemId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AIApplicationId):
            self.id = AIApplicationId(self.id)

        if not isinstance(self.application_domain, list):
            self.application_domain = [self.application_domain] if self.application_domain is not None else []
        self.application_domain = [v if isinstance(v, AIApplicationDomain) else AIApplicationDomain(v) for v in self.application_domain]

        if self.intended_purpose is not None and not isinstance(self.intended_purpose, str):
            self.intended_purpose = str(self.intended_purpose)

        if not isinstance(self.jurisdictional_issues, list):
            self.jurisdictional_issues = [self.jurisdictional_issues] if self.jurisdictional_issues is not None else []
        self.jurisdictional_issues = [v if isinstance(v, JurisdictionalIssueType) else JurisdictionalIssueType(v) for v in self.jurisdictional_issues]

        if not isinstance(self.societal_impacts, list):
            self.societal_impacts = [self.societal_impacts] if self.societal_impacts is not None else []
        self.societal_impacts = [v if isinstance(v, SocietalImpactCategory) else SocietalImpactCategory(v) for v in self.societal_impacts]

        if self.hosting_system is not None and not isinstance(self.hosting_system, AISystemId):
            self.hosting_system = AISystemId(self.hosting_system)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Task(NamedEntity):
    """
    AI task addressed by a model or system (e.g. classification, regression, planning). Provides a first-class entity
    for the task categories enumerated across Clause 3 terminology.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO22989["Task"]
    class_class_curie: ClassVar[str] = "iso22989:Task"
    class_name: ClassVar[str] = "Task"
    class_model_uri: ClassVar[URIRef] = ISO22989.Task

    id: Union[str, TaskId] = None
    name: str = None
    task_category: Union[str, "TaskCategory"] = None
    input_modalities: Optional[Union[Union[str, "DataModality"], list[Union[str, "DataModality"]]]] = empty_list()
    output_label_type: Optional[Union[str, "DataLabelType"]] = None
    performance_metric: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TaskId):
            self.id = TaskId(self.id)

        if self._is_empty(self.task_category):
            self.MissingRequiredField("task_category")
        if not isinstance(self.task_category, TaskCategory):
            self.task_category = TaskCategory(self.task_category)

        if not isinstance(self.input_modalities, list):
            self.input_modalities = [self.input_modalities] if self.input_modalities is not None else []
        self.input_modalities = [v if isinstance(v, DataModality) else DataModality(v) for v in self.input_modalities]

        if self.output_label_type is not None and not isinstance(self.output_label_type, DataLabelType):
            self.output_label_type = DataLabelType(self.output_label_type)

        if not isinstance(self.performance_metric, list):
            self.performance_metric = [self.performance_metric] if self.performance_metric is not None else []
        self.performance_metric = [v if isinstance(v, str) else str(v) for v in self.performance_metric]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Prediction(NamedEntity):
    """
    Prediction produced by an AI model (Clause 7.4.2).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO22989["Prediction"]
    class_class_curie: ClassVar[str] = "iso22989:Prediction"
    class_name: ClassVar[str] = "Prediction"
    class_model_uri: ClassVar[URIRef] = ISO22989.Prediction

    id: Union[str, PredictionId] = None
    name: str = None
    predicted_value: Optional[str] = None
    confidence: Optional[Union[float, ConfidenceScore]] = None
    produced_by: Optional[Union[str, AIModelId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PredictionId):
            self.id = PredictionId(self.id)

        if self.predicted_value is not None and not isinstance(self.predicted_value, str):
            self.predicted_value = str(self.predicted_value)

        if self.confidence is not None and not isinstance(self.confidence, ConfidenceScore):
            self.confidence = ConfidenceScore(self.confidence)

        if self.produced_by is not None and not isinstance(self.produced_by, AIModelId):
            self.produced_by = AIModelId(self.produced_by)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Decision(NamedEntity):
    """
    Decision produced by an AI system on the basis of one or more predictions (Clause 7.4.3).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO22989["Decision"]
    class_class_curie: ClassVar[str] = "iso22989:Decision"
    class_name: ClassVar[str] = "Decision"
    class_model_uri: ClassVar[URIRef] = ISO22989.Decision

    id: Union[str, DecisionId] = None
    name: str = None
    decision_outcome: Optional[str] = None
    decision_policy: Optional[str] = None
    based_on_predictions: Optional[Union[Union[str, PredictionId], list[Union[str, PredictionId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DecisionId):
            self.id = DecisionId(self.id)

        if self.decision_outcome is not None and not isinstance(self.decision_outcome, str):
            self.decision_outcome = str(self.decision_outcome)

        if self.decision_policy is not None and not isinstance(self.decision_policy, str):
            self.decision_policy = str(self.decision_policy)

        if not isinstance(self.based_on_predictions, list):
            self.based_on_predictions = [self.based_on_predictions] if self.based_on_predictions is not None else []
        self.based_on_predictions = [v if isinstance(v, PredictionId) else PredictionId(v) for v in self.based_on_predictions]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Action(NamedEntity):
    """
    Action carried out as a result of an AI-system decision (Clause 7.4.4).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO22989["Action"]
    class_class_curie: ClassVar[str] = "iso22989:Action"
    class_name: ClassVar[str] = "Action"
    class_model_uri: ClassVar[URIRef] = ISO22989.Action

    id: Union[str, ActionId] = None
    name: str = None
    action_target: Optional[str] = None
    execution_status: Optional[Union[str, "ExecutionStatus"]] = None
    triggered_by: Optional[Union[str, DecisionId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ActionId):
            self.id = ActionId(self.id)

        if self.action_target is not None and not isinstance(self.action_target, str):
            self.action_target = str(self.action_target)

        if self.execution_status is not None and not isinstance(self.execution_status, ExecutionStatus):
            self.execution_status = ExecutionStatus(self.execution_status)

        if self.triggered_by is not None and not isinstance(self.triggered_by, DecisionId):
            self.triggered_by = DecisionId(self.triggered_by)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class InferenceEngine(NamedEntity):
    """
    Component performing inference over a model or knowledge base (Clause 3.1.17).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO22989["InferenceEngine"]
    class_class_curie: ClassVar[str] = "iso22989:InferenceEngine"
    class_name: ClassVar[str] = "InferenceEngine"
    class_model_uri: ClassVar[URIRef] = ISO22989.InferenceEngine

    id: Union[str, InferenceEngineId] = None
    name: str = None
    inference_strategy: Optional[str] = None
    uses_model: Optional[Union[str, AIModelId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, InferenceEngineId):
            self.id = InferenceEngineId(self.id)

        if self.inference_strategy is not None and not isinstance(self.inference_strategy, str):
            self.inference_strategy = str(self.inference_strategy)

        if self.uses_model is not None and not isinstance(self.uses_model, AIModelId):
            self.uses_model = AIModelId(self.uses_model)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class KnowledgeGraph(KnowledgeRepresentation):
    """
    Graph-structured knowledge representation, often used for reasoning and retrieval (Clause 8.5).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO22989["KnowledgeGraph"]
    class_class_curie: ClassVar[str] = "iso22989:KnowledgeGraph"
    class_name: ClassVar[str] = "KnowledgeGraph"
    class_model_uri: ClassVar[URIRef] = ISO22989.KnowledgeGraph

    id: Union[str, KnowledgeGraphId] = None
    name: str = None
    node_count: Optional[int] = None
    edge_count: Optional[int] = None
    ontology_reference: Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, KnowledgeGraphId):
            self.id = KnowledgeGraphId(self.id)

        if self.node_count is not None and not isinstance(self.node_count, int):
            self.node_count = int(self.node_count)

        if self.edge_count is not None and not isinstance(self.edge_count, int):
            self.edge_count = int(self.edge_count)

        if not isinstance(self.ontology_reference, list):
            self.ontology_reference = [self.ontology_reference] if self.ontology_reference is not None else []
        self.ontology_reference = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.ontology_reference]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ExpertSystem(NamedEntity):
    """
    Rule-based system encoding domain expertise (Clause 8.5.2).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO22989["ExpertSystem"]
    class_class_curie: ClassVar[str] = "iso22989:ExpertSystem"
    class_name: ClassVar[str] = "ExpertSystem"
    class_model_uri: ClassVar[URIRef] = ISO22989.ExpertSystem

    id: Union[str, ExpertSystemId] = None
    name: str = None
    rule_count: Optional[int] = None
    inference_engine: Optional[Union[dict, InferenceEngine]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ExpertSystemId):
            self.id = ExpertSystemId(self.id)

        if self.rule_count is not None and not isinstance(self.rule_count, int):
            self.rule_count = int(self.rule_count)

        if self.inference_engine is not None and not isinstance(self.inference_engine, InferenceEngine):
            self.inference_engine = InferenceEngine(**as_dict(self.inference_engine))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CognitiveComputingSystem(AIConcept):
    """
    System combining AI techniques to emulate human cognitive functions (Clause 5.5).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO22989["CognitiveComputingSystem"]
    class_class_curie: ClassVar[str] = "iso22989:CognitiveComputingSystem"
    class_name: ClassVar[str] = "CognitiveComputingSystem"
    class_model_uri: ClassVar[URIRef] = ISO22989.CognitiveComputingSystem

    id: Union[str, CognitiveComputingSystemId] = None
    name: str = None
    cognitive_capabilities: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CognitiveComputingSystemId):
            self.id = CognitiveComputingSystemId(self.id)

        if not isinstance(self.cognitive_capabilities, list):
            self.cognitive_capabilities = [self.cognitive_capabilities] if self.cognitive_capabilities is not None else []
        self.cognitive_capabilities = [v if isinstance(v, str) else str(v) for v in self.cognitive_capabilities]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SemanticComputingSystem(AIConcept):
    """
    System whose behaviour is driven by the explicit semantics of its inputs and knowledge sources (Clause 5.6).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO22989["SemanticComputingSystem"]
    class_class_curie: ClassVar[str] = "iso22989:SemanticComputingSystem"
    class_name: ClassVar[str] = "SemanticComputingSystem"
    class_model_uri: ClassVar[URIRef] = ISO22989.SemanticComputingSystem

    id: Union[str, SemanticComputingSystemId] = None
    name: str = None
    semantic_model: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SemanticComputingSystemId):
            self.id = SemanticComputingSystemId(self.id)

        if self.semantic_model is not None and not isinstance(self.semantic_model, str):
            self.semantic_model = str(self.semantic_model)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SoftComputingSystem(AIConcept):
    """
    System employing soft computing techniques tolerant of imprecision and uncertainty (Clause 5.7).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO22989["SoftComputingSystem"]
    class_class_curie: ClassVar[str] = "iso22989:SoftComputingSystem"
    class_name: ClassVar[str] = "SoftComputingSystem"
    class_model_uri: ClassVar[URIRef] = ISO22989.SoftComputingSystem

    id: Union[str, SoftComputingSystemId] = None
    name: str = None
    soft_computing_techniques: Union[Union[str, "SoftComputingTechnique"], list[Union[str, "SoftComputingTechnique"]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SoftComputingSystemId):
            self.id = SoftComputingSystemId(self.id)

        if self._is_empty(self.soft_computing_techniques):
            self.MissingRequiredField("soft_computing_techniques")
        if not isinstance(self.soft_computing_techniques, list):
            self.soft_computing_techniques = [self.soft_computing_techniques] if self.soft_computing_techniques is not None else []
        self.soft_computing_techniques = [v if isinstance(v, SoftComputingTechnique) else SoftComputingTechnique(v) for v in self.soft_computing_techniques]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DataProcess(NamedEntity):
    """
    Discrete data-handling process applied to a dataset during AI system development or operation (Clause 5.10).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO22989["DataProcess"]
    class_class_curie: ClassVar[str] = "iso22989:DataProcess"
    class_name: ClassVar[str] = "DataProcess"
    class_model_uri: ClassVar[URIRef] = ISO22989.DataProcess

    id: Union[str, DataProcessId] = None
    name: str = None
    process_type: Union[str, "DataProcessType"] = None
    input_dataset: Optional[Union[str, DatasetId]] = None
    output_dataset: Optional[Union[str, DatasetId]] = None
    parameters: Optional[Union[str, list[str]]] = empty_list()
    executed_by: Optional[Union[str, AIStakeholderRoleId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DataProcessId):
            self.id = DataProcessId(self.id)

        if self._is_empty(self.process_type):
            self.MissingRequiredField("process_type")
        if not isinstance(self.process_type, DataProcessType):
            self.process_type = DataProcessType(self.process_type)

        if self.input_dataset is not None and not isinstance(self.input_dataset, DatasetId):
            self.input_dataset = DatasetId(self.input_dataset)

        if self.output_dataset is not None and not isinstance(self.output_dataset, DatasetId):
            self.output_dataset = DatasetId(self.output_dataset)

        if not isinstance(self.parameters, list):
            self.parameters = [self.parameters] if self.parameters is not None else []
        self.parameters = [v if isinstance(v, str) else str(v) for v in self.parameters]

        if self.executed_by is not None and not isinstance(self.executed_by, AIStakeholderRoleId):
            self.executed_by = AIStakeholderRoleId(self.executed_by)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DataSample(NamedEntity):
    """
    Individual data record within a dataset (Clause 3.2.13).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO22989["DataSample"]
    class_class_curie: ClassVar[str] = "iso22989:DataSample"
    class_name: ClassVar[str] = "DataSample"
    class_model_uri: ClassVar[URIRef] = ISO22989.DataSample

    id: Union[str, DataSampleId] = None
    name: str = None
    sample_payload: Optional[str] = None
    sample_label: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DataSampleId):
            self.id = DataSampleId(self.id)

        if self.sample_payload is not None and not isinstance(self.sample_payload, str):
            self.sample_payload = str(self.sample_payload)

        if self.sample_label is not None and not isinstance(self.sample_label, str):
            self.sample_label = str(self.sample_label)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DataLabel(NamedEntity):
    """
    Label or annotation attached to one or more data samples (Clause 3.2.10).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO22989["DataLabel"]
    class_class_curie: ClassVar[str] = "iso22989:DataLabel"
    class_name: ClassVar[str] = "DataLabel"
    class_model_uri: ClassVar[URIRef] = ISO22989.DataLabel

    id: Union[str, DataLabelId] = None
    name: str = None
    label_value: str = None
    label_type: Optional[Union[str, "DataLabelType"]] = None
    annotator: Optional[Union[str, AIStakeholderRoleId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DataLabelId):
            self.id = DataLabelId(self.id)

        if self._is_empty(self.label_value):
            self.MissingRequiredField("label_value")
        if not isinstance(self.label_value, str):
            self.label_value = str(self.label_value)

        if self.label_type is not None and not isinstance(self.label_type, DataLabelType):
            self.label_type = DataLabelType(self.label_type)

        if self.annotator is not None and not isinstance(self.annotator, AIStakeholderRoleId):
            self.annotator = AIStakeholderRoleId(self.annotator)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GroundTruthRecord(NamedEntity):
    """
    Trusted reference record used to evaluate or train an AI model (Clause 3.2.7).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO22989["GroundTruthRecord"]
    class_class_curie: ClassVar[str] = "iso22989:GroundTruthRecord"
    class_name: ClassVar[str] = "GroundTruthRecord"
    class_model_uri: ClassVar[URIRef] = ISO22989.GroundTruthRecord

    id: Union[str, GroundTruthRecordId] = None
    name: str = None
    ground_truth_value: str = None
    provenance_statement: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GroundTruthRecordId):
            self.id = GroundTruthRecordId(self.id)

        if self._is_empty(self.ground_truth_value):
            self.MissingRequiredField("ground_truth_value")
        if not isinstance(self.ground_truth_value, str):
            self.ground_truth_value = str(self.ground_truth_value)

        if self.provenance_statement is not None and not isinstance(self.provenance_statement, str):
            self.provenance_statement = str(self.provenance_statement)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Robot(NamedEntity):
    """
    Embodied agent able to perceive its environment and act in the physical world (Clause 5.3 / Clause 9.5 robotics
    field).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO22989["Robot"]
    class_class_curie: ClassVar[str] = "iso22989:Robot"
    class_name: ClassVar[str] = "Robot"
    class_model_uri: ClassVar[URIRef] = ISO22989.Robot

    id: Union[str, RobotId] = None
    name: str = None
    embodiment: Optional[str] = None
    controlled_by: Optional[Union[str, AISystemId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RobotId):
            self.id = RobotId(self.id)

        if self.embodiment is not None and not isinstance(self.embodiment, str):
            self.embodiment = str(self.embodiment)

        if self.controlled_by is not None and not isinstance(self.controlled_by, AISystemId):
            self.controlled_by = AISystemId(self.controlled_by)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IoTDevice(NamedEntity):
    """
    Device participating in an Internet-of-Things deployment (Clause 5.14.2).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO22989["IoTDevice"]
    class_class_curie: ClassVar[str] = "iso22989:IoTDevice"
    class_name: ClassVar[str] = "IoTDevice"
    class_model_uri: ClassVar[URIRef] = ISO22989.IoTDevice

    id: Union[str, IoTDeviceId] = None
    name: str = None
    device_role: Union[str, "IoTDeviceRole"] = None
    sensing_capabilities: Optional[Union[str, list[str]]] = empty_list()
    actuating_capabilities: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IoTDeviceId):
            self.id = IoTDeviceId(self.id)

        if self._is_empty(self.device_role):
            self.MissingRequiredField("device_role")
        if not isinstance(self.device_role, IoTDeviceRole):
            self.device_role = IoTDeviceRole(self.device_role)

        if not isinstance(self.sensing_capabilities, list):
            self.sensing_capabilities = [self.sensing_capabilities] if self.sensing_capabilities is not None else []
        self.sensing_capabilities = [v if isinstance(v, str) else str(v) for v in self.sensing_capabilities]

        if not isinstance(self.actuating_capabilities, list):
            self.actuating_capabilities = [self.actuating_capabilities] if self.actuating_capabilities is not None else []
        self.actuating_capabilities = [v if isinstance(v, str) else str(v) for v in self.actuating_capabilities]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IoTSystem(NamedEntity):
    """
    Networked system composed of IoT devices, possibly enhanced with AI capabilities (Clause 5.14.2).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO22989["IoTSystem"]
    class_class_curie: ClassVar[str] = "iso22989:IoTSystem"
    class_name: ClassVar[str] = "IoTSystem"
    class_model_uri: ClassVar[URIRef] = ISO22989.IoTSystem

    id: Union[str, IoTSystemId] = None
    name: str = None
    devices: Optional[Union[dict[Union[str, IoTDeviceId], Union[dict, IoTDevice]], list[Union[dict, IoTDevice]]]] = empty_dict()
    ai_components: Optional[Union[Union[str, AIComponentId], list[Union[str, AIComponentId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IoTSystemId):
            self.id = IoTSystemId(self.id)

        self._normalize_inlined_as_list(slot_name="devices", slot_type=IoTDevice, key_name="id", keyed=True)

        if not isinstance(self.ai_components, list):
            self.ai_components = [self.ai_components] if self.ai_components is not None else []
        self.ai_components = [v if isinstance(v, AIComponentId) else AIComponentId(v) for v in self.ai_components]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CyberPhysicalSystem(NamedEntity):
    """
    System that tightly integrates computational and physical components, typically with feedback loops between
    sensing and actuation (Clause 5.14.3).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO22989["CyberPhysicalSystem"]
    class_class_curie: ClassVar[str] = "iso22989:CyberPhysicalSystem"
    class_name: ClassVar[str] = "CyberPhysicalSystem"
    class_model_uri: ClassVar[URIRef] = ISO22989.CyberPhysicalSystem

    id: Union[str, CyberPhysicalSystemId] = None
    name: str = None
    physical_processes: Optional[Union[str, list[str]]] = empty_list()
    cyber_components: Optional[Union[Union[str, AIComponentId], list[Union[str, AIComponentId]]]] = empty_list()
    iot_subsystem: Optional[Union[str, IoTSystemId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CyberPhysicalSystemId):
            self.id = CyberPhysicalSystemId(self.id)

        if not isinstance(self.physical_processes, list):
            self.physical_processes = [self.physical_processes] if self.physical_processes is not None else []
        self.physical_processes = [v if isinstance(v, str) else str(v) for v in self.physical_processes]

        if not isinstance(self.cyber_components, list):
            self.cyber_components = [self.cyber_components] if self.cyber_components is not None else []
        self.cyber_components = [v if isinstance(v, AIComponentId) else AIComponentId(v) for v in self.cyber_components]

        if self.iot_subsystem is not None and not isinstance(self.iot_subsystem, IoTSystemId):
            self.iot_subsystem = IoTSystemId(self.iot_subsystem)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AbbreviationEntry(NamedEntity):
    """
    Record of a single abbreviation listed in Clause 4 of the standard.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO22989["AbbreviationEntry"]
    class_class_curie: ClassVar[str] = "iso22989:AbbreviationEntry"
    class_name: ClassVar[str] = "AbbreviationEntry"
    class_model_uri: ClassVar[URIRef] = ISO22989.AbbreviationEntry

    id: Union[str, AbbreviationEntryId] = None
    name: str = None
    abbreviation_code: Union[str, "AbbreviationCode"] = None
    expansion: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AbbreviationEntryId):
            self.id = AbbreviationEntryId(self.id)

        if self._is_empty(self.abbreviation_code):
            self.MissingRequiredField("abbreviation_code")
        if not isinstance(self.abbreviation_code, AbbreviationCode):
            self.abbreviation_code = AbbreviationCode(self.abbreviation_code)

        if self._is_empty(self.expansion):
            self.MissingRequiredField("expansion")
        if not isinstance(self.expansion, str):
            self.expansion = str(self.expansion)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AIConceptsCollection(YAMLRoot):
    """
    Top-level container aggregating AI systems, models, datasets, lifecycle processes, stakeholder roles, applications
    and trustworthiness records for serialisation as a single artefact.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO22989["AIConceptsCollection"]
    class_class_curie: ClassVar[str] = "iso22989:AIConceptsCollection"
    class_name: ClassVar[str] = "AIConceptsCollection"
    class_model_uri: ClassVar[URIRef] = ISO22989.AIConceptsCollection

    ai_systems: Optional[Union[dict[Union[str, AISystemId], Union[dict, AISystem]], list[Union[dict, AISystem]]]] = empty_dict()
    ai_models: Optional[Union[dict[Union[str, AIModelId], Union[dict, AIModel]], list[Union[dict, AIModel]]]] = empty_dict()
    ai_datasets: Optional[Union[dict[Union[str, DatasetId], Union[dict, Dataset]], list[Union[dict, Dataset]]]] = empty_dict()
    ai_lifecycle_processes: Optional[Union[dict[Union[str, AILifecycleProcessId], Union[dict, AILifecycleProcess]], list[Union[dict, AILifecycleProcess]]]] = empty_dict()
    ai_stakeholder_roles: Optional[Union[dict[Union[str, AIStakeholderRoleId], Union[dict, AIStakeholderRole]], list[Union[dict, AIStakeholderRole]]]] = empty_dict()
    ai_applications: Optional[Union[dict[Union[str, AIApplicationId], Union[dict, AIApplication]], list[Union[dict, AIApplication]]]] = empty_dict()
    trustworthiness_records: Optional[Union[dict[Union[str, TrustworthinessPropertyId], Union[dict, TrustworthinessProperty]], list[Union[dict, TrustworthinessProperty]]]] = empty_dict()
    tasks: Optional[Union[dict[Union[str, TaskId], Union[dict, Task]], list[Union[dict, Task]]]] = empty_dict()
    data_processes: Optional[Union[dict[Union[str, DataProcessId], Union[dict, DataProcess]], list[Union[dict, DataProcess]]]] = empty_dict()
    iot_systems: Optional[Union[dict[Union[str, IoTSystemId], Union[dict, IoTSystem]], list[Union[dict, IoTSystem]]]] = empty_dict()
    cyber_physical_systems: Optional[Union[dict[Union[str, CyberPhysicalSystemId], Union[dict, CyberPhysicalSystem]], list[Union[dict, CyberPhysicalSystem]]]] = empty_dict()
    knowledge_graphs: Optional[Union[dict[Union[str, KnowledgeGraphId], Union[dict, KnowledgeGraph]], list[Union[dict, KnowledgeGraph]]]] = empty_dict()
    expert_systems: Optional[Union[dict[Union[str, ExpertSystemId], Union[dict, ExpertSystem]], list[Union[dict, ExpertSystem]]]] = empty_dict()
    abbreviations: Optional[Union[dict[Union[str, AbbreviationEntryId], Union[dict, AbbreviationEntry]], list[Union[dict, AbbreviationEntry]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="ai_systems", slot_type=AISystem, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="ai_models", slot_type=AIModel, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="ai_datasets", slot_type=Dataset, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="ai_lifecycle_processes", slot_type=AILifecycleProcess, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="ai_stakeholder_roles", slot_type=AIStakeholderRole, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="ai_applications", slot_type=AIApplication, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="trustworthiness_records", slot_type=TrustworthinessProperty, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="tasks", slot_type=Task, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="data_processes", slot_type=DataProcess, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="iot_systems", slot_type=IoTSystem, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="cyber_physical_systems", slot_type=CyberPhysicalSystem, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="knowledge_graphs", slot_type=KnowledgeGraph, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="expert_systems", slot_type=ExpertSystem, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="abbreviations", slot_type=AbbreviationEntry, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AIPlatformProvider(AIProvider):
    """
    Provider of platform infrastructure on which AI services are operated (Clause 5.19.2).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO22989["AIPlatformProvider"]
    class_class_curie: ClassVar[str] = "iso22989:AIPlatformProvider"
    class_name: ClassVar[str] = "AIPlatformProvider"
    class_model_uri: ClassVar[URIRef] = ISO22989.AIPlatformProvider

    id: Union[str, AIPlatformProviderId] = None
    name: str = None
    stakeholder_role_type: Union[str, "AIStakeholderRoleType"] = 'ai_provider'

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AIPlatformProviderId):
            self.id = AIPlatformProviderId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AIServiceProductProvider(AIProvider):
    """
    Provider of an AI-enabled service or product to customers (Clause 5.19.2).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO22989["AIServiceProductProvider"]
    class_class_curie: ClassVar[str] = "iso22989:AIServiceProductProvider"
    class_name: ClassVar[str] = "AIServiceProductProvider"
    class_model_uri: ClassVar[URIRef] = ISO22989.AIServiceProductProvider

    id: Union[str, AIServiceProductProviderId] = None
    name: str = None
    stakeholder_role_type: Union[str, "AIStakeholderRoleType"] = 'ai_provider'

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AIServiceProductProviderId):
            self.id = AIServiceProductProviderId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ModelDesigner(AIProducer):
    """
    Producer role responsible for designing AI models (Clause 5.19.3).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO22989["ModelDesigner"]
    class_class_curie: ClassVar[str] = "iso22989:ModelDesigner"
    class_name: ClassVar[str] = "ModelDesigner"
    class_model_uri: ClassVar[URIRef] = ISO22989.ModelDesigner

    id: Union[str, ModelDesignerId] = None
    name: str = None
    stakeholder_role_type: Union[str, "AIStakeholderRoleType"] = 'ai_producer'

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ModelDesignerId):
            self.id = ModelDesignerId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ModelImplementer(AIProducer):
    """
    Producer role responsible for implementing AI models in code (Clause 5.19.3).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO22989["ModelImplementer"]
    class_class_curie: ClassVar[str] = "iso22989:ModelImplementer"
    class_name: ClassVar[str] = "ModelImplementer"
    class_model_uri: ClassVar[URIRef] = ISO22989.ModelImplementer

    id: Union[str, ModelImplementerId] = None
    name: str = None
    stakeholder_role_type: Union[str, "AIStakeholderRoleType"] = 'ai_producer'

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ModelImplementerId):
            self.id = ModelImplementerId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ComputationVerifier(AIProducer):
    """
    Producer role verifying the computational behaviour of an AI system (Clause 5.19.3).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO22989["ComputationVerifier"]
    class_class_curie: ClassVar[str] = "iso22989:ComputationVerifier"
    class_name: ClassVar[str] = "ComputationVerifier"
    class_model_uri: ClassVar[URIRef] = ISO22989.ComputationVerifier

    id: Union[str, ComputationVerifierId] = None
    name: str = None
    stakeholder_role_type: Union[str, "AIStakeholderRoleType"] = 'ai_producer'

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ComputationVerifierId):
            self.id = ComputationVerifierId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ModelVerifier(AIProducer):
    """
    Producer role verifying that models meet specified requirements (Clause 5.19.3).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO22989["ModelVerifier"]
    class_class_curie: ClassVar[str] = "iso22989:ModelVerifier"
    class_name: ClassVar[str] = "ModelVerifier"
    class_model_uri: ClassVar[URIRef] = ISO22989.ModelVerifier

    id: Union[str, ModelVerifierId] = None
    name: str = None
    stakeholder_role_type: Union[str, "AIStakeholderRoleType"] = 'ai_producer'

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ModelVerifierId):
            self.id = ModelVerifierId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AIUser(AICustomer):
    """
    End user of an AI system or AI-backed service (Clause 5.19.4).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO22989["AIUser"]
    class_class_curie: ClassVar[str] = "iso22989:AIUser"
    class_name: ClassVar[str] = "AIUser"
    class_model_uri: ClassVar[URIRef] = ISO22989.AIUser

    id: Union[str, AIUserId] = None
    name: str = None
    stakeholder_role_type: Union[str, "AIStakeholderRoleType"] = 'ai_customer'

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AIUserId):
            self.id = AIUserId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AISystemIntegrator(AIPartner):
    """
    Partner integrating AI components into a wider system (Clause 5.19.5).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO22989["AISystemIntegrator"]
    class_class_curie: ClassVar[str] = "iso22989:AISystemIntegrator"
    class_name: ClassVar[str] = "AISystemIntegrator"
    class_model_uri: ClassVar[URIRef] = ISO22989.AISystemIntegrator

    id: Union[str, AISystemIntegratorId] = None
    name: str = None
    stakeholder_role_type: Union[str, "AIStakeholderRoleType"] = 'ai_partner'

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AISystemIntegratorId):
            self.id = AISystemIntegratorId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DataProvider(AIPartner):
    """
    Partner supplying datasets used by AI systems (Clause 5.19.5).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO22989["DataProvider"]
    class_class_curie: ClassVar[str] = "iso22989:DataProvider"
    class_name: ClassVar[str] = "DataProvider"
    class_model_uri: ClassVar[URIRef] = ISO22989.DataProvider

    id: Union[str, DataProviderId] = None
    name: str = None
    stakeholder_role_type: Union[str, "AIStakeholderRoleType"] = 'ai_partner'

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DataProviderId):
            self.id = DataProviderId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AIAuditor(AIPartner):
    """
    Partner performing independent audits of AI systems (Clause 5.19.5).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO22989["AIAuditor"]
    class_class_curie: ClassVar[str] = "iso22989:AIAuditor"
    class_name: ClassVar[str] = "AIAuditor"
    class_model_uri: ClassVar[URIRef] = ISO22989.AIAuditor

    id: Union[str, AIAuditorId] = None
    name: str = None
    stakeholder_role_type: Union[str, "AIStakeholderRoleType"] = 'ai_partner'

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AIAuditorId):
            self.id = AIAuditorId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AIEvaluator(AIPartner):
    """
    Partner performing evaluations of AI system performance and trustworthiness (Clause 5.19.5).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO22989["AIEvaluator"]
    class_class_curie: ClassVar[str] = "iso22989:AIEvaluator"
    class_name: ClassVar[str] = "AIEvaluator"
    class_model_uri: ClassVar[URIRef] = ISO22989.AIEvaluator

    id: Union[str, AIEvaluatorId] = None
    name: str = None
    stakeholder_role_type: Union[str, "AIStakeholderRoleType"] = 'ai_partner'

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AIEvaluatorId):
            self.id = AIEvaluatorId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DataSubject(AISubject):
    """
    Individual whose personal data is processed by an AI system (Clause 5.19.6).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO22989["DataSubject"]
    class_class_curie: ClassVar[str] = "iso22989:DataSubject"
    class_name: ClassVar[str] = "DataSubject"
    class_model_uri: ClassVar[URIRef] = ISO22989.DataSubject

    id: Union[str, DataSubjectId] = None
    name: str = None
    stakeholder_role_type: Union[str, "AIStakeholderRoleType"] = 'ai_subject'

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DataSubjectId):
            self.id = DataSubjectId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PolicyMaker(RelevantAuthority):
    """
    Authority defining policy applicable to AI systems (Clause 5.19.7).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO22989["PolicyMaker"]
    class_class_curie: ClassVar[str] = "iso22989:PolicyMaker"
    class_name: ClassVar[str] = "PolicyMaker"
    class_model_uri: ClassVar[URIRef] = ISO22989.PolicyMaker

    id: Union[str, PolicyMakerId] = None
    name: str = None
    stakeholder_role_type: Union[str, "AIStakeholderRoleType"] = 'relevant_authority'

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PolicyMakerId):
            self.id = PolicyMakerId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Regulator(RelevantAuthority):
    """
    Authority responsible for regulatory oversight of AI systems (Clause 5.19.7).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO22989["Regulator"]
    class_class_curie: ClassVar[str] = "iso22989:Regulator"
    class_name: ClassVar[str] = "Regulator"
    class_model_uri: ClassVar[URIRef] = ISO22989.Regulator

    id: Union[str, RegulatorId] = None
    name: str = None
    stakeholder_role_type: Union[str, "AIStakeholderRoleType"] = 'relevant_authority'

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RegulatorId):
            self.id = RegulatorId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AutonomyAssessment(NamedEntity):
    """
    Structured assessment of the autonomy level of an AI system using the criteria listed in Clause 5.13.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO22989["AutonomyAssessment"]
    class_class_curie: ClassVar[str] = "iso22989:AutonomyAssessment"
    class_name: ClassVar[str] = "AutonomyAssessment"
    class_model_uri: ClassVar[URIRef] = ISO22989.AutonomyAssessment

    id: Union[str, AutonomyAssessmentId] = None
    name: str = None
    autonomy_level: Optional[Union[str, "AutonomyLevel"]] = None
    autonomy_criterion_scores: Optional[Union[str, list[str]]] = empty_list()
    clause_reference: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AutonomyAssessmentId):
            self.id = AutonomyAssessmentId(self.id)

        if self.autonomy_level is not None and not isinstance(self.autonomy_level, AutonomyLevel):
            self.autonomy_level = AutonomyLevel(self.autonomy_level)

        if not isinstance(self.autonomy_criterion_scores, list):
            self.autonomy_criterion_scores = [self.autonomy_criterion_scores] if self.autonomy_criterion_scores is not None else []
        self.autonomy_criterion_scores = [v if isinstance(v, str) else str(v) for v in self.autonomy_criterion_scores]

        if self.clause_reference is not None and not isinstance(self.clause_reference, str):
            self.clause_reference = str(self.clause_reference)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class VerificationValidationFramework(NamedEntity):
    """
    Verifiability and validatability claim for an AI system characterised according to the levels in Clause 5.16.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO22989["VerificationValidationFramework"]
    class_class_curie: ClassVar[str] = "iso22989:VerificationValidationFramework"
    class_name: ClassVar[str] = "VerificationValidationFramework"
    class_model_uri: ClassVar[URIRef] = ISO22989.VerificationValidationFramework

    id: Union[str, VerificationValidationFrameworkId] = None
    name: str = None
    verification_validation_level: Optional[Union[str, "VerificationValidationLevel"]] = None
    clause_reference: Optional[str] = None
    verification_methods: Optional[Union[str, list[str]]] = empty_list()
    validation_methods: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, VerificationValidationFrameworkId):
            self.id = VerificationValidationFrameworkId(self.id)

        if self.verification_validation_level is not None and not isinstance(self.verification_validation_level, VerificationValidationLevel):
            self.verification_validation_level = VerificationValidationLevel(self.verification_validation_level)

        if self.clause_reference is not None and not isinstance(self.clause_reference, str):
            self.clause_reference = str(self.clause_reference)

        if not isinstance(self.verification_methods, list):
            self.verification_methods = [self.verification_methods] if self.verification_methods is not None else []
        self.verification_methods = [v if isinstance(v, str) else str(v) for v in self.verification_methods]

        if not isinstance(self.validation_methods, list):
            self.validation_methods = [self.validation_methods] if self.validation_methods is not None else []
        self.validation_methods = [v if isinstance(v, str) else str(v) for v in self.validation_methods]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanMachineTeam(AIConcept):
    """
    Collaboration arrangement combining one or more humans with one or more AI systems to pursue shared goals (Clauses
    3.3.3, 5.13).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO22989["HumanMachineTeam"]
    class_class_curie: ClassVar[str] = "iso22989:HumanMachineTeam"
    class_name: ClassVar[str] = "HumanMachineTeam"
    class_model_uri: ClassVar[URIRef] = ISO22989.HumanMachineTeam

    id: Union[str, HumanMachineTeamId] = None
    name: str = None
    human_roles: Optional[Union[str, list[str]]] = empty_list()
    ai_systems_involved: Optional[Union[Union[str, AISystemId], list[Union[str, AISystemId]]]] = empty_list()
    task_allocation: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, HumanMachineTeamId):
            self.id = HumanMachineTeamId(self.id)

        if not isinstance(self.human_roles, list):
            self.human_roles = [self.human_roles] if self.human_roles is not None else []
        self.human_roles = [v if isinstance(v, str) else str(v) for v in self.human_roles]

        if not isinstance(self.ai_systems_involved, list):
            self.ai_systems_involved = [self.ai_systems_involved] if self.ai_systems_involved is not None else []
        self.ai_systems_involved = [v if isinstance(v, AISystemId) else AISystemId(v) for v in self.ai_systems_involved]

        if self.task_allocation is not None and not isinstance(self.task_allocation, str):
            self.task_allocation = str(self.task_allocation)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntelligenceAugmentation(AIConcept):
    """
    Use of AI to enhance the cognitive capabilities of humans rather than replace them (Clause 5.13 context).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO22989["IntelligenceAugmentation"]
    class_class_curie: ClassVar[str] = "iso22989:IntelligenceAugmentation"
    class_name: ClassVar[str] = "IntelligenceAugmentation"
    class_model_uri: ClassVar[URIRef] = ISO22989.IntelligenceAugmentation

    id: Union[str, IntelligenceAugmentationId] = None
    name: str = None
    augmented_capability: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntelligenceAugmentationId):
            self.id = IntelligenceAugmentationId(self.id)

        if not isinstance(self.augmented_capability, list):
            self.augmented_capability = [self.augmented_capability] if self.augmented_capability is not None else []
        self.augmented_capability = [v if isinstance(v, str) else str(v) for v in self.augmented_capability]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Recommendation(NamedEntity):
    """
    Recommendation produced by an AI system (Clauses 7.4, 10).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO22989["Recommendation"]
    class_class_curie: ClassVar[str] = "iso22989:Recommendation"
    class_name: ClassVar[str] = "Recommendation"
    class_model_uri: ClassVar[URIRef] = ISO22989.Recommendation

    id: Union[str, RecommendationId] = None
    name: str = None
    recommendation_outcome_type: Optional[Union[str, "RecommendationOutcomeType"]] = None
    confidence: Optional[Union[float, ConfidenceScore]] = None
    recommended_items: Optional[Union[str, list[str]]] = empty_list()
    based_on_predictions: Optional[Union[Union[str, PredictionId], list[Union[str, PredictionId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RecommendationId):
            self.id = RecommendationId(self.id)

        if self.recommendation_outcome_type is not None and not isinstance(self.recommendation_outcome_type, RecommendationOutcomeType):
            self.recommendation_outcome_type = RecommendationOutcomeType(self.recommendation_outcome_type)

        if self.confidence is not None and not isinstance(self.confidence, ConfidenceScore):
            self.confidence = ConfidenceScore(self.confidence)

        if not isinstance(self.recommended_items, list):
            self.recommended_items = [self.recommended_items] if self.recommended_items is not None else []
        self.recommended_items = [v if isinstance(v, str) else str(v) for v in self.recommended_items]

        if not isinstance(self.based_on_predictions, list):
            self.based_on_predictions = [self.based_on_predictions] if self.based_on_predictions is not None else []
        self.based_on_predictions = [v if isinstance(v, PredictionId) else PredictionId(v) for v in self.based_on_predictions]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EvaluationMetric(NamedEntity):
    """
    Metric used to evaluate AI system or model performance (Clause 7.4.3).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO22989["EvaluationMetric"]
    class_class_curie: ClassVar[str] = "iso22989:EvaluationMetric"
    class_name: ClassVar[str] = "EvaluationMetric"
    class_model_uri: ClassVar[URIRef] = ISO22989.EvaluationMetric

    id: Union[str, EvaluationMetricId] = None
    name: str = None
    metric_name: str = None
    metric_value: Optional[float] = None
    metric_unit: Optional[str] = None
    reference_dataset: Optional[Union[str, DatasetId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EvaluationMetricId):
            self.id = EvaluationMetricId(self.id)

        if self._is_empty(self.metric_name):
            self.MissingRequiredField("metric_name")
        if not isinstance(self.metric_name, str):
            self.metric_name = str(self.metric_name)

        if self.metric_value is not None and not isinstance(self.metric_value, float):
            self.metric_value = float(self.metric_value)

        if self.metric_unit is not None and not isinstance(self.metric_unit, str):
            self.metric_unit = str(self.metric_unit)

        if self.reference_dataset is not None and not isinstance(self.reference_dataset, DatasetId):
            self.reference_dataset = DatasetId(self.reference_dataset)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Threshold(NamedEntity):
    """
    Decision threshold applied to a metric, prediction or score (Clause 7.4.3).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO22989["Threshold"]
    class_class_curie: ClassVar[str] = "iso22989:Threshold"
    class_name: ClassVar[str] = "Threshold"
    class_model_uri: ClassVar[URIRef] = ISO22989.Threshold

    id: Union[str, ThresholdId] = None
    name: str = None
    threshold_value: float = None
    applies_to_metric: Optional[str] = None
    threshold_policy: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ThresholdId):
            self.id = ThresholdId(self.id)

        if self._is_empty(self.threshold_value):
            self.MissingRequiredField("threshold_value")
        if not isinstance(self.threshold_value, float):
            self.threshold_value = float(self.threshold_value)

        if self.applies_to_metric is not None and not isinstance(self.applies_to_metric, str):
            self.applies_to_metric = str(self.applies_to_metric)

        if self.threshold_policy is not None and not isinstance(self.threshold_policy, str):
            self.threshold_policy = str(self.threshold_policy)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Neuron(AIConcept):
    """
    Computational unit in a neural network combining weighted inputs with a bias and an activation function (Clause
    3.4.9).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO22989["Neuron"]
    class_class_curie: ClassVar[str] = "iso22989:Neuron"
    class_name: ClassVar[str] = "Neuron"
    class_model_uri: ClassVar[URIRef] = ISO22989.Neuron

    id: Union[str, NeuronId] = None
    name: str = None
    activation_function: Optional[Union[str, "ActivationFunctionType"]] = None
    input_arity: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NeuronId):
            self.id = NeuronId(self.id)

        if self.activation_function is not None and not isinstance(self.activation_function, ActivationFunctionType):
            self.activation_function = ActivationFunctionType(self.activation_function)

        if self.input_arity is not None and not isinstance(self.input_arity, int):
            self.input_arity = int(self.input_arity)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ConvolutionOperation(AIConcept):
    """
    Convolution operation as used in convolutional neural networks (Clause 3.4.3).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO22989["ConvolutionOperation"]
    class_class_curie: ClassVar[str] = "iso22989:ConvolutionOperation"
    class_name: ClassVar[str] = "ConvolutionOperation"
    class_model_uri: ClassVar[URIRef] = ISO22989.ConvolutionOperation

    id: Union[str, ConvolutionOperationId] = None
    name: str = None
    kernel_size: Optional[Union[int, list[int]]] = empty_list()
    stride: Optional[int] = None
    padding: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ConvolutionOperationId):
            self.id = ConvolutionOperationId(self.id)

        if not isinstance(self.kernel_size, list):
            self.kernel_size = [self.kernel_size] if self.kernel_size is not None else []
        self.kernel_size = [v if isinstance(v, int) else int(v) for v in self.kernel_size]

        if self.stride is not None and not isinstance(self.stride, int):
            self.stride = int(self.stride)

        if self.padding is not None and not isinstance(self.padding, str):
            self.padding = str(self.padding)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DataDrift(NamedEntity):
    """
    Observed change in the statistical distribution of operational data relative to training data (Clause 5.11.9.1).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO22989["DataDrift"]
    class_class_curie: ClassVar[str] = "iso22989:DataDrift"
    class_name: ClassVar[str] = "DataDrift"
    class_model_uri: ClassVar[URIRef] = ISO22989.DataDrift

    id: Union[str, DataDriftId] = None
    name: str = None
    drift_type: Optional[str] = None
    detected_at: Optional[str] = None
    affected_dataset: Optional[Union[str, DatasetId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DataDriftId):
            self.id = DataDriftId(self.id)

        if self.drift_type is not None and not isinstance(self.drift_type, str):
            self.drift_type = str(self.drift_type)

        if self.detected_at is not None and not isinstance(self.detected_at, str):
            self.detected_at = str(self.detected_at)

        if self.affected_dataset is not None and not isinstance(self.affected_dataset, DatasetId):
            self.affected_dataset = DatasetId(self.affected_dataset)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CatastrophicForgetting(NamedEntity):
    """
    Phenomenon by which a continually-trained model loses previously acquired competence (Clause 5.11.9.1).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO22989["CatastrophicForgetting"]
    class_class_curie: ClassVar[str] = "iso22989:CatastrophicForgetting"
    class_name: ClassVar[str] = "CatastrophicForgetting"
    class_model_uri: ClassVar[URIRef] = ISO22989.CatastrophicForgetting

    id: Union[str, CatastrophicForgettingId] = None
    name: str = None
    affected_model: Optional[Union[str, AIModelId]] = None
    mitigation_strategy: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CatastrophicForgettingId):
            self.id = CatastrophicForgettingId(self.id)

        if self.affected_model is not None and not isinstance(self.affected_model, AIModelId):
            self.affected_model = AIModelId(self.affected_model)

        if self.mitigation_strategy is not None and not isinstance(self.mitigation_strategy, str):
            self.mitigation_strategy = str(self.mitigation_strategy)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FaultToleranceMechanism(NamedEntity):
    """
    Mechanism enabling an AI system to continue operating correctly in the presence of component faults (Clause 5.15.4
    context).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO22989["FaultToleranceMechanism"]
    class_class_curie: ClassVar[str] = "iso22989:FaultToleranceMechanism"
    class_name: ClassVar[str] = "FaultToleranceMechanism"
    class_model_uri: ClassVar[URIRef] = ISO22989.FaultToleranceMechanism

    id: Union[str, FaultToleranceMechanismId] = None
    name: str = None
    mechanism_type: Optional[str] = None
    coverage_scope: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FaultToleranceMechanismId):
            self.id = FaultToleranceMechanismId(self.id)

        if self.mechanism_type is not None and not isinstance(self.mechanism_type, str):
            self.mechanism_type = str(self.mechanism_type)

        if self.coverage_scope is not None and not isinstance(self.coverage_scope, str):
            self.coverage_scope = str(self.coverage_scope)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NaturalLanguage(AIConcept):
    """
    Natural language treated as an object of processing or generation by an AI system (Clause 9.2).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO22989["NaturalLanguage"]
    class_class_curie: ClassVar[str] = "iso22989:NaturalLanguage"
    class_name: ClassVar[str] = "NaturalLanguage"
    class_model_uri: ClassVar[URIRef] = ISO22989.NaturalLanguage

    id: Union[str, NaturalLanguageId] = None
    name: str = None
    language_code: Optional[str] = None
    script: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NaturalLanguageId):
            self.id = NaturalLanguageId(self.id)

        if self.language_code is not None and not isinstance(self.language_code, str):
            self.language_code = str(self.language_code)

        if self.script is not None and not isinstance(self.script, str):
            self.script = str(self.script)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RiskItem(NamedEntity):
    """
    Risk associated with an AI system, capturing source, potential event, consequence and treatment metadata (Clause
    3.5.11; aligned with ISO/IEC 23894 risk concepts).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO22989["RiskItem"]
    class_class_curie: ClassVar[str] = "iso22989:RiskItem"
    class_name: ClassVar[str] = "RiskItem"
    class_model_uri: ClassVar[URIRef] = ISO22989.RiskItem

    id: Union[str, RiskItemId] = None
    name: str = None
    risk_source: Optional[str] = None
    potential_event: Optional[str] = None
    consequence: Optional[str] = None
    likelihood: Optional[Union[float, ConfidenceScore]] = None
    severity: Optional[str] = None
    mitigation_strategy: Optional[Union[str, list[str]]] = empty_list()
    affected_stakeholders: Optional[Union[Union[str, AIStakeholderRoleId], list[Union[str, AIStakeholderRoleId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RiskItemId):
            self.id = RiskItemId(self.id)

        if self.risk_source is not None and not isinstance(self.risk_source, str):
            self.risk_source = str(self.risk_source)

        if self.potential_event is not None and not isinstance(self.potential_event, str):
            self.potential_event = str(self.potential_event)

        if self.consequence is not None and not isinstance(self.consequence, str):
            self.consequence = str(self.consequence)

        if self.likelihood is not None and not isinstance(self.likelihood, ConfidenceScore):
            self.likelihood = ConfidenceScore(self.likelihood)

        if self.severity is not None and not isinstance(self.severity, str):
            self.severity = str(self.severity)

        if not isinstance(self.mitigation_strategy, list):
            self.mitigation_strategy = [self.mitigation_strategy] if self.mitigation_strategy is not None else []
        self.mitigation_strategy = [v if isinstance(v, str) else str(v) for v in self.mitigation_strategy]

        if not isinstance(self.affected_stakeholders, list):
            self.affected_stakeholders = [self.affected_stakeholders] if self.affected_stakeholders is not None else []
        self.affected_stakeholders = [v if isinstance(v, AIStakeholderRoleId) else AIStakeholderRoleId(v) for v in self.affected_stakeholders]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class InputData(NamedEntity):
    """
    Data presented to an AI system at inference time or during training (Clause 3.2.9).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO22989["InputData"]
    class_class_curie: ClassVar[str] = "iso22989:InputData"
    class_name: ClassVar[str] = "InputData"
    class_model_uri: ClassVar[URIRef] = ISO22989.InputData

    id: Union[str, InputDataId] = None
    name: str = None
    data_source_type: Optional[Union[str, "DataSourceType"]] = None
    data_collection_method: Optional[Union[str, "DataCollectionMethod"]] = None
    modality: Optional[Union[str, "DataModality"]] = None
    consumed_by: Optional[Union[str, AISystemId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, InputDataId):
            self.id = InputDataId(self.id)

        if self.data_source_type is not None and not isinstance(self.data_source_type, DataSourceType):
            self.data_source_type = DataSourceType(self.data_source_type)

        if self.data_collection_method is not None and not isinstance(self.data_collection_method, DataCollectionMethod):
            self.data_collection_method = DataCollectionMethod(self.data_collection_method)

        if self.modality is not None and not isinstance(self.modality, DataModality):
            self.modality = DataModality(self.modality)

        if self.consumed_by is not None and not isinstance(self.consumed_by, AISystemId):
            self.consumed_by = AISystemId(self.consumed_by)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Inference(NamedEntity):
    """
    Act of deriving conclusions, predictions or recommendations from a model or knowledge base (Clause 3.1.17).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO22989["Inference"]
    class_class_curie: ClassVar[str] = "iso22989:Inference"
    class_name: ClassVar[str] = "Inference"
    class_model_uri: ClassVar[URIRef] = ISO22989.Inference

    id: Union[str, InferenceId] = None
    name: str = None
    inference_strategy: Optional[str] = None
    performed_by: Optional[Union[str, InferenceEngineId]] = None
    over_model: Optional[Union[str, AIModelId]] = None
    produced_output: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, InferenceId):
            self.id = InferenceId(self.id)

        if self.inference_strategy is not None and not isinstance(self.inference_strategy, str):
            self.inference_strategy = str(self.inference_strategy)

        if self.performed_by is not None and not isinstance(self.performed_by, InferenceEngineId):
            self.performed_by = InferenceEngineId(self.performed_by)

        if self.over_model is not None and not isinstance(self.over_model, AIModelId):
            self.over_model = AIModelId(self.over_model)

        if self.produced_output is not None and not isinstance(self.produced_output, str):
            self.produced_output = str(self.produced_output)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OECDLifecycleMapping(NamedEntity):
    """
    Informative mapping between an ISO/IEC 22989 life-cycle stage and an OECD life-cycle stage (Annex A).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO22989["OECDLifecycleMapping"]
    class_class_curie: ClassVar[str] = "iso22989:OECDLifecycleMapping"
    class_name: ClassVar[str] = "OECDLifecycleMapping"
    class_model_uri: ClassVar[URIRef] = ISO22989.OECDLifecycleMapping

    id: Union[str, OECDLifecycleMappingId] = None
    name: str = None
    iso_stage: Union[str, "AILifecycleStage"] = None
    oecd_stage: Union[str, "OECDLifecycleStage"] = None
    mapping_notes: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OECDLifecycleMappingId):
            self.id = OECDLifecycleMappingId(self.id)

        if self._is_empty(self.iso_stage):
            self.MissingRequiredField("iso_stage")
        if not isinstance(self.iso_stage, AILifecycleStage):
            self.iso_stage = AILifecycleStage(self.iso_stage)

        if self._is_empty(self.oecd_stage):
            self.MissingRequiredField("oecd_stage")
        if not isinstance(self.oecd_stage, OECDLifecycleStage):
            self.oecd_stage = OECDLifecycleStage(self.oecd_stage)

        if self.mapping_notes is not None and not isinstance(self.mapping_notes, str):
            self.mapping_notes = str(self.mapping_notes)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Organization(NamedEntity):
    """
    Organisation that establishes and operates an AI management system; Annex SL harmonised anchor shared across ISO
    management-system standards (ISO/IEC 42001, ISO/IEC 27001).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO22989["Organization"]
    class_class_curie: ClassVar[str] = "iso22989:Organization"
    class_name: ClassVar[str] = "Organization"
    class_model_uri: ClassVar[URIRef] = ISO22989.Organization

    id: Union[str, OrganizationId] = None
    name: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OrganizationId):
            self.id = OrganizationId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class InterestedParty(NamedEntity):
    """
    Person or organisation that can affect, be affected by, or perceive itself to be affected by a decision or
    activity; Annex SL harmonised stakeholder anchor shared across ISO management-system standards.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO22989["InterestedParty"]
    class_class_curie: ClassVar[str] = "iso22989:InterestedParty"
    class_name: ClassVar[str] = "InterestedParty"
    class_model_uri: ClassVar[URIRef] = ISO22989.InterestedParty

    id: Union[str, InterestedPartyId] = None
    name: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, InterestedPartyId):
            self.id = InterestedPartyId(self.id)

        super().__post_init__(**kwargs)


# Enumerations
class AISystemType(EnumDefinitionImpl):
    """
    High-level capability classification of an AI system, from narrow (single-task) through general (broad
    cross-domain) systems and the historical strong/weak AI distinction in Clause 5.2.
    """
    narrow_ai = PermissibleValue(
        text="narrow_ai",
        description="AI system designed and deployed for a single, well-bounded task.")
    general_ai = PermissibleValue(
        text="general_ai",
        description="Hypothetical AI system able to perform any cognitive task a human can perform.")
    weak_ai = PermissibleValue(
        text="weak_ai",
        description="Historical term largely overlapping with narrow AI; emphasises tool-like behaviour.")
    strong_ai = PermissibleValue(
        text="strong_ai",
        description="Historical term largely overlapping with general AI; emphasises human-equivalent cognition.")

    _defn = EnumDefinition(
        name="AISystemType",
        description="""High-level capability classification of an AI system, from narrow (single-task) through general (broad cross-domain) systems and the historical strong/weak AI distinction in Clause 5.2.""",
    )

class SymbolicApproach(EnumDefinitionImpl):
    """
    The symbolic vs subsymbolic axis used in Clause 5.9 to classify AI reasoning techniques.
    """
    symbolic = PermissibleValue(
        text="symbolic",
        description="Approaches that manipulate explicit symbolic representations (rules, logic, knowledge graphs).")
    subsymbolic = PermissibleValue(
        text="subsymbolic",
        description="""Approaches that operate on distributed numeric representations (neural networks, statistical models).""")
    hybrid = PermissibleValue(
        text="hybrid",
        description="Approaches that combine symbolic and subsymbolic techniques (neuro-symbolic AI).")

    _defn = EnumDefinition(
        name="SymbolicApproach",
        description="The symbolic vs subsymbolic axis used in Clause 5.9 to classify AI reasoning techniques.",
    )

class MachineLearningParadigm(EnumDefinitionImpl):
    """
    Top-level machine-learning paradigms enumerated in Clause 5.11.
    """
    supervised = PermissibleValue(
        text="supervised",
        description="Learning from labelled input-output examples.")
    unsupervised = PermissibleValue(
        text="unsupervised",
        description="""Learning structure from unlabelled data (clustering, density estimation, dimensionality reduction).""")
    semi_supervised = PermissibleValue(
        text="semi_supervised",
        description="Learning from a mixture of labelled and unlabelled data.")
    reinforcement = PermissibleValue(
        text="reinforcement",
        description="Learning policies by interaction with an environment that issues rewards.")
    transfer = PermissibleValue(
        text="transfer",
        description="Reusing knowledge learned on one task to accelerate learning on a related task.")
    self_supervised = PermissibleValue(
        text="self_supervised",
        description="Learning representations from data using auxiliary tasks derived from the data itself.")

    _defn = EnumDefinition(
        name="MachineLearningParadigm",
        description="Top-level machine-learning paradigms enumerated in Clause 5.11.",
    )

class MLAlgorithmFamily(EnumDefinitionImpl):
    """
    Example machine-learning algorithm families enumerated in Clause 5.12.
    """
    neural_network = PermissibleValue(
        text="neural_network",
        description="Networks of interconnected processing units (artificial neurons) trained by gradient methods.")
    bayesian_network = PermissibleValue(
        text="bayesian_network",
        description="Probabilistic graphical models encoding conditional dependencies between variables.")
    decision_tree = PermissibleValue(
        text="decision_tree",
        description="Tree-structured models splitting the input space on feature thresholds.")
    support_vector_machine = PermissibleValue(
        text="support_vector_machine",
        description="Margin-maximising classifiers operating in (possibly kernelised) feature spaces.")
    genetic_algorithm = PermissibleValue(
        text="genetic_algorithm",
        description="Population-based optimisation inspired by biological evolution (Clause 5.8).")

    _defn = EnumDefinition(
        name="MLAlgorithmFamily",
        description="Example machine-learning algorithm families enumerated in Clause 5.12.",
    )

class AutonomyLevel(EnumDefinitionImpl):
    """
    Degree of system autonomy as discussed in Clause 5.13 (autonomy, heteronomy and automation). Encodes both the
    qualitative axis (autonomous / heteronomous / automated) and the six-level operational autonomy gradient widely
    used by ISO/IEC JTC 1/SC 42 work products.
    """
    automated = PermissibleValue(
        text="automated",
        description="System executes a fixed predefined behaviour without runtime adaptation.")
    heteronomous = PermissibleValue(
        text="heteronomous",
        description="System operates under external direction or supervision.")
    autonomous = PermissibleValue(
        text="autonomous",
        description="System pursues goals using its own decision-making within a defined operating envelope.")
    level_0_no_automation = PermissibleValue(
        text="level_0_no_automation",
        description="Human performs all tasks; no autonomous functionality (Clause 5.13).")
    level_1_assistance = PermissibleValue(
        text="level_1_assistance",
        description="System assists the operator with one or more specific tasks.")
    level_2_partial_automation = PermissibleValue(
        text="level_2_partial_automation",
        description="System performs some sub-functions; operator retains overall control.")
    level_3_conditional_automation = PermissibleValue(
        text="level_3_conditional_automation",
        description="System handles defined tasks but expects the operator to intervene when requested.")
    level_4_high_automation = PermissibleValue(
        text="level_4_high_automation",
        description="System performs the mission within a defined operating envelope without operator intervention.")
    level_5_full_automation = PermissibleValue(
        text="level_5_full_automation",
        description="System performs the entire mission autonomously across all conditions.")

    _defn = EnumDefinition(
        name="AutonomyLevel",
        description="""Degree of system autonomy as discussed in Clause 5.13 (autonomy, heteronomy and automation). Encodes both the qualitative axis (autonomous / heteronomous / automated) and the six-level operational autonomy gradient widely used by ISO/IEC JTC 1/SC 42 work products.""",
    )

class TrustworthinessPropertyType(EnumDefinitionImpl):
    """
    Properties contributing to AI trustworthiness, enumerated in Clause 5.15 (robustness, reliability, resilience,
    controllability, explainability, predictability, transparency, fairness and bias-related properties).
    """
    robustness = PermissibleValue(
        text="robustness",
        description="Ability to maintain performance under varied or adversarial conditions.")
    reliability = PermissibleValue(
        text="reliability",
        description="Consistent intended behaviour over time under stated conditions.")
    resilience = PermissibleValue(
        text="resilience",
        description="Ability to recover acceptable behaviour after disruption or failure.")
    controllability = PermissibleValue(
        text="controllability",
        description="Property of allowing authorised humans to intervene in system behaviour.")
    explainability = PermissibleValue(
        text="explainability",
        description="""Property of producing explanations of system behaviour that are intelligible to relevant audiences.""")
    predictability = PermissibleValue(
        text="predictability",
        description="Property of behaviour being anticipatable given known inputs and state.")
    transparency = PermissibleValue(
        text="transparency",
        description="Property of disclosing meaningful information about the system to interested parties.")
    fairness = PermissibleValue(
        text="fairness",
        description="Property of avoiding inappropriate or harmful discrimination across groups.")
    bias_mitigation = PermissibleValue(
        text="bias_mitigation",
        description="Property of identifying and reducing unwanted bias in data, models or outcomes.")
    accountability = PermissibleValue(
        text="accountability",
        description="Property of having identifiable parties answerable for system behaviour and outcomes.")
    privacy = PermissibleValue(
        text="privacy",
        description="Property of respecting personal data and individual privacy expectations.",
        meaning=NIST_AI_RMF_COMMON["TrustworthinessCharacteristicEnum#PRIVACY_ENHANCED"])
    safety = PermissibleValue(
        text="safety",
        description="Property of not causing unacceptable risk of harm to people, property or environment.",
        meaning=NIST_AI_RMF_COMMON["TrustworthinessCharacteristicEnum#SAFE"])
    availability = PermissibleValue(
        text="availability",
        description="""Property of being accessible and usable on demand by authorised entities (Clause 5.15.3 context).""")
    integrity = PermissibleValue(
        text="integrity",
        description="""Property of safeguarding accuracy and completeness of data, models and outputs (Clause 5.15 Note).""")
    authenticity = PermissibleValue(
        text="authenticity",
        description="""Property of being able to verify the origin and identity of inputs, models and outputs (Clause 5.15 Note).""")
    security = PermissibleValue(
        text="security",
        description="""Property of preserving confidentiality, integrity and availability of the AI system and its data (Clause 5.15 context).""")
    usability = PermissibleValue(
        text="usability",
        description="""Property of being effectively, efficiently and satisfactorily usable by the intended users (Clause 5.15 Note).""")
    quality = PermissibleValue(
        text="quality",
        description="""Aggregate property reflecting how well the AI system meets stated and implied needs (Clause 5.15 Note).""")
    fault_tolerance = PermissibleValue(
        text="fault_tolerance",
        description="""Property of continuing to operate correctly in the presence of component faults (Clause 5.15.4 context).""")

    _defn = EnumDefinition(
        name="TrustworthinessPropertyType",
        description="""Properties contributing to AI trustworthiness, enumerated in Clause 5.15 (robustness, reliability, resilience, controllability, explainability, predictability, transparency, fairness and bias-related properties).""",
    )

class BiasType(EnumDefinitionImpl):
    """
    Categories of bias relevant to AI systems as discussed in Clause 5.15.9 and ISO/IEC TR 24027.
    """
    data_bias = PermissibleValue(
        text="data_bias",
        description="Bias introduced through sampling, labelling or representation of training data.")
    algorithmic_bias = PermissibleValue(
        text="algorithmic_bias",
        description="Bias introduced through model or algorithm choice and parameterisation.")
    societal_bias = PermissibleValue(
        text="societal_bias",
        description="Bias reflecting structural inequalities in the data-generating environment.")
    cognitive_bias = PermissibleValue(
        text="cognitive_bias",
        description="Bias introduced through human cognition during design, labelling or interpretation.")
    automation_bias = PermissibleValue(
        text="automation_bias",
        description="Tendency of users to over-rely on automated outputs.")

    _defn = EnumDefinition(
        name="BiasType",
        description="Categories of bias relevant to AI systems as discussed in Clause 5.15.9 and ISO/IEC TR 24027.",
    )

class AILifecycleStage(EnumDefinitionImpl):
    """
    AI system life-cycle stages identified in Clause 6.2.
    """
    inception = PermissibleValue(
        text="inception",
        description="Identification of need, opportunity and high-level objectives for the AI system.")
    design_and_development = PermissibleValue(
        text="design_and_development",
        description="Architecture, model selection, data preparation, training and integration activities.")
    verification_and_validation = PermissibleValue(
        text="verification_and_validation",
        description="Evidence-gathering activities establishing that the system meets specified requirements.")
    deployment = PermissibleValue(
        text="deployment",
        description="Release of the AI system into its operational environment.",
        meaning=NIST_AI_600_1["GaiLifecycleStageEnum#DEPLOYMENT"])
    operation_and_monitoring = PermissibleValue(
        text="operation_and_monitoring",
        description="Routine use of the AI system with ongoing observation of behaviour and performance.")
    continuous_validation = PermissibleValue(
        text="continuous_validation",
        description="Ongoing checks that the system continues to meet validation criteria during operation.")
    re_evaluation = PermissibleValue(
        text="re_evaluation",
        description="""Periodic or event-triggered reassessment of the system, often leading to retraining or redesign.""")
    retirement = PermissibleValue(
        text="retirement",
        description="Decommissioning of the AI system and management of residual data and artefacts.",
        meaning=NIST_AI_600_1["GaiLifecycleStageEnum#DECOMMISSIONING"])

    _defn = EnumDefinition(
        name="AILifecycleStage",
        description="AI system life-cycle stages identified in Clause 6.2.",
    )

class AIFunctionalComponent(EnumDefinitionImpl):
    """
    Functional building blocks of an AI system as introduced in Clause 7.
    """
    data_and_information = PermissibleValue(
        text="data_and_information",
        description="Data acquisition, storage and information management functions.")
    knowledge_and_learning = PermissibleValue(
        text="knowledge_and_learning",
        description="Functions producing or maintaining knowledge representations and learned models.")
    prediction = PermissibleValue(
        text="prediction",
        description="Functions producing predictions from inputs using a trained model or knowledge base.")
    decision = PermissibleValue(
        text="decision",
        description="Functions selecting a course of action based on predictions and constraints.")
    action = PermissibleValue(
        text="action",
        description="Functions enacting decisions on the environment or downstream systems.")

    _defn = EnumDefinition(
        name="AIFunctionalComponent",
        description="Functional building blocks of an AI system as introduced in Clause 7.",
    )

class AIStakeholderRoleType(EnumDefinitionImpl):
    """
    AI stakeholder roles enumerated in Clause 5.19.
    """
    ai_provider = PermissibleValue(
        text="ai_provider",
        description="Party that makes an AI system available to AI customers.")
    ai_producer = PermissibleValue(
        text="ai_producer",
        description="Party that designs, develops or assembles AI systems or components.")
    ai_customer = PermissibleValue(
        text="ai_customer",
        description="Party that uses an AI system or a service backed by an AI system.")
    ai_partner = PermissibleValue(
        text="ai_partner",
        description="""Party providing services that support the AI life cycle (data brokers, integrators, evaluators).""")
    ai_subject = PermissibleValue(
        text="ai_subject",
        description="Person or group whose data is used by, or who is otherwise affected by, the AI system.")
    relevant_authority = PermissibleValue(
        text="relevant_authority",
        description="Body with regulatory, supervisory or standards-setting responsibility for AI.")

    _defn = EnumDefinition(
        name="AIStakeholderRoleType",
        description="AI stakeholder roles enumerated in Clause 5.19.",
    )

class EngineeringApproach(EnumDefinitionImpl):
    """
    Non-learning engineering approaches contributing to AI, from Clause 8.5.
    """
    expert_system = PermissibleValue(
        text="expert_system",
        description="Rule-based system encoding domain expertise (Clause 8.5.2).")
    logic_programming = PermissibleValue(
        text="logic_programming",
        description="Programming paradigm based on formal logic (Clause 8.5.3).")
    knowledge_graph = PermissibleValue(
        text="knowledge_graph",
        description="Graph-structured knowledge representation used for reasoning and retrieval.")
    constraint_satisfaction = PermissibleValue(
        text="constraint_satisfaction",
        description="Solving problems by satisfying a set of declared constraints.")

    _defn = EnumDefinition(
        name="EngineeringApproach",
        description="Non-learning engineering approaches contributing to AI, from Clause 8.5.",
    )

class ComputingResourceType(EnumDefinitionImpl):
    """
    Categories of computing resource used by AI systems, drawn from Clauses 8.6 (cloud and edge computing) and 8.7
    (resource pools).
    """
    cloud = PermissibleValue(
        text="cloud",
        description="Centralised, elastically provisioned computing resources accessed over a network.")
    edge = PermissibleValue(
        text="edge",
        description="Computing resources located close to data sources or end users.")
    on_premises = PermissibleValue(
        text="on_premises",
        description="Computing resources owned and operated within the organisation's own facilities.")
    cpu = PermissibleValue(
        text="cpu",
        description="General-purpose central-processing-unit compute capacity.")
    gpu = PermissibleValue(
        text="gpu",
        description="""Graphics-processing-unit compute capacity, commonly used for neural network training and inference.""")
    tpu = PermissibleValue(
        text="tpu",
        description="Tensor-processing-unit or similar accelerator specialised for ML workloads.")
    asic = PermissibleValue(
        text="asic",
        description="Application-specific integrated circuit designed for a fixed AI workload (Clause 8.7.2).")
    fpga = PermissibleValue(
        text="fpga",
        description="Field-programmable gate array offering reconfigurable hardware acceleration.")
    npu = PermissibleValue(
        text="npu",
        description="Neural-network processing unit specialised for neural-network inference and training.")
    dsp = PermissibleValue(
        text="dsp",
        description="Digital signal processor used to accelerate signal-processing workloads.")

    _defn = EnumDefinition(
        name="ComputingResourceType",
        description="""Categories of computing resource used by AI systems, drawn from Clauses 8.6 (cloud and edge computing) and 8.7 (resource pools).""",
    )

class DataModality(EnumDefinitionImpl):
    """
    Modalities of input data handled by AI systems, drawn from the data, NLP and CV terminology sections (Clauses 3.2,
    3.6, 3.7).
    """
    structured = PermissibleValue(
        text="structured",
        description="Tabular or relational data with an explicit schema.")
    semi_structured = PermissibleValue(
        text="semi_structured",
        description="Data with self-describing structure such as JSON, XML or graph formats.")
    unstructured = PermissibleValue(
        text="unstructured",
        description="Data without an explicit schema (free text, images, audio, video).")
    text = PermissibleValue(
        text="text",
        description="Natural-language text data.")
    image = PermissibleValue(
        text="image",
        description="Two-dimensional visual data.")
    video = PermissibleValue(
        text="video",
        description="Temporal sequences of visual frames.")
    audio = PermissibleValue(
        text="audio",
        description="Acoustic signal data.")
    sensor = PermissibleValue(
        text="sensor",
        description="Telemetry or measurement data from physical sensors.")
    time_series = PermissibleValue(
        text="time_series",
        description="Ordered observations indexed by time.")
    graph = PermissibleValue(
        text="graph",
        description="Data represented as nodes and edges.")

    _defn = EnumDefinition(
        name="DataModality",
        description="""Modalities of input data handled by AI systems, drawn from the data, NLP and CV terminology sections (Clauses 3.2, 3.6, 3.7).""",
    )

class DatasetRole(EnumDefinitionImpl):
    """
    Role a dataset plays in a machine-learning workflow, drawn from Clauses 5.11.6–5.11.8.
    """
    training = PermissibleValue(
        text="training",
        description="Dataset used to fit model parameters.")
    validation = PermissibleValue(
        text="validation",
        description="Dataset used to tune hyperparameters and select among candidate models.")
    test = PermissibleValue(
        text="test",
        description="Dataset used for a final unbiased estimate of model performance.")
    production = PermissibleValue(
        text="production",
        description="Live data observed during operational deployment.")
    reference = PermissibleValue(
        text="reference",
        description="Curated dataset used as a benchmark across experiments.")

    _defn = EnumDefinition(
        name="DatasetRole",
        description="Role a dataset plays in a machine-learning workflow, drawn from Clauses 5.11.6–5.11.8.",
    )

class NLPComponentType(EnumDefinitionImpl):
    """
    Components of a natural-language-processing pipeline as enumerated in Clauses 3.6 and 9.2.
    """
    tokenisation = PermissibleValue(
        text="tokenisation",
        description="Segmenting text into tokens such as words or subwords.")
    lemmatisation = PermissibleValue(
        text="lemmatisation",
        description="Reducing tokens to their canonical dictionary form.")
    part_of_speech_tagging = PermissibleValue(
        text="part_of_speech_tagging",
        description="Assigning grammatical category labels to tokens.")
    syntactic_parsing = PermissibleValue(
        text="syntactic_parsing",
        description="Producing syntactic structure for sentences.")
    semantic_analysis = PermissibleValue(
        text="semantic_analysis",
        description="Deriving meaning representations from text.")
    named_entity_recognition = PermissibleValue(
        text="named_entity_recognition",
        description="Identifying and classifying named entities in text.")
    sentiment_analysis = PermissibleValue(
        text="sentiment_analysis",
        description="Estimating subjective polarity or affect in text.")
    machine_translation = PermissibleValue(
        text="machine_translation",
        description="Automatically translating text between natural languages.")
    speech_recognition = PermissibleValue(
        text="speech_recognition",
        description="Converting acoustic speech signals into text.")
    speech_synthesis = PermissibleValue(
        text="speech_synthesis",
        description="Generating speech audio from text.")
    natural_language_understanding = PermissibleValue(
        text="natural_language_understanding",
        description="Deriving structured meaning, intent or entities from natural-language input (Clause 9.2).")
    natural_language_generation = PermissibleValue(
        text="natural_language_generation",
        description="Producing natural-language output from structured inputs (Clause 9.2).")
    automatic_summarization = PermissibleValue(
        text="automatic_summarization",
        description="Producing condensed summaries of longer text (Clause 3.6.1).")
    dialogue_management = PermissibleValue(
        text="dialogue_management",
        description="Controlling multi-turn conversational interaction (Clause 9.2.2).")
    information_retrieval = PermissibleValue(
        text="information_retrieval",
        description="Finding relevant documents or passages in a collection in response to a query.")
    question_answering = PermissibleValue(
        text="question_answering",
        description="Producing direct answers to natural-language questions.")
    relationship_extraction = PermissibleValue(
        text="relationship_extraction",
        description="Identifying typed relationships between entities mentioned in text.")
    emotion_recognition = PermissibleValue(
        text="emotion_recognition",
        description="Detecting affective or emotional state expressed in text or speech.")
    optical_character_recognition = PermissibleValue(
        text="optical_character_recognition",
        description="Converting images of printed or handwritten text into machine-readable text (Clause 3.6.12).")
    coreference_resolution = PermissibleValue(
        text="coreference_resolution",
        description="Linking mentions in text that refer to the same entity.")

    _defn = EnumDefinition(
        name="NLPComponentType",
        description="Components of a natural-language-processing pipeline as enumerated in Clauses 3.6 and 9.2.",
    )

class ComputerVisionTask(EnumDefinitionImpl):
    """
    Computer-vision tasks drawn from Clauses 3.7 and 9.1.
    """
    image_classification = PermissibleValue(
        text="image_classification",
        description="Assigning a class label to an image.")
    object_detection = PermissibleValue(
        text="object_detection",
        description="Localising and classifying objects within an image.")
    semantic_segmentation = PermissibleValue(
        text="semantic_segmentation",
        description="Assigning a class label to each pixel in an image.")
    instance_segmentation = PermissibleValue(
        text="instance_segmentation",
        description="Assigning labels to pixels grouped by individual object instance.")
    image_recognition = PermissibleValue(
        text="image_recognition",
        description="General recognition of image content, including faces and scenes.")
    pose_estimation = PermissibleValue(
        text="pose_estimation",
        description="Estimating the spatial pose of objects or persons.")
    optical_character_recognition = PermissibleValue(
        text="optical_character_recognition",
        description="Extracting machine-readable text from images of printed or handwritten content.")
    face_recognition = PermissibleValue(
        text="face_recognition",
        description="Identifying or verifying persons from facial images (Clause 3.7.2).")
    scene_recognition = PermissibleValue(
        text="scene_recognition",
        description="Classifying the type of scene or environment depicted in an image.")
    motion_tracking = PermissibleValue(
        text="motion_tracking",
        description="Following the position of objects across successive frames in video.")
    visual_anomaly_detection = PermissibleValue(
        text="visual_anomaly_detection",
        description="Identifying visual patterns that deviate from expected behaviour.")
    three_d_reconstruction = PermissibleValue(
        text="three_d_reconstruction",
        description="Recovering three-dimensional structure from one or more images.")
    action_recognition = PermissibleValue(
        text="action_recognition",
        description="Recognising discrete actions performed in video.")
    activity_recognition = PermissibleValue(
        text="activity_recognition",
        description="Recognising higher-level activities composed of multiple actions in video.")

    _defn = EnumDefinition(
        name="ComputerVisionTask",
        description="Computer-vision tasks drawn from Clauses 3.7 and 9.1.",
    )

class AIField(EnumDefinitionImpl):
    """
    Sub-fields of AI referenced in Clause 9.
    """
    computer_vision = PermissibleValue(
        text="computer_vision",
        description="AI sub-field concerned with interpreting visual information.")
    natural_language_processing = PermissibleValue(
        text="natural_language_processing",
        description="AI sub-field concerned with processing and generating human language.")
    data_mining = PermissibleValue(
        text="data_mining",
        description="Extraction of patterns and knowledge from large data sets.")
    planning = PermissibleValue(
        text="planning",
        description="AI sub-field concerned with sequencing actions to achieve goals.")
    robotics = PermissibleValue(
        text="robotics",
        description="AI sub-field concerned with embodied autonomous systems.")
    knowledge_representation_and_reasoning = PermissibleValue(
        text="knowledge_representation_and_reasoning",
        description="AI sub-field concerned with explicit representation and inference over knowledge.")
    speech_processing = PermissibleValue(
        text="speech_processing",
        description="AI sub-field concerned with processing and producing speech signals.")
    multi_agent_systems = PermissibleValue(
        text="multi_agent_systems",
        description="AI sub-field concerned with coordination and interaction among multiple agents.")

    _defn = EnumDefinition(
        name="AIField",
        description="Sub-fields of AI referenced in Clause 9.",
    )

class AIApplicationDomain(EnumDefinitionImpl):
    """
    Example AI application domains presented in Clause 10.
    """
    fraud_detection = PermissibleValue(
        text="fraud_detection",
        description="Identification of fraudulent transactions or behaviours (Clause 10.2).")
    automated_vehicles = PermissibleValue(
        text="automated_vehicles",
        description="AI capabilities used in self-driving or driver-assistance systems (Clause 10.3).")
    predictive_maintenance = PermissibleValue(
        text="predictive_maintenance",
        description="Anticipating equipment failures from sensor data (Clause 10.4).")
    recommendation = PermissibleValue(
        text="recommendation",
        description="Personalised recommendation of items or actions.")
    medical_diagnosis = PermissibleValue(
        text="medical_diagnosis",
        description="AI-assisted diagnostic decision support in healthcare.")
    content_generation = PermissibleValue(
        text="content_generation",
        description="AI-generated text, images, audio or other media.")
    agriculture = PermissibleValue(
        text="agriculture",
        description="AI applications in farming, crop and livestock management (Clause 10.1).")
    automotive = PermissibleValue(
        text="automotive",
        description="AI applications in vehicle design, manufacture and in-vehicle services (Clause 10.1).")
    banking_and_finance = PermissibleValue(
        text="banking_and_finance",
        description="AI applications in banking, finance and capital markets (Clause 10.1).")
    defense_and_security = PermissibleValue(
        text="defense_and_security",
        description="AI applications in defence and physical security (Clause 10.1).")
    education = PermissibleValue(
        text="education",
        description="AI applications in learning, teaching and assessment (Clause 10.1).")
    energy_and_utilities = PermissibleValue(
        text="energy_and_utilities",
        description="AI applications in energy generation, distribution and consumption (Clause 10.1).")
    healthcare = PermissibleValue(
        text="healthcare",
        description="AI applications in clinical care and health management (Clause 10.1).")
    legal_services = PermissibleValue(
        text="legal_services",
        description="AI applications in legal research, contracting and compliance (Clause 10.1).")
    manufacturing = PermissibleValue(
        text="manufacturing",
        description="AI applications in industrial production (Clause 10.1).")
    media_and_entertainment = PermissibleValue(
        text="media_and_entertainment",
        description="AI applications in media production, distribution and recommendation (Clause 10.1).")
    mixed_reality = PermissibleValue(
        text="mixed_reality",
        description="AI applications in virtual, augmented and mixed reality (Clause 10.1).")
    public_sector = PermissibleValue(
        text="public_sector",
        description="AI applications in government and public administration (Clause 10.1).")
    retail = PermissibleValue(
        text="retail",
        description="AI applications in retail and e-commerce (Clause 10.1).")
    space = PermissibleValue(
        text="space",
        description="AI applications in space exploration and operations (Clause 10.1).")
    telecommunications = PermissibleValue(
        text="telecommunications",
        description="AI applications in telecommunications networks and services (Clause 10.1).")

    _defn = EnumDefinition(
        name="AIApplicationDomain",
        description="Example AI application domains presented in Clause 10.",
    )

class OECDLifecycleStage(EnumDefinitionImpl):
    """
    OECD AI system life-cycle stages used in the informative mapping of Annex A.
    """
    plan_and_design = PermissibleValue(
        text="plan_and_design",
        description="OECD stage covering planning and design activities.",
        meaning=NIST_AI_RMF["AiLifecycleStageEnum#PLAN_AND_DESIGN"])
    collect_and_process_data = PermissibleValue(
        text="collect_and_process_data",
        description="OECD stage covering data collection and processing.",
        meaning=NIST_AI_RMF["AiLifecycleStageEnum#COLLECT_AND_PROCESS_DATA"])
    build_and_use_model = PermissibleValue(
        text="build_and_use_model",
        description="OECD stage covering model building and inference.",
        meaning=NIST_AI_RMF["AiLifecycleStageEnum#BUILD_AND_USE_MODEL"])
    verify_and_validate = PermissibleValue(
        text="verify_and_validate",
        description="OECD stage covering verification and validation.",
        meaning=NIST_AI_RMF["AiLifecycleStageEnum#VERIFY_AND_VALIDATE"])
    deploy = PermissibleValue(
        text="deploy",
        description="OECD stage covering deployment of the AI system.")
    operate_and_monitor = PermissibleValue(
        text="operate_and_monitor",
        description="OECD stage covering operation and monitoring of the AI system.",
        meaning=NIST_AI_RMF["AiLifecycleStageEnum#OPERATE_AND_MONITOR"])

    _defn = EnumDefinition(
        name="OECDLifecycleStage",
        description="OECD AI system life-cycle stages used in the informative mapping of Annex A.",
    )

class JurisdictionalIssueType(EnumDefinitionImpl):
    """
    Categories of jurisdictional issue surfaced in Clause 5.17.
    """
    data_residency = PermissibleValue(
        text="data_residency",
        description="Constraints on the geographical location of stored or processed data.")
    cross_border_transfer = PermissibleValue(
        text="cross_border_transfer",
        description="Constraints on movement of data or AI outputs across legal jurisdictions.")
    liability = PermissibleValue(
        text="liability",
        description="Allocation of legal responsibility for AI-system actions and outcomes.")
    regulatory_compliance = PermissibleValue(
        text="regulatory_compliance",
        description="Conformity with applicable AI-specific or sector-specific regulations.")
    intellectual_property = PermissibleValue(
        text="intellectual_property",
        description="Ownership and licensing of training data, models and outputs.")

    _defn = EnumDefinition(
        name="JurisdictionalIssueType",
        description="Categories of jurisdictional issue surfaced in Clause 5.17.",
    )

class SocietalImpactCategory(EnumDefinitionImpl):
    """
    Categories of societal impact discussed in Clause 5.18.
    """
    employment = PermissibleValue(
        text="employment",
        description="Effects on labour markets and the nature of work.")
    human_rights = PermissibleValue(
        text="human_rights",
        description="Effects on the exercise of fundamental human rights.")
    environment = PermissibleValue(
        text="environment",
        description="Environmental footprint of AI development and deployment.")
    democratic_processes = PermissibleValue(
        text="democratic_processes",
        description="Effects on political discourse, elections and civic participation.")
    digital_divide = PermissibleValue(
        text="digital_divide",
        description="Differential access to and impact of AI systems across populations.")

    _defn = EnumDefinition(
        name="SocietalImpactCategory",
        description="Categories of societal impact discussed in Clause 5.18.",
    )

class NeuralNetworkArchitecture(EnumDefinitionImpl):
    """
    Architectural families of neural networks enumerated across Clause 3.4 and Clause 5.12.1.
    """
    feed_forward = PermissibleValue(
        text="feed_forward",
        description="Feed-forward neural network with unidirectional information flow (Clause 3.4.6).")
    recurrent = PermissibleValue(
        text="recurrent",
        description="Recurrent neural network with feedback connections (Clause 3.4.10).")
    long_short_term_memory = PermissibleValue(
        text="long_short_term_memory",
        description="LSTM recurrent architecture mitigating short memory in plain RNNs (Clause 3.4.7).")
    gated_recurrent_unit = PermissibleValue(
        text="gated_recurrent_unit",
        description="GRU recurrent architecture, a simplified gating variant of LSTM.")
    convolutional = PermissibleValue(
        text="convolutional",
        description="Convolutional neural network using local receptive fields (Clause 3.4.2).")
    transformer = PermissibleValue(
        text="transformer",
        description="Attention-based architecture used for sequence modelling.")
    autoencoder = PermissibleValue(
        text="autoencoder",
        description="Encoder-decoder architecture trained to reconstruct inputs for representation learning.")
    generative_adversarial = PermissibleValue(
        text="generative_adversarial",
        description="Adversarial pairing of generator and discriminator networks.")
    deep = PermissibleValue(
        text="deep",
        description="Neural network with many hidden layers (deep learning, Clause 3.4.4).")

    _defn = EnumDefinition(
        name="NeuralNetworkArchitecture",
        description="Architectural families of neural networks enumerated across Clause 3.4 and Clause 5.12.1.",
    )

class NeuralNetworkPhenomenon(EnumDefinitionImpl):
    """
    Training-time phenomena that affect neural-network learning, drawn from Clause 3.4.
    """
    vanishing_gradient = PermissibleValue(
        text="vanishing_gradient",
        description="Gradient signal shrinks across layers during back-propagation, slowing learning.")
    exploding_gradient = PermissibleValue(
        text="exploding_gradient",
        description="Gradient signal grows without bound across layers during back-propagation (Clause 3.4.5).")
    catastrophic_forgetting = PermissibleValue(
        text="catastrophic_forgetting",
        description="Previously learned knowledge is lost when the network is retrained on new data.")
    overfitting = PermissibleValue(
        text="overfitting",
        description="Model fits training data idiosyncrasies and fails to generalise.")
    underfitting = PermissibleValue(
        text="underfitting",
        description="Model lacks capacity or training to capture the underlying signal.")

    _defn = EnumDefinition(
        name="NeuralNetworkPhenomenon",
        description="Training-time phenomena that affect neural-network learning, drawn from Clause 3.4.",
    )

class ActivationFunctionType(EnumDefinitionImpl):
    """
    Common activation functions used in neural networks (Clause 3.4.1).
    """
    sigmoid = PermissibleValue(
        text="sigmoid",
        description="Logistic sigmoid activation.")
    tanh = PermissibleValue(
        text="tanh",
        description="Hyperbolic tangent activation.")
    relu = PermissibleValue(
        text="relu",
        description="Rectified linear unit activation.")
    leaky_relu = PermissibleValue(
        text="leaky_relu",
        description="Rectified linear unit with non-zero gradient below zero.")
    softmax = PermissibleValue(
        text="softmax",
        description="Softmax activation producing a probability distribution.")
    linear = PermissibleValue(
        text="linear",
        description="Identity / linear activation.")
    other = PermissibleValue(
        text="other",
        description="Activation function not enumerated explicitly.")

    _defn = EnumDefinition(
        name="ActivationFunctionType",
        description="Common activation functions used in neural networks (Clause 3.4.1).",
    )

class AgentArchitectureType(EnumDefinitionImpl):
    """
    Agent architectures discussed in Clause 5.3 (agent paradigm).
    """
    reflex_agent = PermissibleValue(
        text="reflex_agent",
        description="Agent that maps current percepts directly to actions.")
    model_based_agent = PermissibleValue(
        text="model_based_agent",
        description="Agent that maintains an internal model of the environment to guide action.")
    goal_based_agent = PermissibleValue(
        text="goal_based_agent",
        description="Agent that selects actions to achieve explicit goals.")
    utility_based_agent = PermissibleValue(
        text="utility_based_agent",
        description="Agent that selects actions to maximise an expected utility function.")
    learning_agent = PermissibleValue(
        text="learning_agent",
        description="Agent that improves its behaviour through experience.")
    multi_agent = PermissibleValue(
        text="multi_agent",
        description="Agent operating jointly with other agents in a shared environment.")

    _defn = EnumDefinition(
        name="AgentArchitectureType",
        description="Agent architectures discussed in Clause 5.3 (agent paradigm).",
    )

class KnowledgeType(EnumDefinitionImpl):
    """
    Types of knowledge distinguished in Clause 3.1 and Clause 5.4 (declarative versus procedural knowledge, etc.).
    """
    declarative = PermissibleValue(
        text="declarative",
        description="Knowledge of facts and relationships (Clause 3.1.12).")
    procedural = PermissibleValue(
        text="procedural",
        description="Knowledge of how to perform tasks (Clause 3.1.28).")
    tacit = PermissibleValue(
        text="tacit",
        description="Implicit, experience-based knowledge that is hard to articulate.")
    common_sense = PermissibleValue(
        text="common_sense",
        description="Background knowledge expected to be shared by typical humans.")
    domain_specific = PermissibleValue(
        text="domain_specific",
        description="Knowledge specific to a particular application domain.")

    _defn = EnumDefinition(
        name="KnowledgeType",
        description="""Types of knowledge distinguished in Clause 3.1 and Clause 5.4 (declarative versus procedural knowledge, etc.).""",
    )

class DataProcessType(EnumDefinitionImpl):
    """
    Data-handling processes enumerated in Clause 5.10 and Clause 3.2 (data acquisition, annotation, preparation,
    quality checking, sampling, augmentation, drift and poisoning handling, etc.).
    """
    data_acquisition = PermissibleValue(
        text="data_acquisition",
        description="Collecting data from one or more sources.")
    exploratory_data_analysis = PermissibleValue(
        text="exploratory_data_analysis",
        description="Initial profiling of a dataset to understand its characteristics (Clause 3.2.6).")
    data_annotation = PermissibleValue(
        text="data_annotation",
        description="Adding labels or other metadata to data items (Clause 3.2.1).")
    data_labeling = PermissibleValue(
        text="data_labeling",
        description="Assigning target labels to records for supervised learning.")
    data_preparation = PermissibleValue(
        text="data_preparation",
        description="Transforming raw data into a form suitable for analysis or training.")
    data_cleaning = PermissibleValue(
        text="data_cleaning",
        description="Detecting and correcting errors and inconsistencies in data.")
    filtering = PermissibleValue(
        text="filtering",
        description="Removing data items that do not match selection criteria.")
    normalisation = PermissibleValue(
        text="normalisation",
        description="Rescaling features to a common range or distribution.")
    de_identification = PermissibleValue(
        text="de_identification",
        description="Removing or transforming personally identifiable information.")
    data_quality_checking = PermissibleValue(
        text="data_quality_checking",
        description="Assessing completeness, accuracy, representativeness and bias of data (Clause 3.2.2).")
    data_sampling = PermissibleValue(
        text="data_sampling",
        description="Selecting a subset of records from a larger population (Clause 3.2.4).")
    data_augmentation = PermissibleValue(
        text="data_augmentation",
        description="Creating additional training examples via transformation of existing data (Clause 3.2.3).")
    feature_engineering = PermissibleValue(
        text="feature_engineering",
        description="Constructing or selecting features used as model inputs.")
    imputation = PermissibleValue(
        text="imputation",
        description="Replacing missing values with substituted estimates (Clause 3.2.8).")
    data_drift_detection = PermissibleValue(
        text="data_drift_detection",
        description="Detecting changes in the statistical distribution of operational data.")
    data_poisoning_detection = PermissibleValue(
        text="data_poisoning_detection",
        description="Identifying adversarial contamination of training data.")
    concept_drift_handling = PermissibleValue(
        text="concept_drift_handling",
        description="""Detecting and responding to changes in the relationship between inputs and target labels (Clause 5.11.9.1).""")
    catastrophic_forgetting_mitigation = PermissibleValue(
        text="catastrophic_forgetting_mitigation",
        description="""Strategies to prevent loss of previously learned knowledge during retraining (Clause 5.11.9.1).""")
    retraining = PermissibleValue(
        text="retraining",
        description="Updating an existing trained model on new or revised data (Clause 5.11.9).")

    _defn = EnumDefinition(
        name="DataProcessType",
        description="""Data-handling processes enumerated in Clause 5.10 and Clause 3.2 (data acquisition, annotation, preparation, quality checking, sampling, augmentation, drift and poisoning handling, etc.).""",
    )

class DataLabelType(EnumDefinitionImpl):
    """
    Categories of target label produced or consumed by ML workflows.
    """
    categorical = PermissibleValue(
        text="categorical",
        description="Discrete unordered class labels.")
    binary = PermissibleValue(
        text="binary",
        description="Two-class label (typically positive / negative).")
    ordinal = PermissibleValue(
        text="ordinal",
        description="Discrete ordered labels.")
    numeric = PermissibleValue(
        text="numeric",
        description="Continuous numeric target value.")
    structured = PermissibleValue(
        text="structured",
        description="Composite or graph-structured label.")
    sequence = PermissibleValue(
        text="sequence",
        description="Ordered sequence of label tokens (e.g. sequence labelling, structured prediction).")
    graph = PermissibleValue(
        text="graph",
        description="Graph-structured label such as a parse tree or relational structure.")
    none = PermissibleValue(
        text="none",
        description="No explicit label (unsupervised or self-supervised setting).")

    _defn = EnumDefinition(
        name="DataLabelType",
        description="Categories of target label produced or consumed by ML workflows.",
    )

class TaskCategory(EnumDefinitionImpl):
    """
    Categories of AI task addressed by AI systems, derived from the\n machine-learning, NLP and computer-vision
    terminology in Clause 3.
    """
    classification = PermissibleValue(
        text="classification",
        description="Assigning a class label to an input.")
    regression = PermissibleValue(
        text="regression",
        description="Predicting a continuous numeric value.")
    clustering = PermissibleValue(
        text="clustering",
        description="Grouping items by similarity without supervision.")
    ranking = PermissibleValue(
        text="ranking",
        description="Ordering items by relevance or preference.")
    recommendation = PermissibleValue(
        text="recommendation",
        description="Suggesting items to a user given context.")
    anomaly_detection = PermissibleValue(
        text="anomaly_detection",
        description="Identifying inputs that deviate from expected behaviour.")
    dimensionality_reduction = PermissibleValue(
        text="dimensionality_reduction",
        description="Producing a lower-dimensional representation of the data.")
    generation = PermissibleValue(
        text="generation",
        description="Producing new content (text, images, audio, etc.).")
    planning = PermissibleValue(
        text="planning",
        description="Producing a sequence of actions that achieve a goal.")
    control = PermissibleValue(
        text="control",
        description="Selecting actions to influence a dynamical system.")
    decision_support = PermissibleValue(
        text="decision_support",
        description="Producing recommendations or explanations to support human decisions.")

    _defn = EnumDefinition(
        name="TaskCategory",
        description="""Categories of AI task addressed by AI systems, derived from the\n      machine-learning, NLP and computer-vision terminology in Clause 3.""",
    )

class AISystemCharacteristic(EnumDefinitionImpl):
    """
    Distinguishing characteristics of AI systems summarised in Clause 5.1.
    """
    interactive = PermissibleValue(
        text="interactive",
        description="Engages in interaction with users or other systems.")
    contextual = PermissibleValue(
        text="contextual",
        description="Adapts behaviour to its operational context.")
    adaptive = PermissibleValue(
        text="adaptive",
        description="Adjusts behaviour over time in response to new data or feedback.")
    oversight_enabled = PermissibleValue(
        text="oversight_enabled",
        description="Provides mechanisms for human oversight and intervention.")
    data_dependent = PermissibleValue(
        text="data_dependent",
        description="Performance depends materially on the data used to build or operate the system.")

    _defn = EnumDefinition(
        name="AISystemCharacteristic",
        description="Distinguishing characteristics of AI systems summarised in Clause 5.1.",
    )

class SoftComputingTechnique(EnumDefinitionImpl):
    """
    Techniques grouped under soft computing in Clause 5.7.
    """
    fuzzy_logic = PermissibleValue(
        text="fuzzy_logic",
        description="Reasoning with degrees of truth rather than crisp Boolean values.")
    evolutionary_computing = PermissibleValue(
        text="evolutionary_computing",
        description="Optimisation inspired by biological evolution (including genetic algorithms).")
    swarm_intelligence = PermissibleValue(
        text="swarm_intelligence",
        description="Optimisation inspired by collective behaviour of decentralised agents.")
    probabilistic_reasoning = PermissibleValue(
        text="probabilistic_reasoning",
        description="Reasoning under uncertainty using probability theory.")
    neural_computing = PermissibleValue(
        text="neural_computing",
        description="Computation realised by networks of artificial neurons.")

    _defn = EnumDefinition(
        name="SoftComputingTechnique",
        description="Techniques grouped under soft computing in Clause 5.7.",
    )

class BigDataCharacteristic(EnumDefinitionImpl):
    """
    Characteristics commonly used to describe big data sources in Clause 8.6.1.
    """
    volume = PermissibleValue(
        text="volume",
        description="Total amount of data managed.")
    velocity = PermissibleValue(
        text="velocity",
        description="Rate at which data is generated or processed.")
    variety = PermissibleValue(
        text="variety",
        description="Range of data types and sources.")
    veracity = PermissibleValue(
        text="veracity",
        description="Trustworthiness and accuracy of the data.")
    value = PermissibleValue(
        text="value",
        description="Usefulness of the data for the intended purpose.")
    variability = PermissibleValue(
        text="variability",
        description="Degree to which data characteristics change over time.")

    _defn = EnumDefinition(
        name="BigDataCharacteristic",
        description="Characteristics commonly used to describe big data sources in Clause 8.6.1.",
    )

class IoTDeviceRole(EnumDefinitionImpl):
    """
    Roles played by devices in IoT and cyber-physical systems (Clause 5.14).
    """
    sensor = PermissibleValue(
        text="sensor",
        description="Device that observes the physical environment.")
    actuator = PermissibleValue(
        text="actuator",
        description="Device that effects changes in the physical environment.")
    gateway = PermissibleValue(
        text="gateway",
        description="Device that connects local IoT subnets to wider networks.")
    edge_compute = PermissibleValue(
        text="edge_compute",
        description="Device providing local computation at the network edge.")
    controller = PermissibleValue(
        text="controller",
        description="Device that supervises or coordinates other IoT devices.")

    _defn = EnumDefinition(
        name="IoTDeviceRole",
        description="Roles played by devices in IoT and cyber-physical systems (Clause 5.14).",
    )

class AbbreviationCode(EnumDefinitionImpl):
    """
    Acronyms and abbreviations listed in Clause 4.
    """
    AI = PermissibleValue(
        text="AI",
        description="Artificial intelligence.")
    API = PermissibleValue(
        text="API",
        description="Application programming interface.")
    ASIC = PermissibleValue(
        text="ASIC",
        description="Application-specific integrated circuit.")
    CNN = PermissibleValue(
        text="CNN",
        description="Convolutional neural network.")
    CPS = PermissibleValue(
        text="CPS",
        description="Cyber-physical system.")
    CPU = PermissibleValue(
        text="CPU",
        description="Central processing unit.")
    CRISP_DM = PermissibleValue(
        text="CRISP_DM",
        description="Cross-industry standard process for data mining.")
    DNN = PermissibleValue(
        text="DNN",
        description="Deep neural network.")
    DSP = PermissibleValue(
        text="DSP",
        description="Digital signal processor.")
    FFNN = PermissibleValue(
        text="FFNN",
        description="Feed-forward neural network.")
    FPGA = PermissibleValue(
        text="FPGA",
        description="Field-programmable gate array.")
    GA = PermissibleValue(
        text="GA",
        description="Genetic algorithm.")
    GPU = PermissibleValue(
        text="GPU",
        description="Graphics processing unit.")
    HMM = PermissibleValue(
        text="HMM",
        description="Hidden Markov model.")
    IoT = PermissibleValue(
        text="IoT",
        description="Internet of Things.")
    IR = PermissibleValue(
        text="IR",
        description="Information retrieval.")
    IT = PermissibleValue(
        text="IT",
        description="Information technology.")
    KDD = PermissibleValue(
        text="KDD",
        description="Knowledge discovery in data.")
    LSTM = PermissibleValue(
        text="LSTM",
        description="Long short-term memory.")
    ML = PermissibleValue(
        text="ML",
        description="Machine learning.")
    MT = PermissibleValue(
        text="MT",
        description="Machine translation.")
    NER = PermissibleValue(
        text="NER",
        description="Named entity recognition.")
    NLG = PermissibleValue(
        text="NLG",
        description="Natural language generation.")
    NLP = PermissibleValue(
        text="NLP",
        description="Natural language processing.")
    NLU = PermissibleValue(
        text="NLU",
        description="Natural language understanding.")
    NN = PermissibleValue(
        text="NN",
        description="Neural network.")
    NPU = PermissibleValue(
        text="NPU",
        description="Neural-network processing unit.")
    OCR = PermissibleValue(
        text="OCR",
        description="Optical character recognition.")
    OECD = PermissibleValue(
        text="OECD",
        description="Organisation for Economic Co-operation and Development.")
    PII = PermissibleValue(
        text="PII",
        description="Personally identifiable information.",
        meaning=ISO29100["PersonallyIdentifiableInformation"])
    POS = PermissibleValue(
        text="POS",
        description="Part of speech.")
    RL = PermissibleValue(
        text="RL",
        description="Reinforcement learning.")
    RNN = PermissibleValue(
        text="RNN",
        description="Recurrent neural network.")
    SVM = PermissibleValue(
        text="SVM",
        description="Support vector machine.")

    _defn = EnumDefinition(
        name="AbbreviationCode",
        description="Acronyms and abbreviations listed in Clause 4.",
    )

class ValidationStrategy(EnumDefinitionImpl):
    """
    Strategies for partitioning data and assessing generalisation, drawn from Clause 5.11.8 and Clause 5.16.
    """
    holdout = PermissibleValue(
        text="holdout",
        description="Single train / validation / test split.")
    two_way_split = PermissibleValue(
        text="two_way_split",
        description="Two-way split (train / test) used when data is limited (Clause 5.11.8).")
    cross_validation = PermissibleValue(
        text="cross_validation",
        description="K-fold cross-validation.")
    stratified_cross_validation = PermissibleValue(
        text="stratified_cross_validation",
        description="Cross-validation that preserves class distribution in each fold.")
    bootstrap = PermissibleValue(
        text="bootstrap",
        description="Resampling-with-replacement estimation of generalisation error.")
    time_series_split = PermissibleValue(
        text="time_series_split",
        description="Forward-chaining split that respects temporal order.")

    _defn = EnumDefinition(
        name="ValidationStrategy",
        description="""Strategies for partitioning data and assessing generalisation, drawn from Clause 5.11.8 and Clause 5.16.""",
    )

class VerificationValidationLevel(EnumDefinitionImpl):
    """
    Levels of verifiability and validatability used to characterise an AI system in Clause 5.16.
    """
    completely_verifiable = PermissibleValue(
        text="completely_verifiable",
        description="System behaviour is fully verifiable against specifications.")
    partially_verifiable_validatable = PermissibleValue(
        text="partially_verifiable_validatable",
        description="System is partially verifiable and validatable against specifications.")
    unverifiable_validatable = PermissibleValue(
        text="unverifiable_validatable",
        description="System is not verifiable but its behaviour can be validated empirically.")
    unverifiable_partially_validatable = PermissibleValue(
        text="unverifiable_partially_validatable",
        description="System is not verifiable and only partially validatable.")
    unverifiable_unvalidatable = PermissibleValue(
        text="unverifiable_unvalidatable",
        description="System is neither verifiable nor validatable with available techniques.")

    _defn = EnumDefinition(
        name="VerificationValidationLevel",
        description="Levels of verifiability and validatability used to characterise an AI system in Clause 5.16.",
    )

class DataSourceType(EnumDefinitionImpl):
    """
    Classification of data sources discussed in Clause 8.6.1.
    """
    first_party = PermissibleValue(
        text="first_party",
        description="Data collected directly by the organisation operating the AI system.")
    second_party = PermissibleValue(
        text="second_party",
        description="Data shared by a partner organisation under agreement.")
    third_party = PermissibleValue(
        text="third_party",
        description="Data acquired from an external data provider.")
    open_data = PermissibleValue(
        text="open_data",
        description="Publicly available data released under an open licence.")
    synthetic = PermissibleValue(
        text="synthetic",
        description="Data generated by simulation, sampling or generative models.")
    queried_union = PermissibleValue(
        text="queried_union",
        description="Data assembled on demand from a union of underlying sources.")

    _defn = EnumDefinition(
        name="DataSourceType",
        description="Classification of data sources discussed in Clause 8.6.1.",
    )

class DataCollectionMethod(EnumDefinitionImpl):
    """
    Methods of data collection enumerated in Clause 8.6.1.
    """
    point_of_sale = PermissibleValue(
        text="point_of_sale",
        description="Captured at the point of a commercial transaction.")
    survey = PermissibleValue(
        text="survey",
        description="Collected through structured questionnaires.")
    research_study = PermissibleValue(
        text="research_study",
        description="Collected as part of a designed research study.")
    sensor_capture = PermissibleValue(
        text="sensor_capture",
        description="Captured by a physical sensor.")
    image_capture = PermissibleValue(
        text="image_capture",
        description="Captured by an imaging device.")
    audio_capture = PermissibleValue(
        text="audio_capture",
        description="Captured by an audio recording device.")
    document_extraction = PermissibleValue(
        text="document_extraction",
        description="Extracted from text or document corpora.")
    web_scraping = PermissibleValue(
        text="web_scraping",
        description="Harvested from publicly accessible web resources.")
    interaction_log = PermissibleValue(
        text="interaction_log",
        description="Recorded from interactions with software or services.")
    transactional_log = PermissibleValue(
        text="transactional_log",
        description="Recorded as a side effect of transactional systems.")

    _defn = EnumDefinition(
        name="DataCollectionMethod",
        description="Methods of data collection enumerated in Clause 8.6.1.",
    )

class AutonomyCriterion(EnumDefinitionImpl):
    """
    Criteria contributing to the assessment of autonomy in Clause 5.13.\n Each criterion is graded independently when
    assigning an\n `AutonomyLevel`.
    """
    external_supervision = PermissibleValue(
        text="external_supervision",
        description="Degree to which an external operator supervises the system.")
    situated_understanding = PermissibleValue(
        text="situated_understanding",
        description="Degree to which the system understands its operational context.")
    reactivity = PermissibleValue(
        text="reactivity",
        description="Degree to which the system reacts to environmental changes.")
    persistence = PermissibleValue(
        text="persistence",
        description="Span over which the system continues operating without intervention.")
    adaptability = PermissibleValue(
        text="adaptability",
        description="Degree to which the system adapts behaviour to new conditions.")
    performance_evaluation = PermissibleValue(
        text="performance_evaluation",
        description="Ability of the system to evaluate its own performance.")
    proactive_planning = PermissibleValue(
        text="proactive_planning",
        description="Ability of the system to plan future actions proactively.")

    _defn = EnumDefinition(
        name="AutonomyCriterion",
        description="""Criteria contributing to the assessment of autonomy in Clause 5.13.\n      Each criterion is graded independently when assigning an\n      `AutonomyLevel`.""",
    )

class NeuroSymbolicApproach(EnumDefinitionImpl):
    """
    Sub-categorisation of hybrid neuro-symbolic approaches mentioned in\n      Clause 5.9.
    """
    symbolic_in_neural = PermissibleValue(
        text="symbolic_in_neural",
        description="Symbolic reasoning embedded within a primarily subsymbolic architecture.")
    neural_in_symbolic = PermissibleValue(
        text="neural_in_symbolic",
        description="Subsymbolic components invoked inside a symbolic reasoning framework.")
    tightly_coupled = PermissibleValue(
        text="tightly_coupled",
        description="Symbolic and subsymbolic components share representations end-to-end.")
    loosely_coupled = PermissibleValue(
        text="loosely_coupled",
        description="Symbolic and subsymbolic components exchange information at well-defined interfaces.")

    _defn = EnumDefinition(
        name="NeuroSymbolicApproach",
        description="Sub-categorisation of hybrid neuro-symbolic approaches mentioned in\n      Clause 5.9.",
    )

class RecommendationOutcomeType(EnumDefinitionImpl):
    """
    High-level categorisation of recommendations produced by an AI system\n      (Clauses 7.4, 10).
    """
    content_recommendation = PermissibleValue(
        text="content_recommendation",
        description="Suggestion of content items.")
    action_recommendation = PermissibleValue(
        text="action_recommendation",
        description="Suggestion of an action to take.")
    ranking_recommendation = PermissibleValue(
        text="ranking_recommendation",
        description="Recommendation expressed as a ranked list.")
    next_best_action = PermissibleValue(
        text="next_best_action",
        description="Recommendation of the single most appropriate next action.")

    _defn = EnumDefinition(
        name="RecommendationOutcomeType",
        description="High-level categorisation of recommendations produced by an AI system\n      (Clauses 7.4, 10).",
    )

class ExecutionStatus(EnumDefinitionImpl):
    """
    Execution status values for actions and processes.
    """
    planned = PermissibleValue(
        text="planned",
        description="Execution has been planned but not yet started.")
    in_progress = PermissibleValue(
        text="in_progress",
        description="Execution is currently in progress.")
    completed = PermissibleValue(
        text="completed",
        description="Execution has completed successfully.")
    failed = PermissibleValue(
        text="failed",
        description="Execution has terminated unsuccessfully.")
    cancelled = PermissibleValue(
        text="cancelled",
        description="Execution was cancelled before completion.")

    _defn = EnumDefinition(
        name="ExecutionStatus",
        description="Execution status values for actions and processes.",
    )

# Slots
class slots:
    pass

slots.id = Slot(uri=DCTERMS.identifier, name="id", curie=DCTERMS.curie('identifier'),
                   model_uri=ISO22989.id, domain=None, range=URIRef)

slots.name = Slot(uri=SCHEMA.name, name="name", curie=SCHEMA.curie('name'),
                   model_uri=ISO22989.name, domain=None, range=str)

slots.description = Slot(uri=DCTERMS.description, name="description", curie=DCTERMS.curie('description'),
                   model_uri=ISO22989.description, domain=None, range=Optional[str])

slots.clause_reference = Slot(uri=ISO22989.clause_reference, name="clause_reference", curie=ISO22989.curie('clause_reference'),
                   model_uri=ISO22989.clause_reference, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[0-9]+(\.[0-9]+){0,3}$'))

slots.aliases = Slot(uri=SKOS.altLabel, name="aliases", curie=SKOS.curie('altLabel'),
                   model_uri=ISO22989.aliases, domain=None, range=Optional[Union[str, list[str]]])

slots.preferred_label = Slot(uri=SKOS.prefLabel, name="preferred_label", curie=SKOS.curie('prefLabel'),
                   model_uri=ISO22989.preferred_label, domain=None, range=Optional[str])

slots.see_also_uri = Slot(uri=RDFS.seeAlso, name="see_also_uri", curie=RDFS.curie('seeAlso'),
                   model_uri=ISO22989.see_also_uri, domain=None, range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]])

slots.ai_system_type = Slot(uri=ISO22989.ai_system_type, name="ai_system_type", curie=ISO22989.curie('ai_system_type'),
                   model_uri=ISO22989.ai_system_type, domain=None, range=Optional[Union[str, "AISystemType"]])

slots.symbolic_approach = Slot(uri=ISO22989.symbolic_approach, name="symbolic_approach", curie=ISO22989.curie('symbolic_approach'),
                   model_uri=ISO22989.symbolic_approach, domain=None, range=Optional[Union[str, "SymbolicApproach"]])

slots.autonomy_level = Slot(uri=ISO22989.autonomy_level, name="autonomy_level", curie=ISO22989.curie('autonomy_level'),
                   model_uri=ISO22989.autonomy_level, domain=None, range=Optional[Union[str, "AutonomyLevel"]])

slots.intended_purpose = Slot(uri=ISO22989.intended_purpose, name="intended_purpose", curie=ISO22989.curie('intended_purpose'),
                   model_uri=ISO22989.intended_purpose, domain=None, range=Optional[str])

slots.application_domain = Slot(uri=ISO22989.application_domain, name="application_domain", curie=ISO22989.curie('application_domain'),
                   model_uri=ISO22989.application_domain, domain=None, range=Optional[Union[Union[str, "AIApplicationDomain"], list[Union[str, "AIApplicationDomain"]]]])

slots.ai_field = Slot(uri=ISO22989.ai_field, name="ai_field", curie=ISO22989.curie('ai_field'),
                   model_uri=ISO22989.ai_field, domain=None, range=Optional[Union[Union[str, "AIField"], list[Union[str, "AIField"]]]])

slots.functional_components = Slot(uri=ISO22989.functional_components, name="functional_components", curie=ISO22989.curie('functional_components'),
                   model_uri=ISO22989.functional_components, domain=None, range=Optional[Union[Union[str, "AIFunctionalComponent"], list[Union[str, "AIFunctionalComponent"]]]])

slots.lifecycle_stage = Slot(uri=ISO22989.lifecycle_stage, name="lifecycle_stage", curie=ISO22989.curie('lifecycle_stage'),
                   model_uri=ISO22989.lifecycle_stage, domain=None, range=Optional[Union[str, "AILifecycleStage"]])

slots.stakeholders = Slot(uri=ISO22989.stakeholders, name="stakeholders", curie=ISO22989.curie('stakeholders'),
                   model_uri=ISO22989.stakeholders, domain=None, range=Optional[Union[dict[Union[str, AIStakeholderRoleId], Union[dict, AIStakeholderRole]], list[Union[dict, AIStakeholderRole]]]])

slots.components = Slot(uri=ISO22989.components, name="components", curie=ISO22989.curie('components'),
                   model_uri=ISO22989.components, domain=None, range=Optional[Union[dict[Union[str, AIComponentId], Union[dict, AIComponent]], list[Union[dict, AIComponent]]]])

slots.models = Slot(uri=ISO22989.models, name="models", curie=ISO22989.curie('models'),
                   model_uri=ISO22989.models, domain=None, range=Optional[Union[dict[Union[str, AIModelId], Union[dict, AIModel]], list[Union[dict, AIModel]]]])

slots.datasets = Slot(uri=ISO22989.datasets, name="datasets", curie=ISO22989.curie('datasets'),
                   model_uri=ISO22989.datasets, domain=None, range=Optional[Union[dict[Union[str, DatasetId], Union[dict, Dataset]], list[Union[dict, Dataset]]]])

slots.trustworthiness_properties = Slot(uri=ISO22989.trustworthiness_properties, name="trustworthiness_properties", curie=ISO22989.curie('trustworthiness_properties'),
                   model_uri=ISO22989.trustworthiness_properties, domain=None, range=Optional[Union[dict[Union[str, TrustworthinessPropertyId], Union[dict, TrustworthinessProperty]], list[Union[dict, TrustworthinessProperty]]]])

slots.model_paradigm = Slot(uri=ISO22989.model_paradigm, name="model_paradigm", curie=ISO22989.curie('model_paradigm'),
                   model_uri=ISO22989.model_paradigm, domain=None, range=Optional[Union[str, "MachineLearningParadigm"]])

slots.algorithm_family = Slot(uri=ISO22989.algorithm_family, name="algorithm_family", curie=ISO22989.curie('algorithm_family'),
                   model_uri=ISO22989.algorithm_family, domain=None, range=Optional[Union[str, "MLAlgorithmFamily"]])

slots.engineering_approach = Slot(uri=ISO22989.engineering_approach, name="engineering_approach", curie=ISO22989.curie('engineering_approach'),
                   model_uri=ISO22989.engineering_approach, domain=None, range=Optional[Union[str, "EngineeringApproach"]])

slots.training_dataset = Slot(uri=ISO22989.training_dataset, name="training_dataset", curie=ISO22989.curie('training_dataset'),
                   model_uri=ISO22989.training_dataset, domain=None, range=Optional[Union[str, DatasetId]])

slots.validation_dataset = Slot(uri=ISO22989.validation_dataset, name="validation_dataset", curie=ISO22989.curie('validation_dataset'),
                   model_uri=ISO22989.validation_dataset, domain=None, range=Optional[Union[str, DatasetId]])

slots.test_dataset = Slot(uri=ISO22989.test_dataset, name="test_dataset", curie=ISO22989.curie('test_dataset'),
                   model_uri=ISO22989.test_dataset, domain=None, range=Optional[Union[str, DatasetId]])

slots.hyperparameters = Slot(uri=ISO22989.hyperparameters, name="hyperparameters", curie=ISO22989.curie('hyperparameters'),
                   model_uri=ISO22989.hyperparameters, domain=None, range=Optional[Union[str, list[str]]])

slots.model_version = Slot(uri=ISO22989.model_version, name="model_version", curie=ISO22989.curie('model_version'),
                   model_uri=ISO22989.model_version, domain=None, range=Optional[str])

slots.trained_on = Slot(uri=ISO22989.trained_on, name="trained_on", curie=ISO22989.curie('trained_on'),
                   model_uri=ISO22989.trained_on, domain=None, range=Optional[str])

slots.data_modality = Slot(uri=ISO22989.data_modality, name="data_modality", curie=ISO22989.curie('data_modality'),
                   model_uri=ISO22989.data_modality, domain=None, range=Optional[Union[Union[str, "DataModality"], list[Union[str, "DataModality"]]]])

slots.dataset_role = Slot(uri=ISO22989.dataset_role, name="dataset_role", curie=ISO22989.curie('dataset_role'),
                   model_uri=ISO22989.dataset_role, domain=None, range=Optional[Union[str, "DatasetRole"]])

slots.data_provenance = Slot(uri=PROV.wasDerivedFrom, name="data_provenance", curie=PROV.curie('wasDerivedFrom'),
                   model_uri=ISO22989.data_provenance, domain=None, range=Optional[str])

slots.record_count = Slot(uri=ISO22989.record_count, name="record_count", curie=ISO22989.curie('record_count'),
                   model_uri=ISO22989.record_count, domain=None, range=Optional[int])

slots.data_quality_notes = Slot(uri=ISO22989.data_quality_notes, name="data_quality_notes", curie=ISO22989.curie('data_quality_notes'),
                   model_uri=ISO22989.data_quality_notes, domain=None, range=Optional[str])

slots.contains_personal_data = Slot(uri=ISO22989.contains_personal_data, name="contains_personal_data", curie=ISO22989.curie('contains_personal_data'),
                   model_uri=ISO22989.contains_personal_data, domain=None, range=Optional[Union[bool, Bool]])

slots.trustworthiness_property_type = Slot(uri=ISO22989.trustworthiness_property_type, name="trustworthiness_property_type", curie=ISO22989.curie('trustworthiness_property_type'),
                   model_uri=ISO22989.trustworthiness_property_type, domain=None, range=Union[str, "TrustworthinessPropertyType"])

slots.property_evidence = Slot(uri=ISO22989.property_evidence, name="property_evidence", curie=ISO22989.curie('property_evidence'),
                   model_uri=ISO22989.property_evidence, domain=None, range=Optional[Union[str, list[str]]])

slots.measurement_method = Slot(uri=ISO22989.measurement_method, name="measurement_method", curie=ISO22989.curie('measurement_method'),
                   model_uri=ISO22989.measurement_method, domain=None, range=Optional[str])

slots.applicable_biases = Slot(uri=ISO22989.applicable_biases, name="applicable_biases", curie=ISO22989.curie('applicable_biases'),
                   model_uri=ISO22989.applicable_biases, domain=None, range=Optional[Union[Union[str, "BiasType"], list[Union[str, "BiasType"]]]])

slots.confidence_score = Slot(uri=ISO22989.confidence_score, name="confidence_score", curie=ISO22989.curie('confidence_score'),
                   model_uri=ISO22989.confidence_score, domain=None, range=Optional[Union[float, ConfidenceScore]])

slots.process_stage = Slot(uri=ISO22989.process_stage, name="process_stage", curie=ISO22989.curie('process_stage'),
                   model_uri=ISO22989.process_stage, domain=None, range=Union[str, "AILifecycleStage"])

slots.process_inputs = Slot(uri=ISO22989.process_inputs, name="process_inputs", curie=ISO22989.curie('process_inputs'),
                   model_uri=ISO22989.process_inputs, domain=None, range=Optional[Union[str, list[str]]])

slots.process_outputs = Slot(uri=ISO22989.process_outputs, name="process_outputs", curie=ISO22989.curie('process_outputs'),
                   model_uri=ISO22989.process_outputs, domain=None, range=Optional[Union[str, list[str]]])

slots.responsible_role = Slot(uri=ISO22989.responsible_role, name="responsible_role", curie=ISO22989.curie('responsible_role'),
                   model_uri=ISO22989.responsible_role, domain=None, range=Optional[Union[str, "AIStakeholderRoleType"]])

slots.start_date = Slot(uri=ISO22989.start_date, name="start_date", curie=ISO22989.curie('start_date'),
                   model_uri=ISO22989.start_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.end_date = Slot(uri=ISO22989.end_date, name="end_date", curie=ISO22989.curie('end_date'),
                   model_uri=ISO22989.end_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.stakeholder_role_type = Slot(uri=ISO22989.stakeholder_role_type, name="stakeholder_role_type", curie=ISO22989.curie('stakeholder_role_type'),
                   model_uri=ISO22989.stakeholder_role_type, domain=None, range=Union[str, "AIStakeholderRoleType"])

slots.organization_name = Slot(uri=ISO22989.organization_name, name="organization_name", curie=ISO22989.curie('organization_name'),
                   model_uri=ISO22989.organization_name, domain=None, range=Optional[str])

slots.contact = Slot(uri=ISO22989.contact, name="contact", curie=ISO22989.curie('contact'),
                   model_uri=ISO22989.contact, domain=None, range=Optional[str])

slots.responsibilities = Slot(uri=ISO22989.responsibilities, name="responsibilities", curie=ISO22989.curie('responsibilities'),
                   model_uri=ISO22989.responsibilities, domain=None, range=Optional[Union[str, list[str]]])

slots.computing_resources = Slot(uri=ISO22989.computing_resources, name="computing_resources", curie=ISO22989.curie('computing_resources'),
                   model_uri=ISO22989.computing_resources, domain=None, range=Optional[Union[Union[str, "ComputingResourceType"], list[Union[str, "ComputingResourceType"]]]])

slots.data_sources = Slot(uri=ISO22989.data_sources, name="data_sources", curie=ISO22989.curie('data_sources'),
                   model_uri=ISO22989.data_sources, domain=None, range=Optional[Union[str, list[str]]])

slots.ecosystem_components = Slot(uri=ISO22989.ecosystem_components, name="ecosystem_components", curie=ISO22989.curie('ecosystem_components'),
                   model_uri=ISO22989.ecosystem_components, domain=None, range=Optional[Union[str, list[str]]])

slots.jurisdictional_issues = Slot(uri=ISO22989.jurisdictional_issues, name="jurisdictional_issues", curie=ISO22989.curie('jurisdictional_issues'),
                   model_uri=ISO22989.jurisdictional_issues, domain=None, range=Optional[Union[Union[str, "JurisdictionalIssueType"], list[Union[str, "JurisdictionalIssueType"]]]])

slots.societal_impacts = Slot(uri=ISO22989.societal_impacts, name="societal_impacts", curie=ISO22989.curie('societal_impacts'),
                   model_uri=ISO22989.societal_impacts, domain=None, range=Optional[Union[Union[str, "SocietalImpactCategory"], list[Union[str, "SocietalImpactCategory"]]]])

slots.ai_systems = Slot(uri=ISO22989.ai_systems, name="ai_systems", curie=ISO22989.curie('ai_systems'),
                   model_uri=ISO22989.ai_systems, domain=None, range=Optional[Union[dict[Union[str, AISystemId], Union[dict, AISystem]], list[Union[dict, AISystem]]]])

slots.ai_models = Slot(uri=ISO22989.ai_models, name="ai_models", curie=ISO22989.curie('ai_models'),
                   model_uri=ISO22989.ai_models, domain=None, range=Optional[Union[dict[Union[str, AIModelId], Union[dict, AIModel]], list[Union[dict, AIModel]]]])

slots.ai_datasets = Slot(uri=ISO22989.ai_datasets, name="ai_datasets", curie=ISO22989.curie('ai_datasets'),
                   model_uri=ISO22989.ai_datasets, domain=None, range=Optional[Union[dict[Union[str, DatasetId], Union[dict, Dataset]], list[Union[dict, Dataset]]]])

slots.ai_lifecycle_processes = Slot(uri=ISO22989.ai_lifecycle_processes, name="ai_lifecycle_processes", curie=ISO22989.curie('ai_lifecycle_processes'),
                   model_uri=ISO22989.ai_lifecycle_processes, domain=None, range=Optional[Union[dict[Union[str, AILifecycleProcessId], Union[dict, AILifecycleProcess]], list[Union[dict, AILifecycleProcess]]]])

slots.ai_stakeholder_roles = Slot(uri=ISO22989.ai_stakeholder_roles, name="ai_stakeholder_roles", curie=ISO22989.curie('ai_stakeholder_roles'),
                   model_uri=ISO22989.ai_stakeholder_roles, domain=None, range=Optional[Union[dict[Union[str, AIStakeholderRoleId], Union[dict, AIStakeholderRole]], list[Union[dict, AIStakeholderRole]]]])

slots.ai_applications = Slot(uri=ISO22989.ai_applications, name="ai_applications", curie=ISO22989.curie('ai_applications'),
                   model_uri=ISO22989.ai_applications, domain=None, range=Optional[Union[dict[Union[str, AIApplicationId], Union[dict, AIApplication]], list[Union[dict, AIApplication]]]])

slots.trustworthiness_records = Slot(uri=ISO22989.trustworthiness_records, name="trustworthiness_records", curie=ISO22989.curie('trustworthiness_records'),
                   model_uri=ISO22989.trustworthiness_records, domain=None, range=Optional[Union[dict[Union[str, TrustworthinessPropertyId], Union[dict, TrustworthinessProperty]], list[Union[dict, TrustworthinessProperty]]]])

slots.component_function = Slot(uri=ISO22989.component_function, name="component_function", curie=ISO22989.curie('component_function'),
                   model_uri=ISO22989.component_function, domain=None, range=Optional[Union[str, "AIFunctionalComponent"]])

slots.parameter_count = Slot(uri=ISO22989.parameter_count, name="parameter_count", curie=ISO22989.curie('parameter_count'),
                   model_uri=ISO22989.parameter_count, domain=None, range=Optional[int])

slots.supports_continuous_learning = Slot(uri=ISO22989.supports_continuous_learning, name="supports_continuous_learning", curie=ISO22989.curie('supports_continuous_learning'),
                   model_uri=ISO22989.supports_continuous_learning, domain=None, range=Optional[Union[bool, Bool]])

slots.catastrophic_forgetting_risk = Slot(uri=ISO22989.catastrophic_forgetting_risk, name="catastrophic_forgetting_risk", curie=ISO22989.curie('catastrophic_forgetting_risk'),
                   model_uri=ISO22989.catastrophic_forgetting_risk, domain=None, range=Optional[Union[float, ConfidenceScore]])

slots.training_duration = Slot(uri=ISO22989.training_duration, name="training_duration", curie=ISO22989.curie('training_duration'),
                   model_uri=ISO22989.training_duration, domain=None, range=Optional[str])

slots.inference_latency_ms = Slot(uri=ISO22989.inference_latency_ms, name="inference_latency_ms", curie=ISO22989.curie('inference_latency_ms'),
                   model_uri=ISO22989.inference_latency_ms, domain=None, range=Optional[float])

slots.model_compression_applied = Slot(uri=ISO22989.model_compression_applied, name="model_compression_applied", curie=ISO22989.curie('model_compression_applied'),
                   model_uri=ISO22989.model_compression_applied, domain=None, range=Optional[Union[bool, Bool]])

slots.label_type = Slot(uri=ISO22989.label_type, name="label_type", curie=ISO22989.curie('label_type'),
                   model_uri=ISO22989.label_type, domain=None, range=Optional[Union[str, "DataLabelType"]])

slots.label_value = Slot(uri=ISO22989.label_value, name="label_value", curie=ISO22989.curie('label_value'),
                   model_uri=ISO22989.label_value, domain=None, range=Optional[str])

slots.ground_truth_available = Slot(uri=ISO22989.ground_truth_available, name="ground_truth_available", curie=ISO22989.curie('ground_truth_available'),
                   model_uri=ISO22989.ground_truth_available, domain=None, range=Optional[Union[bool, Bool]])

slots.ground_truth_value = Slot(uri=ISO22989.ground_truth_value, name="ground_truth_value", curie=ISO22989.curie('ground_truth_value'),
                   model_uri=ISO22989.ground_truth_value, domain=None, range=Optional[str])

slots.feature_count = Slot(uri=ISO22989.feature_count, name="feature_count", curie=ISO22989.curie('feature_count'),
                   model_uri=ISO22989.feature_count, domain=None, range=Optional[int])

slots.data_source_type = Slot(uri=ISO22989.data_source_type, name="data_source_type", curie=ISO22989.curie('data_source_type'),
                   model_uri=ISO22989.data_source_type, domain=None, range=Optional[Union[str, "DataSourceType"]])

slots.data_collection_method = Slot(uri=ISO22989.data_collection_method, name="data_collection_method", curie=ISO22989.curie('data_collection_method'),
                   model_uri=ISO22989.data_collection_method, domain=None, range=Optional[Union[str, "DataCollectionMethod"]])

slots.collection_date_range = Slot(uri=ISO22989.collection_date_range, name="collection_date_range", curie=ISO22989.curie('collection_date_range'),
                   model_uri=ISO22989.collection_date_range, domain=None, range=Optional[str])

slots.data_version = Slot(uri=ISO22989.data_version, name="data_version", curie=ISO22989.curie('data_version'),
                   model_uri=ISO22989.data_version, domain=None, range=Optional[str])

slots.task_category = Slot(uri=ISO22989.task_category, name="task_category", curie=ISO22989.curie('task_category'),
                   model_uri=ISO22989.task_category, domain=None, range=Optional[Union[str, "TaskCategory"]])

slots.input_modalities = Slot(uri=ISO22989.input_modalities, name="input_modalities", curie=ISO22989.curie('input_modalities'),
                   model_uri=ISO22989.input_modalities, domain=None, range=Optional[Union[Union[str, "DataModality"], list[Union[str, "DataModality"]]]])

slots.output_label_type = Slot(uri=ISO22989.output_label_type, name="output_label_type", curie=ISO22989.curie('output_label_type'),
                   model_uri=ISO22989.output_label_type, domain=None, range=Optional[Union[str, "DataLabelType"]])

slots.performance_metric = Slot(uri=ISO22989.performance_metric, name="performance_metric", curie=ISO22989.curie('performance_metric'),
                   model_uri=ISO22989.performance_metric, domain=None, range=Optional[Union[str, list[str]]])

slots.predicted_value = Slot(uri=ISO22989.predicted_value, name="predicted_value", curie=ISO22989.curie('predicted_value'),
                   model_uri=ISO22989.predicted_value, domain=None, range=Optional[str])

slots.decision_outcome = Slot(uri=ISO22989.decision_outcome, name="decision_outcome", curie=ISO22989.curie('decision_outcome'),
                   model_uri=ISO22989.decision_outcome, domain=None, range=Optional[str])

slots.decision_policy = Slot(uri=ISO22989.decision_policy, name="decision_policy", curie=ISO22989.curie('decision_policy'),
                   model_uri=ISO22989.decision_policy, domain=None, range=Optional[str])

slots.action_target = Slot(uri=ISO22989.action_target, name="action_target", curie=ISO22989.curie('action_target'),
                   model_uri=ISO22989.action_target, domain=None, range=Optional[str])

slots.execution_status = Slot(uri=ISO22989.execution_status, name="execution_status", curie=ISO22989.curie('execution_status'),
                   model_uri=ISO22989.execution_status, domain=None, range=Optional[Union[str, "ExecutionStatus"]])

slots.risk_items = Slot(uri=ISO22989.risk_items, name="risk_items", curie=ISO22989.curie('risk_items'),
                   model_uri=ISO22989.risk_items, domain=None, range=Optional[Union[str, list[str]]])

slots.approval_criteria = Slot(uri=ISO22989.approval_criteria, name="approval_criteria", curie=ISO22989.curie('approval_criteria'),
                   model_uri=ISO22989.approval_criteria, domain=None, range=Optional[Union[str, list[str]]])

slots.node_count = Slot(uri=ISO22989.node_count, name="node_count", curie=ISO22989.curie('node_count'),
                   model_uri=ISO22989.node_count, domain=None, range=Optional[int])

slots.edge_count = Slot(uri=ISO22989.edge_count, name="edge_count", curie=ISO22989.curie('edge_count'),
                   model_uri=ISO22989.edge_count, domain=None, range=Optional[int])

slots.ontology_reference = Slot(uri=ISO22989.ontology_reference, name="ontology_reference", curie=ISO22989.curie('ontology_reference'),
                   model_uri=ISO22989.ontology_reference, domain=None, range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]])

slots.rule_count = Slot(uri=ISO22989.rule_count, name="rule_count", curie=ISO22989.curie('rule_count'),
                   model_uri=ISO22989.rule_count, domain=None, range=Optional[int])

slots.resource_type = Slot(uri=ISO22989.resource_type, name="resource_type", curie=ISO22989.curie('resource_type'),
                   model_uri=ISO22989.resource_type, domain=None, range=Optional[Union[str, "ComputingResourceType"]])

slots.nlp_component_type = Slot(uri=ISO22989.nlp_component_type, name="nlp_component_type", curie=ISO22989.curie('nlp_component_type'),
                   model_uri=ISO22989.nlp_component_type, domain=None, range=Optional[Union[str, "NLPComponentType"]])

slots.cv_task = Slot(uri=ISO22989.cv_task, name="cv_task", curie=ISO22989.curie('cv_task'),
                   model_uri=ISO22989.cv_task, domain=None, range=Optional[Union[str, "ComputerVisionTask"]])

slots.device_role = Slot(uri=ISO22989.device_role, name="device_role", curie=ISO22989.curie('device_role'),
                   model_uri=ISO22989.device_role, domain=None, range=Optional[Union[str, "IoTDeviceRole"]])

slots.abbreviation_code = Slot(uri=ISO22989.abbreviation_code, name="abbreviation_code", curie=ISO22989.curie('abbreviation_code'),
                   model_uri=ISO22989.abbreviation_code, domain=None, range=Optional[Union[str, "AbbreviationCode"]])

slots.expansion = Slot(uri=ISO22989.expansion, name="expansion", curie=ISO22989.curie('expansion'),
                   model_uri=ISO22989.expansion, domain=None, range=Optional[str])

slots.validation_strategy = Slot(uri=ISO22989.validation_strategy, name="validation_strategy", curie=ISO22989.curie('validation_strategy'),
                   model_uri=ISO22989.validation_strategy, domain=None, range=Optional[Union[str, "ValidationStrategy"]])

slots.verification_validation_level = Slot(uri=ISO22989.verification_validation_level, name="verification_validation_level", curie=ISO22989.curie('verification_validation_level'),
                   model_uri=ISO22989.verification_validation_level, domain=None, range=Optional[Union[str, "VerificationValidationLevel"]])

slots.autonomy_criterion_scores = Slot(uri=ISO22989.autonomy_criterion_scores, name="autonomy_criterion_scores", curie=ISO22989.curie('autonomy_criterion_scores'),
                   model_uri=ISO22989.autonomy_criterion_scores, domain=None, range=Optional[Union[str, list[str]]])

slots.recommendation_outcome_type = Slot(uri=ISO22989.recommendation_outcome_type, name="recommendation_outcome_type", curie=ISO22989.curie('recommendation_outcome_type'),
                   model_uri=ISO22989.recommendation_outcome_type, domain=None, range=Optional[Union[str, "RecommendationOutcomeType"]])

slots.confidence = Slot(uri=ISO22989.confidence, name="confidence", curie=ISO22989.curie('confidence'),
                   model_uri=ISO22989.confidence, domain=None, range=Optional[Union[float, ConfidenceScore]])

slots.provenance_statement = Slot(uri=PROV.wasDerivedFrom, name="provenance_statement", curie=PROV.curie('wasDerivedFrom'),
                   model_uri=ISO22989.provenance_statement, domain=None, range=Optional[str])

slots.aIAgent__agent_architecture = Slot(uri=ISO22989.agent_architecture, name="aIAgent__agent_architecture", curie=ISO22989.curie('agent_architecture'),
                   model_uri=ISO22989.aIAgent__agent_architecture, domain=None, range=Optional[Union[str, "AgentArchitectureType"]])

slots.aIAgent__goal_set = Slot(uri=ISO22989.goal_set, name="aIAgent__goal_set", curie=ISO22989.curie('goal_set'),
                   model_uri=ISO22989.aIAgent__goal_set, domain=None, range=Optional[Union[str, list[str]]])

slots.knowledgeRepresentation__knowledge_type = Slot(uri=ISO22989.knowledge_type, name="knowledgeRepresentation__knowledge_type", curie=ISO22989.curie('knowledge_type'),
                   model_uri=ISO22989.knowledgeRepresentation__knowledge_type, domain=None, range=Optional[Union[str, "KnowledgeType"]])

slots.knowledgeRepresentation__representation_form = Slot(uri=ISO22989.representation_form, name="knowledgeRepresentation__representation_form", curie=ISO22989.curie('representation_form'),
                   model_uri=ISO22989.knowledgeRepresentation__representation_form, domain=None, range=Optional[str])

slots.aISystem__system_characteristics = Slot(uri=ISO22989.system_characteristics, name="aISystem__system_characteristics", curie=ISO22989.curie('system_characteristics'),
                   model_uri=ISO22989.aISystem__system_characteristics, domain=None, range=Optional[Union[Union[str, "AISystemCharacteristic"], list[Union[str, "AISystemCharacteristic"]]]])

slots.aISystem__task_categories = Slot(uri=ISO22989.task_categories, name="aISystem__task_categories", curie=ISO22989.curie('task_categories'),
                   model_uri=ISO22989.aISystem__task_categories, domain=None, range=Optional[Union[Union[str, "TaskCategory"], list[Union[str, "TaskCategory"]]]])

slots.aISystem__agent_architecture = Slot(uri=ISO22989.agent_architecture, name="aISystem__agent_architecture", curie=ISO22989.curie('agent_architecture'),
                   model_uri=ISO22989.aISystem__agent_architecture, domain=None, range=Optional[Union[str, "AgentArchitectureType"]])

slots.aISystem__data_processes = Slot(uri=ISO22989.data_processes, name="aISystem__data_processes", curie=ISO22989.curie('data_processes'),
                   model_uri=ISO22989.aISystem__data_processes, domain=None, range=Optional[Union[dict[Union[str, DataProcessId], Union[dict, DataProcess]], list[Union[dict, DataProcess]]]])

slots.aISystem__iot_integration = Slot(uri=ISO22989.iot_integration, name="aISystem__iot_integration", curie=ISO22989.curie('iot_integration'),
                   model_uri=ISO22989.aISystem__iot_integration, domain=None, range=Optional[Union[str, IoTSystemId]])

slots.aIComponent__depends_on = Slot(uri=ISO22989.depends_on, name="aIComponent__depends_on", curie=ISO22989.curie('depends_on'),
                   model_uri=ISO22989.aIComponent__depends_on, domain=None, range=Optional[Union[Union[str, AIComponentId], list[Union[str, AIComponentId]]]])

slots.aIModel__neural_network_architecture = Slot(uri=ISO22989.neural_network_architecture, name="aIModel__neural_network_architecture", curie=ISO22989.curie('neural_network_architecture'),
                   model_uri=ISO22989.aIModel__neural_network_architecture, domain=None, range=Optional[Union[str, "NeuralNetworkArchitecture"]])

slots.aIModel__activation_function = Slot(uri=ISO22989.activation_function, name="aIModel__activation_function", curie=ISO22989.curie('activation_function'),
                   model_uri=ISO22989.aIModel__activation_function, domain=None, range=Optional[Union[str, "ActivationFunctionType"]])

slots.aIModel__training_phenomena = Slot(uri=ISO22989.training_phenomena, name="aIModel__training_phenomena", curie=ISO22989.curie('training_phenomena'),
                   model_uri=ISO22989.aIModel__training_phenomena, domain=None, range=Optional[Union[Union[str, "NeuralNetworkPhenomenon"], list[Union[str, "NeuralNetworkPhenomenon"]]]])

slots.neuralNetworkModel__number_of_layers = Slot(uri=ISO22989.number_of_layers, name="neuralNetworkModel__number_of_layers", curie=ISO22989.curie('number_of_layers'),
                   model_uri=ISO22989.neuralNetworkModel__number_of_layers, domain=None, range=Optional[int])

slots.neuralNetworkModel__number_of_parameters = Slot(uri=ISO22989.number_of_parameters, name="neuralNetworkModel__number_of_parameters", curie=ISO22989.curie('number_of_parameters'),
                   model_uri=ISO22989.neuralNetworkModel__number_of_parameters, domain=None, range=Optional[int])

slots.dataset__label_type = Slot(uri=ISO22989.label_type, name="dataset__label_type", curie=ISO22989.curie('label_type'),
                   model_uri=ISO22989.dataset__label_type, domain=None, range=Optional[Union[str, "DataLabelType"]])

slots.dataset__ground_truth_available = Slot(uri=ISO22989.ground_truth_available, name="dataset__ground_truth_available", curie=ISO22989.curie('ground_truth_available'),
                   model_uri=ISO22989.dataset__ground_truth_available, domain=None, range=Optional[Union[bool, Bool]])

slots.dataset__feature_count = Slot(uri=ISO22989.feature_count, name="dataset__feature_count", curie=ISO22989.curie('feature_count'),
                   model_uri=ISO22989.dataset__feature_count, domain=None, range=Optional[int])

slots.dataset__data_processes_applied = Slot(uri=ISO22989.data_processes_applied, name="dataset__data_processes_applied", curie=ISO22989.curie('data_processes_applied'),
                   model_uri=ISO22989.dataset__data_processes_applied, domain=None, range=Optional[Union[dict[Union[str, DataProcessId], Union[dict, DataProcess]], list[Union[dict, DataProcess]]]])

slots.aILifecycleProcess__process_sub_type = Slot(uri=ISO22989.process_sub_type, name="aILifecycleProcess__process_sub_type", curie=ISO22989.curie('process_sub_type'),
                   model_uri=ISO22989.aILifecycleProcess__process_sub_type, domain=None, range=Optional[str])

slots.aIEcosystem__big_data_characteristics = Slot(uri=ISO22989.big_data_characteristics, name="aIEcosystem__big_data_characteristics", curie=ISO22989.curie('big_data_characteristics'),
                   model_uri=ISO22989.aIEcosystem__big_data_characteristics, domain=None, range=Optional[Union[Union[str, "BigDataCharacteristic"], list[Union[str, "BigDataCharacteristic"]]]])

slots.resourcePool__capacity_units = Slot(uri=ISO22989.capacity_units, name="resourcePool__capacity_units", curie=ISO22989.curie('capacity_units'),
                   model_uri=ISO22989.resourcePool__capacity_units, domain=None, range=Optional[str])

slots.aIApplication__hosting_system = Slot(uri=ISO22989.hosting_system, name="aIApplication__hosting_system", curie=ISO22989.curie('hosting_system'),
                   model_uri=ISO22989.aIApplication__hosting_system, domain=None, range=Optional[Union[str, AISystemId]])

slots.prediction__produced_by = Slot(uri=ISO22989.produced_by, name="prediction__produced_by", curie=ISO22989.curie('produced_by'),
                   model_uri=ISO22989.prediction__produced_by, domain=None, range=Optional[Union[str, AIModelId]])

slots.decision__based_on_predictions = Slot(uri=ISO22989.based_on_predictions, name="decision__based_on_predictions", curie=ISO22989.curie('based_on_predictions'),
                   model_uri=ISO22989.decision__based_on_predictions, domain=None, range=Optional[Union[Union[str, PredictionId], list[Union[str, PredictionId]]]])

slots.action__triggered_by = Slot(uri=ISO22989.triggered_by, name="action__triggered_by", curie=ISO22989.curie('triggered_by'),
                   model_uri=ISO22989.action__triggered_by, domain=None, range=Optional[Union[str, DecisionId]])

slots.inferenceEngine__inference_strategy = Slot(uri=ISO22989.inference_strategy, name="inferenceEngine__inference_strategy", curie=ISO22989.curie('inference_strategy'),
                   model_uri=ISO22989.inferenceEngine__inference_strategy, domain=None, range=Optional[str])

slots.inferenceEngine__uses_model = Slot(uri=ISO22989.uses_model, name="inferenceEngine__uses_model", curie=ISO22989.curie('uses_model'),
                   model_uri=ISO22989.inferenceEngine__uses_model, domain=None, range=Optional[Union[str, AIModelId]])

slots.expertSystem__inference_engine = Slot(uri=ISO22989.inference_engine, name="expertSystem__inference_engine", curie=ISO22989.curie('inference_engine'),
                   model_uri=ISO22989.expertSystem__inference_engine, domain=None, range=Optional[Union[dict, InferenceEngine]])

slots.cognitiveComputingSystem__cognitive_capabilities = Slot(uri=ISO22989.cognitive_capabilities, name="cognitiveComputingSystem__cognitive_capabilities", curie=ISO22989.curie('cognitive_capabilities'),
                   model_uri=ISO22989.cognitiveComputingSystem__cognitive_capabilities, domain=None, range=Optional[Union[str, list[str]]])

slots.semanticComputingSystem__semantic_model = Slot(uri=ISO22989.semantic_model, name="semanticComputingSystem__semantic_model", curie=ISO22989.curie('semantic_model'),
                   model_uri=ISO22989.semanticComputingSystem__semantic_model, domain=None, range=Optional[str])

slots.softComputingSystem__soft_computing_techniques = Slot(uri=ISO22989.soft_computing_techniques, name="softComputingSystem__soft_computing_techniques", curie=ISO22989.curie('soft_computing_techniques'),
                   model_uri=ISO22989.softComputingSystem__soft_computing_techniques, domain=None, range=Union[Union[str, "SoftComputingTechnique"], list[Union[str, "SoftComputingTechnique"]]])

slots.dataProcess__process_type = Slot(uri=ISO22989.process_type, name="dataProcess__process_type", curie=ISO22989.curie('process_type'),
                   model_uri=ISO22989.dataProcess__process_type, domain=None, range=Union[str, "DataProcessType"])

slots.dataProcess__input_dataset = Slot(uri=ISO22989.input_dataset, name="dataProcess__input_dataset", curie=ISO22989.curie('input_dataset'),
                   model_uri=ISO22989.dataProcess__input_dataset, domain=None, range=Optional[Union[str, DatasetId]])

slots.dataProcess__output_dataset = Slot(uri=ISO22989.output_dataset, name="dataProcess__output_dataset", curie=ISO22989.curie('output_dataset'),
                   model_uri=ISO22989.dataProcess__output_dataset, domain=None, range=Optional[Union[str, DatasetId]])

slots.dataProcess__parameters = Slot(uri=ISO22989.parameters, name="dataProcess__parameters", curie=ISO22989.curie('parameters'),
                   model_uri=ISO22989.dataProcess__parameters, domain=None, range=Optional[Union[str, list[str]]])

slots.dataProcess__executed_by = Slot(uri=ISO22989.executed_by, name="dataProcess__executed_by", curie=ISO22989.curie('executed_by'),
                   model_uri=ISO22989.dataProcess__executed_by, domain=None, range=Optional[Union[str, AIStakeholderRoleId]])

slots.dataSample__sample_payload = Slot(uri=ISO22989.sample_payload, name="dataSample__sample_payload", curie=ISO22989.curie('sample_payload'),
                   model_uri=ISO22989.dataSample__sample_payload, domain=None, range=Optional[str])

slots.dataSample__sample_label = Slot(uri=ISO22989.sample_label, name="dataSample__sample_label", curie=ISO22989.curie('sample_label'),
                   model_uri=ISO22989.dataSample__sample_label, domain=None, range=Optional[str])

slots.dataLabel__annotator = Slot(uri=ISO22989.annotator, name="dataLabel__annotator", curie=ISO22989.curie('annotator'),
                   model_uri=ISO22989.dataLabel__annotator, domain=None, range=Optional[Union[str, AIStakeholderRoleId]])

slots.robot__embodiment = Slot(uri=ISO22989.embodiment, name="robot__embodiment", curie=ISO22989.curie('embodiment'),
                   model_uri=ISO22989.robot__embodiment, domain=None, range=Optional[str])

slots.robot__controlled_by = Slot(uri=ISO22989.controlled_by, name="robot__controlled_by", curie=ISO22989.curie('controlled_by'),
                   model_uri=ISO22989.robot__controlled_by, domain=None, range=Optional[Union[str, AISystemId]])

slots.ioTDevice__sensing_capabilities = Slot(uri=ISO22989.sensing_capabilities, name="ioTDevice__sensing_capabilities", curie=ISO22989.curie('sensing_capabilities'),
                   model_uri=ISO22989.ioTDevice__sensing_capabilities, domain=None, range=Optional[Union[str, list[str]]])

slots.ioTDevice__actuating_capabilities = Slot(uri=ISO22989.actuating_capabilities, name="ioTDevice__actuating_capabilities", curie=ISO22989.curie('actuating_capabilities'),
                   model_uri=ISO22989.ioTDevice__actuating_capabilities, domain=None, range=Optional[Union[str, list[str]]])

slots.ioTSystem__devices = Slot(uri=ISO22989.devices, name="ioTSystem__devices", curie=ISO22989.curie('devices'),
                   model_uri=ISO22989.ioTSystem__devices, domain=None, range=Optional[Union[dict[Union[str, IoTDeviceId], Union[dict, IoTDevice]], list[Union[dict, IoTDevice]]]])

slots.ioTSystem__ai_components = Slot(uri=ISO22989.ai_components, name="ioTSystem__ai_components", curie=ISO22989.curie('ai_components'),
                   model_uri=ISO22989.ioTSystem__ai_components, domain=None, range=Optional[Union[Union[str, AIComponentId], list[Union[str, AIComponentId]]]])

slots.cyberPhysicalSystem__physical_processes = Slot(uri=ISO22989.physical_processes, name="cyberPhysicalSystem__physical_processes", curie=ISO22989.curie('physical_processes'),
                   model_uri=ISO22989.cyberPhysicalSystem__physical_processes, domain=None, range=Optional[Union[str, list[str]]])

slots.cyberPhysicalSystem__cyber_components = Slot(uri=ISO22989.cyber_components, name="cyberPhysicalSystem__cyber_components", curie=ISO22989.curie('cyber_components'),
                   model_uri=ISO22989.cyberPhysicalSystem__cyber_components, domain=None, range=Optional[Union[Union[str, AIComponentId], list[Union[str, AIComponentId]]]])

slots.cyberPhysicalSystem__iot_subsystem = Slot(uri=ISO22989.iot_subsystem, name="cyberPhysicalSystem__iot_subsystem", curie=ISO22989.curie('iot_subsystem'),
                   model_uri=ISO22989.cyberPhysicalSystem__iot_subsystem, domain=None, range=Optional[Union[str, IoTSystemId]])

slots.aIConceptsCollection__tasks = Slot(uri=ISO22989.tasks, name="aIConceptsCollection__tasks", curie=ISO22989.curie('tasks'),
                   model_uri=ISO22989.aIConceptsCollection__tasks, domain=None, range=Optional[Union[dict[Union[str, TaskId], Union[dict, Task]], list[Union[dict, Task]]]])

slots.aIConceptsCollection__data_processes = Slot(uri=ISO22989.data_processes, name="aIConceptsCollection__data_processes", curie=ISO22989.curie('data_processes'),
                   model_uri=ISO22989.aIConceptsCollection__data_processes, domain=None, range=Optional[Union[dict[Union[str, DataProcessId], Union[dict, DataProcess]], list[Union[dict, DataProcess]]]])

slots.aIConceptsCollection__iot_systems = Slot(uri=ISO22989.iot_systems, name="aIConceptsCollection__iot_systems", curie=ISO22989.curie('iot_systems'),
                   model_uri=ISO22989.aIConceptsCollection__iot_systems, domain=None, range=Optional[Union[dict[Union[str, IoTSystemId], Union[dict, IoTSystem]], list[Union[dict, IoTSystem]]]])

slots.aIConceptsCollection__cyber_physical_systems = Slot(uri=ISO22989.cyber_physical_systems, name="aIConceptsCollection__cyber_physical_systems", curie=ISO22989.curie('cyber_physical_systems'),
                   model_uri=ISO22989.aIConceptsCollection__cyber_physical_systems, domain=None, range=Optional[Union[dict[Union[str, CyberPhysicalSystemId], Union[dict, CyberPhysicalSystem]], list[Union[dict, CyberPhysicalSystem]]]])

slots.aIConceptsCollection__knowledge_graphs = Slot(uri=ISO22989.knowledge_graphs, name="aIConceptsCollection__knowledge_graphs", curie=ISO22989.curie('knowledge_graphs'),
                   model_uri=ISO22989.aIConceptsCollection__knowledge_graphs, domain=None, range=Optional[Union[dict[Union[str, KnowledgeGraphId], Union[dict, KnowledgeGraph]], list[Union[dict, KnowledgeGraph]]]])

slots.aIConceptsCollection__expert_systems = Slot(uri=ISO22989.expert_systems, name="aIConceptsCollection__expert_systems", curie=ISO22989.curie('expert_systems'),
                   model_uri=ISO22989.aIConceptsCollection__expert_systems, domain=None, range=Optional[Union[dict[Union[str, ExpertSystemId], Union[dict, ExpertSystem]], list[Union[dict, ExpertSystem]]]])

slots.aIConceptsCollection__abbreviations = Slot(uri=ISO22989.abbreviations, name="aIConceptsCollection__abbreviations", curie=ISO22989.curie('abbreviations'),
                   model_uri=ISO22989.aIConceptsCollection__abbreviations, domain=None, range=Optional[Union[dict[Union[str, AbbreviationEntryId], Union[dict, AbbreviationEntry]], list[Union[dict, AbbreviationEntry]]]])

slots.verificationValidationFramework__verification_methods = Slot(uri=ISO22989.verification_methods, name="verificationValidationFramework__verification_methods", curie=ISO22989.curie('verification_methods'),
                   model_uri=ISO22989.verificationValidationFramework__verification_methods, domain=None, range=Optional[Union[str, list[str]]])

slots.verificationValidationFramework__validation_methods = Slot(uri=ISO22989.validation_methods, name="verificationValidationFramework__validation_methods", curie=ISO22989.curie('validation_methods'),
                   model_uri=ISO22989.verificationValidationFramework__validation_methods, domain=None, range=Optional[Union[str, list[str]]])

slots.humanMachineTeam__human_roles = Slot(uri=ISO22989.human_roles, name="humanMachineTeam__human_roles", curie=ISO22989.curie('human_roles'),
                   model_uri=ISO22989.humanMachineTeam__human_roles, domain=None, range=Optional[Union[str, list[str]]])

slots.humanMachineTeam__ai_systems_involved = Slot(uri=ISO22989.ai_systems_involved, name="humanMachineTeam__ai_systems_involved", curie=ISO22989.curie('ai_systems_involved'),
                   model_uri=ISO22989.humanMachineTeam__ai_systems_involved, domain=None, range=Optional[Union[Union[str, AISystemId], list[Union[str, AISystemId]]]])

slots.humanMachineTeam__task_allocation = Slot(uri=ISO22989.task_allocation, name="humanMachineTeam__task_allocation", curie=ISO22989.curie('task_allocation'),
                   model_uri=ISO22989.humanMachineTeam__task_allocation, domain=None, range=Optional[str])

slots.intelligenceAugmentation__augmented_capability = Slot(uri=ISO22989.augmented_capability, name="intelligenceAugmentation__augmented_capability", curie=ISO22989.curie('augmented_capability'),
                   model_uri=ISO22989.intelligenceAugmentation__augmented_capability, domain=None, range=Optional[Union[str, list[str]]])

slots.recommendation__recommended_items = Slot(uri=ISO22989.recommended_items, name="recommendation__recommended_items", curie=ISO22989.curie('recommended_items'),
                   model_uri=ISO22989.recommendation__recommended_items, domain=None, range=Optional[Union[str, list[str]]])

slots.recommendation__based_on_predictions = Slot(uri=ISO22989.based_on_predictions, name="recommendation__based_on_predictions", curie=ISO22989.curie('based_on_predictions'),
                   model_uri=ISO22989.recommendation__based_on_predictions, domain=None, range=Optional[Union[Union[str, PredictionId], list[Union[str, PredictionId]]]])

slots.evaluationMetric__metric_name = Slot(uri=ISO22989.metric_name, name="evaluationMetric__metric_name", curie=ISO22989.curie('metric_name'),
                   model_uri=ISO22989.evaluationMetric__metric_name, domain=None, range=str)

slots.evaluationMetric__metric_value = Slot(uri=ISO22989.metric_value, name="evaluationMetric__metric_value", curie=ISO22989.curie('metric_value'),
                   model_uri=ISO22989.evaluationMetric__metric_value, domain=None, range=Optional[float])

slots.evaluationMetric__metric_unit = Slot(uri=ISO22989.metric_unit, name="evaluationMetric__metric_unit", curie=ISO22989.curie('metric_unit'),
                   model_uri=ISO22989.evaluationMetric__metric_unit, domain=None, range=Optional[str])

slots.evaluationMetric__reference_dataset = Slot(uri=ISO22989.reference_dataset, name="evaluationMetric__reference_dataset", curie=ISO22989.curie('reference_dataset'),
                   model_uri=ISO22989.evaluationMetric__reference_dataset, domain=None, range=Optional[Union[str, DatasetId]])

slots.threshold__threshold_value = Slot(uri=ISO22989.threshold_value, name="threshold__threshold_value", curie=ISO22989.curie('threshold_value'),
                   model_uri=ISO22989.threshold__threshold_value, domain=None, range=float)

slots.threshold__applies_to_metric = Slot(uri=ISO22989.applies_to_metric, name="threshold__applies_to_metric", curie=ISO22989.curie('applies_to_metric'),
                   model_uri=ISO22989.threshold__applies_to_metric, domain=None, range=Optional[str])

slots.threshold__threshold_policy = Slot(uri=ISO22989.threshold_policy, name="threshold__threshold_policy", curie=ISO22989.curie('threshold_policy'),
                   model_uri=ISO22989.threshold__threshold_policy, domain=None, range=Optional[str])

slots.neuron__activation_function = Slot(uri=ISO22989.activation_function, name="neuron__activation_function", curie=ISO22989.curie('activation_function'),
                   model_uri=ISO22989.neuron__activation_function, domain=None, range=Optional[Union[str, "ActivationFunctionType"]])

slots.neuron__input_arity = Slot(uri=ISO22989.input_arity, name="neuron__input_arity", curie=ISO22989.curie('input_arity'),
                   model_uri=ISO22989.neuron__input_arity, domain=None, range=Optional[int])

slots.convolutionOperation__kernel_size = Slot(uri=ISO22989.kernel_size, name="convolutionOperation__kernel_size", curie=ISO22989.curie('kernel_size'),
                   model_uri=ISO22989.convolutionOperation__kernel_size, domain=None, range=Optional[Union[int, list[int]]])

slots.convolutionOperation__stride = Slot(uri=ISO22989.stride, name="convolutionOperation__stride", curie=ISO22989.curie('stride'),
                   model_uri=ISO22989.convolutionOperation__stride, domain=None, range=Optional[int])

slots.convolutionOperation__padding = Slot(uri=ISO22989.padding, name="convolutionOperation__padding", curie=ISO22989.curie('padding'),
                   model_uri=ISO22989.convolutionOperation__padding, domain=None, range=Optional[str])

slots.dataDrift__drift_type = Slot(uri=ISO22989.drift_type, name="dataDrift__drift_type", curie=ISO22989.curie('drift_type'),
                   model_uri=ISO22989.dataDrift__drift_type, domain=None, range=Optional[str])

slots.dataDrift__detected_at = Slot(uri=ISO22989.detected_at, name="dataDrift__detected_at", curie=ISO22989.curie('detected_at'),
                   model_uri=ISO22989.dataDrift__detected_at, domain=None, range=Optional[str])

slots.dataDrift__affected_dataset = Slot(uri=ISO22989.affected_dataset, name="dataDrift__affected_dataset", curie=ISO22989.curie('affected_dataset'),
                   model_uri=ISO22989.dataDrift__affected_dataset, domain=None, range=Optional[Union[str, DatasetId]])

slots.catastrophicForgetting__affected_model = Slot(uri=ISO22989.affected_model, name="catastrophicForgetting__affected_model", curie=ISO22989.curie('affected_model'),
                   model_uri=ISO22989.catastrophicForgetting__affected_model, domain=None, range=Optional[Union[str, AIModelId]])

slots.catastrophicForgetting__mitigation_strategy = Slot(uri=ISO22989.mitigation_strategy, name="catastrophicForgetting__mitigation_strategy", curie=ISO22989.curie('mitigation_strategy'),
                   model_uri=ISO22989.catastrophicForgetting__mitigation_strategy, domain=None, range=Optional[str])

slots.faultToleranceMechanism__mechanism_type = Slot(uri=ISO22989.mechanism_type, name="faultToleranceMechanism__mechanism_type", curie=ISO22989.curie('mechanism_type'),
                   model_uri=ISO22989.faultToleranceMechanism__mechanism_type, domain=None, range=Optional[str])

slots.faultToleranceMechanism__coverage_scope = Slot(uri=ISO22989.coverage_scope, name="faultToleranceMechanism__coverage_scope", curie=ISO22989.curie('coverage_scope'),
                   model_uri=ISO22989.faultToleranceMechanism__coverage_scope, domain=None, range=Optional[str])

slots.naturalLanguage__language_code = Slot(uri=ISO22989.language_code, name="naturalLanguage__language_code", curie=ISO22989.curie('language_code'),
                   model_uri=ISO22989.naturalLanguage__language_code, domain=None, range=Optional[str])

slots.naturalLanguage__script = Slot(uri=ISO22989.script, name="naturalLanguage__script", curie=ISO22989.curie('script'),
                   model_uri=ISO22989.naturalLanguage__script, domain=None, range=Optional[str])

slots.riskItem__risk_source = Slot(uri=ISO22989.risk_source, name="riskItem__risk_source", curie=ISO22989.curie('risk_source'),
                   model_uri=ISO22989.riskItem__risk_source, domain=None, range=Optional[str])

slots.riskItem__potential_event = Slot(uri=ISO22989.potential_event, name="riskItem__potential_event", curie=ISO22989.curie('potential_event'),
                   model_uri=ISO22989.riskItem__potential_event, domain=None, range=Optional[str])

slots.riskItem__consequence = Slot(uri=ISO22989.consequence, name="riskItem__consequence", curie=ISO22989.curie('consequence'),
                   model_uri=ISO22989.riskItem__consequence, domain=None, range=Optional[str])

slots.riskItem__likelihood = Slot(uri=ISO22989.likelihood, name="riskItem__likelihood", curie=ISO22989.curie('likelihood'),
                   model_uri=ISO22989.riskItem__likelihood, domain=None, range=Optional[Union[float, ConfidenceScore]])

slots.riskItem__severity = Slot(uri=ISO22989.severity, name="riskItem__severity", curie=ISO22989.curie('severity'),
                   model_uri=ISO22989.riskItem__severity, domain=None, range=Optional[str])

slots.riskItem__mitigation_strategy = Slot(uri=ISO22989.mitigation_strategy, name="riskItem__mitigation_strategy", curie=ISO22989.curie('mitigation_strategy'),
                   model_uri=ISO22989.riskItem__mitigation_strategy, domain=None, range=Optional[Union[str, list[str]]])

slots.riskItem__affected_stakeholders = Slot(uri=ISO22989.affected_stakeholders, name="riskItem__affected_stakeholders", curie=ISO22989.curie('affected_stakeholders'),
                   model_uri=ISO22989.riskItem__affected_stakeholders, domain=None, range=Optional[Union[Union[str, AIStakeholderRoleId], list[Union[str, AIStakeholderRoleId]]]])

slots.inputData__modality = Slot(uri=ISO22989.modality, name="inputData__modality", curie=ISO22989.curie('modality'),
                   model_uri=ISO22989.inputData__modality, domain=None, range=Optional[Union[str, "DataModality"]])

slots.inputData__consumed_by = Slot(uri=ISO22989.consumed_by, name="inputData__consumed_by", curie=ISO22989.curie('consumed_by'),
                   model_uri=ISO22989.inputData__consumed_by, domain=None, range=Optional[Union[str, AISystemId]])

slots.inference__inference_strategy = Slot(uri=ISO22989.inference_strategy, name="inference__inference_strategy", curie=ISO22989.curie('inference_strategy'),
                   model_uri=ISO22989.inference__inference_strategy, domain=None, range=Optional[str])

slots.inference__performed_by = Slot(uri=ISO22989.performed_by, name="inference__performed_by", curie=ISO22989.curie('performed_by'),
                   model_uri=ISO22989.inference__performed_by, domain=None, range=Optional[Union[str, InferenceEngineId]])

slots.inference__over_model = Slot(uri=ISO22989.over_model, name="inference__over_model", curie=ISO22989.curie('over_model'),
                   model_uri=ISO22989.inference__over_model, domain=None, range=Optional[Union[str, AIModelId]])

slots.inference__produced_output = Slot(uri=ISO22989.produced_output, name="inference__produced_output", curie=ISO22989.curie('produced_output'),
                   model_uri=ISO22989.inference__produced_output, domain=None, range=Optional[str])

slots.oECDLifecycleMapping__iso_stage = Slot(uri=ISO22989.iso_stage, name="oECDLifecycleMapping__iso_stage", curie=ISO22989.curie('iso_stage'),
                   model_uri=ISO22989.oECDLifecycleMapping__iso_stage, domain=None, range=Union[str, "AILifecycleStage"])

slots.oECDLifecycleMapping__oecd_stage = Slot(uri=ISO22989.oecd_stage, name="oECDLifecycleMapping__oecd_stage", curie=ISO22989.curie('oecd_stage'),
                   model_uri=ISO22989.oECDLifecycleMapping__oecd_stage, domain=None, range=Union[str, "OECDLifecycleStage"])

slots.oECDLifecycleMapping__mapping_notes = Slot(uri=ISO22989.mapping_notes, name="oECDLifecycleMapping__mapping_notes", curie=ISO22989.curie('mapping_notes'),
                   model_uri=ISO22989.oECDLifecycleMapping__mapping_notes, domain=None, range=Optional[str])

slots.AbbreviatedTerm_expansion = Slot(uri=ISO22989.expansion, name="AbbreviatedTerm_expansion", curie=ISO22989.curie('expansion'),
                   model_uri=ISO22989.AbbreviatedTerm_expansion, domain=AbbreviatedTerm, range=str)

slots.NeuralNetworkModel_algorithm_family = Slot(uri=ISO22989.algorithm_family, name="NeuralNetworkModel_algorithm_family", curie=ISO22989.curie('algorithm_family'),
                   model_uri=ISO22989.NeuralNetworkModel_algorithm_family, domain=NeuralNetworkModel, range=Optional[Union[str, "MLAlgorithmFamily"]])

slots.AIProvider_stakeholder_role_type = Slot(uri=ISO22989.stakeholder_role_type, name="AIProvider_stakeholder_role_type", curie=ISO22989.curie('stakeholder_role_type'),
                   model_uri=ISO22989.AIProvider_stakeholder_role_type, domain=AIProvider, range=Union[str, "AIStakeholderRoleType"])

slots.AIProducer_stakeholder_role_type = Slot(uri=ISO22989.stakeholder_role_type, name="AIProducer_stakeholder_role_type", curie=ISO22989.curie('stakeholder_role_type'),
                   model_uri=ISO22989.AIProducer_stakeholder_role_type, domain=AIProducer, range=Union[str, "AIStakeholderRoleType"])

slots.AICustomer_stakeholder_role_type = Slot(uri=ISO22989.stakeholder_role_type, name="AICustomer_stakeholder_role_type", curie=ISO22989.curie('stakeholder_role_type'),
                   model_uri=ISO22989.AICustomer_stakeholder_role_type, domain=AICustomer, range=Union[str, "AIStakeholderRoleType"])

slots.AIPartner_stakeholder_role_type = Slot(uri=ISO22989.stakeholder_role_type, name="AIPartner_stakeholder_role_type", curie=ISO22989.curie('stakeholder_role_type'),
                   model_uri=ISO22989.AIPartner_stakeholder_role_type, domain=AIPartner, range=Union[str, "AIStakeholderRoleType"])

slots.AISubject_stakeholder_role_type = Slot(uri=ISO22989.stakeholder_role_type, name="AISubject_stakeholder_role_type", curie=ISO22989.curie('stakeholder_role_type'),
                   model_uri=ISO22989.AISubject_stakeholder_role_type, domain=AISubject, range=Union[str, "AIStakeholderRoleType"])

slots.RelevantAuthority_stakeholder_role_type = Slot(uri=ISO22989.stakeholder_role_type, name="RelevantAuthority_stakeholder_role_type", curie=ISO22989.curie('stakeholder_role_type'),
                   model_uri=ISO22989.RelevantAuthority_stakeholder_role_type, domain=RelevantAuthority, range=Union[str, "AIStakeholderRoleType"])

slots.ResourcePool_resource_type = Slot(uri=ISO22989.resource_type, name="ResourcePool_resource_type", curie=ISO22989.curie('resource_type'),
                   model_uri=ISO22989.ResourcePool_resource_type, domain=ResourcePool, range=Union[str, "ComputingResourceType"])

slots.NLPComponent_nlp_component_type = Slot(uri=ISO22989.nlp_component_type, name="NLPComponent_nlp_component_type", curie=ISO22989.curie('nlp_component_type'),
                   model_uri=ISO22989.NLPComponent_nlp_component_type, domain=NLPComponent, range=Union[str, "NLPComponentType"])

slots.ComputerVisionFunction_cv_task = Slot(uri=ISO22989.cv_task, name="ComputerVisionFunction_cv_task", curie=ISO22989.curie('cv_task'),
                   model_uri=ISO22989.ComputerVisionFunction_cv_task, domain=ComputerVisionFunction, range=Union[str, "ComputerVisionTask"])

slots.Task_task_category = Slot(uri=ISO22989.task_category, name="Task_task_category", curie=ISO22989.curie('task_category'),
                   model_uri=ISO22989.Task_task_category, domain=Task, range=Union[str, "TaskCategory"])

slots.DataLabel_label_value = Slot(uri=ISO22989.label_value, name="DataLabel_label_value", curie=ISO22989.curie('label_value'),
                   model_uri=ISO22989.DataLabel_label_value, domain=DataLabel, range=str)

slots.GroundTruthRecord_ground_truth_value = Slot(uri=ISO22989.ground_truth_value, name="GroundTruthRecord_ground_truth_value", curie=ISO22989.curie('ground_truth_value'),
                   model_uri=ISO22989.GroundTruthRecord_ground_truth_value, domain=GroundTruthRecord, range=str)

slots.IoTDevice_device_role = Slot(uri=ISO22989.device_role, name="IoTDevice_device_role", curie=ISO22989.curie('device_role'),
                   model_uri=ISO22989.IoTDevice_device_role, domain=IoTDevice, range=Union[str, "IoTDeviceRole"])

slots.AbbreviationEntry_abbreviation_code = Slot(uri=ISO22989.abbreviation_code, name="AbbreviationEntry_abbreviation_code", curie=ISO22989.curie('abbreviation_code'),
                   model_uri=ISO22989.AbbreviationEntry_abbreviation_code, domain=AbbreviationEntry, range=Union[str, "AbbreviationCode"])

slots.AbbreviationEntry_expansion = Slot(uri=ISO22989.expansion, name="AbbreviationEntry_expansion", curie=ISO22989.curie('expansion'),
                   model_uri=ISO22989.AbbreviationEntry_expansion, domain=AbbreviationEntry, range=str)
