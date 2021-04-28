# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head.next==None and n==1:
            return None
        """
        nhead:找到需要删除的节点
        pre_nhead:找到需要删除的节点的前一个节点
        temp:通过从temp向后遍历找到倒数第n个节点
        """
        nhead = pre_nhead = temp = head
        flag = 1 #如果flag没变，说明没进while循环，说明要删除的是头节点
        while n-1>0:
            temp =temp.next
            n-=1
        # print(temp.val)
        while temp.next!=None:
            flag = 0
            temp = temp.next
            pre_nhead = nhead
            nhead = nhead.next
        if flag:
            head = head.next
            return head 
        pre_nhead.next = nhead.next
        return head