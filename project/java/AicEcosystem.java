package example;

/* metamodel_version: 1.12.0 */
/* version: 2022 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  The AI systems around one context of use, with the data, resources and parties that surround them, each kind of record in a list of its own.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AicEcosystem  {

  private List<AicSystem> aicEcosystemSystems;
  private List<AicComponent> aicEcosystemComponents;
  private List<AicKnowledge> aicEcosystemKnowledge;
  private List<AicTask> aicEcosystemTasks;
  private List<AicModel> aicEcosystemModels;
  private List<AicDataset> aicEcosystemDatasets;
  private List<AicStakeholder> aicEcosystemStakeholders;
  private List<AicLifecycleProcess> aicEcosystemLifecycleProcesses;
  private List<AicTrustworthinessClaim> aicEcosystemClaims;
  private List<AicAssessment> aicEcosystemAssessments;
  private List<AicPrediction> aicEcosystemPredictions;
  private List<AicDecision> aicEcosystemDecisions;
  private List<AicAction> aicEcosystemActions;
  private List<AicApplication> aicEcosystemApplications;
  private List<AicResourcePool> aicEcosystemResourcePools;
  private List<AicIotDevice> aicEcosystemIotDevices;
  private List<AicIotSystem> aicEcosystemIotSystems;
  private List<AicCyberPhysicalSystem> aicEcosystemCyberPhysicalSystems;
  private URI aicId;
  private String title;
  private String description;


}