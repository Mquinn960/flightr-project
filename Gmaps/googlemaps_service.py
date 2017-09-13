""" Main google maps service """

import json
from datetime import datetime

import googlemaps
import requests

class GooglemapsService(object):
    """ Main service for returning Gmap data, utilises the "googlemaps" python wrapper """

    # put this in env variables/settings in live
    api_key = 'AIzaSyCHAy-DjgELWCsLPVdciEhm8gSkt4XACTc'

    def __init__(self):
        """ Instantiate new Google Maps object when service is called """
        self.gmaps = googlemaps.Client(key=self.api_key)

    def get_reverse_geocode_result(self, userlat_long, result_type=None, location_type=None):
        """ Takes Lat and Long of user and returns reverse geocode JSON's formatted address """
        json_response = self.gmaps.reverse_geocode(userlat_long, result_type, location_type)
        return json_response[0]['formatted_address']

    def get_user_location(self, return_type=None):
        """ Attempts to geolocate the service user and returns lat and long or address if specified """
        json_response = self.gmaps.geolocate()
        user_location_coords = "%s,%s" % (json_response['location']['lat'], json_response['location']['lng'])

        if return_type is None:
            return_type = "coords"

        if return_type == "coords":
            return user_location_coords
        elif return_type == "address":
            return self.get_reverse_geocode_result(user_location_coords)

    def get_user_ip_location(self):
        """ Attempts to return user's location based on IP leveraging Free Geo IP service 
            Returns the JSON response with keys 'latitude' and 'longitude' """
        send_url = 'http://freegeoip.net/json'
        response = requests.get(send_url)
        json_response = json.loads(response.text)
        #latitude = json_response['latitude']
        #longitude = json_response['longitude']
        return json_response

    def get_user_journey_time(self, origin=None, destination=None):
        """ Uses distance matrix to retrieve time to desination, defaults to Aberdeen Airport """
        if origin is None:
            origin = self.get_user_location()
        if destination is None:
            destination = "57.1975253, -2.2057843"
        
        json_response = self.gmaps.distance_matrix(origin, destination)
        return json_response['rows'][0]['elements'][0]['duration']['text']

if __name__ == "__main__":
    """ console test stub """
    gmap_service = GooglemapsService()
    print(gmap_service.get_user_journey_time())
