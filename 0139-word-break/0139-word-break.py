class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        '''
        
        leetcode -> leet code
        
        algo:
        1) use re
        
        '''
        words = set(wordDict)
        q = [0]
        seen = set()
        
        while q:
            start = q.pop(0)
            if start == len(s): return True
            for end in range(start + 1, len(s) + 1):
                if end in seen:continue
                if s[start:end] in words:
                    seen.add(end)
                    q.append(end)
        
        return False
        
        