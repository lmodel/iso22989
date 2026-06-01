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
  Phenomenon by which a continually-trained model loses previously acquired competence (Clause 5.11.9.1).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CatastrophicForgetting extends NamedEntity {

  private AIModel affectedModel;
  private String mitigationStrategy;


}