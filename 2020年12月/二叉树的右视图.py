# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        #层序遍历之后，返回每一层的最后一个数
        if root == None:
            return []
        s = [root]
        res = []
        num = []
        result = []
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
        for i in range(len(res)):
            result.append(res[i][-1])
        return result