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
  Informative mapping between an ISO/IEC 22989 life-cycle stage and an OECD life-cycle stage (Annex A).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OECDLifecycleMapping extends NamedEntity {

  private String isoStage;
  private String oecdStage;
  private String mappingNotes;


}