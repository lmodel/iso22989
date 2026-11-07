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
  What every record has, so that other records can refer to it: an identifier, a title and a description.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AicRecordMixin  {

  private URI aicId;
  private String title;
  private String description;


}