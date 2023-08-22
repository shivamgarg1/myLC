class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''
        k = -1
        [1, 1, 2, 2, 2, 3]
        0   1  2  3  4  5
        0 ^ 1 => 0, so if k < 0, then k = 1, i++
        1 ^ 2 => !0, so swap curr elmenent with k
        .
        .
        .
        
        if k < 0: return len(nums)
        else: return len(nums) - k
        
        
        algo:
        1) xor curr and prev elements, 
            2) if 0, then same and set this index to be where next uniq number needs to be put
            3) else, increment regular counter. 
        
        
        
        [1, 1, 2, 3, 4]
        [1, 2, 3, 4, .]
        
        '''
        k = 1
        i = 1
        while i < len(nums):
            if nums[i-1] != nums[i]:
                nums[k] = nums[i]
                k += 1
            i += 1
        return k