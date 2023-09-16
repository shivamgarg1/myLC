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
        min_level = sys.maxsize
        max_level = -sys.maxsize
        q = [(root, 0)]
        while q:
            node, level = q.pop(0)
            min_level = min(min_level, level)
            max_level = max(max_level, level)
            m[level].append(node.val)
            if node.left:
                q.append((node.left, level - 1))
            if node.right:
                q.append((node.right, level + 1))
        
        return [m[i] for i in range(min_level, max_level + 1)]