class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        '''
        
        3, 2, 3
        
        1, 2, 11, 4, 5, 6
        
        '''
        if not nums:return []
        c1 = None
        c2 = None
        count1 = 0
        count2 = 0
        for num in nums:
            if c1 == num:
                count1 += 1
            elif c2 == num:
                count2 += 1
            elif count1 == 0:
                c1 = num
                count1 += 1
            elif count2 == 0:
                c2 = num
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
        
        res = []
        for c in [c1, c2]:
            if nums.count(c) > len(nums) // 3:
                res.append(c)
                
        return res
        