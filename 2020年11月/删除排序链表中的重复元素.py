# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head==None or head.next==None:
            return head
        p=head
        q=head.next
        while q:
            if p.val==q.val:
                p.next=q.next
                q=q.next
            else:
                p=q
                q=q.next
        return head