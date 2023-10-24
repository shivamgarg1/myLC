class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        m = {0: -1}
        count = 0
        max_l = 0
        for i, num in enumerate(nums):
            count = count + 1 if num == 1 else count - 1
            if count in m:
                max_l = max(max_l, i - m[count])
            else:
                m[count] = i
        
        return max_l