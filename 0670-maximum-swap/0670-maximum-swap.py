class Solution:
    def maximumSwap(self, num: int) -> int:
        
        '''
        num = 2736
        stack = [2]
                [2, ]
        
        
        '''
        nums = [ i for i in str(num)]
        max_digit = nums[-1]
        max_idx = len(nums) - 1
        l = r = -1
        for i in range(len(nums)-1, -1, -1):
            if nums[i] > max_digit:
                max_digit = nums[i]
                max_idx = i
            elif nums[i] < max_digit:
                l = i
                r = max_idx
        
        if l == -1:return num
        nums[l], nums[r] = nums[r], nums[l]
        return int(''.join(nums))