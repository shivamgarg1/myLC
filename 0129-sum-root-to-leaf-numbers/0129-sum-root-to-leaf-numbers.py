# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        
        
        def dfs(node, num):
            if not node:return
            
            if not node.right and not node.left:
                self.res += int(num + str(node.val))
                return
            
            dfs(node.left, num + str(node.val))
            dfs(node.right, num + str(node.val))
    
        
        dfs(root, '')
        return self.res