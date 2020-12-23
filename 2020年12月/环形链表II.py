# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        res=[] #用来保存当前节点
        node=head
        while node!=None:
            if node.next not in res: 
                res.append(node)
                node=node.next
            else: #如果下一个节点在res中，说明有环
                return node.next
        return None