class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        nums1 = [1] * l
        nums2 = [1] * l
        
        for i in range(1, l):
            nums1[i] = nums1[i-1] * nums[i-1]
        
        j = l - 2
        while j >=0:
            nums2[j] = nums2[j+1] * nums[j+1]
            j -= 1
        
        ans = [1] * l
        for i in range(l):
            ans[i] = nums1[i] * nums2[i]
        
        return ans