class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        res=[]
        for i in accounts:
            res.append(sum(i))
        return max(res)