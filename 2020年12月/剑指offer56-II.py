class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d={}
        for i in nums:
            if i in d.keys():
                d[i]+=1
            else:
                d[i]=0
        for k,v in d.items():
            if v==0:
                return k