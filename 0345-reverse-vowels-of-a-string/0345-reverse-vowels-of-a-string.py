class Solution:
    def reverseVowels(self, s: str) -> str:
        left = 0
        right = len(s) - 1
        ans = [char for char in s]
        m = set({'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'})
        l = len(s)
        while left < right:
            while left < l and s[left] not in m:
                left += 1
            while right >= 0 and s[right] not in m:
                right -= 1
            if left < l and s[left] in m and right >= 0 and s[right] in m and left < right:
                ans[left], ans[right] = ans[right], ans[left]
            
            left += 1
            right -= 1
        
        
        return ''.join(ans)
                
            