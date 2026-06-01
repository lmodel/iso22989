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
  Networked system composed of IoT devices, possibly enhanced with AI capabilities (Clause 5.14.2).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class IoTSystem extends NamedEntity {

  private List<IoTDevice> devices;
  private List<AIComponent> aiComponents;


}