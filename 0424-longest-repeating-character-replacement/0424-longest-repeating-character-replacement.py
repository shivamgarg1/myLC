class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        
        A A B B A
        
        A B C A
        
        
        
        
        '''
        
        m = defaultdict(int)
        left = 0
        max_freq = 0
        res = 0
        for i in range(len(s)):
            m[s[i]] += 1
            max_freq = max(max_freq, m[s[i]])
            
            flag = False
            if i - left + 1 - max_freq <= k:
                flag = True
            if not flag:
                m[s[left]] -= 1
                left += 1
            
            res = i - left + 1
        return res
        
        