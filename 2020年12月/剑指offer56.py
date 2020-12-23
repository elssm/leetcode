class Solution(object):
    def singleNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for k,v in dict(Counter(nums)).items():
            if v==1:
                res.append(k)
        return res