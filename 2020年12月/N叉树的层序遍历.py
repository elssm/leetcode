"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if root ==None:
            return []
        s = [root]
        res = []
        num = []
        while s:
            num=[]
            for i in s: #将本层节点加入num
                num.append(i.val)
            res.append(num)
            for i in range(len(s)): #对本层节点遍历并加入本层节点的孩子节点
                node = s.pop(0)
                s.extend(node.children)     
        return res
