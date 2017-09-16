from django.test import TestCase
from mock import MagicMock

from Flightaware.flightawareService import FlightawareService
from Flightaware.models import Flight


class FlightawareTests(TestCase):
    def test_find_flight(self):
        expected_flight = Flight(flight_number='N1234',
                                 aircraft_type='jet',
                                 origin='Berlin',
                                 status='Flying',
                                 actual_arrival_time='time')

        response = MagicMock()
        response.json = MagicMock(
            return_value={'FlightInfoStatusResult': {'flights': [
                {'ident': expected_flight.fight_number,
                 'aircrafttype': expected_flight.aircraft_type,
                 'origin': expected_flight.origin,
                 'status': expected_flight.status,
                 'actual_arrival_time': expected_flight.actual_arrival_time}]}})

        actual_flight = FlightawareService.find_flight(expected_flight.fight_number, response)

        self.assertEqual(expected_flight.fight_number, actual_flight.fight_number)
        self.assertEqual(expected_flight.aircraft_type, actual_flight.aircraft_type)
        self.assertEqual(expected_flight.origin, actual_flight.origin)
