from django.db import models

# Create your models here.

class Journey:
    """Holds user geolocation information"""

    def __init__(self, userLat, userLong, userAddress):
        self.userLat = userLat
        self.userLong = userLong
        self.userAddress = userAddress

    userLat = None
    userLong = None
    userAddress = None
    