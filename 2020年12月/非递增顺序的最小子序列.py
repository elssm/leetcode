class Solution(object):
    def minSubsequence(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums=sorted(nums,reverse=True)
        for i in range(1,len(nums)):
            if sum(nums[0:i])>sum(nums[i:len(nums)]):
                return nums[0:i]
        return nums