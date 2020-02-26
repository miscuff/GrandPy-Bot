import pytest
from gpbot import Parser


class TestParser:

    def setup_method(self):
        self.test_parser = Parser()
        self.sentence = "Est-ce que tu connais l'adresse d'OpenClassrooms ?"

    def test_init(self):
        keyword = "a"
        assert keyword in self.test_parser.stopwords




