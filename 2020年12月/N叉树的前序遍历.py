"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        #递归
        # res = []
        # def pre(root):
        #     if root == None:
        #         return []
        #     res.append(root.val)
        #     for i in root.children:
        #         pre(i)
        # pre(root)
        # return res

        #非递归
        if root == None:
            return []
        s=[root]
        res = []
        while s:
            node = s.pop()
            res.append(node.val)
            s.extend(node.children[::-1])
        return res