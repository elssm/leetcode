# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # if root==None:
        #     return []
        # return [root.val]+self.preorderTraversal(root.left)+self.preorderTraversal(root.right)
        res=[]
        def pre(node):
            if node==None:
                return []
            res.append(node.val)
            pre(node.left)
            pre(node.right)
        pre(root)
        return res