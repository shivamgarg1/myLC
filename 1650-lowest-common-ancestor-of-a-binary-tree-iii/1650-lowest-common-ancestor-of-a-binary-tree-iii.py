"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        '''
        
        
        subtree 1:
        p -> d -> c -> b -> a -> null
        
        
        
        case1:
        q -> b -> a -> null, ans = b
        
        case2:
        
        q -> p -> .. ans = p
        
        case3:
        p -> d -> c -> 'q' -> a -> null ans = q
        
        
        '''
        
        seen = set()
        while p:
            if p == q: return q
            seen.add(p)
            p = p.parent
        
        while q:
            if q in seen:return q
            q = q.parent
            
        