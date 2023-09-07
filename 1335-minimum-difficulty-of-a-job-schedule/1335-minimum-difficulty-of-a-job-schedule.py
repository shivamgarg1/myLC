'''

class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        
        
        l = len(jobDifficulty)
        if d > l:return -1
        self.min_cost = sys.maxsize
        #@lru_cache(maxsize=None)
        def rec(i, d, min_cost, arr):
            if d == 0:
                print(arr, min_cost)
                self.min_cost = min(self.min_cost, min_cost)
                return
            total_cost = sys.maxsize
            for j in range(i, l-d+1):
                if d == 1:
                    cost = max(jobDifficulty[j:])
                elif i != j :
                    cost = max(jobDifficulty[i:j+1])
                else:
                    cost = jobDifficulty[j]
                rec(j+1, d -1, min_cost + cost, arr + [j+1])
            return
        
        rec(0, d, 0, [0])
        if self.min_cost >= sys.maxsize:return -1
        return self.min_cost
'''
class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        # If we cannot schedule at least one job per day, 
        # it is impossible to create a schedule
        if n < d:
            return -1
        
        hardest_job_remaining = [0] * n
        hardest_job = 0
        for i in range(n - 1, -1, -1):
            hardest_job = max(hardest_job, jobDifficulty[i])
            hardest_job_remaining[i] = hardest_job
        
        @lru_cache(None)
        def dp(i, day):
            # Base case, it's the last day so we need to finish all the jobs
            if day == d:
                return hardest_job_remaining[i]
            
            best = float("inf")
            hardest = 0
            # Iterate through the options and choose the best
            for j in range(i, n - (d - day)): # Leave at least 1 job per remaining day
                hardest = max(hardest, jobDifficulty[j])
                best = min(best, hardest + dp(j + 1, day + 1)) # Recurrence relation

            return best
        
        return dp(0, 1)