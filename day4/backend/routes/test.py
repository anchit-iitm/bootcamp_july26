from flask import Blueprint

test_bp = Blueprint('test', __name__)

@test_bp.route("/")
def hello():
    return "Hello, World!"

@test_bp.route("/hello/<name>")
def hello_name(name):
    return f"hello, {name}!"