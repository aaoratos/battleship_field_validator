from ._test_data import *
from .validator import validate_battlefield


def test_validate_battlefield() -> None:
    assert validate_battlefield(VALID_FIELD) == True
    assert validate_battlefield(INVALID_FIELD_WITH_OVERLAP) == False
    assert validate_battlefield(INVALID_FIELD_WRONG_SHIPS_NUMBER) == False
    assert validate_battlefield(VALID_FIELD_RANDOM_85) == True
    assert validate_battlefield(VALID_FIELD_RANDOM_49) == True
    assert validate_battlefield(VALID_FIELD_RANDOM_111) == True
