class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        l = len(coins)
        @lru_cache(maxsize=None)
        def rec(i, rs):
            if i == l:
                if rs > amount:return -1
                elif rs == amount:return 0
            elif rs > amount:return -1
            elif rs == amount: return 0
            
            tmp = sys.maxsize
            for j in range(i, l):
                if coins[j] + rs <= amount:
                    count = rec(j, rs + coins[j])
                    if count != -1:
                        tmp = min(tmp, count + 1)
            
            return tmp if tmp != sys.maxsize else -1
        
        return rec(0, 0)