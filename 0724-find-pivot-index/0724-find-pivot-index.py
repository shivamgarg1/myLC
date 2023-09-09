class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        s = sum(nums) - nums[0]
        lsum = 0
        if s == lsum:return 0
        for i in range(1, len(nums)):
            lsum += nums[i-1]
            s -= nums[i]
            if lsum == s:return i
        
        return -1