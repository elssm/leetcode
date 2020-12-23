# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head==None:
            return head
        node=head
        count=0
        while node!=None: #计算链表长度和最后一个节点
            count+=1
            pre=node
            node=node.next
        s=k%count 
        t=count-s
        pre.next=head
        for i in range(t):
            prenode=head
            head=head.next
        prenode.next=None
        return head        