class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        '''
        
        1) first going veritcal upwards
        2) horizontal rightwards
            common:
                1) move row+1, col+1
                2) if the element is not same as starting element of diagonal, return false
        return true
        '''
        
        
        R = len(matrix)
        C = len(matrix[0])
        
        
        def checkToeplitz(row, col):
            start = matrix[row][col]
            while 0 <= row < R and 0 <= col < C:
                if start != matrix[row][col]:
                    return False
                row += 1
                col += 1
            return True
        
        # start with bottom left
        for r in range(R-1, -1, -1):
            if not checkToeplitz(r, 0):return False
        
        for c in range(1, C):
            if not checkToeplitz(0, c):return False
            
        return True