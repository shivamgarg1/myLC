class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        left = 0
        right = len(nums) - 1
        res = -1
        while left < right:
            s = nums[left] + nums[right]
            if s < k: 
                res = max(res, s)
                left += 1
            elif s >= k: 
                right = right - 1
        
        return res