class Solution:
    def maximumCoins(self, heroes: List[int], monsters: List[int], coins: List[int]) -> List[int]:
        
        '''
        heroes   -   [1, 4, 2]
        monsters -   [1, 1, 2, 3, 5 ]
        coins    -   [2, 3, 5, 6, 4 ]
        prefix_sum - [2, 5, 10, 16, 20]
        '''
        
        coin_l = len(coins)
        monst_coin = [(monsters[i], coins[i]) for i in range(coin_l)]
        monst_coin = sorted(monst_coin, key = lambda x:x[0])
        prefix_sum = [monst_coin[0][1]]
        for i in range(1, coin_l):
            prefix_sum.append(prefix_sum[i-1] + monst_coin[i][1])
        res = []

        def binary_search(tgt):
            l = 0 
            r = coin_l
            while l < r:
                mid = l + ( r - l ) // 2
                if monst_coin[mid][0] > tgt:
                    r = mid
                else:
                    l = mid + 1
            
            return l
        
        for hero in heroes:
            l = binary_search(hero)
            if l == 0 and monst_coin[0][0] > hero:
                res.append(0)
            else: res.append(prefix_sum[l - 1])
        return res