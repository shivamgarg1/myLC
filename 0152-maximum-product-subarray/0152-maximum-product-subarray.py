class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        '''
        
        [-3, 0, 1, -2]
        -3, 0, 0, -2
        -2, 
        
        '''
        max_pr = nums[0]
        min_pr = nums[0]
        res = nums[0]
        for num in nums[1:]:
            vals = num, num * max_pr, num * min_pr
            max_pr = max(vals)
            min_pr = min(vals)
            
            res = max(res, max_pr)
    
        return res