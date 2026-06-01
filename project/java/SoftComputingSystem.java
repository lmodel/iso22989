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
  System employing soft computing techniques tolerant of imprecision and uncertainty (Clause 5.7).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class SoftComputingSystem extends AIConcept {

  private List<String> softComputingTechniques;


}