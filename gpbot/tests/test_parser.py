import pytest
from gpbot import Parser


class TestParser:

    def setup_method(self):
        self.test_parser = Parser()
        self.sentence = "Je voudrais aller à Paris !"

    def test_init(self):
        keyword = "a"
        assert keyword in self.test_parser.stopwords

    def test_sentence(self):
        sentence_with_keywords = self.test_parser.get_keywords(self.sentence)
        assert sentence_with_keywords == ['voudrais', 'aller', 'Paris']


