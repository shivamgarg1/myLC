class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        '''
        
        
        algo:
        1) brute force: 
        
        
        '''
        
        
        if len(nums) == 2: return 0 if nums[0] > nums[1] else 1
        if len(nums) == 1:return 0
        
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = l + ( r - l ) // 2
            if nums[mid] > nums[mid +1]:
                r = mid
            else:
                l = mid + 1
        
        return l
        