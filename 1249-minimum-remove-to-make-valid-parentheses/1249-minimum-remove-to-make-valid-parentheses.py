class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        '''
        )(
        opens/ closes
        (()
        ())
        
        '''
        
        opens = 0
        res = ''
        for char in s:
            if char == '(':
                opens += 1
                res += char
            elif char == ')' and opens > 0:
                opens -=1 
                res += char
            elif char == ')' and opens == 0:
                continue
            else:
                res += char
        ans = ''
        
        if opens > 0:
            l = len(res)
            i = l - 1
            closes = 0
            while i >= 0:
                if res[i] == ')':
                    closes += 1
                    ans += res[i]
                elif res[i] == '(' and closes > 0:
                    closes -= 1
                    ans += res[i]
                elif res[i] == '(' and closes == 0:
                    i -= 1
                    continue
                else:
                    ans += res[i]
                i -= 1 
            
            return ans[::-1]
        else: return res