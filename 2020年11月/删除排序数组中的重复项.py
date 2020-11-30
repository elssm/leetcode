class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c=0
        for i in range(1,len(nums)):
            if nums[i]!=nums[c]:
                nums[c+1]=nums[i]
                c+=1
        return c+1
