class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        l = len(coins)
        @lru_cache(maxsize=None)
        def rec(rem):
            if rem < 0:return -1
            if rem == 0:return 0
            
            tmp = sys.maxsize
            for coin in coins:
                res = rec(rem-coin)
                if res != -1:
                    tmp = min(tmp, res+1)
            
            return tmp if tmp != sys.maxsize else -1
        
        return rec(amount)
            
        