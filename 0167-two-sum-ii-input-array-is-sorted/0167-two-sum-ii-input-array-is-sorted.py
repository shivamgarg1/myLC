class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        '''
        
        [1, 4, 6, 10, 10] target = 10
        ^              ^
        
        
        '''
        
    
        l = 0
        r = len(numbers) - 1
        
        
        while l < r:
            curr_sum = numbers[l] + numbers[r]
            if curr_sum == target:
                return [l+1, r+1]
            elif curr_sum < target:
                start = numbers[l]
                l += 1
                while l < r and numbers[l] == start:
                    l += 1
            elif curr_sum > target:
                start = numbers[r]
                r -= 1
                while l < r and numbers[r] == start:
                    r -= 1
        
        return []
            