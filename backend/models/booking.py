class Booking:
    def __init__(self, booking_id, user_id, flight_id, seat_id, status):
        self.booking_id = booking_id
        self.user_id = user_id
        self.flight_id = flight_id
        self.seat_id = seat_id
        self.status = status

    def to_dict(self):
        return {
            "booking_id": self.booking_id,
            "user_id": self.user_id,
            "flight_id": self.flight_id,
            "seat_id": self.seat_id,
            "status": self.status
        }