class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        '''
        
        1) for every permutation, find if consecutive pairs are perfect squares
        
        Time: N!
        Space: O(N)
        
        '''
        
        candidates = defaultdict(list)
        
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        
        for num_k in counts:
            for next_num_k in counts:
                if sqrt(next_num_k + num_k ).is_integer():
                    candidates[num_k].append(next_num_k)
        
        self.res = 0
        l = len(nums)
        def dfs(num, i):
            if i == l: 
                self.res += 1
                return
            
            counts[num] -= 1
            for candidate in candidates[num]:
                if counts[candidate] > 0:
                    dfs(candidate, i + 1)
            counts[num] += 1
        
        for candidate in candidates:
            dfs(candidate, 1)
            #print('after:', candidate, ':', self.res)
        
        return self.res
            
                    