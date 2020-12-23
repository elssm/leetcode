class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[[]]
        for i in nums:
            # print([j+[i] for j in res])
            res+=[j+[i] for j in res]
        return res