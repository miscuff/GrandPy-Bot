from .utils.parser import Parser
from .utils.googleapi import GoogleApi
from .utils.mediawiki import MediaWiki


class Grandpy():

    def __init__(self):
        self.parser = Parser()
        self.google_map = GoogleApi()
        self.media_wiki = MediaWiki()

    def grandpy_answer(self, sentence):
        """
        :param: sentence
        :return:
        """
        if sentence == "":
            return self._format_grandpy_answer("")
        else:
            geo_location = self._get_location(sentence)
            page_id = self._id_media_wiki(geo_location)
            story = self._story_media_wiki(page_id)
            url = self._url_media_wiki(geo_location, page_id)
            return self._format_grandpy_answer(geo_location, story, url)

    def _format_grandpy_answer(self, geo_location, story, url):
        """
        :param geo_location:
        :return: a dictionary with geo_location, story and url
        """
        answer = {}
        answer['location'] = geo_location
        answer['story'] = story
        answer['url'] = url

        return answer

    def _get_location(self, sentence):
        """
        :param sentence:
        :return: location with latitude and longitude
        """
        keywords = self.parser.get_keywords(sentence)
        address = self.google_map.search(keywords)
        return address["geometry"]["location"]

    def _id_media_wiki(self, location):
        """
        :param location:
        :return: id of a page Media Wiki
        """
        lat = location["lat"]
        lng = location["lng"]
        page = self.media_wiki.fetch_places_nearby(lat, lng)
        page_id = next(iter(page))
        return page_id

    def _url_media_wiki(self, location, page_id):
        """
        :param location and page_id
        :return: url of a page media wiki
        """
        lat = location["lat"]
        lng = location["lng"]
        api_response = self.media_wiki.fetch_places_nearby(lat, lng)
        return api_response[page_id]['fullurl']

    def _story_media_wiki(self, page_id):
        """
        :param page_id:
        :return: the story associate to the page_id
        """
        return self.media_wiki.get_extract(page_id)
