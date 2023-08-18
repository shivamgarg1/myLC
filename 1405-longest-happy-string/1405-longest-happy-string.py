class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        
        h = []
        if a: h.append((-a, 'a'))
        if b: h.append((-b, 'b'))
        if c: h.append((-c, 'c'))
        
        heapq.heapify(h)
        res = ''
        while h :
            count, char = heappop(h)
            if len(res) >= 2 and res[-1] == char and res[-2] == char:
                if h:
                    next_count, next_char = heappop(h)
                    res += next_char
                    if next_count + 1 != 0:
                        heappush(h, (next_count+1, next_char))
                else:return res
            res += char
            if count+1:
                heappush(h, (count+1, char))
        
        return res