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
  Process or activity associated with a stage of the AI system life cycle (Clause 6).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AILifecycleProcess extends NamedEntity {

  private String processStage;
  private List<String> processInputs;
  private List<String> processOutputs;
  private String responsibleRole;
  private LocalDate startDate;
  private LocalDate endDate;
  private List<String> riskItems;
  private List<String> approvalCriteria;
  private String processSubType;


}