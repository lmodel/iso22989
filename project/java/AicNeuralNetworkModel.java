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
  A kind of machine learning model built from layers of simple connected units.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AicNeuralNetworkModel extends AicMachineLearningModel {

  private String aicNetworkArchitecture;
  private Integer aicNetworkLayerCount;
  private List<String> aicNetworkActivationFunctions;


}