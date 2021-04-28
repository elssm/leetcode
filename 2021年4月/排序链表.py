# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        h_head = ListNode(None) #申请头节点
        res = [] #将节点保存在列表中
        while head is not None:
            next_h = head.next
            head.next = None #为了列表排序时不超时
            res.append(head)
            head = next_h
            # head = head.next
        res = sorted(res,key = lambda x:x.val)
        # print(res)
        n = len(res)
        if n == 0:
            return None
        h_head.next = res[0]
        for i in range(n-1):
            res[i].next = res[i+1]
        # print(res)
        return h_head.next