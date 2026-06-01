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
  AIModel realised as a neural network (Clause 5.12.1, Clause 3.4 terms).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class NeuralNetworkModel extends AIModel {

  private Integer numberOfLayers;
  private Integer numberOfParameters;


}