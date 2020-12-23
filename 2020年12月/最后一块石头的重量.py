class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        while len(stones)>1:
            stones = sorted(stones)
            a=stones.pop()
            if len(stones)!=0:
                b=stones.pop()
            if a!=b:
                stones.append(abs(a-b))
        if len(stones)==1:
            return stones[0]
        else:
            return 0
