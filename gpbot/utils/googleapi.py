import requests

from config import GOOGLE_SEARCH_URL, GOOGLE_API_KEY
from .exceptions import ZeroResultsException, NoResponseException


class GoogleApi:

    @staticmethod
    def search(keywords):
        '''
            Call google maps search api with keywords and
            returns the first result
        '''
        parameters = {
            "query": "+".join(keywords),
            "key": GOOGLE_API_KEY
        }

        response = requests.get(GOOGLE_SEARCH_URL, params=parameters)
        if response.ok:
            response.encoding = 'UTF-8'
            data = response.json()
            try:
                return data["results"][0]
            except (IndexError, KeyError):
                raise ZeroResultsException
        else:
            raise NoResponseException
