class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        h = []
        for num in arr:
            h.append((abs(x - num), num))
        heapq.heapify(h)
        res = []
        while k > 0:
            res.append(heappop(h)[1])
            k -= 1
        return sorted(res)