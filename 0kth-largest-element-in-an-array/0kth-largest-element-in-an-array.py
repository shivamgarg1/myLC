class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''
        
        min heap to store smallest k elements
        
        
        1, 2, 3, 4, 5 k=3
        
        3, 4, 5
        
        O(K) + (N-k )Log k ~ NLogk
        
        '''
        h = []
        for num in nums:
            heappush(h, num)
            if len(h) > k:
                heappop(h)
        return h[0]