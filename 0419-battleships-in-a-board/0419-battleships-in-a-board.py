class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        seen = set()
        R = len(board)
        C = len(board[0])
        
        
        def dfs(r, c):
            for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                new_r = r + dr
                new_c = c + dc
                if 0 <= new_r < R and 0 <= new_c < C :
                    if board[new_r][new_c] == 'X' and (new_r, new_c) not in seen:
                        seen.add((new_r, new_c))
                        dfs(new_r, new_c)
                        
        count = 0
        for r in range(R):
            for c in range(C):
                if board[r][c] == 'X' and (r, c) not in seen:
                    count += 1
                    seen.add((r, c))
                    dfs(r, c)
        
        return count