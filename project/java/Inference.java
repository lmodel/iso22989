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
  Act of deriving conclusions, predictions or recommendations from a model or knowledge base (Clause 3.1.17).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Inference extends NamedEntity {

  private String inferenceStrategy;
  private InferenceEngine performedBy;
  private AIModel overModel;
  private String producedOutput;


}