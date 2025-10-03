from flask import Flask, render_template, redirect, request, Response, url_for, session

app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template("login.html")

# ------------ Login system for form.html ----------------------
# @app.route("/submit", methods = ["POST"])
# def submit():
#     username = request.form.get("username")
#     password = request.form.get("password")
# --------------------------------------------------------------


@app.route("/login", methods = ["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    """if username == "ashutosht05" and password == "pass":
        return render_template("welcome.html", name = username)"""
    
    # Above logic is valid for only one username and password, but what if we have more than one!

    valid_user = {
        "ashutosht05": "pass",
        "ashut05": "pass12",
        "ashukt": "pass23",
        "ashukt05": "pass1234",
    }
    
    if username in valid_user.keys() and password == valid_user[username]:
        return render_template("welcome.html", name = username)
    
    else:
        return "Invalid credentials!"