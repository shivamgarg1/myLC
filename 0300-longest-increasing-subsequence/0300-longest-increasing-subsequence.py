class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = []
        for num in nums:
            if not res:
                res.append(num)
            elif num > res[-1]:
                res.append(num)
            elif num < res[-1]:
                i = 0
                while num > res[i]:
                    i += 1
                
                res[i] = num
        return len(res)
        