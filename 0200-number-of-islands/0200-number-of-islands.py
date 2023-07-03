class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        count = 0
        
        def rec(r, c):
            if grid[r][c] != '1':return
            
            grid[r][c] = -1
            
            for dr, dc in [(-1,0), (0, 1), (1, 0), (0, -1)]:
                new_r = r + dr
                new_c = c + dc
                if 0 <= new_r < rows and 0 <= new_c < cols:
                    rec(new_r, new_c)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    count += 1
                    rec(r, c)
        
        return count
            
            
            