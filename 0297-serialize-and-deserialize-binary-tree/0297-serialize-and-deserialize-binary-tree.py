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
        
        self.res = ''
        
        def dfs(node):
            if not node:
                self.res += 'None'
                self.res += ','
                return
            self.res += str(node.val)
            self.res += ','
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        if self.res[-1] == ',':
            self.res = self.res[:-1]
        return self.res
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data_val = data.split(',')
        self.i = -1
        def create_nodes(data_val):
            self.i += 1
            if data_val[self.i] == 'None':
                return None
            
            new_node = TreeNode(int(data_val[self.i]))
            new_node.left = create_nodes(data_val)
            new_node.right = create_nodes(data_val)
            return new_node
        
        return create_nodes(data_val)
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))