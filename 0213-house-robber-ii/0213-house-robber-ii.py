class Solution:
    def rob(self, nums: List[int]) -> int:
        
        l = len(nums)
        if l <= 2:return max(nums)
        @lru_cache(maxsize=None)
        def rec(start, i):
            if i >= len(nums):return 0
            if i == l - 1 and start == 0: return 0
            
            return max( nums[i] + rec(start, i+2), rec(start, i + 1))
        
        return max(rec(0, 0), rec(1, 1))