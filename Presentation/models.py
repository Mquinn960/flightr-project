import time
import json

from django.db import models

from Flightaware import flightawareService
from Gmaps import googlemaps_service

# Create your models here.

class Results:
    def __init__(self, flight_number, twitter_handle):
        
        self.maps = googlemaps_service.GooglemapsService()
        self.flightaware = flightawareService.FlightawareService()

        self.flight_number = flight_number
        self.twitter_handle = twitter_handle
        # Error with service currently
        self.flightaware = self.flightaware.find_flight(self.flight_number)

        epoch_time = int(time.time())
        journey_time = self.maps.get_user_journey_time(time_type='value')
        arrival_time = (self.flightaware.estimated_arrival_time['epoch'] - self.flightaware.arrival_delay)

        suggested_delay = (int(arrival_time) - int(epoch_time)) - int(journey_time)
        suggested_departure_time = (int(epoch_time) + suggested_delay)

        if self.flightaware.arrival_delay == 0:
            self.flightaware.arrival_delay = "No delay"
        else:
            m, s = divmod(self.flightaware.arrival_delay, 60)
            h, m = divmod(m, 60)
            if h < 1:
                self.flightaware.arrival_delay = "%d Minutes" % (m)
            else:
                self.flightaware.arrival_delay = "%d Hours and %d Minutes" % (h, m)
        
        time_to_leave = suggested_departure_time - (int(epoch_time))

        m, s = divmod(time_to_leave, 60)
        h, m = divmod(m, 60)
        
        if h < 1:
            time_to_leave = "%d Minutes" % (m)
        else:
            time_to_leave = "%d Hours and %d Minutes" % (h, m)
                        
        suggested_departure_time = time.strftime('%H:%M %d/%m/%Y', time.localtime(suggested_departure_time))

        self.journey_time = self.maps.get_user_journey_time()
        self.epoch_time = epoch_time
        self.arrival_time = arrival_time
        self.flight_delay = self.flightaware.arrival_delay
        self.suggested_departure_time = suggested_departure_time
        self.time_to_leave = time_to_leave
