class Solution:
    def calculate(self, s: str) -> int:
        '''
        1. 2*3 / 2
        2. 2 / 0
        3. ""
        4. 23 / 5
        
        algo:
        1. iterate on s:
        2. use stack ds
        3. collect all numerics in seq
        4. if + or - sign then use with the numeric
            else, ( * or / sign), then do the operatio
        
        
        
        num = '23 + 32 * 10'
        stack = [23]
                [23, +]
                [23, +, 32]
                [23, +, 32, *]
                [23, +, 32, *] num = 10, 10 * 32
                [23, + 320]
        when iteration is over add all the items of the stack. Subtraction will be taken care iteself.
        
        '''
        
        stack = []
        ops = set(['+', '-', '*', '/'])
        i = 0
        curr_op = ''
        num = ''
        while i < len(s):
            if s[i] == ' ':
                i += 1
                continue
            elif s[i] in ops:
                curr_op = s[i]
            else:
                while i < len(s) and s[i].isnumeric():
                    num += s[i]
                    i += 1
                i -= 1
                if curr_op == '*':
                    top = stack.pop(-1)
                    stack.append(str(int(top) * int(num)))
                elif curr_op == '/':
                    top = stack.pop(-1)
                    stack.append(str(int(int(top) / int(num))))
                else:
                    stack.append(curr_op + num)
                num = ''
                curr_op = ''
            i += 1
        res = 0
        i = 0 
        while i < len(stack):
            res += int(stack[i])
            i += 1
        return res