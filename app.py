from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/dates", methods=["POST", "GET"])
def dates():
    if request.method == "POST":
        date = request.form['date']
        # data от бд
        data = {
            "21.01.2020": {
                "windows": [
                    {
                        1: [True, False, True],
                        2: [True, False]
                    },

                    {
                        4: [True, False, True],
                        5: [True, False]
                    },
                ],

                "roomCount": 4,
                "isCorrect": True,
                "roomNumbers": [1, 2, 3],
            },

            "21.01.2021": {
                "windows": [
                    {
                        1: [True, False, True],
                        2: [True, False]
                    },

                    {
                        4: [True, False, True],
                        5: [True, False]
                    },
                ],

                "roomCount": 4,
                "isCorrect": True,
                "roomNumbers": [1, 2, 3],
            },
        }
        return render_template("windows.html", data=data)

    # dates от бд
    dates = ["dddd", "dddddddd", "ddddddddddd"]
    return render_template("dates.html", dates=dates)


@app.route("/input", methods=["POST", "GET"])
def input():
    if request.method == "POST":
        roomPerFloor = request.form['roomPerFloor']
        windowsPerRoom = request.form['windowsPerRoom']
        lightInfo = request.form['lightInfo']

        # данные в алгоритм
        data = {
            "введенные данные": {
                "windows": [
                    {
                        1: [True, False, True],
                        2: [True, False]
                    },

                    {
                        4: [True, False, True],
                        5: [True, False]
                    },
                ],

                "roomCount": 4,
                "isCorrect": "введенные данные",
                "roomNumbers": [1, 2, 3],
            }
        }
        return render_template("windows.html", data=data)

    return render_template("input.html")


app.run(debug=True)
