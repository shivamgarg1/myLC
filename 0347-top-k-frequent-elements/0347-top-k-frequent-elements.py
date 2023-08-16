class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = defaultdict(int)
        for num in nums:
            m[num] += 1
        
        ls = []
        for key in m:
            ls.append((-m[key], key))
        
        heapq.heapify(ls)
        res = []
        while k > 0:
            res.append(heappop(ls)[1])
            k -= 1
        return res