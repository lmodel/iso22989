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
  Abstract base class for a glossary term defined in Clause 3. Concrete subclasses partition the terminology along Clauses 3.1–3.7.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public abstract class Term extends NamedEntity {



}