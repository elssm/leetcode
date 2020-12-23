class Solution(object):
    def luckyNumbers (self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        temp=[]
        temp1=[]
        res=[]
        matrix1=map(list,zip(*matrix))
        for i in range(len(matrix)):
            temp.append(min(matrix[i]))
        for i in range(len(matrix1)):
            temp1.append(max(matrix1[i]))
        # return list(set(temp).intersection(set(temp1)))
        for i in temp:
            if i in temp1:
                res.append(i)
        return res

