class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        result=''
        res = dict(Counter(s))
        s = sorted(res.items(),key=lambda res:res[1], reverse=True)
        for i in range(len(s)):
            result+=s[i][0]*s[i][1]
        return result