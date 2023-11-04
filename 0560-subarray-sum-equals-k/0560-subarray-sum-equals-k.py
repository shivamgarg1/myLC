class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        '''
        
        3, 4, 0, 7
        3, 7,
        
        '''
        count = 0
        
        m = {0 : 1}
        rs = 0
        for num in nums:
            rs += num
            if rs - k in m:
                count += m[rs -k]
            
            if rs in m:
                m[rs] += 1
            else:
                m[rs] = 1
        
        return count
        