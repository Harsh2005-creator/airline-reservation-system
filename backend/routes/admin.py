from flask import Blueprint, request, jsonify
from db import get_db

admin_routes = Blueprint('admin', __name__)

# ---------------- ADD FLIGHT ----------------
@admin_routes.route('/add_flight', methods=['POST'])
def add_flight():
    try:
        data = request.json

        # ✅ validation
        required_fields = ['flight_no', 'source', 'destination', 'departure', 'arrival', 'total_seats']
        for field in required_fields:
            if field not in data or data[field] == "":
                return jsonify({"error": f"{field} is required"}), 400

        db = get_db()
        cursor = db.cursor()

        # insert flight
        cursor.execute("""
            INSERT INTO flights (flight_no, source, destination, departure, arrival, total_seats)
            VALUES (%s,%s,%s,%s,%s,%s)
        """, (
            data['flight_no'],
            data['source'],
            data['destination'],
            data['departure'],
            data['arrival'],
            data['total_seats']
        ))

        flight_id = cursor.lastrowid

        # auto-generate seats
        for i in range(1, int(data['total_seats']) + 1):
            seat_no = f"S{i}"
            cursor.execute("""
                INSERT INTO seats (flight_id, seat_no, status)
                VALUES (%s,%s,'available')
            """, (flight_id, seat_no))

        db.commit()

        return jsonify({
            "message": "Flight added successfully",
            "flight_id": flight_id
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ---------------- DELETE FLIGHT ----------------
@admin_routes.route('/delete_flight/<int:flight_id>', methods=['DELETE'])
def delete_flight(flight_id):
    try:
        db = get_db()
        cursor = db.cursor()

        # 🔥 delete dependent data first (IMPORTANT)
        cursor.execute("DELETE FROM bookings WHERE flight_id=%s", (flight_id,))
        cursor.execute("DELETE FROM seats WHERE flight_id=%s", (flight_id,))

        # delete flight
        cursor.execute("DELETE FROM flights WHERE flight_id=%s", (flight_id,))

        db.commit()

        return jsonify({"message": "Flight deleted successfully"})

    except Exception as e:
        return jsonify({"error": str(e)}), 500