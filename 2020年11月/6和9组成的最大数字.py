class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        num = int(str(num).replace('6','9',1))
        return num