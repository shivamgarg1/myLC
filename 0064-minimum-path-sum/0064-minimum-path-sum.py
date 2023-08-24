class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])
        dp =  [[0] * C for i in range(R)]
        for c in range(C):
            dp[0][c] = dp[0][c-1] + grid[0][c] if c > 0 else grid[0][0]
        
        
        for r in range(1, R):
            dp[r][0] = dp[r-1][0] + grid[r][0]
        
        for r in range(1, R):
            for c in range(1, C):
                dp[r][c] = min(dp[r-1][c], dp[r][c-1]) + grid[r][c]
        
        return dp[R-1][C-1]
        