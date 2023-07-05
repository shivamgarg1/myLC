class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        seen = set()
        rows = len(grid)
        cols = len(grid[0])
        
        def rec(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols: return False
            if grid[r][c] != 0:return True
            if (r, c) in seen:return True
            seen.add((r,c))
            
            is_closed = True
            for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                new_r = r + dx
                new_c = c + dy
                if not rec(new_r, new_c):
                    is_closed = False
            
            return is_closed
        
        count = 0
        for r in range(rows):
            for c in range(cols):
                if (r, c) not in seen and grid[r][c] == 0 and rec(r, c):
                    count += 1
        
        return count
        