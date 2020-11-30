class Solution(object):
    def swapNumbers(self, numbers):
        """
        :type numbers: List[int]
        :rtype: List[int]
        """
        numbers[0]=numbers[0]+numbers[1]
        numbers[1]=numbers[0]-numbers[1]
        numbers[0]=numbers[0]-numbers[1]
        return numbers