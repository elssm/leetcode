class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum=0
        minnum = min(nums)
        for i in nums:
            sum+=i-minnum
        return sum