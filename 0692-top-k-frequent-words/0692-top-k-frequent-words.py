
class Pair:
    def __init__(self, word, count):
        self.freq = count
        self.word = word
    
    def __lt__(self, p):
        #return self.freq < p.freq or (self.freq == p.freq and self.word > p.word)
        
        if self.freq < p.freq:return True
        elif self.freq == p.freq:
            if self.word > p.word:return True
        return False
        


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        m = defaultdict(int)
        for word in words:
            m[word] += 1
        pq = []
        
        
        
        for word, freq, in m.items():
            heappush(pq, Pair(word, freq ) )
            if len(pq) > k:
                heappop(pq)
        
        return [p.word for p in sorted(pq, reverse=True)]