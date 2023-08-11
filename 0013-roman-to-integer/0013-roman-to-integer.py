class Solution:
    def romanToInt(self, s: str) -> int:
        last = s[0]
        m = {
            'I':1, 
            'V': 5,
            'X': 10,
            'L': 50,
            'C':100,
            'D': 500,
            'M':1000
            }
        
        running_sum = m[last]
        
        for char in s[1:]:
            if last == 'I':
                if char == 'V' or char == 'X':
                    running_sum -= 2
                    #running_sum -= m[last]
            
            elif last == 'X':
                if char == 'L' or char =='C':
                    running_sum += -20
                    #running_sum -= m[last]
                    
            elif last == 'C':
                if char == 'D' or char == 'M':
                    running_sum -= 200
                    #running_sum -= m[last]
            
            #unning_sum -= m[last]
            running_sum += m[char]
                
            last = char
                
        return running_sum