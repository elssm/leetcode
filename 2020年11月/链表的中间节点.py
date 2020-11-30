# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head==None or head.next==None:
            return head
        p=head
        q=head.next #快慢指针
        while p.next!=None:
            p=p.next
            if q.next==None:
                return p
            if q.next.next==None:
                return p
            q=q.next.next
        return p
