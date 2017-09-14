from Flightaware.models import Flight
from Flightaware.soapAdapter import SoapAdapter


class FlightawareService(object):

        @staticmethod
        def find_flight(flight_number, adapter=None):
            if adapter is None:
                adapter = SoapAdapter()

            result = adapter.api.service.FlightInfo(indent=flight_number)

            return Flight(result['ident'], result['aircrafttype'], result['origin'])
