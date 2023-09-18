class Solution:
    def wordBreak(self, s: str, words: List[str]) -> List[str]:
        '''
        algo:
        1) use dfs approach
        2) initialize running_str variable which consists of '' 
        3) check if running_Str is present in wordDict
        4) 
        
        '''
        
        res = []
        l = len(s)
        
        def rec(i, rs):
            if i == l:
                res.append(rs[1:])
                return
            
            for word in words:
                word_len = len(word)
                if word_len > l - i : continue
                elif word == s[i : i + word_len]:
                    rec(i+word_len, rs + ' ' + word)
            return
        
        rec(0, '')
        return res
        