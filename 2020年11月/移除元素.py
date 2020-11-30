class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        c=0
        for i in range(len(nums)):
            if nums[i]!=val: #判断如果这个数不等于val，就从数组第一个数开始覆盖，之后返回c的大小
                nums[c]=nums[i]
                c+=1
        return c