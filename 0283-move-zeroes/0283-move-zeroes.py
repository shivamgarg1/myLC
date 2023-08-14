class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        last_non_zero_index = 0
        curr = 0
        while curr < len(nums):
            if nums[curr] != 0:
                nums[last_non_zero_index], nums[curr] = nums[curr], nums[last_non_zero_index]
                last_non_zero_index += 1
            
            curr += 1
        