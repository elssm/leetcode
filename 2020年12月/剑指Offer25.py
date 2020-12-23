# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        node=ListNode()
        if l1==None:
            node.next=l2
        if l2==None:
            node.next=l1
        head=node
        while l1 !=None and l2!=None:
            if l1.val>l2.val:
                head.next=l2
                l2=l2.next
                head=head.next
            else:
                head.next=l1
                l1=l1.next
                head=head.next
        if l1!=None:
            head.next=l1
        if l2!=None:
            head.next=l2
        return node.next
