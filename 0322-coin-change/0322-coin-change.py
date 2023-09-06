class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        @lru_cache(maxsize=None)
        def rec(amt):
            if amt == 0:return 0
            min_count = sys.maxsize
            for coin in coins:
                if amt >= coin:
                    count = rec(amt - coin)
                    min_count = min(min_count, count)
            
            return min_count + 1
        
        count = rec(amount)
        if count >= sys.maxsize:return -1
        return count
            
        