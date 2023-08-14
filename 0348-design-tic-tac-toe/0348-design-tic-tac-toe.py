class TicTacToe:

    '''
    
    algo:
    1) create n x n 2d array and initialize all values with -1, indicating empty spaces
    2) keep a counter for moves by each player
    3) define a fun check_result only at and after N moves
    4) check_result will check horizontal, vertical and diagonals for each player and return appropriate integer
    
    -1 1
    1 2
    '''
    
    
    def __init__(self, n: int):
        
        self.rows = [0] * n
        self.cols = [0] * n
        self.n = n
        self.dia = 0
        self.antidia = 0
        
    def move(self, row: int, col: int, player: int) -> int:
        
        delta = 1 if player == 1 else -1
        self.rows[row] += delta
        self.cols[col] += delta
        if row == col:
            self.dia += delta
        if col == self.n - row - 1:
            self.antidia += delta
        if abs(self.rows[row]) == self.n or abs(self.cols[col]) == self.n or abs(self.dia) == self.n or abs(self.antidia) == self.n:
            return player
        return 0
        