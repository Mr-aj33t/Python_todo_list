from flask import Flask, render_template, request, redirect, url_for # type: ignore
from flask_sqlalchemy import SQLAlchemy # type: ignore
from sqlalchemy import text  # type: ignore # Import the text function

app = Flask(__name__)

# Corrected database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://flask_user:%40J33t%40jk@localhost:3306/todo_list'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)

@app.route("/")
def home():
    todo_list = Todo.query.all()
    return render_template("index.html", todo_list=todo_list)


@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("title")
    new_todo = Todo(title=title, complete=False)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/update/<int:todo_id>")
def update(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/reset", methods=["POST"])
def reset():
    db.session.query(Todo).delete()
    db.session.commit()
    db.session.execute(text("TRUNCATE TABLE todo"))  # Use the text function to declare the SQL expression
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
