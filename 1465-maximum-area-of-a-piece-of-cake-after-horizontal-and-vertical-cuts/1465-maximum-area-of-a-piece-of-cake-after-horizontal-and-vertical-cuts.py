class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts = [0] + horizontalCuts + [h]
        verticalCuts = [0] + verticalCuts + [w]
        horizontalCuts.sort()
        verticalCuts.sort()
        
        d_h = [-horizontalCuts[i] + horizontalCuts[i-1] for i in range(1, len(horizontalCuts))]
        d_v = [-verticalCuts[i] + verticalCuts[i-1] for i in range(1, len(verticalCuts))]
        heapq.heapify(d_h)
        heapq.heapify(d_v)
        return (d_h[0] * d_v[0]) % (10**9 + 7)
    