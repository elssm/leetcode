class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        stack=[]
        index=0
        for i in range(len(S)):
            if len(stack)==0 or (stack[index-1]!="(" or S[i]!=")"):
                stack.append(S[i])
                index+=1
                continue 
            else:
                stack.pop()
                index-=1
                continue
        return index
