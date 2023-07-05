class Solution:
    def removeOuterParentheses(self, s: str) -> str: 
        ls = []
        opens = 0
        for i, char in enumerate(s):
            if char == '(':
                if opens == 0:
                    start_index = i
                    ls.append(i)
                opens += 1
            else:
                opens -= 1
            if opens == 0:
                ls.append(i)
        
        res = ''
        for i, char in enumerate(s):
            if ls and i == ls[0]:
                ls.pop(0)
            else:
                res += char
        
        return res
                