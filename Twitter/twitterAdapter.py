"""Creates an object of the twitter api"""
from twython import Twython

class TwitterAdaptor:
    """API authentication"""
    def __init__(self):
        self.app_key = '4am7P2QD0tVygnfhXXsYKNxy0'
        self.app_secret = 'Fmngx5ds15AHxI1ePYfm91yT0wMV20C8t4yWzyY6VaqjetaXjQ'
        self.oauth_token = '905805253907546113-Jfy6Hfpeigfg92fnjnCo6v3XiexBrc5'
        self.oauth_token_secret = 'EoDjJBzh8m25Tl4CHZiutCbj7Ns0xks76bjvzSolDKUtM'
        self.api = Twython(self.app_key, self.app_secret, self.oauth_token, self.oauth_token_secret)
    app_key = None
    app_secret = None
    oauth_token = None
    oauth_token_secret = None
    api = None
