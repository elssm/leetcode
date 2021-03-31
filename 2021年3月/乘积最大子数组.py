class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rev_nums = nums[::-1]
        for i in range(1,len(nums)):
            nums[i] *= nums[i-1] or 1
            rev_nums[i] *= rev_nums[i-1] or 1
        return max(max(nums),max(rev_nums))