class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        if x == 0 : return True
        s = str(x)
        l = len(s)
        i = 0
        while i < l // 2:
            if s[i] != s[l - 1 -i]:return False
            i += 1
        return True
        