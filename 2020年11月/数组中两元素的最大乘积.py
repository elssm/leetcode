class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s=sorted(nums)
        return (s[-1]-1)*(s[-2]-1)