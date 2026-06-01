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
  Record of a single abbreviation listed in Clause 4 of the standard.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AbbreviationEntry extends NamedEntity {

  private String abbreviationCode;
  private String expansion;


}