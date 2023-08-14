class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        m = defaultdict(int)
        for i, num in enumerate(nums):
            if num not in m:
                m[num] = i
            else:
                if abs(m[num] - i) <= k:return True
                m[num] = i
        
        return False