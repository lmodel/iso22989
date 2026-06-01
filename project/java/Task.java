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
  AI task addressed by a model or system (e.g. classification, regression, planning). Provides a first-class entity for the task categories enumerated across Clause 3 terminology.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Task extends NamedEntity {

  private String taskCategory;
  private List<String> inputModalities;
  private String outputLabelType;
  private List<String> performanceMetric;


}