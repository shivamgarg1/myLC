class Solution:
    def rob(self, nums: List[int]) -> int:
        l = len(nums)
        
        @lru_cache(maxsize=None)
        def rec(i) :
            if i < 0 :return 0
            
            return max(nums[i] + rec(i-2), rec(i-1))
    
        return rec(l-1)