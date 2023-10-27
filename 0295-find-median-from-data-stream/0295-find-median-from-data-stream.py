class MedianFinder:

    def __init__(self):
        self.min_h = []
        self.max_h = []
        self.l = 0
        

    def addNum(self, num: int) -> None:
        self.l += 1
        heappush(self.max_h, -num)
        heappush(self.min_h, -heappop(self.max_h))
        if len(self.min_h) > len(self.max_h):
            heappush(self.max_h, -heappop(self.min_h))
        

    def findMedian(self) -> float:
        if self.l % 2 == 0:
            first = self.min_h[0]
            second = -self.max_h[0]
            return ( first + second ) / 2
        return -self.max_h[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()