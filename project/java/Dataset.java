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
  Collection of data items used by an AI system in a training, validation, test, reference or production role.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Dataset extends NamedEntity {

  private List<String> dataModality;
  private String datasetRole;
  private String dataProvenance;
  private Integer recordCount;
  private String dataQualityNotes;
  private Boolean containsPersonalData;
  private String labelType;
  private Boolean groundTruthAvailable;
  private Integer featureCount;
  private List<DataProcess> dataProcessesApplied;


}