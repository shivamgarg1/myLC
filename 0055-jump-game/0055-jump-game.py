class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        l = len(nums)
        dp = {}
        #@lru_cache(maxsize=None)
        def rec(i):
            if i >= l-1:return True
            if nums[i] == 0: return False
            if i in dp:return dp[i]
            for val in range(nums[i], 0, -1):
                if rec(i + val):
                    dp[i] = True
                    return True
            dp[i] = False
            return False
        
        return rec(0)