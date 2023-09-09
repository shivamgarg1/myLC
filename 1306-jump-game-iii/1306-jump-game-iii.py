class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        l = len(arr)
        visited = [False] * l
        
        q = [start]
        while q:
            top = q.pop(0)
            if top >= l:continue
            elif top < 0: continue
            if visited[top]:continue
            visited[top] = True
            if arr[top] == 0:return True
            q.append(top + arr[top])
            q.append(top - arr[top])
        
        return False