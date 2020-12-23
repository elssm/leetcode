class WordsFrequency(object):

    def __init__(self, book):
        """
        :type book: List[str]
        """
        #使用collections中内置Counter计数器
        self.book = Counter(book)


    def get(self, word):
        """
        :type word: str
        :rtype: int
        """
        return self.book[word]



# Your WordsFrequency object will be instantiated and called as such:
# obj = WordsFrequency(book)
# param_1 = obj.get(word)