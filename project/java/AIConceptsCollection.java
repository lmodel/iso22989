package None;

/* metamodel_version: 1.11.0 */
/* version: 0.1.0 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  Top-level container aggregating AI systems, models, datasets, lifecycle processes, stakeholder roles, applications and trustworthiness records for serialisation as a single artefact.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AIConceptsCollection  {

  private List<AISystem> aiSystems;
  private List<AIModel> aiModels;
  private List<Dataset> aiDatasets;
  private List<AILifecycleProcess> aiLifecycleProcesses;
  private List<AIStakeholderRole> aiStakeholderRoles;
  private List<AIApplication> aiApplications;
  private List<TrustworthinessProperty> trustworthinessRecords;
  private List<Task> tasks;
  private List<DataProcess> dataProcesses;
  private List<IoTSystem> iotSystems;
  private List<CyberPhysicalSystem> cyberPhysicalSystems;
  private List<KnowledgeGraph> knowledgeGraphs;
  private List<ExpertSystem> expertSystems;
  private List<AbbreviationEntry> abbreviations;


}