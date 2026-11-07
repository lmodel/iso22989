# iso22989

This project is a LinkML vocabulary for describing an AI system in the terms of ISO/IEC 22989:2022: the system and its kinds, its models, data and tasks, its stage of life, the parties around it, the trustworthiness claims made for it, and the fields and applications it belongs to. It holds no text of the standard.

- [Schema documentation](elements/index.md), generated from the schema
- [About](about.md): how the elements are named and what the model leaves out
- [Rights](rights.md): what may be reproduced, and what may not
- [`iso22989.yaml`](schema/iso22989.yaml): the schema

## Validating data

`linkml-validate -s src/iso22989/schema/iso22989.yaml -C AicSystem system.yaml` checks a file against the JSON Schema generated from the schema, and `tests/test_data.py` holds every example to it. `project/jsonschema/iso22989.schema.json` is the same schema for anyone without LinkML. Write dates as quoted strings, as JSON carries them, because the validator reads a date as text.

Validate a file before loading it into either model in `src/iso22989/datamodel/`. The dataclasses check required fields and enum values, but no pattern, no minimum and no `any_of` rule. The Pydantic models also check a pattern or a minimum that a field carries. Neither checks the `any_of` rule on `AicIotDevice` or the rules that hold a stakeholder's sub-roles to its role.

No validator checks these rules, and `tests/test_data.py` checks them over the examples:

- that a reference names a record the ecosystem holds, of the class the reference ranges over;
- that no two records share an `aic_id`;
- that a piece of life-cycle work ends on or after the day it begins.
