class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x:x[0])
        pq = [intervals[0][1]]
        l = 1
        count = 1
        for start, end in intervals[1:]:
            if start < pq[0]:
                heappush(pq, end)
                l += 1
                count = max(count, l)
            else:
                while pq and pq[0] <= start:
                    heappop(pq)
                    l -= 1
                heappush(pq, end)
                l += 1
        return count