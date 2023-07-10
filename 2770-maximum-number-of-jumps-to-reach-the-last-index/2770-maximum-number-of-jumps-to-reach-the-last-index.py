class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        l = len(nums)
        dp = [-1] * l
        def rec(i):
            if i == l - 1: 
                return 0 
            if dp[i] != -1:return dp[i]
            steps = -sys.maxsize
            for j in range(i+1, l):
                if abs(nums[j] - nums[i]) <= target:
                    steps = max(steps, 1 + rec(j))
            dp[i] = steps
            return steps
            
        
        steps = rec(0)
        if steps > 0:return steps
        return -1