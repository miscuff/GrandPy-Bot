from .stopwords import STOP_WORDS


class Parser:
    """
        Parse a sentence with the words in STOP_WORDS
    """
    def __init__(self):
        """
        Init Parser with stopwords
        """
        self.stopwords = STOP_WORDS

    def get_keywords(self, sentence):
        """
        Returns the keywords of a sentence
        """
        return self._words_filter(self._sentence_filter(sentence))

    def _sentence_filter(self, sentence):
        """
        Split the sentence and return list of words
        """
        if sentence is None:
            return None
        sentence = "".join(c if c not in "'-" else " " for c in sentence)
        words = sentence.split(" ")
        return words

    def _words_filter(self, words):
        """
        filter a list of words by removing stop words
        """
        if words is None:
            return None
        words_filtered = []
        for w in words:
            if w.lower() not in STOP_WORDS:
                words_filtered.append(w)
        return words_filtered
