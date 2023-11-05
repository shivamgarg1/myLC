class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        '''
        
        1, 2, 3, 4
        
        
        |
        | |
        | | |
        | | | |
        
        4 3 2 1
        
        
        4, 5, 4
        
        '''
        stack = []
        max_area = 0
        for i, height in enumerate([0] + heights + [0]):
            while stack and stack[-1][1] > height:
                current_height = stack.pop()[1]
                max_area = max(max_area, current_height * (i - stack[-1][0] - 1))
            stack.append((i, height))
        
        return max_area