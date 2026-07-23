from flask import Flask, request
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

@app.route("/about", methods=["POST"])
def about():
    all_data = data.query.all()
    rows = [{"id": row.id, "name": row.name} for row in all_data]
    return {
        "data": rows,
        "message": "data retrieved successfully"}

@app.route("/about/<name>")
def about_name(name):
    return {
        "name": name,
        "message": f"Hello, {name}!"
    }

@app.route("/contact", methods=["POST"])
def contact():
    if request.method == "POST":
        user_data = request.json.get('name')
        new_data = data(name=user_data)
        db.session.add(new_data)
        db.session.commit()
        return {
            "message": "data added successfully",
            "name": user_data
        }




if __name__ == "__main__":
    app.run(debug=True)