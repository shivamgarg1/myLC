class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        
        l = len(stickers)
        
        memo = {}
        def dfs(stickers, target, i):
            if target == '': return 0
            if i == l: return sys.maxsize
            
            if (i, target) in memo:
                return memo[(i, target)]
            
            res = dfs(stickers, target, i + 1)
            
            new_target = target
            char_removed = False
            for char in stickers[i]:
                new_target_idx = new_target.find(char)
                if new_target_idx != -1:
                    char_removed = True
                    new_target = new_target[:new_target_idx] + new_target[new_target_idx+1:]

            if char_removed:
                res = min(res, 1 + dfs(stickers, new_target, i) )
            
            memo[(i, target)] = res 
            return res
                
            
        
        ans = dfs(stickers, target, 0) 
        return ans if ans != sys.maxsize else -1
