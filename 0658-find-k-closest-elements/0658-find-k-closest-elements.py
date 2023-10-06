class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        '''
        
        Time : k Log(N) + K Log K 
        
              _           _
        1, 2, 3, 4, 5, 6, 7
        ^           ^
        
        
        
        
        
        '''
        
        
        l = 0
        r = len(arr) - k
        while l < r:
            mid = l + ( r - l ) // 2
            if x - arr[mid] > arr[mid+k] - x: 
                l = mid + 1
            else:
                r = mid 
        
        return arr[l : l + k]