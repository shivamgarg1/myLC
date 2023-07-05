class Solution:
    def removeOuterParentheses(self, s: str) -> str: 
        ls = []
        opens = 0
        for char in s:
            if char == '(':
                if opens != 0:
                    ls.append(char)
                opens += 1
            else:
                opens -= 1
                if opens != 0:
                    ls.append(char)
        
        return "".join(ls)