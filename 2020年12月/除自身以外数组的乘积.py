class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #初始化res1和res2，res1保存当前数字左边所有的数字乘积
        #res2保存当前数字右边所有的数字乘积，最后对应相乘
        res=[]
        res1=[1 for i in range(len(nums))]
        res2 = [1 for i in range(len(nums))]
        for i in range(1,len(nums)):
            res1[i]=nums[i-1]*res1[i-1]
        for j in range(len(nums)-2,-1,-1):
            res2[j]=nums[j+1]*res2[j+1]
        for i in range(len(res1)):
            res.append(res1[i]*res2[i])
        return res