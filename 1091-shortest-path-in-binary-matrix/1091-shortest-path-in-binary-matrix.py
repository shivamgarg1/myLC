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
        
        if grid[0][0] == 1 or grid[R-1][C-1] == 1: return -1
        elif R == 1 and C == 1 and grid[R-1][C-1] == 0: return 1
        q = [[0,0]]
        while q :
            top = q.pop(0)
            for dr, dc in [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]:
                new_dr = top[0] + dr
                new_dc = top[1] + dc
                
                if 0 <= new_dr < R and 0<= new_dc < C and grid[new_dr][new_dc] == 0:
                    grid[new_dr][new_dc] = grid[top[0]][top[1]] -1
                    
                    q.append([new_dr, new_dc])
        
        if grid[R-1][C-1] == 0: return -1
        
        return abs(grid[R-1][C-1]) + 1