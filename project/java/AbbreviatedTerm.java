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
  Abbreviation or acronym listed in Clause 4 with its expansion and optional definition reference.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AbbreviatedTerm extends NamedEntity {

  private String expansion;


}