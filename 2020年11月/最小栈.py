class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.l = [] #列表操作
        self.index = -1


    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.l.append(x)
        self.index+=1


    def pop(self):
        """
        :rtype: None
        """
        self.l.pop()
        self.index-=1


    def top(self):
        """
        :rtype: int
        """
        return self.l[-1]
        # return self.l[self.index]


    def getMin(self):
        """
        :rtype: int
        """
        return min(self.l)



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()