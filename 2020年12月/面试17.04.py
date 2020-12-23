class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #方法一 公式法
        return ((len(nums)+1)*len(nums))//2 - sum(nums)

        #方法二
        # res=[]
        # for i in range(len(nums)+1):
        #     res.append(-1)
        # for i in nums:
        #     res[i]=i
        # for i in range(len(res)):
        #     if res[i]==-1:
        #         return i