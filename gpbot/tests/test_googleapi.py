import urllib.request
from gpbot import GoogleApi

from io import BytesIO
import json


class TestGoogleApi:

    def setup_method(self):
        self.test_google_api = GoogleApi()
        self.keywords = ["Paris", "france"]

    def response(self):
        """
        :return: Location for Paris
        """
        response_google = self.test_google_api.search(self.keywords)
        return response_google['geometry']['location']

    def test_http_return(self, monkeypatch):
        """
        :param monkeypatch:
        :return: Check that the location are corrects
        """
        results = {"lat": 48.856614, "lng": 2.3522219}

        def mockreturn(request):
            return BytesIO(json.dumps(results).encode())

        # apply the monkeypatch for requests.get to mock_get
        monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)

        assert self.response() == results
