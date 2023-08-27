class Solution:
    def minSteps(self, n: int) -> int:
        '''
        n = 1 => 0
        n = 2 => 2
        n = 3 => 3
        n = 4 => 4
        n = 5 => 5
        n = 6 =>
        
        A, A, A, A, 
        
        n = 6
        
        2, 3,
        
        n = 9
        
        '''
        running_sum = 0
        i = 2
        while n > 1:
            while n % i == 0:
                running_sum += i
                n /= i
            
            i += 1
        
        return running_sum
        