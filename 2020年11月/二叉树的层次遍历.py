# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # Definition for a binary tree node.
        if root==None:
            return []
        queue = []
        queue.append(root)
        res = []
        num=[]
        temp=[]
        while len(queue)>0:
            while len(queue)>0:
                node = queue.pop(0)
                # print(type(node))
                num.append(node.val)
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            # print(type(temp[0]))
            res.append(num)
            num=[]
            for i in range(len(temp)):
                queue.append(temp[i])
            temp=[]
        res.reverse()
        return res
