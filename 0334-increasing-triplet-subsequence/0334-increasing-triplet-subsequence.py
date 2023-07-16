class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = sys.maxsize
        sec = sys.maxsize
        for num in nums:
            if num <= first:
                first = num
            elif num <= sec:
                sec = num
            else: return True
        return False
            