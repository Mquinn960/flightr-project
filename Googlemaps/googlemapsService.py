from datetime import datetime

import googlemaps
from django.conf import settings

API_KEY = getattr(settings, "GOOGLE_API_KEY", None)

class GooglemapsService(object):
    """Main service for returning Gmap data, utilises the "googlemaps" python wrapper package"""

    def __init__(self):
        """something"""

    def somethingElse():
        """ """
