class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        l = len(coins)
        @lru_cache(maxsize=None)
        def rec(rs):
            if rs > amount:return -1
            elif rs == amount:return 0
            
            tmp = sys.maxsize
            for coin in coins:
                if coin + rs <= amount:
                    count = rec(rs + coin)
                    if count != -1:
                        tmp = min(tmp, count + 1)
            
            return tmp if tmp != sys.maxsize else -1
        
        return rec(0)