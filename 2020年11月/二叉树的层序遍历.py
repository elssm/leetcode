# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root==None:
            return []
        queue = []
        queue.append(root) #先将根节点入队列
        res = [] #保存最终层次遍历的结果
        num=[] #保存本层的值
        temp=[] #临时保存下一层的节点
        while len(queue)>0:
            while len(queue)>0:
                node = queue.pop(0) #出队列
                # print(type(node))
                num.append(node.val) #将值加入num中
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            # print(type(temp[0]))
            res.append(num) #将本层节点存入res中
            num=[] #对num置空
            for i in range(len(temp)): #将temp中的节点加入到queue中，不能直接queue.append
                queue.append(temp[i])
            temp=[] #对temp置空
        return res



