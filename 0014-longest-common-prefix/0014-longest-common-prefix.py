class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for word in strs[1:]:
            common = ''
            i = 0
            j = 0
            while i < len(prefix) and j < len(word):
                if word[j] == prefix[i]:
                    common += word[j]
                else: break
                i += 1
                j += 1
            prefix = common
        
        return prefix