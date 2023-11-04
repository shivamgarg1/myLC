class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        '''
        [0 , 1, -1, 0, 1, 1, 3], k = 2
        
        
        [0, 2, 1, ,3 , 4 ]
        0   2   3  6
        k = 4
        
        '''
        
        d = collections.deque([[0, 0]])
        res, cur = float('inf'), 0
        for i, a in enumerate(A):
            cur += a
            while d and cur - d[0][1] >= K:
                res = min(res, i + 1 - d.popleft()[0])
            while d and cur <= d[-1][1]:
                d.pop()
            d.append([i + 1, cur])
        return res if res < float('inf') else -1