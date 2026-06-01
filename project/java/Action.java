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
  Action carried out as a result of an AI-system decision (Clause 7.4.4).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Action extends NamedEntity {

  private String actionTarget;
  private String executionStatus;
  private Decision triggeredBy;


}