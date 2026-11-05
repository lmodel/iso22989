"""Data test."""

import glob
import json
import os
from pathlib import Path

import jsonschema
import pytest
import yaml
from linkml.validator import validate
from linkml_runtime.loaders import yaml_loader
from linkml_runtime.utils.schemaview import SchemaView

import iso22989.datamodel.iso22989

ROOT = Path(__file__).parent.parent
DATA_DIR = Path(__file__).parent / "data"
DATA_DIR_VALID = DATA_DIR / "valid"
DATA_DIR_INVALID = DATA_DIR / "invalid"

VALID_EXAMPLE_FILES = sorted(glob.glob(os.path.join(DATA_DIR_VALID, "*.yaml")))
INVALID_EXAMPLE_FILES = sorted(glob.glob(os.path.join(DATA_DIR_INVALID, "*.yaml")))

SCHEMA = ROOT / "src" / "iso22989" / "schema" / "iso22989.yaml"
COMMITTED_JSON_SCHEMA = ROOT / "project" / "jsonschema" / "iso22989.schema.json"


def _class_of(filepath):
    return Path(filepath).stem.split("-")[0]


@pytest.mark.parametrize("filepath", VALID_EXAMPLE_FILES)
def test_valid_data_files(filepath):
    """Each valid example loads into the generated dataclass of its class."""
    tgt_class = getattr(iso22989.datamodel.iso22989, _class_of(filepath))
    obj = yaml_loader.load(filepath, target_class=tgt_class)
    assert obj


# The JSON Schema the validator generates is the one check that applies every
# constraint, so each example is held to it: a valid one must pass, and a
# counter-example must fail. The examples quote their dates, as JSON carries
# them, because the validator reads a date as text.
@pytest.mark.parametrize("filepath", VALID_EXAMPLE_FILES)
def test_valid_data_files_validate(filepath):
    """Every valid example passes the validator."""
    report = validate(
        yaml.safe_load(Path(filepath).read_text(encoding="utf-8")),
        str(SCHEMA),
        _class_of(filepath),
    )
    assert not report.results, [r.message for r in report.results]


@pytest.mark.parametrize("filepath", VALID_EXAMPLE_FILES)
def test_valid_data_files_pass_the_committed_json_schema(filepath):
    """Every valid example passes the JSON Schema a user without LinkML takes."""
    document = json.loads(COMMITTED_JSON_SCHEMA.read_text(encoding="utf-8"))
    schema = {
        "$schema": document["$schema"],
        "$defs": document["$defs"],
        "$ref": f"#/$defs/{_class_of(filepath)}",
    }
    jsonschema.validate(
        yaml.safe_load(Path(filepath).read_text(encoding="utf-8")),
        schema,
        cls=jsonschema.Draft201909Validator,
    )


@pytest.mark.parametrize("filepath", INVALID_EXAMPLE_FILES)
def test_invalid_data_files_fail(filepath):
    """Every counter-example fails the validator at the place its first line
    names, as `# Fails at: <JSON pointer>`, so a file that starts failing for
    another reason fails this test."""
    text = Path(filepath).read_text(encoding="utf-8")
    first = text.splitlines()[0]
    assert first.startswith("# Fails at: "), (
        f"{filepath}: the first line names where it fails, as # Fails at: /key"
    )
    pointer = first.removeprefix("# Fails at: ").strip()
    report = validate(yaml.safe_load(text), str(SCHEMA), _class_of(filepath))
    messages = [r.message for r in report.results]
    assert any(m.endswith(f" in {pointer}") for m in messages), messages


def test_every_class_has_an_example():
    """Each class that data can be written in has a valid example: every class
    but the mixin."""
    classes = {
        name
        for name, cls in yaml.safe_load(SCHEMA.read_text())["classes"].items()
        if not cls.get("abstract") and not cls.get("mixin")
    }
    examples = {_class_of(f) for f in VALID_EXAMPLE_FILES}
    assert classes <= examples, sorted(classes - examples)


# The rules the validator cannot check, held over the examples. docs/index.md
# lists them.
VIEW = SchemaView(str(SCHEMA))
CLASSES = set(VIEW.all_classes())
DESIGNATORS = {
    name: slot.name
    for name in CLASSES
    for slot in VIEW.class_induced_slots(name)
    if slot.designates_type
}
ROLE_OF = {
    name: value.annotations["role"].value
    for name, value in VIEW.get_enum(
        "AicStakeholderSubRole"
    ).permissible_values.items()
}


