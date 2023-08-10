# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        '''
        [1, 2, 3, 4,5]
        
        1) do dfs
        2) check for number of nodes in left subtree
        3) check for number of nodes in right subtree
        4) check if this is max + 1
        5) return max of left branch/ right branch + 1
        6) return self.max_count
        '''
        
        
        self.max_count = 0
        
        def dfs(node):
            if not node: return 0
            l = dfs(node.left)
            r = dfs(node.right)
            self.max_count = max(self.max_count, l + r+1)
            return max(l, r) + 1
        
        dfs(root)
        return self.max_count - 1
        
        
        
        