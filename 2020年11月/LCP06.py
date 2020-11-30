class Solution(object):
    def minCount(self, coins):
        """
        :type coins: List[int]
        :rtype: int
        """
        count = 0
        for i in range(len(coins)):
            if coins[i]%2==0:
                count+=(coins[i]/2)
            else:
                count+=(coins[i]//2)+1
        return count