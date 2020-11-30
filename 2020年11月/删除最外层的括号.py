class Solution(object):
    def removeOuterParentheses(self, S):
        """
        :type S: str
        :rtype: str
        """
        stack = []
        index = 0
        s = ''
        for i in range(len(S)):
            if len(stack)==0: #如果栈空，当前字符直接入栈
                stack.append(S[i])
                index=0 #修改index为0
            #如果栈顶元素为'('当前元素为')',index=0表示栈里只有一个字符
            #则说明此时这对就是最外层括号，删除栈顶元素，修改index，s不改变
            elif stack[index] == '(' and S[i] == ')' and index ==0: 
                stack.pop()
                index-=1
            #如果栈顶为'('，当前元素也是'('，不管index是多少，直接入栈，并且
            #把当前元素加入s字符串中，并修改index
            elif stack[index] == '(' and S[i] == '(' and (index ==0 or index!=0):
                s+=S[i]
                stack.append(S[i])
                index+=1
            #剩下情况就是不是最外层括号，先更新当前字符串s，再把之前入栈的'('出栈
            #并修改index
            else:
                s+=S[i]
                stack.pop()
                index-=1
        return s