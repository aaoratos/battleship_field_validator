from ._test_data import *
from .validator import validate_battlefield


def test_validate_battlefield() -> None:
    assert validate_battlefield(VALID_FIELD) == True
    assert validate_battlefield(INVALID_FIELD_WITH_OVERLAP) == False
    assert validate_battlefield(INVALID_FIELD_WRONG_SHIPS_NUMBER) == False
    assert validate_battlefield(INVALID_FIELD_EMPTY) == False
    assert validate_battlefield(VALID_FIELD_RANDOM_01) == True
    assert validate_battlefield(VALID_FIELD_RANDOM_02) == True
    assert validate_battlefield(VALID_FIELD_RANDOM_03) == True
    assert validate_battlefield(VALID_FIELD_RANDOM_04) == True
