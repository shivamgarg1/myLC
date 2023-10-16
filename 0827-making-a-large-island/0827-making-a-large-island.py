class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        '''
        
        1) store in a list indexed areas, where index starts from 2. 0 and 1 can contain 0 area islands
        2) for every 0, find out inclusion of areas[N/E/S/W] will aggregate to. 
        2.5) initialize max_area to max of all areas list
        3) update max_area if it is more than previous max_area
        4) return max_area
        
        
        '''
        
        areas = [0, 0]
        R = len(grid)
        C = len(grid[0])
        index = 2
        
        def dfs(r, c, index):
            if r >= R or r < 0 or c >= C or c < 0 or grid[r][c] != 1:return 0
            grid[r][c] = index
            total_ways = 0
            for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                new_r = r + dr
                new_c = c + dc
                #if grid[new_r][new_c] == 1:
                total_ways += dfs(new_r, new_c, index)
            return total_ways + 1
        
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    area = dfs(r, c, index)
                    areas.append(area)
                    index += 1
                    
        max_area = max(areas)
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0:
                    tmp_area = 0
                    seen = set()
                    for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                        new_r = r + dr
                        new_c = c + dc
                        if 0 <= new_r < R and 0 <= new_c < C and grid[new_r][new_c] not in seen:
                            tmp_area += areas[grid[new_r][new_c]]
                            seen.add(grid[new_r][new_c])
                    max_area = max(max_area, 1 + tmp_area)
        
        return max_area
