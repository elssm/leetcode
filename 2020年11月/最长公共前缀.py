class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs)==0:
            return ""
        c=[]
        for i in range(len(strs)):
            c.append(len(strs[i]))
        minl = min(c) #求出字符串中长度最短的作为最短长度
        s=''
        for i in range(minl):
            res=[] #预设一个空列表
            for j in range(len(strs)):
                res.append(strs[j][i]) #把各个字符串的同位置字符存进res中
            if res[1:] == res[:-1]: #比较res中字符是否全部相同
                s+=strs[j][i] #若相同添加到s中
            else:   #若存在不同直接跳出循环
                break
        return s
        
            