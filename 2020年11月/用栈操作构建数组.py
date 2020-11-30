class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
        c=[]
        num=1
        for i in range(target[-1]): #target[-1]是列表中最大的值
            if num in target: #如果数在列表中，只需要一次push
                c.append('Push')
                num+=1
            else: #如果不在，则需要一次Push一次Pop
                c.append('Push')
                c.append('Pop')
                num+=1
        return c
