class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        count = 0
        i = 0
        last = sys.maxsize
        while i < len(nums):
            if nums[i] > threshold or ( i > 0 and nums[i] % 2 == nums[i-1] % 2):
                count = max(count, i - last)
                last = sys.maxsize
            if last == sys.maxsize and nums[i] <= threshold and nums[i] % 2 == 0:
                last = i
            i += 1
        
        
        return max(count, i - last)