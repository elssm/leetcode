class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        res=[]
        for i in matrix:
            res+=i
        res=sorted(res)
        return res[k-1]