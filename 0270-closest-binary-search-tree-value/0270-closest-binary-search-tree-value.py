# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        
        '''
        
            5
           /\
          3  7
        
        
        '''
        
        def dfs(node):
            if not node:return
            if abs(node.val - target) < abs(self.res - target):
                self.res = node.val
            elif abs(node.val - target) == abs(self.res - target) and node.val < self.res:
                self.res = node.val
            
            
            #if node.val < target:return
            dfs(node.left)
            if node.val > target:return
            dfs(node.right)
        
        self.res = sys.maxsize
        dfs(root)
        return self.res