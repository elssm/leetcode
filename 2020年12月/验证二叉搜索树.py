# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        #中序遍历之后判断是否排序正常
        res = []
        def inorder(node):
            if node == None:
                return False
            inorder(node.left)
            res.append(node.val)
            inorder(node.right)
        inorder(root)
        if sorted(list(set(res))) == res:
            return True
        else:
            return False