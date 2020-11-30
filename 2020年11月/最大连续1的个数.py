class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxnum=0
        count=0
        for i in range(len(nums)):
            if nums[i]==1:
                count+=1
            else:
                if count>maxnum:
                    maxnum=count
                count=0
        if count>maxnum:
            maxnum=count
        return maxnum