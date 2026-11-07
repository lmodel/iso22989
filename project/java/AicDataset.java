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
  A set of data kept together in one format.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AicDataset  {

  private List<String> aicDatasetRoles;
  private String aicDatasetSource;
  private Integer aicDatasetSampleCount;
  private List<String> aicDatasetLabels;
  private String aicDatasetGroundTruth;
  private Boolean aicDatasetHoldsPii;
  private List<AicDataProcess> aicDatasetProcesses;
  private URI aicId;
  private String title;
  private String description;


}