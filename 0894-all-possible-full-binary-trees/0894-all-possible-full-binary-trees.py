# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        
        '''
        
        n = 1
        n = 3
           0
           /\
          0  0
          
          0, 0 , 0, 0, 0
          
        '''
        
        if n % 2 == 0: return []
        
        dp = defaultdict(list)
        dp[1].append(TreeNode(0))
        
        for count in range(3, n+1, 2):
            for i in range(1, count - 1, 2):
                j = count - i - 1
                for l in dp[i]:
                    for r in dp[j]: 
                        node = TreeNode(0, l, r)
                        dp[count].append(node)
        
        return dp[n]