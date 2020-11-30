class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        list_s=[]
        list_t=[]
        for i in range(len(S)):
            if S[i]!='#':
                list_s.append(S[i])
            else:
                if len(list_s)!=0:
                    list_s.pop(-1)
        for i in range(len(T)):
            if T[i]!='#':
                list_t.append(T[i])
            else:
                if len(list_t)!=0: #如果长度为空，则不移除
                    list_t.pop(-1)
        return list_s==list_t