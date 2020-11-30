class Solution(object):
    def multiply(self, A, B):
        """
        :type A: int
        :type B: int
        :rtype: int
        """
        if B==0:
            return 0
        return self.multiply(A,B-1)+A