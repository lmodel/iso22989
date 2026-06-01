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
  Verifiability and validatability claim for an AI system characterised according to the levels in Clause 5.16.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class VerificationValidationFramework extends NamedEntity {

  private String verificationValidationLevel;
  private List<String> verificationMethods;
  private List<String> validationMethods;


}