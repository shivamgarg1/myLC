class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        l = len(coins)
    
        memo = [[-1] * (amount + 1) for i in range(len(coins))]
        def rec(i, amt):
            
            if amt == 0:
                return 1
            if i == l:return 0
            if memo[i][amt] != -1:return memo[i][amt]
            if coins[i] > amt:
                memo[i][amt] = rec(i+1, amt)
            else:
                memo[i][amt] = rec(i, amt - coins[i]) + rec(i+1, amt)
            return memo[i][amt]
        return rec(0, amount)
    