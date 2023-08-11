# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.total_sum = 0
        
        def dfs(node, running_str):
            if not node:return
            running_str += str(node.val)
            if not node.left and not node.right:
                self.total_sum += int(running_str)
                running_str = running_str[:-1]
                return
            dfs(node.left, running_str )
            dfs(node.right, running_str)
        dfs(root, '')
        return self.total_sum