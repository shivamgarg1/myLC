class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        q = deque([(0, 0)])
        R = len(nums)
        res = []
        while q:
            r, c = q.popleft()
            res.append(nums[r][c])
            if c == 0 and r + 1 < R:
                q.append((r+1, c))
            if c + 1 < len(nums[r]):
                q.append((r, c+1))
        
        return res