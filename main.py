import string

from test_data import *


def check_ship_part_placement(field: list[list[int]], x: int, y: int) -> bool:
    """
    Checks whether a ship part placement is valid according to the game rules.

    :param field: two-dimensional array representing the battlefield
    :param x: ship's X coordinate on the field
    :param y: ship's Y coordinate on the field
    :return: True if the placement is valid, False if errors were detected (overlap or contact with another ship)
    """
    if not field[x][y]:
        raise ValueError(f'No ship part found at [{x}, {y}]')

    return True


def print_field(field: list[list[int]]) -> None:
    """
    Prints the battlefield in the game format.

    :param field: two-dimensional array representing the battlefield to print
    :return:
    """
    print('  ', *string.ascii_uppercase[:10])
    for i, row in enumerate(field):
        row_num = f' {i + 1} ' if i < 9 else f'{i + 1} '
        print(row_num + ' '.join([col and "*" or "." for col in row]))


def validate_battlefield(field: list[list[int]]) -> bool:
    # TODO: get rid of this stub and implement the proper validation
    if not field[0][0]:
        return False
    return True


def main():
    for i, field in enumerate(TEST_BATTLEFIELDS):
        res = validate_battlefield(field) and 'Valid' or 'Invalid'
        print(f'Test Field #{i + 1}: {res}\n')
        print_field(field)


if __name__ == '__main__':
    main()
