class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        '''
        algo:
        1) use dfs approach
        2) initialize running_str variable which consists of '' 
        3) check if running_Str is present in wordDict
        4) 
        
        '''
        
        l = len(s)
        ans = []
        def dfs(running_str, i):
            if i == l:
                ans.append(running_str[1:])
                return
            
            for j in range(len(wordDict)):
                word_l = len(wordDict[j])
                if wordDict[j] == s[i:i+word_l]:
                    dfs(running_str + ' ' + wordDict[j], i+word_l)
            
            return
        
        dfs('', 0)
        return ans