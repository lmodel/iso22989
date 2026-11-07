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
  A system that moves or acts on physical things through its own actuators.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AicRobot extends AicSystem {

  private List<String> aicRobotActuators;
  private List<String> aicRobotSensors;


}