class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows==0:
            return []
        if numRows==1:
            return [[1]]
        if numRows==2:
            return [[1],[1,1]]
        nums=[[1],[1,1]]
        for i in range(3,numRows+1):
            nums_list=[1]
            for j in range(1,i-1):
                nums_list.append(nums[i-2][j-1]+nums[i-2][j])
            nums_list.append(1)
            nums.append(nums_list)
            nums_list=[]
        return nums