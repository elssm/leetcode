# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #层序遍历之后输出最后一个列表中的第一个值
        s = [root]
        num = []
        res = []
        while s:
            num = []
            for i in s:
                num.append(i.val)
            res.append(num)
            for i in range(len(s)):
                node = s.pop(0)
                if node.left:
                    s.append(node.left)
                if node.right:
                    s.append(node.right)    
        return res[-1][0]