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
  A connected device that reads from or acts on its physical surroundings.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AicIotDevice  {

  private List<String> aicDeviceSenses;
  private List<String> aicDeviceActuates;
  private URI aicId;
  private String title;
  private String description;


}