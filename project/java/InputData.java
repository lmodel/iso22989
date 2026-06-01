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
  Data presented to an AI system at inference time or during training (Clause 3.2.9).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class InputData extends NamedEntity {

  private String dataSourceType;
  private String dataCollectionMethod;
  private String modality;
  private AISystem consumedBy;


}