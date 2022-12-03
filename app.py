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


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


GRADES = ["Class-9", "Class-10", "Class-11", "Class-12"]
SUBJECTS = {"title": "Subject", "type": "checkbox", "body": ["Mathematics", "Science"]}
STREAMS = {"title": "Stream", "type": "radio", "body": ["Science", "Commerce"]}


@app.route("/")
def index():
    session["user_id"] = 0
    return render_template("index.html")


@app.route("/admissions", methods=["GET", "POST"])
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
        if session["user_id"] != 0:
            student = db.execute("SELECT * FROM student WHERE id=?", session["user_id"])
            student = student[0]

            return render_template("forms.html", grades=GRADES, subjects=SUBJECTS, student=student)

        student = {}
        return render_template("forms.html", grades=GRADES, subjects=SUBJECTS, student=student)
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

        session["user_id"] = student[0]["id"]

        return redirect("/subject")




@app.route("/subject", methods=["GET", "POST"])
def subject():
    if request.method == "GET":
        student = db.execute("SELECT * FROM student WHERE id=?", session["user_id"])
        grade = student[0]["grade"]

        if grade in ["Class-9", "Class-10"]:
            return render_template("subject.html", subjects=SUBJECTS, id=student[0]["id"], grade=student[0]["grade"])

        if grade in ["Class-11", "Class-12"]:
            return render_template("subject.html", subjects=STREAMS, id=student[0]["id"], grade=student[0]["grade"])


    if request.method == "POST":
        id = request.form.get("id")
        grade = request.form.get("grade")
        subject = request.form.get("subject")
        stream = request.form.get("stream")

        if stream:
            db.execute("INSERT INTO streams (str_id, grade, stream) VALUES(?, ?, ?)", id, grade, stream)

        if subject:
            db.execute("INSERT INTO subjects (sub_id, grade, subject) VALUES(?, ?, ?)", id, grade, subject)

        return redirect("/parents")


@app.route("/parents", methods=["GET", "POST"])
def parents():
    if request.method == "GET":
        
        student = db.execute("SELECT * FROM student WHERE id=?", session["user_id"])

        father = db.execute("SELECT * FROM father WHERE id=?", session["user_id"])
        mother = db.execute("SELECT * FROM mother WHERE id=?", session["user_id"])

        if not father or not mother:
            return render_template("parents.html", id=student[0]["id"])

        return render_template("parents.html", id=student[0]["id"])

    if request.method == "POST":
        f_f_name = request.form.get("f_first_name")
        f_m_name = request.form.get("f_middle_name")
        f_l_name = request.form.get("f_last_name")
        f_email = request.form.get("f_email")
        f_own_ph = request.form.get("f_own_ph")
        f_occupation = request.form.get("f_occupation")

        m_f_name = request.form.get("m_first_name")
        m_m_name = request.form.get("m_middle_name")
        m_l_name = request.form.get("m_last_name")
        m_email = request.form.get("m_email")
        m_own_ph = request.form.get("m_own_ph")
        m_occupation = request.form.get("m_occupation")

        db.execute("INSERT INTO father (father_id, first_name, middle_name, last_name, email, ph_no, occupation) VALUES(?, ?, ?, ?, ?, ?, ?", session["user_id"], f_f_name, f_m_name, f_l_name, f_email, f_own_ph, f_occupation)
        db.execute("INSERT INTO mother (mother_id, first_name, middle_name, last_name, email, ph_no, occupation) VALUES(?, ?, ?, ?, ?, ?, ?", session["user_id"], m_f_name, m_m_name, m_l_name, m_email, m_own_ph, m_occupation)

        request("/comfirm")


@app.route("/about", methods=["GET", "POST"])
def about():
    if request.method == "GET":
        ...
        #TODO
    if request.method == "POST":
        ...
        #TODO

    
@app.route("/clear", methods=["GET", "POST"])
def clear():
    session["user_id"] = 0
    return redirect("/student")