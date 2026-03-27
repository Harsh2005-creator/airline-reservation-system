class Flight:
    def __init__(self, flight_id, flight_no, source, destination, departure, arrival, total_seats):
        self.flight_id = flight_id
        self.flight_no = flight_no
        self.source = source
        self.destination = destination
        self.departure = departure
        self.arrival = arrival
        self.total_seats = total_seats

    def to_dict(self):
        return {
            "flight_id": self.flight_id,
            "flight_no": self.flight_no,
            "source": self.source,
            "destination": self.destination,
            "departure": str(self.departure),
            "arrival": str(self.arrival),
            "total_seats": self.total_seats
        }