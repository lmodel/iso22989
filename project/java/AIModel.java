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
  Trained or rule-based model embedded in an AI system. Carries paradigm, algorithm family, dataset references and version metadata.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AIModel extends NamedEntity {

  private String modelParadigm;
  private String algorithmFamily;
  private String engineeringApproach;
  private Dataset trainingDataset;
  private Dataset validationDataset;
  private Dataset testDataset;
  private List<String> hyperparameters;
  private String modelVersion;
  private String trainedOn;
  private Boolean supportsContinuousLearning;
  private Float catastrophicForgettingRisk;
  private Integer parameterCount;
  private String trainingDuration;
  private Float inferenceLatencyMs;
  private Boolean modelCompressionApplied;
  private String neuralNetworkArchitecture;
  private String activationFunction;
  private List<String> trainingPhenomena;


}