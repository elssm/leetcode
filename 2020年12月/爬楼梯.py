class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        #知道前三个值，后面每个值都是最后两个值相加
        res=[1,2,3]
        for i in range(n-3):
            res.append(res[-1]+res[-2])
        return res[n-1]