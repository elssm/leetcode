class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        stack=[]
        s=list(s)
        for i in range(len(s)):
            stack.append(s[i])
            if stack.count("L")==stack.count("R"):
                stack=[]
                count+=1
        return count