class Solution:
    def reorganizeString(self, s: str) -> str:
        m = defaultdict(int)
        for char in s:
            m[char] += 1
        
        pq = []
        for k in m:
            pq.append((-m[k], k))
        heapq.heapify(pq)
        res = ''
        while pq:
            count, char = heappop(pq)
            if res and res[-1] == char:
                if pq:
                    next_count, next_char = heappop(pq)
                    res += next_char
                    if next_count+1 != 0:
                        heappush(pq,(next_count+1, next_char))
                else:
                    return ''
            
            res += char
            if count+1 != 0:
                heappush(pq,(count+1, char))
        print(res)
        if len(res) != len(s): return ''
        return res
                
                