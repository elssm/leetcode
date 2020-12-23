class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        #方法一：join函数
        # return " ".join(i[::-1] for i in s.split())

        #方法二
        res = ""
        s1 = list(s.split(" "))
        for i in range(len(s1)-1):
            res+=s1[i][::-1]
            res+=" "
        res+=s1[-1][::-1]
        return res
