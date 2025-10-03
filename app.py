from flask import Flask, request, render_template, Response, url_for, redirect, session

app = Flask(__name__)

@app.route("/")
def student_profile():
    return render_template("jinja.html", name = "Arun", is_Topper = True, subjects = ["Maths", "Science", "History"])