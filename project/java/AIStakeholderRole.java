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
  Stakeholder role enacted by an organisation or individual in relation to an AI system (Clause 5.19).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AIStakeholderRole extends NamedEntity {

  private String stakeholderRoleType;
  private String organizationName;
  private String contact;
  private List<String> responsibilities;


}