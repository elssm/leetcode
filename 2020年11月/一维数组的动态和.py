class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res=[]
        for i in range(1,len(nums)+1):
            s=0
            for j in range(i):
                s+=nums[j]
            res.append(s)
        return res
