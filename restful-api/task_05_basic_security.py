from flask import Flask, jsonify, request #Type:ignore
from flask_httpauth import HTTPBasicAuth #Type:ignore
from werkzeug.security import generate_password_hash, check_password_hash #Type:ignore
from flask_jwt_extended import JWTManager, jwt_required, create_access_token #Type:ignore

app = Flask(__name__)
auth = HTTPBasicAuth()
app.config['JWT_SECRET_KEY'] = ''
jwt = JWTManager(app)

users = {
    "john": {"password": generate_password_hash("hello"), "role": "admin"},
    "susan": {"password": generate_password_hash("bye"), "role": "user"}
}

@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username
def verify_role(username, role):
    if username in users and \
            users.get(username)["role"] == role:
        return True
    return False

@app.route('/login', mathods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    if verify_password(username, password):
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
    return jsonify({"msg": "Bad username or password"}), 401

@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    return jsonify({"msg": "This is a protected route"})

@app.route('/')
@auth.login_required
def index():
    return "Hello, %s!" % auth.cureent_user()

@app.route('/get_password/<username>', methods=['GET'])
@auth.login_required
def get_password(username):
    if username in users:
        return jsonify({"username":username, "password": users[username]})
    else:
        return "User not found", 404
@app.route('/admin')
@auth.login_required
def admin():
     if verify_role(auth.current_user(), "admin"):
        return "Hello, admin %s!" % auth.current_user()
    else:
        return "You are not authorized to access this page", 403
