def solve_algorithm(windows, windows_for_room) -> list[int]:
    last_index = 0
    room = 1
    lit_rooms = []

    for _, flags in windows.items():
        for i in windows_for_room:
            if any(flags[last_index:last_index + i]):
                lit_rooms += [room]
            last_index += i
            room += 1
        last_index = 0

    return lit_rooms


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

    result = solve_algorithm(windows, windows_for_room)

    print(result)