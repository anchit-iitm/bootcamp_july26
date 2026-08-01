# from app import app
# from flask import current_app as app
from app import create_flask_server
from models import db, user_datastore
from security import ph

app = create_flask_server()


def init_roles():
    # new_role = roles(name='admin', description='Administrator')
    # db.session.add(new_role)
    user_datastore.find_or_create_role(name='admin', description='Administrator')
    user_datastore.find_or_create_role(name='user', description='End user')
    user_datastore.find_or_create_role(name='manager', description='Content editor')
    db.session.commit()

def add_admin_user():
    if not user_datastore.find_user(id=1):
        admin_user = user_datastore.create_user(
            email='admin@abc.com',
            password=ph.hash('admin'),
        )
        admin_role = user_datastore.find_role('admin')
        user_datastore.add_role_to_user(admin_user, admin_role)
        db.session.commit()

with app.app_context():
    db.create_all()
    init_roles()
    add_admin_user()