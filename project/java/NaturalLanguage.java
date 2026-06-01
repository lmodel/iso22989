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
  Natural language treated as an object of processing or generation by an AI system (Clause 9.2).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class NaturalLanguage extends AIConcept {

  private String languageCode;
  private String script;


}