class Solution:
    def simplifyPath(self, path: str) -> str:
        '''
        
        ./home/
        
        /.home./
        /home.
        
        /home/ <-> /HomE/
        
        
        
        /home/
        /./
        /../
        /...home/
        /.home/
        /.home.../
        /home//path/
        
        algo:
            1) split the string on '/'
            2) iterate on tmp array 
                3) if only 1'.' at start of word, ignore
                4) if 2 '.' only, then pop last elmeent from result stack
            5) join the result stack with '/'
        
        '''
        
        
        tmp = path.split('/')
        stack = []
        for word in tmp:
            tmp_word = ''
            if not word:continue
            if word.startswith('.') and len(word) == 2 and word[1] == '.':
                if stack:
                    stack.pop(-1)
            elif word.startswith('.') and len(word) == 1:
                tmp_word = word[1:]
                if tmp_word:
                    stack.append(tmp_word)
            else:
                stack.append(word)
        
        res = '/'.join(stack)
        if not res:
            res = '/' + res
        elif res and res[0] != '/':
            res = '/' + res
        return res
        
                