import urllib.request
import json

from io import BytesIO

from gpbot import MediaWiki


class TestGoogleApi:

    def setup_method(self):
        self.test_media_wiki = MediaWiki()
        self.lat = 48.856614
        self.lng = 2.3522219

    def test_http_return(self, monkeypatch):
        """
        :param monkeypatch:
        :return: Check that the pageId is correct
        """
        results = '49947'

        def mockreturn(request):
            return BytesIO(json.dumps(results).encode())

        # apply the monkeypatch for requests.get to mock_get
        monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)

        page = self.test_media_wiki.fetch_places_nearby(self.lat, self.lng)
        page_id = next(iter(page))

        assert page_id == results
