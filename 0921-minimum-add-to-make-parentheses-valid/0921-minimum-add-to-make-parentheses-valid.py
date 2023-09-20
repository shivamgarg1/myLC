class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        '''
        
        (
        
        '''
        
        opens = 0
        count = 0
        for char in s:
            if char == '(':
                opens += 1
            elif char == ')' and not opens:
                count += 1
            elif char == ')':
                opens -= 1
        
        return opens + count