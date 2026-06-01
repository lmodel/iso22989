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
  Observed change in the statistical distribution of operational data relative to training data (Clause 5.11.9.1).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class DataDrift extends NamedEntity {

  private String driftType;
  private String detectedAt;
  private Dataset affectedDataset;


}