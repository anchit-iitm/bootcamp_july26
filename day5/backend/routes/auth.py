from flask import Blueprint, request, jsonify
from models import db, user_datastore
from security import ph

auth_bp = Blueprint('auth_part', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    if not data or 'email' not in data or 'password' not in data:
        return jsonify({'message': 'Email and password are required'}), 400
    email = data['email']
    password = data['password']
    role = data.get('role')
    if role not in ['user', 'manager']:
        return jsonify({'message': 'Invalid role'}), 400
    if not user_datastore.find_user(email=email):
            new_user = user_datastore.create_user(
                email=email,
                password=ph.hash(password),
            )
            admin_role = user_datastore.find_role(role)
            user_datastore.add_role_to_user(new_user, admin_role)
            if role == 'manager':
                user_datastore.deactivate_user(new_user)
            db.session.commit()
            return jsonify({'message': 'User registered successfully'}), 201
    else:
        return jsonify({'message': 'email id already exists'}), 400

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data or 'email' not in data or 'password' not in data:
        return jsonify({'message': 'Email and password are required'}), 400
    email = data['email']
    password = data['password']
    user = user_datastore.find_user(email=email)
    if not user:
        return jsonify({'message': 'Invalid email or password'}), 401
    if not ph.verify(user.password, password):
        return jsonify({'message': 'Invalid email or password'}), 401
    if not user.active:
        return jsonify({'message': 'Contact administrator'}), 403
    from flask_security import login_user
    login_user(user)
    db.session.commit()
    return jsonify({'message': 'login successful', 'user_id': user.id, 'authToken': user.get_auth_token(), 'email': user.email}), 200