class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        res=[[1]*n]*m #创建二维数组
        for i in range(1,m):
            for j in range(1,n):
                res[i][j]=res[i][j-1]+res[i-1][j]
        return res[-1][-1]