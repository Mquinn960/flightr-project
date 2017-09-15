import logging

from suds.client import Client


class SoapAdapter:
    def __init__(self):
        logging.basicConfig(level=logging.INFO)
        self.username = 'RaspberyPirates'
        self.apiKey = '4b694ca29e116426788a13a11672f6722f3f3353'
        self.wsdlFile = 'http://flightxml.flightaware.com/soap/FlightXML2/wsdl'
        self.api = Client(self.wsdlFile, username=self.username, password=self.apiKey)

    username = None
    apiKey = None
    wsdlFile = None
    api = None
