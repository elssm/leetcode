class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if(len(A)<=2):
            return False
        else:
            maxindex=A.index(max(A))
            if maxindex==0 or maxindex==len(A)-1:
                return False
            for i in range(maxindex):
                if A[i]>=A[i+1]:
                    return False
            for j in range(maxindex+1,len(A)):
                if A[j-1]<=A[j]:
                    return False
            return True