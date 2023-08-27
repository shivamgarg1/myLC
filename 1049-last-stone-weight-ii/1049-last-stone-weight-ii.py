class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        '''
        [2,7,4,1,8,1]
        
        set1 = 2, 7
        set2 = 4, 8
        '''
        
        
        l = len(stones)
        
        @lru_cache(maxsize=None)
        def rec(running_sum, i):
            if i == l:
                if running_sum < 0:return sys.maxsize
                return running_sum
            
            return min(rec(running_sum + stones[i], i + 1), rec(running_sum - stones[i], i + 1))
        
        res = rec(0, 0)
        return res if res != sys.maxsize else 0