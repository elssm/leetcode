class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_num=0
        nums = sorted(nums)
        for i in range(1,len(nums)):
            if nums[i]-nums[i-1] > max_num:
                max_num = nums[i]-nums[i-1]
        return max_num