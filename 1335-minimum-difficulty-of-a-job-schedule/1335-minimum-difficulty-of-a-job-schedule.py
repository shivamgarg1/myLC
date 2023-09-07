class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        
        
        l = len(jobDifficulty)
        if d > l:return -1
        self.min_cost = sys.maxsize
        diffs = jobDifficulty[:]
        for i in range(l-2, -1, -1):
            diffs[i] = max(diffs[i+1] , diffs[i])
        @cache
        def rec(i, d):
            if d == 1:
                return diffs[i]
            total_cost = 0
            res = sys.maxsize
            for j in range(i, l-d+1):
                total_cost = max(total_cost, jobDifficulty[j])
                res = min( res, total_cost + rec(j+1, d -1))
            return res
        
        return rec(0, d)