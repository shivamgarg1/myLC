class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l = len(nums)
        nums = sorted(nums)
        res = set()
        for i in range(len(nums)-2):
            j = i + 1
            k = l-1
            target = 0 - nums[i]
            while j < k:
                if nums[j] + nums[k] == target:
                    res.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                elif nums[j] + nums[k] > target:
                    k -= 1
                elif nums[j] + nums[k] < target:
                    j += 1
        
        return res