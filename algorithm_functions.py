def solve_algorithm(windows, windows_for_room):
    # Тут твой код
    return [1, 2, 4, 6, 7,  8, 11, 12]  # Формат возвращаемых данных


if __name__ == '__main__':
    windows = {
        "floor_1": [
            False,
            True,
            False,
            True,
            False,
            False
        ],
        "floor_2": [
            True,
            False,
            True,
            False,
            False,
            True
        ],
        "floor_3": [
            False,
            False,
            True,
            False,
            True,
            False
        ],
        "floor_4": [
            False,
            False,
            False,
            True,
            False,
            True
        ]
    }
    windows_for_room = [3, 2, 1]

    solve_algorithm(windows, windows_for_room)
