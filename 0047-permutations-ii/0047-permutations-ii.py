class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        
        res = set()
        l = len(nums)
        def permute(nums, i):
            if i == l:
                res.add(tuple(nums))
                return
            for j in range(i, l):
                nums[i], nums[j] = nums[j], nums[i]
                permute(nums, i + 1)
                nums[i], nums[j] = nums[j], nums[i]
        
        permute(nums, 0)
        return list(res)