"""Main twitter services"""
from twython import Twython
from twitterAdapter import TwitterAdaptor

class TwitterService(object):
    """Methods used by service layer"""
    def send_notification(self, twitter_handle, message):
        adapter = TwitterAdaptor()
        adapter.api.update_status(twitter_handle + message)
