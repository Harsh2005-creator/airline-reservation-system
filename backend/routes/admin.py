from flask import Blueprint, request, jsonify
from db import get_db
import joblib
import os

admin_routes = Blueprint('admin', __name__)

# ==========================================
# 🤖 LOAD ML MODEL FOR ADMIN DASHBOARD
# ==========================================
MODEL_PATH = os.path.join(os.path.dirname(__file__), '../flight_price_model.pkl')
price_model = None
try:
    if os.path.exists(MODEL_PATH):
        price_model = joblib.load(MODEL_PATH)
except Exception as e:
    print(f"Error loading ML model in admin: {e}")


# ==========================================
# 📈 GET ML GRAPH DATA (NEW ROUTE)
# ==========================================
@admin_routes.route('/ml_graph', methods=['GET'])
def get_ml_graph():
    if not price_model:
        return jsonify({"error": "Model not found"}), 400

    total_seats = 180
    graph_data = []

    # Simulate seats dropping from 180 down to 1
    # We step by 5 to make a smooth chart
    for available in range(180, 0, -5):
        price = price_model.predict([[total_seats, available]])[0]
        graph_data.append({
            "seats_left": available,
            "predicted_price": int(price)
        })
        
    # Also grab the absolute last seat price (1 seat left)
    final_price = price_model.predict([[total_seats, 1]])[0]
    graph_data.append({"seats_left": 1, "predicted_price": int(final_price)})

    return jsonify(graph_data)


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