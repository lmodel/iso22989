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
  Embodied agent able to perceive its environment and act in the physical world (Clause 5.3 / Clause 9.5 robotics field).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Robot extends NamedEntity {

  private String embodiment;
  private AISystem controlledBy;


}