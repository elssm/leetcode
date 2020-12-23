class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        count=[]
        stack = []
        index=0
        for i in range(len(s)):
            if index==0:
                if s[i]=="(" or s[i]==")":
                    stack.append(s[i])
                    index+=1
                    count.append(i)
            else:
                if stack[index-1]=="(" and s[i]==")":
                    stack.pop()
                    index-=1
                    count.pop()
                elif s[i]==")" or s[i]=="(":
                    stack.append(s[i])
                    index+=1
                    count.append(i)
        l = list(s)
        for i in reversed(count):
            l.pop(i)
        s =''.join(l)
        return s

