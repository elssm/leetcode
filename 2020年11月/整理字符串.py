class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for i in range(len(s)):
            if len(stack)==0: #空栈字符直接入栈
                stack.append(s[i])
                index=0
                continue
            if abs(ord(s[i]) - ord(stack[index]))==32: #如果当前字符减去栈顶字符为32
                stack.pop()
                index-=1
            else:
                stack.append(s[i])
                index+=1
        s=''
        for i in range(len(stack)):
            s+=stack[i]
        return s