import threading

from Flightaware.flightawareService import FlightawareService
from Gmaps.googlemaps_service import GooglemapsService
from Presentation.models import FlightDetails
from Twitter.TwitterService import TwitterService
import time


class WatcherService(object):
    @staticmethod
    def get_details(flight_number):
        flight = FlightawareService.find_flight(flight_number)

        epoch_time = int(time.time())
        journey_time = GooglemapsService.get_user_journey_time(time_type='value')
        arrival_time = (flight.estimated_arrival_time['epoch'] - flight.arrival_delay)

        suggested_delay = (int(arrival_time) - int(epoch_time)) - int(journey_time)
        suggested_departure_time = (int(epoch_time) + suggested_delay)

        arrival_delay = flight.arrival_delay

        if arrival_delay == 0:
            arrival_delay = "No delay"
        else:
            m, s = divmod(arrival_delay, 60)
            h, m = divmod(m, 60)
            if h < 1:
                arrival_delay = "%d Minutes" % m
            else:
                arrival_delay = "%d Hours and %d Minutes" % (h, m)

        time_to_leave = suggested_departure_time - (int(epoch_time))

        m, s = divmod(time_to_leave, 60)
        h, m = divmod(m, 60)

        if h < 1:
            time_to_leave = "%d Minutes" % m
        else:
            time_to_leave = "%d Hours and %d Minutes" % (h, m)

        suggested_departure_time = time.strftime('%H:%M %d/%m/%Y', time.localtime(suggested_departure_time))
        journey_time = GooglemapsService.get_user_journey_time()

        return FlightDetails(flight_number=flight.fight_number,
                             flight_status=flight.status,
                             current_flight_delay=arrival_delay,
                             journey_time_to_airport=journey_time,
                             suggested_time_to_start_journey=suggested_departure_time,
                             time_till_leave_time=time_to_leave)

    @staticmethod
    def watch(twitter_handel, flight_number):
        flight = WatcherService.get_details(flight_number)
        thread = threading.Thread(target=WatcherService.start_watch, args=(twitter_handel, flight_number))
        thread.start()
        return flight

    @staticmethod
    def start_watch(twitter_handel, flight_number):
        flight = WatcherService.get_details(flight_number)
        status = None
        delay = None
        journey_time = None
        is_first_run = True

        while flight.flight_status != 'Arrived':
            if is_first_run:
                TwitterService.send_notification(twitter_handle=twitter_handel,
                                                 message='The status of you flight is: ' + flight.flight_status)
                TwitterService.send_notification(twitter_handle=twitter_handel,
                                                 message='Your flight is delayed by: ' + flight.current_flight_delay)
                TwitterService.send_notification(twitter_handle=twitter_handel,
                                                 message='Your current journey time is: '
                                                         + flight.journey_time_to_airport)
                is_first_run = False

            if flight.flight_status != status:
                TwitterService.send_notification(twitter_handle=twitter_handel,
                                                 message='The status of your flight is: ' + status)
                status = flight.flight_status

            if flight.current_flight_delay != delay:
                TwitterService.send_notification(twitter_handle=twitter_handel,
                                                 message='Your flight is delayed by: ' + delay)
                delay = flight.current_flight_delay

            if flight.journey_time_to_airport != journey_time:
                TwitterService.send_notification(twitter_handle=twitter_handel,
                                                 message='Your current journey time is: '
                                                         + journey_time
                                                         + ' You should start your journey at: '
                                                         + flight.suggested_time_to_start_journey)
                journey_time = flight.journey_time_to_airport

            flight = WatcherService.get_details(flight_number)
