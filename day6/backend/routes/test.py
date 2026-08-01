from flask import Blueprint

test_bp = Blueprint('test', __name__)

@test_bp.route("/")
def hello():
    return "Hello, World!"

@test_bp.route("/hello/<name>")
def hello_name(name):
    return f"hello, {name}!"


@test_bp.route("/task/hello")
def check_task():
    from jobs.tasks import hello_task, db_query_task
    result = db_query_task.delay()
    while not result.ready():
        pass
    return f"Task submitted! Task ID: {result.result}"

@test_bp.route("/mail")
def test_mail():
    from mailing import mail
    from flask_mail import Message
    from models import User

    users = User.query.all()
    for user in users:
        msg = Message()
        msg.subject = "Test Email"
        msg.recipients = [user.email]
        msg.body = "This is a test email from Flask-Mail."
        msg.html = f"<b>This is a test email from Flask-Mail to {user.email}</b>"
        mail.send(msg)
    return "Email sent!"