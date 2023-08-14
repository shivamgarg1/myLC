class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nzi = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[nzi] = nums[i]
                nzi += 1
        for i in range(nzi, len(nums)):
            nums[i] = 0