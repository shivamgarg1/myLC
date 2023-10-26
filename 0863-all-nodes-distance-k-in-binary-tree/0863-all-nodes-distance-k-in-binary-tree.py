# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        self.res = []
        def dfs(node, parent):
            if not node:return
            node.parent = parent
            dfs(node.left, node)
            dfs(node.right, node)
        
        
        visited = set()
        def dfs2(node, level):
            if not node or node.val in visited:return
            visited.add(node.val)
            if level == k:
                self.res.append(node.val)
            dfs2(node.left, level + 1)
            dfs2(node.right, level + 1)
            dfs2(node.parent, level + 1)
        
        dfs(root, None)
        dfs2(target, 0)
        return self.res
        
        