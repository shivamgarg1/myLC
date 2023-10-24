class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        '''
        
        nums = [ 0, 1, 0, 0, 1, 1, 1, 0, 1], k = 2
                 ^  ^  ^  max_num = 3, i = 1
                    ^  ^  ^  ^  ^   ^  max_num = 6, i = 2
                          1  2  3   4  5  6
        
        
        Time = O(N^2)
        Space = O(1)
        
        '''
        
        z_idx = []
        max_l = 0
        running_l = 0
        for i, num in enumerate(nums):
            if num == 1:
                running_l += 1
            elif k > 0:
                k -= 1
                z_idx.append(i)
                running_l += 1
            elif k == 0:
                max_l = max(running_l, max_l)
                if z_idx:
                    running_l = i - z_idx.pop(0)
                    z_idx.append(i)
                else:running_l = 0
                
    
        return max(max_l, running_l)