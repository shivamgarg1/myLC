class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        '''
        
        hashMap with key has sum of digits and list of values with elements having that sum
        
        
        '''
        m = defaultdict(list)
        for num in nums:
            count = sum([int(i) for i in str(num)])
            m[count].append(num)
        for k in m:
            m[k].sort()
        max_sum = -sys.maxsize
        for k in m:
            if len(m[k]) >= 2:
                max_sum = max(max_sum, m[k][-1] + m[k][-2])
            
        return max_sum if max_sum != -sys.maxsize else -1