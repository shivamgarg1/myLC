class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        '''
        
        1) initialize queue ds
        2) start with (0, 0)
        3) initialize a counter 
        4) start iterating on candidate paths - 8 directional
        5) if (n-1, n-1) is reached, return the counter, 
         -> else return -1
        
        
        
        R = 2, C= 2
        iteration1) r = 0, c= 0
        
        '''
        
        
        R = len(grid)
        C = len(grid[0])
        if grid[0][0] == 1 or grid[R-1][C-1]:return -1
        if R == 1 and C == 1 and grid[0][0] == 0: return 1
        
        count = 1
        q = [(0, 0)]
        grid[0][0] = 1
        while q:
            r, c = q.pop(0)
            for dr, dc in [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]:
                new_r = dr + r
                new_c = dc + c
                if 0 <= new_r < R and 0 <= new_c < C :
                    if new_r == R - 1 and new_c == C - 1 and grid[new_r][new_c] == 0:
                        return grid[r][c] + 1
                    elif grid[new_r][new_c] == 0:
                        grid[new_r][new_c] = grid[r][c] + 1
                        q.append((new_r, new_c))
        
        return -1