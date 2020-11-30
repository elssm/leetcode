class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        #第一种方法
        c=[]
        while n>0:
            c.append(n%2)
            n=n/2
        return c.count(1)
        
        #第二种方法（参考）
        # return bin(n).count('1')