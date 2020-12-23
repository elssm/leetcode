# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        #中序遍历之后存入res中，返回res[k-1]即可
        res = []

        def pre(node):
            if node == None:
                return 0
            pre(node.left)
            res.append(node.val)
            pre(node.right)
        pre(root)
        return res[k-1]
        # print(res)