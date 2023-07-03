class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [-1] * ( len(edges) + 1)
        def find(x):
            if parent[x] < 0: return x
            return find(parent[x])

        def union(x, y):
            x = find(x)
            parent[find(y)] = x

        for x, y in edges:
            if find(x) != find(y):
                union(x, y)
            else:
                return [x,y]