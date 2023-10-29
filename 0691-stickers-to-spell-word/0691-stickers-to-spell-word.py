class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        stickers.sort(key = lambda x: len(x))
        sticker_counter = [Counter(sticker) for sticker in stickers]
        memo = {}
        def dfs(target):
            #if target == '' : return 0
            if target in memo: return memo[target]
            
            
            res = sys.maxsize
            
            for sticker in sticker_counter:
                if target[0] not in sticker: continue
                new_target = target
                for char in sticker:
                    new_target = new_target.replace(char, '', sticker[char])
                
                if new_target == '': 
                    res = 1
                    break
                elif new_target != target:
                    res = min(res, 1 + dfs(new_target))
                
            
            memo[target] = res
            return res
        
        ans = dfs(target)
        return -1 if ans == sys.maxsize else ans