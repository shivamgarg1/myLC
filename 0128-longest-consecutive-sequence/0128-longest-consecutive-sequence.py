class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:return 0
        m = set(nums)
        max_count = -sys.maxsize
        count = 0
        i = 0
        while i < len(nums):
            if nums[i] in m:
                count += 1
                num = nums[i] + 1
                while num in m:
                    count += 1
                    m.remove(num)
                    num += 1
                num = nums[i] - 1
                while num in m:
                    count += 1
                    m.remove(num)
                    num -= 1
                
                m.remove(nums[i])
            
            i += 1
            max_count = max(max_count, count)
            count = 0
        
        
        return max_count
                    
                    
                    
            