# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''
        
           1
          / \
         2   3
        / \  / \
        4  5 6  7
        
        ans -> [4], [2], [1, 5, 6], [3], [7]
        assumptions:
        binary t, no loops, at least 1 node.
        
        Space: O(N)
        Time: O(N)
        
        '''
        if not root:return[]
        m = defaultdict(list)
        
        q = [(root, 0)]
        min_c = max_c = 0
        
        while q:
            new_q = []
            for node, col in q:
                max_c = max(max_c, col)
                min_c = min(min_c, col)
                m[col].append(node.val)
                if node.left:
                    new_q.append((node.left, col-1))
                if node.right:
                    new_q.append((node.right, col+1))
            q = new_q
        
        
        res = [m[k] for k in range(min_c, max_c+1)]
        return res