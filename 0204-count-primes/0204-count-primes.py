class Solution:
    def countPrimes(self, n: int) -> int:
        if n == 0 or n == 1:return 0
        primes = [True] * n
        primes[0] = False
        primes[1] = False
        for i in range(2, int(sqrt(n)) + 1):
            if primes[i]:
                for multiple in range(2*i, n, i):
                    primes[multiple] = False
        return sum(primes)