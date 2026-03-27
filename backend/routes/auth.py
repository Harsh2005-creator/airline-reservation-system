from flask import Blueprint, request, jsonify
from db import get_db

auth_routes = Blueprint('auth', __name__)

@auth_routes.route('/register', methods=['POST'])
def register():
    data = request.json
    db = get_db()
    cursor = db.cursor()

    cursor.execute(
        "INSERT INTO users (name,email,password) VALUES (%s,%s,%s)",
        (data['name'], data['email'], data['password'])
    )
    db.commit()

    return jsonify({"message": "User registered"})