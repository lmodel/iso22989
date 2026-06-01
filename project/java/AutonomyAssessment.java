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
  Structured assessment of the autonomy level of an AI system using the criteria listed in Clause 5.13.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AutonomyAssessment extends NamedEntity {

  private String autonomyLevel;
  private List<String> autonomyCriterionScores;


}