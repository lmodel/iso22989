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
  One verification or validation of a system.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AicAssessment  {

  private String aicAssessmentKind;
  private AicSystem aicAssessmentSystem;
  private String aicAssessmentMethod;
  private String aicAssessmentResult;
  private LocalDate aicAssessmentDate;
  private URI aicId;
  private String title;
  private String description;


}