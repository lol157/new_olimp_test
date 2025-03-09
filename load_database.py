from database_manager import DatabaseManager
from requests_api import RequestCollector
from algorithm_functions import solve_algorithm


def reformat_windows(windows, windows_for_room):
    new_windows = []
    c = 1
    for floor_num, bool_lst in windows.items():
        dct = {}
        last_index = 0
        for i in windows_for_room:
            dct[c] = bool_lst[last_index:last_index + i]
            c += 1
            last_index += i
        new_windows.append(dct)
    return new_windows


if __name__ == '__main__':
    rc = RequestCollector()
    with DatabaseManager() as db:
        db.create_database()

        api_data = rc.get_dates_data()

        result_dict = {}

        for date_key, data in api_data:
            windows = data['windows']['data']
            windows_for_room = data['windows_for_room']['data']

            algorithm_res = solve_algorithm(windows, windows_for_room)
            is_correct = rc.test_algo(date_key, algorithm_res)

            new_windows = reformat_windows(windows, windows_for_room)

            result_dict[date_key] = {
                "windows": new_windows,
                "roomCount": len(algorithm_res),
                "isCorrect": is_correct,
                "roomNumbers": algorithm_res
            }

        db.add_data(result_dict)



