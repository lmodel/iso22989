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
  Mechanism enabling an AI system to continue operating correctly in the presence of component faults (Clause 5.15.4 context).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class FaultToleranceMechanism extends NamedEntity {

  private String mechanismType;
  private String coverageScope;


}