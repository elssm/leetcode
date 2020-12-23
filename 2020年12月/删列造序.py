class Solution(object):
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        #方法-
        # count=0
        # temp=[]
        # for i in range(len(A[0])):
        #     for j in range(len(A)):
        #         temp.append(A[j][i])
        #     if sorted(temp)!=temp:
        #         count+=1
        #     temp=[]
        # return count

        #zip函数
        res=0
        for i in zip(*A):
            if sorted(list(i))!=list(i):
                res+=1
        return res