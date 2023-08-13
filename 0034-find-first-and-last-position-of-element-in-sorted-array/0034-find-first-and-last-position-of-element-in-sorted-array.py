class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        '''
        
        1) use binary search
        2) 
        
        
        '''
        
        l = 0
        r = len(nums)
        while l < r:
            mid = l + ( r - l ) // 2
            if nums[mid] >= target:
                r = mid
            else:
                l = mid + 1
        
        if l == len(nums) or target != nums[l]: return [-1, -1]
        
        low = l 
        
        l = 0
        r = len(nums)
        while l < r:
            mid = l + ( r - l ) // 2
            if nums[mid] <= target:
                l= mid + 1
            else:
                r = mid
        
        if l == len(nums) or target != nums[l]:
            l -= 1
        return [low, l]
        
        