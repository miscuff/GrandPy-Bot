import requests

from config import WIKI_SEARCH_URL
from exceptions import ZeroResultsException, NoResponseException


class MediaWiki:

    @staticmethod
    def fetch_places_nearby(lat, lon):
        '''
            Call media wiki  api with lat and lon and
            returns the result
        '''

        parameters = {
            "action": "query",
            "prop": "coordinates|pageimages|description|info",
            "inprop": "url",
            "pithumbsize": 144,
            "generator": "geosearch",
            "ggsradius": 10000,
            "ggslimit": 10,
            "ggscoord": str(lat) + "|" + str(lon),
            "format": "json",
        }

        response = requests.get(WIKI_SEARCH_URL, params=parameters)
        if response.ok:
            response.encoding = 'UTF-8'
            data = response.json()
            places = data['query'] and data['query']['pages']
            try:
                return places
            except (IndexError, KeyError):
                raise ZeroResultsException
        else:
            raise NoResponseException

test = MediaWiki()
print(test.fetch_places_nearby("42", "-2"))
