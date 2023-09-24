class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        @lru_cache(maxsize=None)
        def rec(i):
            if i == 0:return 1
            elif i == 1:return x
            half = rec(i // 2)
            if i % 2 == 0:
                return half * half
            elif i % 2 == 1:
                return x * half * half
        
        
        res = rec(abs(n))
        return res if n >= 0 else 1 / res