# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        
        '''
        
             2
             /
             1 
             
             
        
        '''
        
        self.res = 0
        
        def dfs(node):
            if not node: return ( 0, 0)
            if not node.left and not node.right:
                self.res += 1
                return (node.val, 1)
            l, lnum = dfs(node.left)
            r, rnum = dfs(node.right)
            
            if floor( (l + r + node.val) / (lnum + rnum + 1) ) == node.val:
                self.res += 1
            return ( l + r + node.val, lnum + rnum + 1)
        
        dfs(root)
        
        return self.res
            
            