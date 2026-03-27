from flask import Blueprint, request, jsonify
from db import get_db

admin_routes = Blueprint('admin', __name__)

@admin_routes.route('/add-flight', methods=['POST'])
def add_flight():
    data = request.json
    db = get_db()
    cursor = db.cursor()

    cursor.execute(
        "INSERT INTO flights (flight_no, source, destination, total_seats) VALUES (%s,%s,%s,%s)",
        (data['flight_no'], data['source'], data['destination'], data['total_seats'])
    )

    db.commit()

    return jsonify({"message": "Flight added"})