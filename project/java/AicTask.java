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
  Something a system is asked to get done.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AicTask  {

  private String aicTaskKind;
  private String aicTaskGoal;
  private List<String> aicTaskLanguages;
  private List<String> aicTaskPerformanceMeasures;
  private URI aicId;
  private String title;
  private String description;


}