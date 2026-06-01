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
  Use of AI to enhance the cognitive capabilities of humans rather than replace them (Clause 5.13 context).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class IntelligenceAugmentation extends AIConcept {

  private List<String> augmentedCapability;


}