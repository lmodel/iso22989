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
  Description of an AI application instance situated in a domain (Clause 10).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AIApplication extends NamedEntity {

  private List<String> applicationDomain;
  private String intendedPurpose;
  private List<String> jurisdictionalIssues;
  private List<String> societalImpacts;
  private AISystem hostingSystem;


}