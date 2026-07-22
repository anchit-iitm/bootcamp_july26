from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

db = SQLAlchemy(app)

class data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)

with app.app_context():
    db.create_all()

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/hello/<name>")
def hello_name(name):
    return f"hello, {name}!"

@app.route("/about")
def about():
    all_data = data.query.all()
    return render_template("about.html", html_data=all_data)

@app.route("/about/<name>")
def about_name(name):
    return render_template("about_name.html", html_name=name)

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "GET":
        return render_template("contact.html")
    if request.method == "POST":
        user_data = request.form.get('name')
        new_data = data(name=user_data)
        db.session.add(new_data)
        db.session.commit()
        return redirect(url_for('about'))

if __name__ == "__main__":
    app.run(debug=True)