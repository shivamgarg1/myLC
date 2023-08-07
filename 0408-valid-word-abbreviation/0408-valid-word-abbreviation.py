class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = j = 0
        m = len(word)
        n = len(abbr)
        
        while i < m and j < n:
            if word[i] == abbr[j]:
                i += 1
                j += 1
            elif abbr[j].isdigit() and abbr[j] == '0':
                return False
            elif abbr[j].isdigit():
                k = j
                while k < n and abbr[k].isdigit():
                    k += 1
                i += int(abbr[j:k])
                j = k
            else: return False
        return i == m and j == n