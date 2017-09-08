"""Tests for the Presentation app module"""

from django.test import TestCase, Client

# Create your tests here.

class HttpTests(TestCase):
    """Specfically Http status code tests"""

    CLIENT = Client()

    def test_site_root_http_code(self):
        """Checks that the main site root is reachable"""

        response = self.CLIENT.get('')
        self.assertEqual(response.status_code, 200)
        