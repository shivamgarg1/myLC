class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        '''
        ((
        '''
        
        opens = 0
        new_s = ''
        for char in s:
            if char == ')' and not opens:continue
            elif char == '(':
                opens += 1
            elif char == ')':
                opens -= 1
            new_s += char
        
        if opens == 0:return new_s
        
        closes = 0
        res = ''
        for i in range(len(new_s) - 1, -1, -1):
            if new_s[i] == ')':
                res += new_s[i]
                closes += 1
            elif new_s[i] == '(' and not closes: continue
            elif new_s[i] == '(':
                closes -= 1
                res += new_s[i]
            else:
                res += new_s[i]
        
        return res[::-1]
            