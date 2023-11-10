class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        '''
        
        algo:
        0) initialize an empty set which will store char digits from 0-9
        1) iterate each row, and check if valid
        2) iterate each col and check if valid
        3) iterate each box and check if valid
        
        '''
        
        # check rows
        for r in range(9):
            m = set()
            for c in range(9):
                if board[r][c] == '.': continue
                if board[r][c] in m:
                    #print("1here:", r, c)
                    return False
                m.add(board[r][c])
        
        
        # check cols
        for c in range(9):
            m = set()
            for r in range(9):
                if board[r][c] == '.': continue
                if board[r][c] in m:
                    #print("2here:", r, c)
                    return False
                m.add(board[r][c])
                
        # check boxes
        
        
        def check(r_offset, c_offset):
            m = set()
            for r in range(r_offset, r_offset + 3):
                for c in range(c_offset, c_offset + 3):
                    if board[r][c] == '.': continue
                    if board[r][c] in m:
                        #print("3here:", r, c)
                        return False
                    m.add(board[r][c])
            return True
        
        
        for r in [0, 3, 6]:
            for c in [0, 3, 6]:
                if not check(r, c):
                    return False
        
        return True