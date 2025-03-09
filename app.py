from flask import Flask, render_template, request
from database_manager import DatabaseManager
from algorithm_functions import solve_algorithm
from load_database import reformat_windows
import json

app = Flask(__name__)


@app.route("/dates", methods=["POST", "GET"])
def dates():
    with DatabaseManager() as db:
        data = db.get_data()
        if request.method == "POST":
            date = request.form['date']
            res = {date: data[date]} if date != 'all_dates' else data

            return render_template("windows.html", data=res)

        # dates от бд
        dates = data.keys()
    return render_template("dates.html", dates=dates)


@app.route("/input", methods=["POST", "GET"])
def input():
    if request.method == "POST":
        roomPerFloor = request.form['roomPerFloor']
        windowsPerRoom = json.loads(request.form['windowsPerRoom'])
        lightInfo = json.loads(request.form['lightInfo'])
        algorithm_res = solve_algorithm(lightInfo, windowsPerRoom)

        # данные в алгоритм
        data = {
            "введенные данные": {
                "windows": reformat_windows(lightInfo, windowsPerRoom),
                "roomCount": roomPerFloor,
                "isCorrect": "введенные данные",
                "roomNumbers": algorithm_res,
            }
        }
        return render_template("windows.html", data=data)

    return render_template("input.html")


app.run(debug=True)
