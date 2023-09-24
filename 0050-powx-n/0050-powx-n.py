class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        @lru_cache(maxsize=None)
        def rec(i):
            if i == 0:return 1
            elif i == 1:return x
            
            if i % 2 == 0:
                return rec(i // 2) * rec( i // 2)
            elif i % 2 == 1:
                return x * rec(i-1)
        
        
        res = rec(abs(n))
        return res if n >= 0 else 1 / res