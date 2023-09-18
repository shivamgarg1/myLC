class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        '''
        1, -2, 0, 3
        
        kleft -> [0, ]
        '''
        l = len(arr)
        kleft = [0] * l
        kleft[0] = arr[0]
        rm = arr[0]
        for i in range(1, l):
            rm = max(arr[i], rm + arr[i])
            kleft[i] = rm
        
        rm = arr[-1]
        max_sum = arr[-1]
        kright = [0] * l
        kright[-1] = arr[-1]
        for i in range(l-2, -1, -1):
            rm = max(arr[i], arr[i] + rm)
            max_sum = max( max_sum, rm)
            kright[i] = rm
        res = max_sum
        for i in range(1, l-1):
            res = max(res, kleft[i-1] + kright[i+1])
        return res