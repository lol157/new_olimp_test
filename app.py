from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/dates", methods=["POST", "GET"])
def dates():
    if request.method == "POST":
        return "post"

    return render_template("dates.html")


@app.route("/input", methods=["POST", "GET"])
def input():
    if request.method == "POST":
        return "post"

    return render_template("input.html")


app.run(debug=True)
