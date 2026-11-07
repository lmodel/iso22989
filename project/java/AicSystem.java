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
  A system built to produce results for goals set by people, using AI techniques, whatever else it is made of.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AicSystem  {

  private String aicSystemType;
  private String aicSystemPurpose;
  private String aicSystemScope;
  private List<String> aicSystemApproaches;
  private List<String> aicSystemTechniques;
  private Boolean aicSystemAutomated;
  private String aicSystemAutonomy;
  private String aicSystemHumanTeaming;
  private String aicSystemStage;
  private List<String> aicSystemFields;
  private List<String> aicSystemSteps;
  private List<AicComponent> aicSystemComponents;
  private List<AicModel> aicSystemModels;
  private List<AicDataset> aicSystemDatasets;
  private List<AicTask> aicSystemTasks;
  private List<AicStakeholder> aicSystemStakeholders;
  private List<AicResourcePool> aicSystemResourcePools;
  private List<String> aicSystemJurisdictionalIssues;
  private List<String> aicSystemSocietalImpacts;
  private URI aicId;
  private String title;
  private String description;


}