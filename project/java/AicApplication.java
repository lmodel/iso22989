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
  One use of a system in a line of work.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AicApplication  {

  private AicSystem aicApplicationSystem;
  private String aicApplicationDomain;
  private String aicApplicationSector;
  private String aicApplicationPurpose;
  private URI aicId;
  private String title;
  private String description;


}