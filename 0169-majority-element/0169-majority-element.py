class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        '''
        
        n = 1 -> len(nums)
        n = 2 -> len(nums)
        n = 3 -> len(nums)
        n = 4 -> 
        
        '''
        
        count = 1
        candidate = nums[0]
        for num in nums[1:]:
            if count == 0:
                candidate = num
            if num == candidate:
                count += 1
            else:
                count -= 1
        
        return candidate