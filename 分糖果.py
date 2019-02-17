class Solution:
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        a=len(candies)
        b=len(set(candies))
        if b<=a/2:
            return b
        else:
            return int(a/2)