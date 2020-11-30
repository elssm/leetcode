class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        if len(ops)==0:
            return m*n
        first=[]
        second=[]
        for i in range(len(ops)):
            first.append(ops[i][0])
            second.append(ops[i][1])
        min1=min(first)
        min2=min(second)
        return min1*min2