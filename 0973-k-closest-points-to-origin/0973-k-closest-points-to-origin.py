class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq = []
        for x, y in points:
            pq.append((x * x + y * y, x, y))
        heapq.heapify(pq)
        res = []
        while k > 0:
            _, x, y = heappop(pq)
            res.append([x,y])
            k -= 1
        return res