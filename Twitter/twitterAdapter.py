"""Creates an object of the twitter api"""
from twython import Twython

class TwitterAdaptor:
    """API authentication"""
    def __init__(self):
        self.app_key = 'Temp'
        self.app_secret = 'Temp'
        self.oauth_token = 'Temp'
        self.oauth_token_secret = 'Temp'
        self.api = Twython(self.app_key, self.app_secret, self.oauth_token, self.oauth_token_secret)
    app_key = None
    app_secret = None
    oauth_token = None
    oauth_token_secret = None
    api = None
