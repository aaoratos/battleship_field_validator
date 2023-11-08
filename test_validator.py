import pytest

from .validator import validate_battlefield
from ._test_data import *


def test_validate_battlefield() -> None:
    assert validate_battlefield(VALID_FIELD) == True
    assert validate_battlefield(INVALID_FIELD_WITH_OVERLAP) == False
    assert validate_battlefield(INVALID_FIELD_WRONG_SHIPS_NUMBER) == False
