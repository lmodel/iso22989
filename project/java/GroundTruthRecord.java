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
  Trusted reference record used to evaluate or train an AI model (Clause 3.2.7).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class GroundTruthRecord extends NamedEntity {

  private String groundTruthValue;
  private String provenanceStatement;


}