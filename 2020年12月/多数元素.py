class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = sorted(nums)
        return res[(len(nums)//2)]