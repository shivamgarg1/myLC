class Solution:
    def maximumCoins(self, heroes: List[int], monsters: List[int], coins: List[int]) -> List[int]:
        
        '''
        heroes   -   [1, 4, 2]
        monsters -   [1, 1, 2, 3, 5 ]
        coins    -   [2, 3, 5, 6, 4 ]
        prefix_sum - [2, 5, 10, 16, 20]
        '''
        
        mon_cost = sorted(list(zip(monsters, coins)))
        ps = [0]
        for _, c in mon_cost: ps.append(ps[-1] + c)

        res = []
        for h in heroes:
            l, r = 0, len(monsters) - 1
            while l <= r:
                m = (l + r) // 2
                if mon_cost[m][0] > h: r = m - 1
                else: l = m + 1
            res.append(ps[l])
        return res