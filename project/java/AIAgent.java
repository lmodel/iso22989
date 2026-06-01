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
  Entity that perceives its environment and acts upon it to achieve goals (Clause 5.3).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AIAgent extends AIConcept {

  private String autonomyLevel;
  private String symbolicApproach;
  private String agentArchitecture;
  private List<String> goalSet;


}