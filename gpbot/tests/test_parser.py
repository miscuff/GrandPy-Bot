from gpbot import Parser


class TestParser:

    def setup_method(self):
        self.test_parser = Parser()
        self.sentence = "Je voudrais aller à Paris !"

    def test_init(self):
        """
        :return: Check that the parser block the letter 'a'
        """
        keyword = "a"
        assert keyword in self.test_parser.stopwords

    def test_sentence(self):
        """
        :return: Check that the parser parse the sentence with removing the
        words
        """
        sentence_with_keywords = self.test_parser.get_keywords(self.sentence)
        assert sentence_with_keywords == ['voudrais', 'aller', 'Paris']


