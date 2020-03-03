import requests

from config import WIKI_SEARCH_URL
from .exceptions import ZeroResultsException, NoResponseException


class MediaWiki:

    @staticmethod
    def fetch_places_nearby(lat, lon):
        """
            Call media wiki  api with lat and lon and
            returns the page id
        """

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
            places = data['query']['pages']
            try:
                return places
            except (IndexError, KeyError):
                raise ZeroResultsException
        else:
            raise NoResponseException

    @staticmethod
    def get_extract(page_id):
        """
            Call MediaWikiApi and get an extract of the page corresponding
            to the id
        """
        get_extract_parameters = {
            "action": "query",
            "pageids": page_id,
            "prop": "extracts",
            "explaintext": "true",
            "exsectionformat": "plain",
            "exsentences": "3",
            "format": "json"
        }
        response = requests.get(WIKI_SEARCH_URL, params=get_extract_parameters)
        if response.ok:
            response.encoding = "UTF-8"
            data = response.json()
            try:
                extract = data["query"]["pages"][page_id]["extract"]
            except KeyError:
                raise ZeroResultsException
            return extract
        else:
            raise NoResponseException
