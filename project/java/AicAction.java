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
  What was done because of a decision.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AicAction  {

  private AicDecision aicActionDecision;
  private String aicActionTarget;
  private ZonedDateTime aicActionTime;
  private URI aicId;
  private String title;
  private String description;


}