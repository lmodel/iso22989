"""Data-driven tests for the ISO/IEC 22989 LinkML schema.

Two example corpora drive these tests:

* ``tests/data/valid/``   — records that MUST load and validate cleanly.
* ``tests/data/invalid/`` — counter-examples that MUST be rejected by schema
  validation. Each counter-example carries a header comment naming the single
  constraint it violates (enum, required slot, pattern, min/max value, type).

In both directories the file-name stem up to the first ``-`` names the target
class, e.g. ``AISystem-001.yaml`` is validated against class ``AISystem``.
"""

import glob
import os
from pathlib import Path

import pytest
import yaml
from linkml_runtime import SchemaView
from linkml_runtime.loaders import yaml_loader
from linkml.validator import validate

import iso22989.datamodel.iso22989 as datamodel

SCHEMA = Path(__file__).parents[1] / "src" / "iso22989" / "schema" / "iso22989.yaml"

DATA_DIR_VALID = Path(__file__).parent / "data" / "valid"
DATA_DIR_INVALID = Path(__file__).parent / "data" / "invalid"

VALID_EXAMPLE_FILES = sorted(glob.glob(os.path.join(DATA_DIR_VALID, "*.yaml")))
INVALID_EXAMPLE_FILES = sorted(glob.glob(os.path.join(DATA_DIR_INVALID, "*.yaml")))


def _target_class(filepath):
    """Infer the target class name from the file stem (text before the first '-')."""
    return Path(filepath).stem.split("-")[0]


def _id(filepath):
    """Readable pytest id: the bare file name."""
    return Path(filepath).name


@pytest.fixture(scope="session")
def schemaview():
    """Parsed schema, shared across tests."""
    return SchemaView(str(SCHEMA))


# ---------------------------------------------------------------------------
# Structural guards — fail loudly if the fixtures or schema go missing, so the
# parametrized tests below can never pass vacuously.
# ---------------------------------------------------------------------------


def test_schema_loads(schemaview):
    """The schema parses and exposes its expected tree-root container."""
    classes = schemaview.all_classes()
    assert "AIConceptsCollection" in classes
    assert "AISystem" in classes


def test_example_corpora_present():
    """Both example directories contain at least one fixture."""
    assert VALID_EXAMPLE_FILES, f"no valid examples under {DATA_DIR_VALID}"
    assert INVALID_EXAMPLE_FILES, f"no invalid examples under {DATA_DIR_INVALID}"


@pytest.mark.parametrize(
    "filepath", VALID_EXAMPLE_FILES + INVALID_EXAMPLE_FILES, ids=_id
)
def test_example_filename_names_a_real_class(filepath, schemaview):
    """Every fixture's stem maps to a concrete class in the schema."""
    target_class_name = _target_class(filepath)
    cls = schemaview.get_class(target_class_name)
    assert cls is not None, f"{filepath}: '{target_class_name}' is not a schema class"
    assert not cls.abstract, f"{filepath}: '{target_class_name}' is abstract"


# ---------------------------------------------------------------------------
# Positive / negative validation
# ---------------------------------------------------------------------------


@pytest.mark.parametrize("filepath", VALID_EXAMPLE_FILES, ids=_id)
def test_valid_data_files(filepath):
    """Valid data files load via the Python model and validate cleanly."""
    target_class_name = _target_class(filepath)
    tgt_class = getattr(datamodel, target_class_name)
    obj = yaml_loader.load(filepath, target_class=tgt_class)
    assert obj

    report = validate(
        yaml.safe_load(Path(filepath).read_text()), str(SCHEMA), target_class_name
    )
    assert not report.results, (
        f"{filepath} unexpectedly failed validation: {report.results}"
    )


@pytest.mark.parametrize("filepath", INVALID_EXAMPLE_FILES, ids=_id)
def test_invalid_data_files(filepath):
    """Invalid (counter-example) data files are rejected by schema validation."""
    target_class_name = _target_class(filepath)
    report = validate(
        yaml.safe_load(Path(filepath).read_text()), str(SCHEMA), target_class_name
    )
    assert report.results, f"{filepath} unexpectedly passed validation"
