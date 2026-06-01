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
  Aggregation of the AI systems, data sources, computing resources and stakeholder roles that surround a deployment context (Clause 8).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AIEcosystem extends NamedEntity {

  private List<String> computingResources;
  private List<String> dataSources;
  private List<String> ecosystemComponents;
  private List<AISystem> aiSystems;
  private List<AIStakeholderRole> aiStakeholderRoles;
  private List<String> bigDataCharacteristics;


}