# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        '''
    
          
        '''
        
        def dfs(node):
            if not node:return (None, 0)
            l , ld = dfs(node.left)
            r, rd = dfs(node.right)
            
            if ld == rd : return (node, ld + 1)
            elif ld > rd : return (l, ld + 1)
            else: return (r, rd + 1)
        
        return dfs(root)[0]