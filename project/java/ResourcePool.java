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
  Pool of computing resources (CPU/GPU/TPU/ASIC/FPGA) available to AI workloads (Clause 8.7).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ResourcePool extends NamedEntity {

  private String resourceType;
  private String capacityUnits;


}