class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        '''
        
        ip = [10, 6, 8, 5, 11, 9]
                               ^
        1) initialize array of l of inputs
        2) iterate from back
            i) if no item in stack, append, set ans index to 0
            ii) if item is less or equal than top elem of stack, append elem, appen 1 to ans index
            iii) if item is more than top elem of stack, pop until larger is found, append num pop + 1
        
        '''
        
        
        stack = []
        l = len(heights)
        ans = [0] * l
        i = l - 1
        while i >= 0:
            if not stack:
                stack.append(heights[i])
                ans[i] = 0
            elif heights[i] <= stack[-1]:
                stack.append(heights[i])
                ans[i] = 1
            else:
                pop_count = 0
                while stack and heights[i] > stack[-1]:
                    pop_count += 1
                    stack.pop(-1)
                if stack:
                    pop_count += 1
                ans[i] = pop_count
                stack.append(heights[i])

            i -= 1
        
        return ans
        
