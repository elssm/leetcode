# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        l1=0
        l2=0
        node1=headA
        node2=headB
        while headA: #求第一个链表长度
            l1+=1
            headA=headA.next
        while headB: #求第二个链表长度
            l2+=1
            headB=headB.next
        s=l1-l2
        while s>0: #对齐两个链表长度
            node1=node1.next
            s-=1
        while s<0:
            node2=node2.next
            s+=1
        # while node1 and node2:
        #     if node1==node2:
        #         return node1
        #     node1=node1.next
        #     node2=node2.next
        # return None
        while node1!=node2: #从头开始判断地址是否相同
            node1=node1.next
            node2=node2.next
        return node1