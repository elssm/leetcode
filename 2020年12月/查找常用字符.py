class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        res = [] #保存最终结果
        count_num = [] #统计每个字符出现的次数
        s = sorted(A,key=len)[0] #获取A中最短的字符串
        for i in range(len(s)):
            if s[i] in res:
                continue
            for j in range(len(A)):
                count_num.append(A[j].count(s[i]))
            min_num = min(count_num)
            for k in range(min_num):
                res.append(s[i])
            count_num=[]
        return res
