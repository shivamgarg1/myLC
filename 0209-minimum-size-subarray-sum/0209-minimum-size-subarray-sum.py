class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        '''
        0   1  2  3  4  5
        [2, 3, 1, 2, 4, 3]
        2   5  6  8  10
        first, last = 0
        rs = 0
        1) iterate on nums
        2) if rs >= taget, move first pointer to the right and subtract its value from rs
        3) at every step store min of last - first + 1
        
            2, 5, 2, first = 0, last = 1
        
        
        '''
        
        first = 0
        last = 0
        rs = 0
        res = sys.maxsize
        
        for i, num in enumerate(nums):
            rs += num
            last = i
            
            while rs >= target:
                res = min(res, last - first + 1)
                rs -= nums[first]
                first += 1
                
        
        return res if res != sys.maxsize else 0