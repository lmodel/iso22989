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
  A body of computing resource that AI work can draw on.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AicResourcePool  {

  private String aicPoolKind;
  private String aicPoolHardware;
  private String aicPoolCapacity;
  private URI aicId;
  private String title;
  private String description;


}