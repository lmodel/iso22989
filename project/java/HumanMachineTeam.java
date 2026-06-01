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
  Collaboration arrangement combining one or more humans with one or more AI systems to pursue shared goals (Clauses 3.3.3, 5.13).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class HumanMachineTeam extends AIConcept {

  private List<String> humanRoles;
  private List<AISystem> aiSystemsInvolved;
  private String taskAllocation;


}