class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        count=0
        for i in range(len(words)):
            flag=1
            for j in words[i]:
                if j not in allowed:
                    flag=0
            if flag:
                count+=1
        return count