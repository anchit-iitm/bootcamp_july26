from flask import Blueprint, request
from models import db, data
from flask_security import auth_token_required, roles_accepted

about_bp = Blueprint('about', __name__)

@about_bp.route("/about", methods=["POST"])
@auth_token_required
def about():
    all_data = data.query.all()
    rows = [{"id": row.id, "name": row.name} for row in all_data]
    return {
        "data": rows,
        "message": "data retrieved successfully"
        }

@about_bp.route("/about/<name>")
def about_name(name):
    return {
        "name": name,
        "message": f"Hello, {name}!"
    }

@about_bp.route("/contact", methods=["POST"])
def contact():
    if request.method == "POST":
        user_data = request.json.get('name')  # getting the name from {"name": "value", "message": "value"} format
        new_data = data(name=user_data)
        db.session.add(new_data)
        db.session.commit()
        return {
            "message": "data added successfully",
            "name": user_data
        }