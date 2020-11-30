class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        c=[]
        j=0
        if s=='':
            return True
        if s[0]==')' or s[0]==']' or s[0]=='}':
            return False
        for i in range(len(s)):
            if len(c)==0:
                c.append(s[i])
            else:
                if (c[-1]=='(' and s[i]==')') or (c[-1]=='[' and s[i]==']')  or (c[-1]=='{' and s[i]=='}'):
                    c.pop(-1) #使用remove出错，不知为何
                else:
                    c.append(s[i])
        if len(c)==0:
            return True
        else:
            return False