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
  Computing and physical processes tied in a loop, each affecting the other.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AicCyberPhysicalSystem  {

  private List<String> aicCpsPhysicalProcesses;
  private AicIotSystem aicCpsIotSystem;
  private List<AicSystem> aicCpsAiSystems;
  private URI aicId;
  private String title;
  private String description;


}