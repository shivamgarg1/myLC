class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        
        '''
        0   1  2   3
        [3, 4, 7, -7], k = 7
         3  7  14  7
        0:-1, 3:0, 7:1, 14:1,   
        ans = 4
        
        
        '''
        
        m = {0: -1}
        
        rs = 0 
        max_len = -sys.maxsize
        for i, num in enumerate(nums):
            rs += num
            if rs - k in m:
                max_len = max(max_len, i - m[rs - k])
            
            if rs not in m:
                m[rs] = i
        
        return max_len if max_len != -sys.maxsize else 0
                