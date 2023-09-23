class Solution:
    def customSortString(self, order: str, s: str) -> str:
        
        m = defaultdict(int)
        for char in s:
            m[char] += 1
        
        res = ''
        for char in order:
            if char in m:
                res += char * m[char]
                m[char] = 0
        
        for char in s:
            if m[char] != 0:
                res += m[char] * char
                m[char] = 0
        return ''.join(res)