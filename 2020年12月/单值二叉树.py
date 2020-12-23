# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        #前序遍历之后set一下
        # res = []
        # def pre(node):
        #     if node == None:
        #         return True
        #     res.append(node.val)
        #     pre(node.left)
        #     pre(node.right)
        # pre(root)
        # # print(res)
        # if len(set(res))==1:
        #     return True
        # else:
        #     return False

        #递归
        if root == None:
            return True
        val = root.val
        def isUnival(root,val):
            if root == None:
                return True
            return root.val == val and isUnival(root.left,val) and isUnival(root.right,val)
        return isUnival(root,val)