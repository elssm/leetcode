class MaxQueue(object):

    def __init__(self):
        self.queue = []


    def max_value(self):
        """
        :rtype: int
        """
        if self.queue:
            return max(self.queue)
        else:
            return -1


    def push_back(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.queue.append(value)


    def pop_front(self):
        """
        :rtype: int
        """
        if self.queue:
            return self.queue.pop(0)
        else:
            return -1


# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()