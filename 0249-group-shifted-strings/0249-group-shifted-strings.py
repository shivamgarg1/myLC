class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        
        '''
        1) all lower case? 
        2) only english chars? 
        3) edge cases? \
            "", 'a'
        4) repetitive chars
            'aa', 'bb'
        
        
        'abc' -> 'bcd': "012"
        'aa' will hash fun : "00"
        'acef' will have hash fn : '0235'
        
        
        Space : O(N)
        Time : O(N len(longest string))
        '''

        m = defaultdict(list)
        for string in strings:
            local_hash = [0]
            start_char = string[0]
            for char in string[1:]:
                num = int(ord(char) - ord(start_char))
                if num < 0:
                    num += 26
                local_hash.append( str(num))
            m[tuple(local_hash)].append(string)
        
        res = []
        for k in m.keys():
            res.append(m[k])
        return res