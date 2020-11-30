# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head==None: #判断头是否为空，头为空则返回空
            return None
        node=head
        while node.next!=None: #去除中间与val相等的元素
            if node.next.val==val:
                node.next=node.next.next
            else:
                node=node.next
        if head.val==val: #判断头是否与val相同
            head=head.next
        return head