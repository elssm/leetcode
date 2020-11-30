class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==3:
            return nums[0]*nums[1]*nums[2]
        a=sorted(nums)
        if a[0]*a[1]*a[len(a)-1] > a[len(a)-1]*a[len(a)-2]*a[len(a)-3]:
            return a[0]*a[1]*a[len(a)-1]
        else:
            return a[len(a)-1]*a[len(a)-2]*a[len(a)-3]