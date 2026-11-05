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
  A representation of something, made so that a system can compute with it.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AicModel  {

  private String aicModelType;
  private String aicModelVersion;
  private String aicModelRepresents;
  private URI aicId;
  private String title;
  private String description;


}