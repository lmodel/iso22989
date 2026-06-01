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
  Label or annotation attached to one or more data samples (Clause 3.2.10).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class DataLabel extends NamedEntity {

  private String labelValue;
  private String labelType;
  private AIStakeholderRole annotator;


}