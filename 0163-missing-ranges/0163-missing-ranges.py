class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        
        '''
        
        [0, 1, 3, 50, 75]
        [0, 99]
        
        [3] => [0, 2], [4, 99]
        last = 0
        if curr_num != last:
            missing_range = [last, curr_num - 1]
            res.append(missing_range)
        last = curr_num + 1
            
        When the while/ for loop finishes check for last number, if less than upper, then
        res.append([last, upper])
        
        Time: O(n)
        Space: 0(N), if output is considered as space otherwise O(1)
        
        [0, 0]
        
        algo:
        1) last
        
        
        
        '''
        
        if not nums:return [[lower, upper]]
        last = lower
        ans = []
        for num in nums:
            if last != num:
                ans.append([last, num-1])
            last = num + 1
        
        if last <= upper:
            ans.append([last, upper])
        return ans
        
        