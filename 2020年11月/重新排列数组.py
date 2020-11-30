class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        res=[]
        j=n
        for i in range(len(nums)-n):
            res.append(nums[i])
            res.append(nums[j])
            j+=1
        return res
