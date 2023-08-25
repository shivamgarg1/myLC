class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        l = len(coins)
        @lru_cache(maxsize=None)
        def rec(ra):
            if ra > amount:return -1
            if ra == amount:return 0
            
            tmp = sys.maxsize
            for coin in coins:
                res = rec(ra+coin)
                if res != -1:
                    tmp = min(tmp, res+1)
            
            return tmp if tmp != sys.maxsize else -1
        
        return rec(0)
            
        