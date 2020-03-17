import urllib.request
from gpbot import MediaWiki

from io import BytesIO
import json


class TestGoogleApi:

    def setup_method(self):
        self.test_media_wiki = MediaWiki()
        self.lat = 48.856614
        self.lng = 2.3522219
        self.id = '49947'

    def test_http_return(self, monkeypatch):
        """
        :param monkeypatch:
        :return: Check that the pageId is correct
        """
        results = {self.id: [
                           {"pageid": 49947}
                        ]
                   }

        def mockreturn(request):
            return BytesIO(json.dumps(results).encode())

            # apply the monkeypatch for requests.get to mock_get

        monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)
        page_id = self.test_media_wiki.fetch_places_nearby(self.lat, self.lng)
        print(page_id)

        assert page_id is not None
