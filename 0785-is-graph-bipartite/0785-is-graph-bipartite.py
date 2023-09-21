class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        
        '''
        
              0(T)
             / \
            1(F)---2(F)
        
        '''
        
        def check(i):
            q = [i]
            while q:
                node = q.pop(0)
                p_color = visited[node]
                for nei in graph[node]:
                    if visited[nei] == -1:
                        visited[nei] = not p_color
                    else:
                        if visited[nei] == p_color:return False
                        continue
                    q.append(nei)
            
            return True
        
        l = len(graph)
        visited = [-1] * l
        for i in range(l):
            if visited[i] == -1:
                visited[i] = True
                if not check(i):return False
        return True