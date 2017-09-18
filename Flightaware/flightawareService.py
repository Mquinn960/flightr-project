from Flightaware.models import Flight
from Flightaware.restAdapter import RestAdapter
import requests


class FlightawareService(object):
    @staticmethod
    def find_flight(flight_number, response=None):
        adapter = RestAdapter()

        payload = {'ident': flight_number, 'howMany': 1}

        # This is for mocking and is generally bad practice, But it's the best I can do ATM
        if response is None:
            response = requests.get(adapter.url + "FlightInfoStatus", params=payload,
                                    auth=(adapter.username, adapter.apiKey))

        result = response.json()['FlightInfoStatusResult']['flights'][0]

        return Flight(result['ident'],
                      result['aircrafttype'],
                      result['origin'],
                      result['status'],
                      result['actual_arrival_time'])
