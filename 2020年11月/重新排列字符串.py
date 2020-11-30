class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        res = []
        s1 = ""
        for i in range(len(s)):
            res.append(s[i])
        j=0
        for i in indices:
            res[i] = s[j]
            j+=1
        for i in res:
            s1+=i
        return s1