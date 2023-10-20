class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        R = len(board)
        C = len(board[0])
        
        
        self.trie = {}
        self.res = []
        for word in words:
            node = self.trie
            for char in word:
                if char not in node:
                    node[char] = {}
                node = node[char]
            node['$'] = word
        
        
        def dfs(r, c, stack, node):
            if (r, c) in stack:return False
            if board[r][c] not in node:return False
            char = board[r][c]
            if '$' in node[char]:
                self.res.append(node[char]['$'])
                node[char].pop('$')
            stack.add((r, c))
            
            for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                new_r = r + dr
                new_c = c + dc
                if 0 <= new_r < R and 0 <= new_c < C:
                    dfs(new_r, new_c, stack, node[char])
            
            stack.remove((r, c))
    
        for r in range(R):
            for c in range(C):
                dfs(r, c, set(), self.trie)
        
        return self.res
            
            