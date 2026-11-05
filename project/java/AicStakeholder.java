package example;

/* metamodel_version: 1.12.0 */
/* version: 2022 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  A person, group or organization with a part in an AI system or an interest in it.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AicStakeholder  {

  private String aicStakeholderRole;
  private List<String> aicStakeholderSubRoles;
  private String aicStakeholderOrganization;
  private String aicStakeholderContact;
  private List<String> aicStakeholderResponsibilities;
  private URI aicId;
  private String title;
  private String description;


}