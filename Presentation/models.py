

class FlightDetails:
    def __init__(self,
                 flight_number,
                 flight_status,
                 current_flight_delay,
                 journey_time_to_airport,
                 suggested_time_to_start_journey,
                 time_till_leave_time):
        self.flight_number = flight_number
        self.flight_status = flight_status
        self.current_flight_delay = current_flight_delay
        self.journey_time_to_airport = journey_time_to_airport
        self.suggested_time_to_start_journey = suggested_time_to_start_journey
        self.time_till_leave_time = time_till_leave_time

    flight_number = None
    flight_status = None
    current_flight_delay = None
    journey_time_to_airport = None
    suggested_time_to_start_journey = None
    time_till_leave_time = None
