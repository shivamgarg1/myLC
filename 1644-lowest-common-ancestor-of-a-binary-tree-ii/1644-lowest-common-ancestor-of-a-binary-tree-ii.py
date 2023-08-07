# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        self.p = False
        self.q = False
        
        def dfs(node, p, q):
            if not node:return
            if node == p:return p
            if node == q:return q
            l = dfs(node.left, p, q)
            r = dfs(node.right, p, q)
            if l and r:return node
            return l or r
        
        def dfs_for_checking_nodes(node, p, q):
            if not node:return
            
            if node == p:
                self.p = True
            if node == q:
                self.q = True
            dfs_for_checking_nodes(node.left, p, q)
            dfs_for_checking_nodes(node.right, p, q)
        
        dfs_for_checking_nodes(root, p, q)
        res = dfs(root, p, q)
        if self.p and self.q:
            return res
        return None