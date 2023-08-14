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
        
        
        self.arr = [[-1] * n for i in range(n)]
        self.count = 0
        self.n = n
        
    def move(self, row: int, col: int, player: int) -> int:
        self.arr[row][col] = player
        self.count += 1
        if self.count >= 2 * self.n - 1:
            return self.check_result(player, row, col)
        return 0
    
    def check_result(self, player, row, col):
        # horizontal
        count = 0
        for i in range(self.n):
            if self.arr[row][i] == player:
                count += 1
        if count == self.n:
            return player
        
        # vertical
        count = 0
        for i in range(self.n):
            if self.arr[i][col] == player:
                count += 1
        if count == self.n:
            return player
        
        # diagonal
        count = 0
        r = c = 0
        while 0 <= r < self.n and 0 <= c < self.n:
            if self.arr[r][c] == player:
                count += 1
            r += 1
            c += 1
        if count == self.n:
            return player
        r = self.n - 1
        c = 0
        count = 0
        while 0 <= r < self.n and 0 <= c < self.n:
            if self.arr[r][c] == player:
                count += 1
            r -= 1
            c += 1
        
        if count == self.n:
            return player
        
        return 0
        
        
            
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)