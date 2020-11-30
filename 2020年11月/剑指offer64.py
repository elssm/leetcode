class Solution(object):
    def sumNums(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1:
            return 1
        if n>1:
            return n+self.sumNums(n-1)