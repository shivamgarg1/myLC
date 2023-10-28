class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        m = defaultdict(list)
        for r in range(len(nums)-1, -1, -1):
            for c in range(len(nums[r])):
                m[r + c].append(nums[r][c])
        i = 0
        res = []
        while i in m:
            res.extend(m[i])
            i += 1
        
        return res