class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        for num in range(2**n, 2**(n+1)):
            num = str(bin(num)[3:])
            tmp = []
            for i in range(n):
                if num[i] == '1':
                    tmp.append(nums[i])
            res.append(tmp)
            
            
        
        return res