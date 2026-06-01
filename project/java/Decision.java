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
  Decision produced by an AI system on the basis of one or more predictions (Clause 7.4.3).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Decision extends NamedEntity {

  private String decisionOutcome;
  private String decisionPolicy;
  private List<Prediction> basedOnPredictions;


}