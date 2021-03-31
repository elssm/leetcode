class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # int count = len(s)
        count = 0
        for j in range(1,len(s)+1):
            i=0
            k=j
            while k<=len(s):
                t=s[i:k]
                if t==t[::-1]:
                    count+=1
                i+=1
                k+=1
        return count