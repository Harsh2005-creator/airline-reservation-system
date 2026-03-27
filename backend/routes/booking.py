from flask import Blueprint, request, jsonify
from db import get_db

booking_routes = Blueprint('booking', __name__)

# ------------------ GET FLIGHTS ------------------
@booking_routes.route('/flights', methods=['GET'])
def get_flights():
    db = get_db()
    cursor = db.cursor(dictionary=True)

    cursor.execute("""
        SELECT f.*, 
        COUNT(s.seat_id) AS total_seats,
        SUM(CASE WHEN s.status='available' THEN 1 ELSE 0 END) AS available_seats
        FROM flights f
        LEFT JOIN seats s ON f.flight_id = s.flight_id
        GROUP BY f.flight_id
    """)

    return jsonify(cursor.fetchall())


# ------------------ GET SEATS ------------------
@booking_routes.route('/seats/<int:flight_id>', methods=['GET'])
def get_seats(flight_id):
    db = get_db()
    cursor = db.cursor(dictionary=True)

    cursor.execute("""
        SELECT seat_id, seat_no, status 
        FROM seats 
        WHERE flight_id=%s
    """, (flight_id,))

    return jsonify(cursor.fetchall())


# ------------------ BOOK TICKET ------------------
@booking_routes.route('/book', methods=['POST'])
def book_ticket():
    data = request.json
    db = get_db()
    cursor = db.cursor()

    seat_id = data['seat_id']
    user_id = data['user_id']
    flight_id = data['flight_id']

    # check if seat is available
    cursor.execute("SELECT status FROM seats WHERE seat_id=%s", (seat_id,))
    result = cursor.fetchone()

    if not result:
        return jsonify({"error": "Seat not found"})

    if result[0] == 'booked':
        return jsonify({"error": "Seat already booked"})

    # insert booking
    cursor.execute("""
        INSERT INTO bookings (user_id, flight_id, seat_id)
        VALUES (%s,%s,%s)
    """, (user_id, flight_id, seat_id))

    # update seat status
    cursor.execute("""
        UPDATE seats 
        SET status='booked' 
        WHERE seat_id=%s
    """, (seat_id,))

    db.commit()

    return jsonify({"message": "Booking successful"})


# ------------------ VIEW BOOKINGS ------------------
@booking_routes.route('/bookings', methods=['GET'])
def get_bookings():
    db = get_db()
    cursor = db.cursor(dictionary=True)

    cursor.execute("""
        SELECT b.booking_id, u.name, f.flight_no, s.seat_no, b.status
        FROM bookings b
        JOIN users u ON b.user_id = u.user_id
        JOIN flights f ON b.flight_id = f.flight_id
        JOIN seats s ON b.seat_id = s.seat_id
    """)

    return jsonify(cursor.fetchall())


# ------------------ CANCEL BOOKING ------------------
@booking_routes.route('/cancel/<int:booking_id>', methods=['DELETE'])
def cancel_booking(booking_id):
    db = get_db()
    cursor = db.cursor()

    cursor.execute("SELECT seat_id FROM bookings WHERE booking_id=%s", (booking_id,))
    result = cursor.fetchone()

    if not result:
        return jsonify({"error": "Booking not found"})

    seat_id = result[0]

    # free seat
    cursor.execute("UPDATE seats SET status='available' WHERE seat_id=%s", (seat_id,))

    # update booking
    cursor.execute("UPDATE bookings SET status='cancelled' WHERE booking_id=%s", (booking_id,))

    db.commit()

    return jsonify({"message": "Booking cancelled"})