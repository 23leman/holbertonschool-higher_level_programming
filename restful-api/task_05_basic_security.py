#!/usr/bin/python3
"""
API Security: Implementing Basic Auth and JWT Authentication in Flask.
"""
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity
)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'holberton_secret_key'
app.config['JWT_SECRET_KEY'] = 'jwt_secret_key'

auth = HTTPBasicAuth()
jwt = JWTManager(app)

# İstifadəçi məlumatları (Hashed passwords)
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


# --- Basic Authentication ---

@auth.verify_password
def verify_password(username, password):
    """Verifies the username and password for Basic Auth."""
    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        return user
    return None


@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    """Route protected by Basic Authentication."""
    return "Basic Auth: Access Granted"


# --- JWT Authentication ---

@app.route('/login', methods=['POST'])
def login():
    """Authenticates user and returns a JWT token."""
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get('username')
    password = data.get('password')

    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        # Rolu tokenin içində saxlayırıq (identity)
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token)

    return jsonify({"error": "Invalid credentials"}), 401


@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    """Route protected by JWT Authentication."""
    return "JWT Auth: Access Granted"


@app.route('/admin-only')
@jwt_required()
def admin_only():
    """Route protected by JWT with Role-based access (admin only)."""
    current_user = get_jwt_identity()
    user = users.get(current_user)

    if user and user.get('role') == 'admin':
        return "Admin Access: Granted"
    
    return jsonify({"error": "Admin access required"}), 403


# --- JWT Error Handlers (Tələb olunan 401 statusları üçün) ---

@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == "__main__":
    app.run()
