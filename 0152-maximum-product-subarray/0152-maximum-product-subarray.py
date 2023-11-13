class Solution:
    def maxProduct(self, A: List[int]) -> int:
        '''
        
        [-3, 0, 1, -2]
        -3, 0, 0, -2
        -2, 
        
        '''
        
        B = A[::-1]
        for i in range(1, len(A)):
            A[i] *= A[i - 1] or 1
            B[i] *= B[i - 1] or 1
        return max(A + B)