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
  System whose behaviour is driven by the explicit semantics of its inputs and knowledge sources (Clause 5.6).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class SemanticComputingSystem extends AIConcept {

  private String semanticModel;


}