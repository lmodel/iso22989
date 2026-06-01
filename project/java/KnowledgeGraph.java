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
  Graph-structured knowledge representation, often used for reasoning and retrieval (Clause 8.5).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class KnowledgeGraph extends KnowledgeRepresentation {

  private Integer nodeCount;
  private Integer edgeCount;
  private List<URI> ontologyReference;


}