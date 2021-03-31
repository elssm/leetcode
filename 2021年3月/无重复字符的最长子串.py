class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)==0:
            return 0
        maxl=0
        i=0
        for j in range(len(s)):
            if s[j] in s[i:j]:
                i = s[i:j].find(s[j])+i+1
            if j-i+1>maxl:
                maxl=j-i+1
        return maxl

