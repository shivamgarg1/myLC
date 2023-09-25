class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        m = { 0 : -1}
        s = 0
        
        for i, num in enumerate(nums):
            s = ( s + num) % k
            if s in m and i - m[s] >  1:return True
            if s not in m:
                m[s] = i
        return False