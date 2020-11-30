class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        c1=""
        c2=""
        for i in range(len(word1)):
            c1=c1+word1[i]
        for i in range(len(word2)):
            c2=c2+word2[i]
        return c1==c2