from ._test_data import *
from .validator import validate_battlefield


def test_validate_battlefield() -> None:
    assert validate_battlefield(VALID_FIELD) is True
    assert validate_battlefield(INVALID_FIELD_WITH_OVERLAP) is False
    assert validate_battlefield(INVALID_FIELD_WRONG_SHIPS_NUMBER) is False
    assert validate_battlefield(INVALID_FIELD_EMPTY) is False
    assert validate_battlefield(VALID_FIELD_RANDOM_01) is True
    assert validate_battlefield(VALID_FIELD_RANDOM_02) is True
    assert validate_battlefield(VALID_FIELD_RANDOM_03) is True
    assert validate_battlefield(VALID_FIELD_RANDOM_04) is True
