""" Test module for Gmaps App """
from django.test import TestCase
from Gmaps.googlemaps_service import GooglemapsService

# Create your tests here.

class GooglemapsTests(TestCase):
    """ Test suite for Google Maps Service """

    gmap = GooglemapsService()

    def test_api_key_not_none(self):
        """ Tests whether API key is populated in Gmap service """
        assert self.gmap.api_key != ""
