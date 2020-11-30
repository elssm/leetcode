class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if r*c != len(nums[0])*len(nums):   #如果无法重塑直接返回原矩阵
            return nums
        newlist=[]  #将原矩阵变为一行的数组
        for i in range(len(nums)):
            for j in range(len(nums[0])):
                newlist.append(nums[i][j])
        res=[]  #新的二维数组
        res_list=[] #每一行的数组
        n=0
        for i in range(r):
            for j in range(c):
                res_list.append(newlist[n])
                n+=1
            res.append(res_list)
            res_list=[]
        return res