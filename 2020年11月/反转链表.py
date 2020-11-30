# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head:
            pre=head
            q=head.next
            while pre.next:
                pre.next=q.next
                q.next=head
                head=q
                q=pre.next
        return head