class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        '''
        
        [4,3,-2,-7,8,2,3,1]
         1 2 3 4 5 6 7 8
        
        
        
        [3, 1, 3] => [3, 1, -3] => [-3, 1, -3]
        
        
        '''
        
        i = 0
        while i < len(nums):
            idx = abs(nums[i]) - 1
            if nums[idx] > 0:
                nums[idx] *= -1
            i += 1
        
        res = [i + 1 for i in range(len(nums)) if nums[i] > 0]
        return res