class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        '''
        counter 
        
        '''
        m = defaultdict(int)
        for char in s:
            m[char] += 1
        
        m_t = defaultdict(int)
        for char in target:
            m_t[char] += 1
        
        min_key = sys.maxsize
        for key in m_t:
            if key not in m:
                return 0
            min_key = min(min_key, m[key] // m_t[key])
            if min_key == 0:return 0
        
        return min_key
                
                    