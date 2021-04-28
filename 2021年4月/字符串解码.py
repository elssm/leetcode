class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        num = 0
        res = ""
        for c in s :
            if c.isdigit():
                num = num*10+int(c)
            elif c == "[":
                stack.append((res,num))
                res = ""
                num = 0
            elif c == "]":
                top = stack.pop()
                res = top[0]+res*top[1]
            else:
                res += c
        return res