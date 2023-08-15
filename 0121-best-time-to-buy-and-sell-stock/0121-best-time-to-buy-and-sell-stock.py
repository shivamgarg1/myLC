class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        
        
        2, 3, 2, 2, 3
        ^     
        
        
        '''
        low = prices[0]
        high = prices [0]
        max_profit = 0
        for price in prices:
            if price > high:
                high = price
            elif price < low:
                low = price
                high = price
            
            max_profit = max(high - low, max_profit)
        
        return max_profit