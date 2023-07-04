class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        
        parent = [-1] * 26
        
        def find(x):
            if parent[x] < 0: return x
            return find(parent[x])
        
        
        def union(x, y):
            x = find(x)
            y = find(y)
            
            if x == y : return
            
            if x < y:
                parent[y] = x
            else:
                parent[x] = y

        for i in range(len(s1)):
            union(ord(s1[i]) - ord('a'), ord(s2[i]) - ord('a'))

        res = ''

        for char in baseStr:
            res += chr(find(ord(char) - ord('a')) + ord('a'))

        return res