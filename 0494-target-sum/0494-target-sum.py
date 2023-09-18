class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        '''
        
        
        brute force way:    
        1) use bit masking approach
        2) use backtracking
        
        '''
        
        l = len(nums)
        @lru_cache(maxsize=None)
        def rec(i, rs):
            if i == l:
                if rs == target:return 1
                else:return 0
            
            return rec(i+1, rs + nums[i]) + rec(i+1, rs - nums[i])
        
        return rec(0, 0)