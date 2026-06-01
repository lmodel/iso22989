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
  Individual data record within a dataset (Clause 3.2.13).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class DataSample extends NamedEntity {

  private String samplePayload;
  private String sampleLabel;


}