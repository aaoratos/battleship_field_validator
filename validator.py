import string


def print_field(field: list[list[int]]) -> None:
    print("  ", *string.ascii_uppercase[:10])
    for i, row in enumerate(field):
        print(f"{i + 1:>2} " + " ".join([col and "*" or "." for col in row]))


def validate_battlefield(field: list[list[int]]) -> bool:
    ships = {1: 0, 2: 0, 3: 0, 4: 0}
    check_f = lambda f, y, x: x + 1 < 10 and f[y][x + 1]
    check_df = lambda f, y, x: y + 1 < 10 and x + 1 < 10 and f[y + 1][x + 1]
    check_db = lambda f, y, x: y + 1 < 10 and x - 1 > 0 and f[y + 1][x - 1]
    check_overlap = lambda f, y, x: check_df(f, y, x) or check_db(f, y, x)
    y_count = [0] * 10
    x_count = 0

    # Алгоритм полагается на тот факт, что мы идём слева направо, сверху вниз,
    # начиная с левого верхнего угла. Таким образом, на каждой итерации
    # нам нужно проверять только клетки в области начиная от диагонали
    # лево-вниз относительно текущей клетки, до клетки справа от текущей,
    # если двигаться против часовой стрелки. Отдельное внимание следует уделить
    # последним строкам и столбцам.

    for i in range(10):
        for j in range(10):
            # если в клетке нет корабля, то проверяем - его просто нет или он закончился
            if not field[i][j]:
                # если в этой колонке выше был корабль (счётчик частей
                # корабля по оси Y в этой колонке не пустой),
                # значит он закончился
                if y_count[j]:
                    # проверяем, не слишком ли много частей мы насчитали
                    if y_count[j] > 4:
                        return False
                    # увеличиваем счётчик кораблей соответствующего размера
                    ships[y_count[j]] += 1
                    # и обнуляем счётчик частей корабля по оси Y в этой колонке
                    y_count[j] = 0
                    continue

                # если счётчик частей корабля по оси Х не пустой,
                # значит горизонтальный корабль закончился
                elif x_count:
                    # проверяем, не слишком ли много частей мы насчитали
                    if x_count > 4:
                        return False
                    # увеличиваем сётчик кораблей соответствующего размера
                    ships[x_count] += 1
                    # и обнуляем счётчик частей корабля по оси X
                    x_count = 0
                    continue

            # в текущей клетке есть корабль
            else:
                # сразу проверяем, есть ли корабли по диагоналям
                # вниз (df, db) от текущей клетки
                if check_overlap(field, i, j):
                    # если есть, то поле не валидно,
                    # дальше можно не продолжать
                    return False

                # если в этой колонке выше был корабль,
                # то увеличиваем счётчик частей по оси Y в этой колонке
                if y_count[j]:
                    y_count[j] += 1
                    continue

                # если в этом ряду слева был корабль,
                # то увеличивеаем счётчик частей по оси X
                elif x_count:
                    x_count += 1
                    # если мы на последней колонке, то обнуляем счётчик по оси X
                    # и заносим что насчитали в счётчик кораблей
                    if j + 1 == 10:
                        ships[x_count] += 1
                        x_count = 0
                    continue

                # если условия выше не выполняются,
                # но справа есть часть корабля,
                # значит корабль - горизонтальный;
                # начинаем считать по оси X
                elif check_f(field, i, j):
                    x_count += 1
                    continue

                # если ни одно условие выше не выполняется,
                # начинаем считать по оси Y
                else:
                    y_count[j] += 1
                    continue

    # заносим в счётчик корабли заканчивающиеся на последней строке, если есть
    for i in y_count:
        if i > 0:
            if i > 4:
                return False
            ships[i] += 1

    return ships[1] == 4 and ships[2] == 3 and ships[3] == 2 and ships[4] == 1
