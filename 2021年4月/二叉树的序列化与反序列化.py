# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def dfs(root):
            if not root:
                return 'null '
            left = dfs(root.left)
            right = dfs(root.right)
            return str(root.val)+' '+left+right
        return dfs(root)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def dfs(data):
            val = data.pop(0)

            if val == 'null':
                return None
            
            node = TreeNode(val)
            node.left = dfs(data)
            node.right = dfs(data)

            return node

        # print(data)
        dataList = data.split(' ') 
        # print(dataList)
        return dfs(dataList)

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))