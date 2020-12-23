class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s=list(s)
        t=list(t)
        i=0
        while i < len(t):
            if t[i] not in s:
                return str(t[i])
            else:
                s.remove(t[i])
                t.pop(i)
                i=0

