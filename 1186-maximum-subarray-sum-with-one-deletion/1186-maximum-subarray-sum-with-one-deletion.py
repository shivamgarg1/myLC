class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        max1 = arr[0]
        max2 = arr[0]
        res = arr[0]
        for num in arr[1:]:
            max1 = max( max1 + num, max2, num)
            max2 = max(max2 + num, num)
            res = max(max1, res)
        
        return res