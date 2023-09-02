# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        '''
        
        1, 2, 3
        ^ 
        
        l = [0 -  i-1]
        
        r = [1 - n]
        '''
        self.memo = {}
        def rec(l , r):
            
            res = []
            if l > r: 
                res.append(None)
                return res
            if (l, r) in self.memo:return self.memo[(l, r)]
            for i in range(l, r+1):
                lnodes = rec(l, i-1)
                rnodes = rec(i+1, r)
                
                for lnode in lnodes:
                    for rnode in rnodes:
                        node = TreeNode(i, lnode, rnode)
                        res.append(node)
            self.memo[(l, r)] = res
            return res
        
        return rec(1, n)