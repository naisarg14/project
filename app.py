from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, jsonify
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash


# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///students.db")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/admissions")
def admissions():
    if request.method == "GET":
        ...
        #TODO
    if request.method == "POST":
        ...
        #TODO


@app.route("/forms")
def forms():
    if request.method == "GET":
        return render_template("forms.html")
    if request.method == "POST":
        ...
        #TODO


@app.route("/about")
def about():
    if request.method == "GET":
        ...
        #TODO
    if request.method == "POST":
        ...
        #TODO