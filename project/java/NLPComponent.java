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
  Component of a natural-language-processing pipeline (Clause 9.2).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class NLPComponent extends NamedEntity {

  private String nlpComponentType;


}