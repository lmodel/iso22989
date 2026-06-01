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
  System combining AI techniques to emulate human cognitive functions (Clause 5.5).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CognitiveComputingSystem extends AIConcept {

  private List<String> cognitiveCapabilities;


}