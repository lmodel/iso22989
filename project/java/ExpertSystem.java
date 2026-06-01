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
  Rule-based system encoding domain expertise (Clause 8.5.2).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ExpertSystem extends NamedEntity {

  private Integer ruleCount;
  private InferenceEngine inferenceEngine;


}