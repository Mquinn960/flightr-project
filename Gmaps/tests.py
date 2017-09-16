""" Test module for Gmaps App """
import requests
from django.test import TestCase

from Gmaps.googlemaps_service import GooglemapsService

# Create your tests here.

class GooglemapsTests(TestCase):
    """ Test suite for Google Maps Service """

    gmap = GooglemapsService()
    gmap_geocode_api = 'https://maps.googleapis.com/maps/api/geocode/json'

    # put this in env variables/settings in live
    api_key = 'AIzaSyCHAy-DjgELWCsLPVdciEhm8gSkt4XACTc'

    def test_api_key_not_none(self):
        """ Tests whether API key is populated in Gmap service """
        assert self.gmap.api_key != ""

    def test_google_api_endpoint_status(self):
        """ Checks that we get a HTTP 200 back from the API endpoint
            using the geolocation API and our API key """
        params = {
            'latlng': '51.5236819, -0.1586294',
            'sensor': 'false',
            'region': 'uk',
            'key': self.api_key
        }

        # Do the request and get the response data
        req = requests.get(self.gmap_geocode_api, params=params)
        res = req.json()

        # Use the first result
        status = res['status']
        assert status == 'OK'

    def test_google_api_geolocation(self):
        """ Tests that geolocation coords sent are returned by the geolocation
            service correctly """

        test_latlng_initial = '51.5236819, -0.1586294'

        params = {
            'latlng': test_latlng_initial,
            'sensor': 'false',
            'region': 'uk',
            'key': self.api_key
        }

        # Do the request and get the response data
        req = requests.get(self.gmap_geocode_api, params=params)
        res = req.json()

        # Use the first result
        result = res['results'][0]

        geodata = dict()
        geodata['lat'] = result['geometry']['location']['lat']
        geodata['lng'] = result['geometry']['location']['lng']

        geodata['coord_string'] = "%s, %s" % (geodata['lat'], geodata['lng'])

        assert geodata['coord_string'] == test_latlng_initial
