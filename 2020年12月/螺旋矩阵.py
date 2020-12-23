class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res=[]
        while len(matrix)!=0:
            for i in matrix[0]: #将二维数组第一行加入res中
                res.append(i)
            matrix.pop(0) #弹出二维数组第一行
            matrix=list(zip(*matrix)) #将剩下的二维数组逆时针旋转90度
            matrix.reverse() #对二维数组进行逆转
        return res