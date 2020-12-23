class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        #思路，从第二天开始遍历，最大收益总是当前这一天减去之前几天的最小值
        #遍历结束后，最大收益就是max_num
        #思路一
        # max_num=0
        # if len(prices)==0:
        #     return 0
        # for i in range(1,len(prices)):
        #     if prices[i]-min(prices[:i])>max_num:
        #         max_num = prices[i]-min(prices[:i])
        # return max_num

        #思路二
        max_num=0
        if len(prices)==0:
            return 0
        min_num=prices[0]
        for i in range(1,len(prices)):
            min_num = min(min_num,prices[i-1])
            if prices[i]-min_num>max_num:
                max_num = prices[i]-min_num
        return max_num
