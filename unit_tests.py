from colorama import Fore
from load_database import reformat_windows
from requests_api import RequestCollector
from algorithm_functions import solve_algorithm


def test(func, res_type, *data):
    try:
        if isinstance(func(*data), res_type):
            print(f'{Fore.GREEN}Test passed')
        else:
            print(f'{Fore.RED}Test failed')
    except:
        print(f'{Fore.RED}Test failed')


if __name__ == '__main__':
    rc = RequestCollector()

    test(rc.get_dates_data, list)

    test(
        reformat_windows, list, {
            "floor_1": [False, True, False, True, False, False],
            "floor_2": [True, False, True, False, False, True],
            "floor_3": [False, False, True, False, True, False],
            "floor_4": [False, False, False, True, False, True]
        },
        [3, 2, 1]
    )

    test(
        reformat_windows, list, {
            "floor_1": [False, True, False, True, False, False],
            "floor_2": [True, False, True, True, False, True],
            "floor_3": [True, True, True, False, False, True],
            "floor_4": [True, False, True, False, False, True],
            "floor_5": [False, False, True, False, True, False],
            "floor_6": [False, False, False, True, False, True]
        },
        [2, 3, 1]
    )

    test(
        reformat_windows, list, {
            "floor_1": [False, True, False, True, False, False],
            "floor_2": [False, False, False, True, False, True]
        },
        [2, 1, 3]
    )

    test(
        solve_algorithm, list, {
            "floor_1": [False, True, False, True, False, False],
            "floor_2": [True, False, True, False, False, True],
            "floor_3": [False, False, True, False, True, False],
            "floor_4": [False, False, False, True, False, True]
        },
        [3, 2, 1]
    )

    test(
        solve_algorithm, list, {
            "floor_1": [False, True, False, True, False, False],
            "floor_2": [True, False, True, True, False, True],
            "floor_3": [True, True, True, False, False, True],
            "floor_4": [True, False, True, False, False, True],
            "floor_5": [False, False, True, False, True, False],
            "floor_6": [False, False, False, True, False, True]
        },
        [2, 3, 1]
    )

    test(
        solve_algorithm, list, {
            "floor_1": [False, True, False, True, False, False],
            "floor_2": [False, False, False, True, False, True]
        },
        [2, 1, 3]
    )

