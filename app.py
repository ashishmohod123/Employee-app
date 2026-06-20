from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect("employees.db")
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS employees(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            dept TEXT,
            salary INTEGER
        )
    """)
    conn.commit()
    conn.close()

init_db()

@app.route("/")
def home():
    conn = sqlite3.connect("employees.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM employees")
    data = cur.fetchall()
    conn.close()
    return render_template("index.html", employees=data)


@app.route("/add", methods=["GET", "POST"])
def add_employee():
    if request.method == "POST":
        name = request.form["name"]
        dept = request.form["dept"]
        salary = request.form["salary"]

        conn = sqlite3.connect("employees.db")
        cur = conn.cursor()
        cur.execute("INSERT INTO employees(name, dept, salary) VALUES(?,?,?)",
                    (name, dept, salary))
        conn.commit()
        conn.close()
        return redirect("/")
    return render_template("add.html")

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    conn = sqlite3.connect("employees.db")
    cur = conn.cursor()

    if request.method == "POST":
        name = request.form["name"]
        dept = request.form["dept"]
        salary = request.form["salary"]

        cur.execute(
            "UPDATE employees SET name=?, dept=?, salary=? WHERE id=?",
            (name, dept, salary, id)
        )

        conn.commit()
        conn.close()

        return redirect("/")

    cur.execute("SELECT * FROM employees WHERE id=?", (id,))
    employee = cur.fetchone()

    conn.close()

    return render_template("edit.html", employee=employee)


@app.route("/delete/<int:id>")
def delete(id):
    conn = sqlite3.connect("employees.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM employees WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)