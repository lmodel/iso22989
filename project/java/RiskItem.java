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
  Risk associated with an AI system, capturing source, potential event, consequence and treatment metadata (Clause 3.5.11; aligned with ISO/IEC 23894 risk concepts).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class RiskItem extends NamedEntity {

  private String riskSource;
  private String potentialEvent;
  private String consequence;
  private Float likelihood;
  private String severity;
  private List<String> mitigationStrategy;
  private List<AIStakeholderRole> affectedStakeholders;


}