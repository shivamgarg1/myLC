class Solution:
    def countAndSay(self, n: int) -> str:
        
        def rec(n):
            if n == 1:
                return '1'
            
            s = rec(n-1)
            count = 1
            i = 1
            new_s = ''
            while i < len(s):
                if s[i-1] == s[i]:
                    count += 1
                else:
                    new_s += str(count)
                    new_s += s[i-1]
                    count = 1
                i += 1
            
            new_s += str(count)
            new_s += s[-1]
            
            return new_s
            
        
        return rec(n)
            
            
            