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
  Device participating in an Internet-of-Things deployment (Clause 5.14.2).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class IoTDevice extends NamedEntity {

  private String deviceRole;
  private List<String> sensingCapabilities;
  private List<String> actuatingCapabilities;


}