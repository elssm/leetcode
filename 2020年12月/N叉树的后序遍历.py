"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        #递归
        # res = []

        # def post(root):
        #     if root == None:
        #         return []
        #     for i in root.children:
        #         post(i)
        #     res.append(root.val)
        # post(root)
        # return res

        #非递归
        if root == None:
            return []
        s=[root]
        res = []
        while s:
            node = s.pop()
            res.append(node.val)
            s.extend(node.children)
        return res[::-1]