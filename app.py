from flask import Flask, render_template, redirect, request, Response, url_for, session

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")
