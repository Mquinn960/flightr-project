from django.test import TestCase
from Twitter.twitterAdapter import TwitterAdaptor


class TwitterTests(TestCase):
    def test_adapter_initialises(self):
        adapter = TwitterAdaptor()
        self.assertIsNotNone(adapter.api)
