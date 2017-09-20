"""Main twitter services"""
from twitterAdapter import TwitterAdaptor


class TwitterService(object):
    """Methods used by service layer"""
    @staticmethod
    def send_notification(twitter_handle, message):
        adapter = TwitterAdaptor()
        message_to_send = twitter_handle + ' ' + message
        adapter.api.update_status(status=message_to_send)
