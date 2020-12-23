# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        res = []
        s = [root]
        while s:
            node = s.pop(0)
            res.append(node.val)
            if node.left:
                s.append(node.left)
            if node.right:
                s.append(node.right)
        return res