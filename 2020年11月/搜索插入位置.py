class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        #第一种方法
        nums.append(target)
        nums = sorted(nums)
        return nums.index(target)

        #第二种方法
        # for i in range(len(nums)):
        #     if nums[i]>=target:
        #         return i
        # return len(nums)