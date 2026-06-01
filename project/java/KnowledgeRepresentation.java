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
  Representation of knowledge usable by an AI system (Clause 5.4), including knowledge graphs, ontologies and rule bases.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class KnowledgeRepresentation extends AIConcept {

  private String symbolicApproach;
  private String knowledgeType;
  private String representationForm;


}