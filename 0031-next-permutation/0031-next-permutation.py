class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
        
        [1, 2, 3] 
        
        
        
        
        
        [1, 3, 2]
        
        algo:
        1) l = len(nums)
        2) find index where the first dip happens
            -> 2, 3, 1, 4, 6, 5, 7 
                     ^
        3) if this is last index, return sorted nums
            else, from this index i, find next largest number and swap
        
        4) return nums
        
        
        
        
        """
        
        l = len(nums)
        i = l - 1
        while i > 0:
            if nums[i] > nums[i-1]:break
            i -= 1
        
        if i == 0:return nums.sort()
        
        tmp = sorted(nums[i:])
        idx = i - 1
        
        for num in tmp:
            nums[i] = num
            i += 1
        
        j = idx + 1
        while j < l:
            if nums[idx] < nums[j]:break
            j += 1
        nums[idx], nums[j] = nums[j], nums[idx]
        
                
            