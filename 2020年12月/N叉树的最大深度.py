"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        #利用队列
        # if root==None:
        #     return 0
        # s = [root]
        # num = []
        # res = []
        # while s:
        #     num = []
        #     for i in s:
        #         num.append(i.val)
        #     res.append(num)
        #     for i in range(len(s)):
        #         node = s.pop(0)
        #         s.extend(node.children)
        # return len(res)

        #递归
        if root == None:
            return 0
        m = 0
        res = 
        for i in root.children:
            m = max(m,self.maxDepth(i))
        return m+1
                