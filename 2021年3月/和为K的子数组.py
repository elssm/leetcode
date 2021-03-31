class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        m={0:1}
        sumN=0
        count=0
        for i in range(len(nums)):
            sumN+=nums[i]
            count+=m.get(sumN-k,0)
            m[sumN]=m.get(sumN,0)+1
        return count