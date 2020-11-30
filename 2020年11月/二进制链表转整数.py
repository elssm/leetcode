# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        #参考方法
        # sum=0
        # while head:
        #     sum=(sum<<1) + head.val
        #     head=head.next
        # return sum
        c=[]
        while head:
            c.append(head.val)
            head=head.next
        j=-1
        sum=0
        for i in range(len(c)):
            sum+=c[j]*pow(2,i)
            j-=1
        return sum