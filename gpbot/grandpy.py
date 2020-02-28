from .utils.parser import Parser
from .utils.googleapi import GoogleApi


class Grandpy():

    def __init__(self):
        self.parser = Parser()
        self.google_map = GoogleApi()

    def grandpy_answer(self, sentence):
        if sentence == "":
            return self._format_grandpy_answer("")
        else:
            keywords = self.parser.get_keywords(sentence)
            address = self.google_map.search(keywords)
            return self._format_grandpy_answer(address["geometry"]["location"])

    def _format_grandpy_answer(self, geo_location):
        """
            Return all elements of Grandpy answer as a JSON Object
        """
        answer = {}
        answer['location'] = geo_location
        return answer