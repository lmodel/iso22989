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
  A body of what a system knows, in a form it can use.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AicKnowledge  {

  private String aicKnowledgeKind;
  private String aicKnowledgeRepresentation;
  private URI aicId;
  private String title;
  private String description;


}