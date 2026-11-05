"""Checks that the schema's numbers are the standard's, and that every term of
Clause 3 is accounted for.

tests/iso22989_numbers.yaml holds the clause numbers of the table of contents
and each term's number with the element that renders it, or why none does. It
holds numbers and element names only, and no text of the standard. These tests
hold the schema's annotations to that file in both directions.
"""

from pathlib import Path

import yaml

ROOT = Path(__file__).parent.parent
SCHEMA = yaml.safe_load(
    (ROOT / "src" / "iso22989" / "schema" / "iso22989.yaml").read_text(encoding="utf-8")
)
NUMBERS = yaml.safe_load(
    (ROOT / "tests" / "iso22989_numbers.yaml").read_text(encoding="utf-8")
)
# Clause 3's sections and how many terms each holds.
TERMS_PER_SECTION = {
    "3.1": 35,
    "3.2": 15,
    "3.3": 17,
    "3.4": 10,
    "3.5": 18,
    "3.6": 18,
    "3.7": 4,
}


def _elements():
    """Each element of the schema by the name the numbers file gives it, with
    its annotations."""
    for name, cls in SCHEMA["classes"].items():
        yield name, cls.get("annotations") or {}
        for attribute, slot in (cls.get("attributes") or {}).items():
            yield f"{name}.{attribute}", slot.get("annotations") or {}
    for name, enum in SCHEMA["enums"].items():
        yield name, enum.get("annotations") or {}
        for value, definition in enum["permissible_values"].items():
            yield f"{name}#{value}", definition.get("annotations") or {}


def _cited_terms():
    """Each (term number, element) the schema's annotations state."""
    for element, annotations in _elements():
        for number in str(annotations.get("iso22989_term", "")).split(","):
            if number.strip():
                yield number.strip(), element


def test_the_file_lists_every_term_of_clause_3():
    """Every number from 3.1.1 to 3.7.4 is in the file, and nothing else."""
    expected = {
        f"{section}.{n}"
        for section, count in TERMS_PER_SECTION.items()
        for n in range(1, count + 1)
    }
    assert set(NUMBERS["terms"]) == expected
    assert len(expected) == 117


def test_each_term_names_an_element_that_cites_it():
    """A term the file gives an element is one that element cites, and an
    element that cites a term is the one the file gives."""
    named = {
        number: element
        for number, element in NUMBERS["terms"].items()
        if isinstance(element, str)
    }
    assert named == dict(_cited_terms())


def test_a_term_left_out_says_why():
    """A term no element renders gives its reason, and no element cites it."""
    cited = {number for number, _ in _cited_terms()}
    for number, entry in NUMBERS["terms"].items():
        if isinstance(entry, dict):
            assert set(entry) == {"not_modelled"}, number
            assert len(entry["not_modelled"].split()) >= 4, number
            assert number not in cited, number


def test_each_clause_cited_is_in_the_table_of_contents():
    """Every clause annotation names a clause the table of contents lists."""
    clauses = set(NUMBERS["clauses"])
    for element, annotations in _elements():
        if "iso22989_clause" in annotations:
            assert str(annotations["iso22989_clause"]) in clauses, element


def test_the_lifecycle_stages_are_the_standards_eight():
    """AicLifecycleStage holds the eight stages, each citing its own clause of
    6.2, in the standard's order."""
    stages = SCHEMA["enums"]["AicLifecycleStage"]["permissible_values"]
    assert list(stages) == [
        "inception",
        "design_and_development",
        "verification_and_validation",
        "deployment",
        "operation_and_monitoring",
        "continuous_validation",
        "re_evaluation",
        "retirement",
    ]
    assert [v["annotations"]["iso22989_clause"] for v in stages.values()] == [
        f"6.2.{n}" for n in range(2, 10)
    ]


def test_the_stakeholder_roles_are_the_standards_six():
    """AicStakeholderRole holds the six roles of clauses 5.19.2 to 5.19.7."""
    roles = SCHEMA["enums"]["AicStakeholderRole"]["permissible_values"]
    assert [v["annotations"]["iso22989_clause"] for v in roles.values()] == [
        f"5.19.{n}" for n in range(2, 8)
    ]


def test_the_lifecycle_mappings_name_oecd_stages():
    """Each stage's related mappings name values of AicOecdLifecycleStage, and
    every value is named by a stage."""
    oecd = set(SCHEMA["enums"]["AicOecdLifecycleStage"]["permissible_values"])
    named = set()
    stages = SCHEMA["enums"]["AicLifecycleStage"]["permissible_values"]
    for stage, definition in stages.items():
        for mapping in definition.get("related_mappings", []):
            prefix, _, value = mapping.partition("#")
            assert prefix == "iso22989:AicOecdLifecycleStage", stage
            named.add(value)
    assert named == oecd
