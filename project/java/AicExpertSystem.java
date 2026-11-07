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
  A system that puts what human specialists know into a form it can reason with.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AicExpertSystem extends AicSystem {

  private List<AicKnowledge> aicExpertKnowledge;
  private String aicExpertInference;


}