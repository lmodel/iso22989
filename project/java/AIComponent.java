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
  Functional component of an AI system, such as a data pipeline, preprocessor, model server, or post-processing module.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AIComponent extends NamedEntity {

  private String componentFunction;
  private List<AIComponent> dependsOn;


}