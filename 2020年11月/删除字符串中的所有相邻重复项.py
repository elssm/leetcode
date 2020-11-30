class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """
        stack = [] #创建一个空栈
        for i in range(len(S)):
            if len(stack)==0: #如果栈空，当前字符直接入栈
                stack.append(S[i])
                index=0 #索引改为0
                continue
            if S[i] == stack[index]: #如果当前字符等于栈顶字符
                stack.pop() #弹出栈顶字符
                index-=1 #索引减1
            else:
                stack.append(S[i]) #栈顶字符不等于当前字符，入栈，索引加1
                index+=1
        s='' #将列表中的值改为字符输出
        for i in range(len(stack)):
            s+=stack[i]
        return s