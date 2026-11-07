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
  A piece of work done at one stage of a system's life.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AicLifecycleProcess  {

  private String aicLifecycleStage;
  private AicSystem aicLifecycleSystem;
  private List<String> aicLifecycleInputs;
  private List<String> aicLifecycleOutputs;
  private AicStakeholder aicLifecycleResponsible;
  private LocalDate aicLifecycleStart;
  private LocalDate aicLifecycleEnd;
  private URI aicId;
  private String title;
  private String description;


}