class Solution:
    def maxLength(self, arr: List[str]) -> int:
        self.max_l = 0
        l = len(arr)
        def dfs(running_char, i):
            running_char_l = len(running_char)
            if running_char and running_char_l == len(set(running_char)):
                self.max_l = max(self.max_l, running_char_l)
            elif running_char:return
            if i == l:return
            for j in range(i, l):
                dfs(running_char + arr[j], j+1)
            
            return
        
        dfs('', 0)
        return self.max_l
            