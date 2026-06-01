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
  Recommendation produced by an AI system (Clauses 7.4, 10).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Recommendation extends NamedEntity {

  private String recommendationOutcomeType;
  private Float confidence;
  private List<String> recommendedItems;
  private List<Prediction> basedOnPredictions;


}