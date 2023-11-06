class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = set()
        l = len(candidates)
        def dfs(i, array, rs):
            if rs == target:
                res.add(tuple(array))
                return
            elif rs > target or i >= l:return
            
            for j in range(i, l):
                dfs(j, array + [candidates[j]], rs + candidates[j])
            return
        
        dfs(0, [], 0)
        return res