def _records(node, cls, found):
    """Collect every record a document holds, as (class, data), with each
    inlined record under the class its slot ranges over, or the class its
    designator names."""
    if isinstance(node, list):
        for item in node:
            _records(item, cls, found)
        return
    if not isinstance(node, dict):
        return
    cls = node.get(DESIGNATORS.get(cls, ""), cls)
    found.append((cls, node))
    slots = {s.name: s for s in VIEW.class_induced_slots(cls)}
    for key, value in node.items():
        slot = slots.get(key)
        if slot and slot.range in CLASSES and (slot.inlined or slot.inlined_as_list):
            _records(value, slot.range, found)


def _all_records(filepath):
    found = []
    _records(
        yaml.safe_load(Path(filepath).read_text(encoding="utf-8")),
        _class_of(filepath),
        found,
    )
    return found


def _is_kind_of(cls, ancestor):
    return ancestor in VIEW.class_ancestors(cls)


def unresolved_references(records):
    """Each reference that names no record of the class it ranges over, and
    each identifier two records share."""
    problems = []
    by_id = {}
    for cls, data in records:
        if "aic_id" in data:
            if data["aic_id"] in by_id:
                problems.append(f"{data['aic_id']} is used twice")
            by_id[data["aic_id"]] = cls
    for cls, data in records:
        slots = {s.name: s for s in VIEW.class_induced_slots(cls)}
        for key, value in data.items():
            slot = slots.get(key)
            if (
                not slot
                or slot.range not in CLASSES
                or slot.inlined
                or slot.inlined_as_list
            ):
                continue
            for target in value if isinstance(value, list) else [value]:
                if target not in by_id:
                    problems.append(f"{key} names {target}, which is not held")
                elif not _is_kind_of(by_id[target], slot.range):
                    problems.append(
                        f"{key} names {target}, a {by_id[target]}, not a {slot.range}"
                    )
    return problems


def misplaced_sub_roles(stakeholder):
    """Each sub-role that sits under a role other than the record's."""
    role = stakeholder.get("aic_stakeholder_role")
    return [
        sub
        for sub in stakeholder.get("aic_stakeholder_sub_roles", [])
        if ROLE_OF[sub] != role
    ]


ECOSYSTEMS = [f for f in VALID_EXAMPLE_FILES if _class_of(f) == "AicEcosystem"]


@pytest.mark.parametrize("filepath", ECOSYSTEMS)
def test_an_ecosystem_resolves_its_references(filepath):
    """Within a whole ecosystem, no two records share an aic_id, and each
    reference names a record the ecosystem holds, of the class it ranges over."""
    assert not unresolved_references(_all_records(filepath))


def test_the_reference_check_finds_a_fault():
    """The check above finds a dangling reference, a reference to the wrong
    class and a repeated identifier."""
    system = {"aic_id": "ex:s", "aic_system_type": "AicSystem"}
    assert unresolved_references(
        [("AicSystem", {**system, "aic_system_models": ["ex:gone"]})]
    ) == ["aic_system_models names ex:gone, which is not held"]
    wrong = unresolved_references(
        [("AicSystem", {**system, "aic_system_models": ["ex:s"]})]
    )
    assert wrong == ["aic_system_models names ex:s, a AicSystem, not a AicModel"]
    assert "ex:s is used twice" in unresolved_references(
        [("AicSystem", system), ("AicSystem", system)]
    )


@pytest.mark.parametrize("filepath", VALID_EXAMPLE_FILES)
def test_every_sub_role_sits_under_the_records_role(filepath):
    """A sub-role belongs to the role the record states."""
    for cls, data in _all_records(filepath):
        if cls == "AicStakeholder":
            assert not misplaced_sub_roles(data), data["aic_id"]


def test_the_sub_role_check_finds_a_fault():
    """A regulator cannot be a kind of AI provider."""
    assert misplaced_sub_roles(
        {"aic_stakeholder_role": "ai_provider", "aic_stakeholder_sub_roles": ["regulator"]}
    ) == ["regulator"]


def test_every_role_has_a_sub_role():
    """The sub-roles name only the six roles, and each role has at least one."""
    roles = set(VIEW.get_enum("AicStakeholderRole").permissible_values)
    assert set(ROLE_OF.values()) == roles
    assert len(roles) == 6


@pytest.mark.parametrize("filepath", VALID_EXAMPLE_FILES)
def test_a_lifecycle_process_ends_on_or_after_its_start(filepath):
    """A piece of life-cycle work ends on or after the day it begins."""
    for cls, data in _all_records(filepath):
        if cls == "AicLifecycleProcess" and "aic_lifecycle_end" in data:
            assert data["aic_lifecycle_start"] <= data["aic_lifecycle_end"]
