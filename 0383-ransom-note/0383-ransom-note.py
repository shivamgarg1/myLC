class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        '''
        
        ransomnote magazine
        "a,b,c"    "a, b"
        
        
        '''
        
        
        m = defaultdict(int)
        for char in magazine:
            m[char] += 1
        for char in ransomNote:
            if char not in m:return False
            elif not m[char] : return False
            m[char] -= 1
        return True