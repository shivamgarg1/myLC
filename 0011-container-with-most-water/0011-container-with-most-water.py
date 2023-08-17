class Solution:
    def maxArea(self, height: List[int]) -> int:
        '''
        
        1, 2, 3, 4, 5
        
        
        1, 2, water = 1
        1, 2, 3 -> water = 2, 2
        1, 2, 3, 4 => water = 
        
        
        
        area = 
        
        2 pointer approach
        1) start_ptr points to beginning
        2) end_ptr points to last element
        3) for every pointer, check area covered
            4) Take greedy approach by moving pointer which is smaller in magnitude
        5) do above until stat > end
        6) return max area
        
        '''
        
        max_area = -sys.maxsize
        start = 0
        end = len(height) - 1
        while start < end:
            area = ( end - start ) * min(height[start], height[end])
            max_area = max(max_area, area)
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
        
        return max_area