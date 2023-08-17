# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        #if root1.val != root2.val: return False
        
        def dfs(node1, node2):
            if ( node1 and not node2) or ( not node1 and node2):return False
            if not node1 and not node2:return True
            if node1.val != node2.val:return False
            l = dfs(node1.left, node2.left) or  dfs(node1.left, node2.right)
            r = dfs(node1.right, node2.right) or dfs(node1.right, node2.left)
            return l and r
        return dfs(root1, root2)