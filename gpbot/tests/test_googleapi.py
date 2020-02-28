import pytest
from gpbot import GoogleApi


class TestGoogleApi:

    def setup_method(self):
        self.test_google_api = GoogleApi()
        self.keywords = ['Paris']

    def get_result(self):
        lat = 48.856614
        lon = 2.3522219
        assert (self.test_google_api['location']['lat'] == lat and
                self.test_google_api['location']['lon'] == lon)
