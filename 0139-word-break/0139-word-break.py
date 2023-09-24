class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        '''
        
        leetcode -> leet code
        
        algo:
        1) use re
        
        '''
        
        l = len(s)
        
        @lru_cache(maxsize=None)
        def dfs(i, rs):
            if i == l:
                if rs == s:return True
                return False
            
            for word in wordDict:
                lword = len(word)
                if lword > l - i: continue
                elif word != s[i : i+lword]:continue
                elif dfs(i+lword, rs + word):return True
            
            return False
        
        return dfs(0, '')
        