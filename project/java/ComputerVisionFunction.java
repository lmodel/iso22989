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
  Computer-vision capability provided by an AI system (Clause 9.1).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ComputerVisionFunction extends NamedEntity {

  private String cvTask;


}