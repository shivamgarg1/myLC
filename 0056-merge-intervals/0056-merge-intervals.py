class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x:x[0])
        res = [intervals[0]]
        last = res[-1][1]
        for start, end in intervals[1:]:
            if start <= last:
                last = max(res[-1][1], end)
                res[-1][1] = last
            else:
                res.append([start, end])
                last = end
    
        return res
                
            