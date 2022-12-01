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


CLASSES = ["Class-9", "Class-10", "Class-11", "Class-12"]
SUBJECTS = ["Mathematics", "Science"]


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


@app.route("/student")
def student():
    if request.method == "GET":
        return render_template("forms.html", classes=CLASSES, subjects=SUBJECTS)
    if request.method == "POST":
        first_name = request.form.get("first_name")
        middle_name = request.form.get("middle_name")
        last_name = request.form.get("last_name")
        birthdate = request.form.get("birthdate")
        email = request.form.get("email")
        own_ph = request.form.get("own_ph")
        address = request.form.get("address")
        address2 = request.form.get("address2")
        grade = request.form.get("grade")


@app.route("/subject")
def subject():
    if request.method == "GET":
        return render_template("forms.html", classes=CLASSES, subjects=SUBJECTS)
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