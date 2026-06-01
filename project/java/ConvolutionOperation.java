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
  Convolution operation as used in convolutional neural networks (Clause 3.4.3).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ConvolutionOperation extends AIConcept {

  private List<Integer> kernelSize;
  private Integer stride;
  private String padding;


}