class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        R = len(matrix)
        C = len(matrix[0])
        
        if R == 1 and C == 1:return 1
        
        memo = {}
        def dfs(r, c, seen, last):
            if (r, c) in seen: return 0
            if matrix[r][c] <= last: return 0
            if (r, c) in memo:return memo[(r, c)]
            seen.add((r, c))
            
            max_len = -sys.maxsize
            for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                new_r = r + dr
                new_c = c + dc
                if 0 <= new_r < R and 0 <= new_c < C:
                    max_len = max(max_len, 1 + dfs(new_r, new_c, seen, matrix[r][c]))
            
            seen.remove((r, c))
            memo[(r, c)] = max_len
            return max_len
        
        res = -sys.maxsize
        for r in range(R):
            for c in range(C):
                res = max(res, dfs(r, c, set(), -1))
        return res
        