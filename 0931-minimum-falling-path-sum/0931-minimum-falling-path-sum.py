class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        '''
        
        algo:
        1) create recursive fn whose resul is stored as:
            base condition:
            if r == R-1 and c == C - 1:return grid[r][c]
            min_sum = min(rec(r+1, c-1), rec(r+1, c+1)) + grid[r][c]
        
        '''
        
        
        R = len(matrix)
        C = len(matrix[0])
        
        @lru_cache(maxsize=None)
        def rec(r, c):
            if r == R - 1 : return matrix[r][c]
            elif c == 0:return min(rec(r+1, c+1), rec(r+1, c)) + matrix[r][c]
            elif c == C - 1:return min(rec(r+1, c-1), rec(r+1, c)) + matrix[r][c]
            else:return min(rec(r+1, c-1), rec(r+1, c+1), rec(r+1, c)) + matrix[r][c]
        
        res = sys.maxsize
        for c in range(C):
            res = min(res, rec(0, c))
        return res