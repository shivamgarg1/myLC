class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        '''
        
        [0, 1, 2, 2, 3, 0 , 4, 2], val = 2
               ^  ^            ^
        
        '''
        
        nptr = -1
        ptr = 0
        while ptr < len(nums):
            if nptr == -1 and nums[ptr] != val:
                ptr += 1
            elif nums[ptr] == val:
                if nptr == -1:
                    nptr = ptr
                ptr += 1
            elif nums[ptr] != val and nptr != -1:
                nums[ptr], nums[nptr] = nums[nptr], nums[ptr]
                ptr += 1
                nptr += 1
            
        
        return nptr if nptr != -1 else len(nums)