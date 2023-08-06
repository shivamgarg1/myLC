class Solution:
    def validPalindrome(self, s: str) -> bool:
        '''
        
        
        . . . i, i+1, i+2, .. . . j-2, j-1, j, . . .
              ^                             ^
              => elem[i+1] == elem[j] 
              or, elem[j-1] == elem[i]
              
              algo: 
              1) create from and back ptrs pointing to first and last elem of arr
              2) if elems at both pointers are same, increment front and dec back ptr.
              3) a. When not same, cehck for i+1/j:
                   -> if same, set i to i +2 and j to j -1
                b. else check for i and j-1, if same, set i to i + 1 and j to j -2
               if not a & b, return false
               4) Also set flag so that only one deletion is tolerated
        
        
        Example 1: "aba" f = 0, b = 2
        Example 2: "abca", f = 0, b = 3
                iter 2) f = 1, b = 2
        
        
        '''
        
        i = 0
        l = len(s)
        for i in range(l // 2):
            if s[i] != s[l-1-i]:
                return s[i+1  : l-i] == s[i+1: l -i][::-1] or s[i:l-i-1] == s[i: l-i-1][::-1]
        return True
        
        '''
        def isParlindrome(arr, front, back):
            while front < back:
                if arr[front] == arr[back]:
                    front += 1
                    back -=1
                else:return False
            return True
        
        front = 0
        back = len(s) - 1
        while front < back:
            
        
        
        '''
        
        
        
        
        
        