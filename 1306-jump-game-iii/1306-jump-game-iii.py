class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        l = len(arr)
        visited = [False] * l
        
        def dfs(i):
            if  i >= l:return False
            elif i < 0:return False
            elif visited[i]:return False
            if arr[i] == 0:return True
            visited[i] = True
            if dfs(i + arr[i]):return True
            elif dfs(i - arr[i]):return True
            return False
        
        return dfs(start)