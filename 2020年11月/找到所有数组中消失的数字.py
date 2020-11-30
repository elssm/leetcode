class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        c=set(nums)
        d=set()
        for i in range(1,len(nums)+1):
                d.add(i)
        result = d.difference(c)

        return list(result)
