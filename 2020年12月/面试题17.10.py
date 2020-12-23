class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = dict(Counter(nums))
        res = sorted(d.items(),key=lambda d:d[1],reverse=True)
        if res[0][1]>len(nums)//2:
            return res[0][0]
        else:
            return -1