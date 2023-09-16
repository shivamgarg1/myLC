class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        '''
        monotonically dec stack
        
        [1, 2, 3, 4, 5]
        [5, 4, 3, 2, 1]
        []
        [5, 5, 5, 5, 5]
        [1, 2, 1, 2, 1, 2]
        
        '''
        
        stack = []
        for i, num in enumerate(heights):
            while stack and heights[stack[-1]] <= num:
                stack.pop()
            stack.append(i)
        
        return stack