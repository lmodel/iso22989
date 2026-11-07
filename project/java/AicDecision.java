package example;

/* metamodel_version: 1.12.0 */
/* version: 2022 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  A choice made on the strength of some predictions.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AicDecision  {

  private String aicDecisionOutcome;
  private List<AicPrediction> aicDecisionPredictions;
  private String aicDecisionCriteria;
  private URI aicId;
  private String title;
  private String description;


}