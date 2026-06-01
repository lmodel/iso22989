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
  Computational unit in a neural network combining weighted inputs with a bias and an activation function (Clause 3.4.9).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Neuron extends AIConcept {

  private String activationFunction;
  private Integer inputArity;


}