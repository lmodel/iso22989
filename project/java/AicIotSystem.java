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
  A networked system that links devices and offers services built on them.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AicIotSystem  {

  private List<AicIotDevice> aicIotDevices;
  private List<AicSystem> aicIotAiSystems;
  private URI aicId;
  private String title;
  private String description;


}