class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ''
        l1 = len(word1)
        l2 = len(word2)
        
        i1 = 0
        i2 = 0
        
        while i1 < l1 and i2 < l2:
            res += word1[i1] + word2[i2]
            i1 += 1
            i2 += 1
        
        while i1 < l1:
            res += word1[i1]
            i1 += 1
        
        while i2 < l2:
            res += word2[i2]
            i2 += 1
        
        return res
            
        