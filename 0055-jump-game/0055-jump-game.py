class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        l = len(nums)
        
        @lru_cache(maxsize=None)
        def rec(i):
            if i == l-1:return True
            if nums[i] == 0: return False
            
            for val in range(1, nums[i] + 1):
                if rec(i + val):return True
            return False
        
        return rec(0)