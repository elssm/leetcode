class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """
        nums=[]
        res=0
        for i in range(n):
            nums.append(start+2*i)
        for i in nums:
            res^=i
        return res
