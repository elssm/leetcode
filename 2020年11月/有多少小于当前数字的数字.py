class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        new_nums = sorted(nums)
        for i in nums:
            res.append(new_nums.index(i))
        return res