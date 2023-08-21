class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        m = defaultdict(int)
        for word in words:
            m[word] += 1
        pq = []
        for key in m:
            pq.append((-m[key], key))
        heapq.heapify(pq)
        res = []
        while k > 0:
            res.append(heappop(pq)[1])
            k -= 1
        return res