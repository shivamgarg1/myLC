class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        '''
        
        [4, 3, 2, 1] -> 0, 1, 2, 3
        [1, 2, 3, 4] -> 3
        [5] -> 0
        [1, 1] -> 0
        [2, 2, 1] -> 
        
        
        Approach:
        0. Create stack ds
        1. Iterate array
            2. if empty, insert index
            2b. else, if smaller than top of stack, insert index
        3. Return the stack
        '''
        
        stack = []
        for i, num in enumerate(heights):
            if not stack:
                stack.append(i)
            else:
                while stack and heights[stack[-1]] <= num:
                    stack.pop(-1)
                stack.append(i)
        
        return stack
        
        