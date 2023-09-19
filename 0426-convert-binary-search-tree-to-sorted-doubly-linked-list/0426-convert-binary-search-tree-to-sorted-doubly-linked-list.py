"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        '''
        
                4
               / \
              2   5
             / \
            1   3 
        
        
        5 <-- 1 <=> 2 <=> 3 <=> 4 <=> 5 --> 1
        '''
        self.min_node = None
        self.max_node = None
        if not root: return
        def dfs(node):
            if not node:return
            dfs(node.left)
            if self.max_node:
                self.max_node.right = node
                node.left = self.max_node
            else:
                self.min_node = node
            self.max_node = node
            dfs(node.right)
            
        dfs(root)
        self.min_node.left = self.max_node
        self.max_node.right = self.min_node
        return self.min_node
            