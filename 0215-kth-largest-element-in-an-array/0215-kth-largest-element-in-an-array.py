class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = []
        for num in nums:
            heappush(h, -num)
        i = 0
        res = 0
        while i != k:
            res = heappop(h)
            i += 1
        return -res
        
        
        