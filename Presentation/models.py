from django.db import models

from Gmaps import googlemaps_service
from Flightaware import flightawareService

# Create your models here.

class Results:
    def __init__(self, flight_number, twitter_handle):
        
        self.maps = googlemaps_service.GooglemapsService()
        self.flightaware = flightawareService.FlightawareService()

        self.flight_number = flight_number
        self.twitter_handle = twitter_handle
        # Error with service currently
        #self.flightaware = self.flightaware.find_flight(self.flight_number)

        # Use this for dist/time calcs based on seconds else return the text default
        #self.journey_time = self.maps.get_user_journey_time(time_type='value')

        self.journey_time = self.maps.get_user_journey_time()
