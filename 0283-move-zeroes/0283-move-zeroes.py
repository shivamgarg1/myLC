class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        
        zindex = -1
        for i, num in enumerate(nums):
            if num == 0 and zindex == -1 :
                zindex = i
            elif num != 0 and zindex != -1:
                nums[i], nums[zindex] = nums[zindex], nums[i]
                zindex += 1
        