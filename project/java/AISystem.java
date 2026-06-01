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
  Engineered system that uses AI techniques to perform tasks delegated to it. Aggregates lifecycle, functional, model and stakeholder data.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AISystem extends NamedEntity {

  private String aiSystemType;
  private String symbolicApproach;
  private String autonomyLevel;
  private String intendedPurpose;
  private List<String> applicationDomain;
  private List<String> aiField;
  private List<String> functionalComponents;
  private String lifecycleStage;
  private List<AIStakeholderRole> stakeholders;
  private List<AIComponent> components;
  private List<AIModel> models;
  private List<Dataset> datasets;
  private List<TrustworthinessProperty> trustworthinessProperties;
  private List<String> jurisdictionalIssues;
  private List<String> societalImpacts;
  private List<String> systemCharacteristics;
  private List<String> taskCategories;
  private String agentArchitecture;
  private List<DataProcess> dataProcesses;
  private IoTSystem iotIntegration;


}