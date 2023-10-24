class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        
        def transpose(mat):
            n = len(mat)
            for i in range(n):
                for j in range(i + 1, n):
                    mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
        
        def reflect(mat):
            n = len(mat)
            for i in range(n):
                for j in range(n // 2):
                    mat[i][j], mat[i][n-j-1] = mat[i][n-j-1], mat[i][j]
        
        transpose(matrix)
        reflect(matrix)