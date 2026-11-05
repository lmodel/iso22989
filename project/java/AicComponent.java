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
  A part of a system that does one job in it.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AicComponent  {

  private String aicComponentStep;
  private List<AicComponent> aicComponentDependsOn;
  private URI aicId;
  private String title;
  private String description;


}