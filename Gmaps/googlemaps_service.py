""" Main google maps service """

import googlemaps


class GooglemapsService(object):
    """ Main service for returning Gmap data, utilises the "googlemaps" python wrapper """

    # put this in env variables/settings in live
    api_key = 'AIzaSyCHAy-DjgELWCsLPVdciEhm8gSkt4XACTc'

    @staticmethod
    def get_reverse_geocode_result(userlat_long, result_type=None, location_type=None):
        """ Takes Lat and Long of user and returns reverse geocode JSON's formatted address """

        gmaps = googlemaps.Client(key=GooglemapsService.api_key)
        json_response = gmaps.reverse_geocode(userlat_long, result_type, location_type)
        return json_response[0]['formatted_address']

    @staticmethod
    def get_user_location(return_type=None):
        """ Attempts to geolocate the service user and returns lat and long or address if specified """

        gmaps = googlemaps.Client(key=GooglemapsService.api_key)
        json_response = gmaps.geolocate()
        user_location_coords = "%s,%s" % (json_response['location']['lat'], json_response['location']['lng'])

        if return_type is None:
            return_type = "coords"

        if return_type == "address":
            return GooglemapsService.get_reverse_geocode_result(user_location_coords)
        else:
            return user_location_coords

    @staticmethod
    def get_user_journey_time(origin=None, destination=None, time_type=None):
        """ Uses distance matrix to retrieve time to desination, defaults to Aberdeen Airport pickup zone"""

        if origin is None:
            origin = GooglemapsService.get_user_location()
        if destination is None:
            destination = "57.1975253, -2.2057843"
        if time_type is None:
            time_type = 'text'

        gmaps = googlemaps.Client(key=GooglemapsService.api_key)
        json_response = gmaps.distance_matrix(origin, destination)
        return json_response['rows'][0]['elements'][0]['duration'][time_type]
