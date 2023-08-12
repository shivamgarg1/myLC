# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        '''
        
        1*
        /\
        2 3*
        \ /
        5 4*
        
        
        algo (DFS approach):
        0) intitialize max_depth 
        1) initialize a map, key is depth and value is node.val
        2) at every node, check righ side node and then left side node
        3) at every level, insert into map key value pair
        4) return values of the map
        
        depth : node.val
        1     : 1
        2     : 3
        3     : 4
    
        '''
        
        if not root: return []
        self.max_depth = 0
        m = defaultdict(int)
        
        def dfs(node, depth):
            if not node:return
            depth += 1
            self.max_depth = max(self.max_depth, depth)
            if self.max_depth not in m:
                m[self.max_depth] = node.val
            
            dfs(node.right, depth)
            dfs(node.left, depth)
        
        dfs(root, 0)
        
        res = []
        for i in range(1, self.max_depth+1):
            res.append(m[i])
        return res
            
        
        