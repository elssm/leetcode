class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        s=sorted(arr)
        for i in range(1,len(arr)-1):
            if s[i]-s[i-1]!=s[i+1]-s[i]:
                return False
        return True