class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''
        h = [-num for num in nums]
        heapq.heapify(h)
        i = 0
        res = 0
        while i != k:
            res = heappop(h)
            i += 1
        return -res
        '''
        pq = []
        l = 0
        for num in nums:
            heappush(pq, num)
            l += 1
            if l > k:
                heappop(pq)
            
        
        return pq[0]
            
        
        