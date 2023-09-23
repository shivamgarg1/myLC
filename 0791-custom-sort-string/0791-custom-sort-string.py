class Solution:
    def customSortString(self, order: str, s: str) -> str:
        
        m = defaultdict(int)
        for i, char in enumerate(order):
            m[char] = i
        
        def compare(left, right):
            if left in m and right in m:
                if m[left] < m[right]:return -1
                elif m[left] > m[right]: return 1
                else:return 0
            elif left in m: return -1
            elif right in m:  
                return 1
            else:return 0
        
        res = list(s)
        res.sort(key=cmp_to_key(compare))
        return ''.join(res)