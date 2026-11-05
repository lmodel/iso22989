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
  A claim that a system has a property people can rely on, with what backs it.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AicTrustworthinessClaim  {

  private AicSystem aicClaimSystem;
  private String aicClaimProperty;
  private List<String> aicClaimEvidence;
  private String aicClaimMeasure;
  private URI aicId;
  private String title;
  private String description;


}