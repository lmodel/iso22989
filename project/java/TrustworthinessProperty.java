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
  Claim about a trustworthiness property of an AI system or model, with evidence and measurement metadata.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class TrustworthinessProperty extends NamedEntity {

  private String trustworthinessPropertyType;
  private List<String> propertyEvidence;
  private String measurementMethod;
  private List<String> applicableBiases;
  private Float confidenceScore;


}