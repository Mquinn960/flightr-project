from Flightaware.models import Flight
from Flightaware.soapAdapter import SoapAdapter


class FlightawareService(object):

        @staticmethod
        def find_flight(flight_number, adapter=None):
            if adapter is None:
                adapter = SoapAdapter()

            result = adapter.api.service.Enroute('ABZ', 10, '', 0)
            flights = result['enroute']

            for flight in flights:
                if flight['ident'] == flight_number:
                    return Flight(flight['ident'], flight['aircrafttype'], flight['origin'])
