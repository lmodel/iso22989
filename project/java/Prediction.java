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
  Prediction produced by an AI model (Clause 7.4.2).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Prediction extends NamedEntity {

  private String predictedValue;
  private Float confidence;
  private AIModel producedBy;


}