class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        '''   
        abbcccb -> a
        algo:
        1) initialize a stack
        2) iterate string and keep count until elements are same
        3) if different, insert char and count
        4) when count == k, dont store anything in the satck and continue iterating
        5) else check top and remove if needed
        
        abccb
        (a, 1), (b, 1)  
         0 
         
         a b c c b d
         
         stack = [['#', 0]]
        for c in s:
            if stack[-1][0] == c:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([c, 1])
        return ''.join(c * k for c, k in stack)
        '''
        stack = [['', 0]]
        for char in s:
            if stack[-1][0] == char:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([char, 1])
        
        return ''.join([char * count for char, count in stack])