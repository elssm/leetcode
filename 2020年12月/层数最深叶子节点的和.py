# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #思路：先把每一层存到一个列表num中，再把num依次存到res中，最后返回res最后一个列表的和
        if root == None:
            return 0
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
        return sum(res[-1])