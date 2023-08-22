class Solution:
    def candy(self, ratings: List[int]) -> int:
        '''
        
        [1, 0, 2]
        
        [5, 4, 3, 2, 1]
        1   0  -1 -2 -3
        5   4   3 2   1
        
        '''
        l = len(ratings)
        arr1 = [1] * l
        arr2 = [1] * l
        for i in range(1, l):
            if ratings[i] > ratings[i-1]:
                arr1[i] = arr1[i-1] + 1
        
        for i in range(l-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                arr2[i] = arr2[i+1] + 1
        
        count = 0
        for i in range(l):
            count += max(arr1[i], arr2[i])
        return count
        
        