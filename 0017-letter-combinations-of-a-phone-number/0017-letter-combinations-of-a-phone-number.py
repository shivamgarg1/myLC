class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:return []
        m = {
            '2' : 'abc',
            '3' : 'def',
            '4' : 'ghi',
            '5' : 'jkl',
            '6' : 'mno',
            '7' : 'pqrs',
            '8' : 'tuv',
            '9' : 'wxyz'
        }
        
        
        l = len(digits)
        
        self.res = []
        
        def rec(running_str, i):
            if i == l:
                self.res.append(running_str)
                return
            
            for char in m[digits[i]]:
                running_str += char
                rec(running_str, i+1)
                running_str = running_str[:-1]
            
            return
        
        rec('', 0)
        return self.res