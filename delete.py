from cs50 import SQL

db = SQL("sqlite:///students.db")

def clear(id):
    db.execute("DELETE FROM subjects WHERE sub_id=?", id)
    db.execute("DELETE FROM streams WHERE str_id=?", id)
    db.execute("DELETE FROM mother WHERE mother_id=?", id)
    db.execute("DELETE FROM father WHERE father_id=?", id)
    db.execute("DELETE FROM student WHERE id=?", id)


clear(2)