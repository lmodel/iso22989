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
  System that tightly integrates computational and physical components, typically with feedback loops between sensing and actuation (Clause 5.14.3).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CyberPhysicalSystem extends NamedEntity {

  private List<String> physicalProcesses;
  private List<AIComponent> cyberComponents;
  private IoTSystem iotSubsystem;


}