import json

print(json.dumps({
                "floor_1": [False, True, False, True, False, False],
                "floor_2": [True, False, True, False, False, True],
                "floor_3": [False, False, True, False, True, False],
                "floor_4": [False, False, False, True, False, True]
            }))