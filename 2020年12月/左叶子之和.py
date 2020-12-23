# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = []
        def sumleaves(node):
            if node == None:
                return 0
            if node.left and node.left.left==None and node.left.right == None:
                res.append(node.left.val)
            sumleaves(node.left)
            sumleaves(node.right)
        sumleaves(root)
        return sum(res)
