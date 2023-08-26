class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        alist = defaultdict(list)
        for i, j in enumerate(equations):
            a, b = j
            alist[a].append((b, values[i]))
            alist[b].append((a, 1 / values[i]))
        
        
        res = []
        def dfs(start, end, stack):
            if start in stack:return -1
            if start == end:return -2
            stack.add(start)
            
            
            tmp = 1
            for nei, ratio in alist[start]:
                tmp = dfs(nei, end, stack)
                if tmp == -2:
                    return ratio
                elif tmp != -1:
                    return ratio * tmp
            
            stack.remove(start)
            return tmp
        
        for a, b in queries:
            if a not in alist or b not in alist:res.append(-1)
            elif a == b:res.append(1)
            else:res.append(dfs(a, b, set()))

        return res