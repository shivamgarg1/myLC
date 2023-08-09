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
        self.ls = []
        if not root:return
        
        def dfs(node):
            if not node:return
            dfs(node.left)
            self.ls.append(node)
            dfs(node.right)
        
        dfs(root)
        
        for i in range(len(self.ls) - 1):
            self.ls[i].right = self.ls[i+1]
            self.ls[i+1].left = self.ls[i]
        self.ls[0].left = self.ls[-1]
        self.ls[-1].right = self.ls[0]
        
        return self.ls[0]