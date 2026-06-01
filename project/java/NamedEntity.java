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
  Abstract base class for any addressable entity in the schema, carrying identity, label and clause-reference metadata.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public abstract class NamedEntity  {

  private URI id;
  private String name;
  private String description;
  private String clauseReference;
  private List<String> aliases;
  private String preferredLabel;
  private List<URI> seeAlsoUri;


}