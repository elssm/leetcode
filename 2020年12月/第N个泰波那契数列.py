class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        #利用动态规划，和爬楼梯类似，不过是加上3个数
        res=[0,1,1]
        for i in range(n-2):
            res.append(res[-1]+res[-2]+res[-3])
        return res[n]

        #方法2
        # a=0
        # b=1
        # c=1
        # for i in range(n):
        #     a,b,c = b,c,a+b+c
        # return a