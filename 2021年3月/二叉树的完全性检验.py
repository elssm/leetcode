# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root==None:
            return False
        q=[root]
        num=[]
        while len(q)>0:
            node = q.pop(0)
            num.append(node)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        temp=0
        for i in range(len(num)):
            if num[i].left==None and num[i].right!=None:
                return False
            elif num[i].left!=None and num[i].right==None:
                temp=i
                for j in range(temp+1,len(num)):
                    if num[j].left!=None or num[j].right!=None:
                        return False
                return True
            elif num[i].left==None and num[i].right==None:
                temp=i
                for j in range(temp+1,len(num)):
                    if num[j].left!=None or num[j].right!=None:
                        return False
                return True
            else:
                continue
        return True
            
