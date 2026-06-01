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
  Metric used to evaluate AI system or model performance (Clause 7.4.3).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class EvaluationMetric extends NamedEntity {

  private String metricName;
  private Float metricValue;
  private String metricUnit;
  private Dataset referenceDataset;


}