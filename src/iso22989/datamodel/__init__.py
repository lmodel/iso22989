"""Data model package for iso22989."""

from pathlib import Path
from .iso22989 import *  # noqa: F403

THIS_PATH = Path(__file__).parent

SCHEMA_DIRECTORY = THIS_PATH.parent / "schema"
MAIN_SCHEMA_PATH = SCHEMA_DIRECTORY / "iso22989.yaml"
