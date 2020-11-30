# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res=ListNode(None) #合并之后的新数组
        p=res #保持头节点不动
        if l1==None:  
            res.next=l2
            return res.next
        if l2==None:
            res.next=l1
            return res.next
        while l1 and l2:
            if l1.val < l2.val:
                p.next=l1
                l1=l1.next
            else:
                p.next=l2
                l2=l2.next
            p=p.next
        if l1: #如果l1还没循环结束
            p.next=l1
        else: #如果l2还没循环结束
            p.next=l2
        return res.next

