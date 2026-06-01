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
  Discrete data-handling process applied to a dataset during AI system development or operation (Clause 5.10).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class DataProcess extends NamedEntity {

  private String processType;
  private Dataset inputDataset;
  private Dataset outputDataset;
  private List<String> parameters;
  private AIStakeholderRole executedBy;


}