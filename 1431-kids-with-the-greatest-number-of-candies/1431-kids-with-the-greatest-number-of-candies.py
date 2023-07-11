class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candy = max(candies)
        res = [False] * len(candies)
        for i, num in enumerate(candies):
            if num + extraCandies >= max_candy:
                res[i] = True
        
        return res