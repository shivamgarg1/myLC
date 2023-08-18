class Solution:
    def wordBreak(self, s: str, words: List[str]) -> List[str]:
        '''
        algo:
        1) use dfs approach
        2) initialize running_str variable which consists of '' 
        3) check if running_Str is present in wordDict
        4) 
        
        '''
        
        l = len(s)
        memo = {}
        @lru_cache(maxsize=None)
        def dfs(i):
            if i in memo:return memo[i]
            res = []
            for word in words:
                if word != s[i : i + len(word)]:
                    continue
                elif len(word) == l - i:
                    res.append(word)
                else:
                    for sentence in dfs(i+len(word)):
                        res.append(word + ' ' + sentence)
            memo[i] = res
            return res
        
        return dfs(0)