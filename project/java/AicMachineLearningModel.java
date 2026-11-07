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
  A model whose numbers were fitted to data by a training run.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AicMachineLearningModel extends AicModel {

  private String aicMlParadigm;
  private String aicMlAlgorithm;
  private List<AicDataset> aicMlDatasets;
  private List<String> aicMlHyperparameters;
  private Integer aicMlParameterCount;
  private LocalDate aicMlTrainedOn;
  private AicMachineLearningModel aicMlRetrainedFrom;
  private Boolean aicMlContinuousLearning;


}