import json
import urllib.request

from io import BytesIO

from gpbot import GoogleApi


class TestGoogleApi:

    def setup_method(self):
        self.test_google_api = GoogleApi()
        self.keywords = ["Paris", "france"]

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

        response = self.test_google_api.search(self.keywords)

        assert response['geometry']['location'] == results
