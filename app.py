from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, jsonify
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology

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


GRADES = ["Class-9", "Class-10", "Class-11", "Class-12"]
SUBJECTS = {"title": "Subject", "type": "checkbox", "body": ["Mathematics", "Science"]}
STREAMS = {"title": "Stream", "type": "radio", "body": ["Science", "Commerce"]}


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


@app.route("/student", methods=["GET", "POST"])
def student():
    if request.method == "GET":
        return render_template("forms.html", grades=GRADES, subjects=SUBJECTS)
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

        if not first_name or not last_name or not birthdate or not email or not own_ph or not address or not grade:
            return apology("Required Fields Cannot Be Empty")

        if grade not in GRADES:
            return apology("Error")

        db.execute("INSERT INTO student (first_name, middle_name, last_name, birthdate, email, own_ph, address, address2, grade) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)", first_name, middle_name, last_name, birthdate, email, int(own_ph), address, address2, grade)

        student = db.execute("SELECT * FROM student WHERE first_name=? AND birthdate=?", first_name, birthdate)


        if grade in["Class-9", "Class-10"]:
            return render_template("subject.html", subjects=SUBJECTS, id=student[0]["id"], grade=student[0]["grade"])

        if grade in["Class-11", "Class-12"]:
            return render_template("subject.html", subjects=STREAMS, id=id)


@app.route("/subject")
def subject():

    id = request.form.get("id")
    grade = request.form.get("grade")
    subject = request.form.get("subject")
    subject = request.form.get("stream")

    return render_template("information.html")


@app.route("/about")
def about():
    if request.method == "GET":
        ...
        #TODO
    if request.method == "POST":
        ...
        #TODO