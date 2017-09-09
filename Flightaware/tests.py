from django.test import TestCase

from Flightaware.soapAdapter import SoapAdapter


class FlightawareTests(TestCase):
    def test_adapter_initialises(self):
        adapter = SoapAdapter()
        self.assertIsNotNone(adapter.api)
