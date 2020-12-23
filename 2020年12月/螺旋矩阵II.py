class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        #思路
        #初始化res之后，顺时针旋转，向每一行头部添加
        if n==1:
            return [[1]]
        res=[[n*n-1],[n*n]]
        i=n*n-2
        while i>=1:
            for j in range(len(res)):
                res[j].insert(0,i)
                i-=1
            res=list(map(list,zip(*res)))
            for j in res:
                j.reverse()
        return res