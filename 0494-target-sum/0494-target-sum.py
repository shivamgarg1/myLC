class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        '''
        
        
        brute force way:    
        1) use bit masking approach
        2) use backtracking
        
        '''
        @lru_cache(maxsize=None)
        def rec(rem, i):
            if i == 0:
                if rem == 0:return 1
                else:return 0
            
            return rec(rem - nums[i-1], i - 1) + rec(rem + nums[i-1], i - 1)
        
        return rec(target, len(nums) )
                
            