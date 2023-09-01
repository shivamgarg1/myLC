class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:return 0
        left = count = 0
        running_prod = 1
        for right, num in enumerate(nums):
            running_prod *= num
            while running_prod >= k:
                running_prod /= nums[left]
                left += 1

            count += right - left + 1
        
        return count