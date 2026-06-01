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
  Decision threshold applied to a metric, prediction or score (Clause 7.4.3).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Threshold extends NamedEntity {

  private float thresholdValue;
  private String appliesToMetric;
  private String thresholdPolicy;


}