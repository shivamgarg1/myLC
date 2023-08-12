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
        i = l -1
        while i > 0:
            if nums[i-1] < nums[i]:
                # find the first element larger than i-1 element and swap
                diff = sys.maxsize
                diff_index = l
                for j in range(i, l):
                    if nums[j] > nums[i-1] and nums[j] - nums[i-1] < diff:
                        diff = nums[j] - nums[i-1]
                        diff_index = j
                
                
                nums[i-1], nums[diff_index] = nums[diff_index], nums[i-1]
                
                tmp = sorted(nums[i:])
                
                
                k = 0
                while k < len(tmp):
                    nums[i+k] = tmp[k]
                    k += 1
                
                return 
            i -= 1
            
        nums.sort()
            
        
                
            