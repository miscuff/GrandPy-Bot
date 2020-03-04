import urllib.request
from gpbot import GoogleApi

from io import BytesIO
import json
import pytest


class TestGoogleApi:

    def setup_method(self):
        self.test_google_api = GoogleApi()
        self.keywords = ["Paris", "france"]

    def test_http_return(self, monkeypatch):
        results = {"lat": 48.856614, "lng": 2.3522219}

        def mockreturn(request):
            return BytesIO(json.dumps(results).encode())

        # apply the monkeypatch for requests.get to mock_get
        monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)

        adress = self.test_google_api.search(self.keywords)

        assert adress['geometry']['location'] == results
