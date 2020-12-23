class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for k,v in dict(Counter(nums)).items():
            if v==2:
                res.append(k)
        return res