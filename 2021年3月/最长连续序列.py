class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        nums = list(set(nums))
        nums = sorted(nums)
        # print(nums)
        res=[1]
        count=1
        for i in range(1,len(nums)):
            if nums[i]-nums[i-1]==1:
                count+=1
            else:
                res.append(count)
                count=1
        res.append(count)
        return max(res)