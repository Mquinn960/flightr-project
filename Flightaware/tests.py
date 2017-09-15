from django.test import TestCase
from mock import MagicMock

from Flightaware.flightawareService import FlightawareService
from Flightaware.models import Flight
from Flightaware.soapAdapter import SoapAdapter


class FlightawareTests(TestCase):
    def test_adapter_initialises(self):
        adapter = SoapAdapter()
        self.assertIsNotNone(adapter.api)

    def test_find_flight(self):
        expected_flight = Flight(flight_number='1234', aircraft_type='jet', origin='Berlin', status='Flying')

        adapter = SoapAdapter()
        adapter.api.service.FlightInfo = MagicMock(return_value={'ident': expected_flight.fight_number,
                                                                 'aircrafttype': expected_flight.aircraft_type,
                                                                 'origin': expected_flight.origin,
                                                                 'status': expected_flight.status})

        actual_flight = FlightawareService.find_flight(expected_flight.fight_number, adapter)

        adapter.api.service.FlightInfo.assert_called_with(indent=expected_flight.fight_number)

        self.assertEqual(expected_flight.fight_number, actual_flight.fight_number)
        self.assertEqual(expected_flight.aircraft_type, actual_flight.aircraft_type)
        self.assertEqual(expected_flight.origin, actual_flight.origin)
