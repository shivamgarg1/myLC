class Solution:
    
    def __init__(self, w: List[int]):
        sm = sum(w)
        plist = [i / sm for i in w]
        self.plist = [plist[0]]
        self.l = len(w)
        for i in range(1, self.l):
            self.plist.append(self.plist[i-1] + plist[i])
    def pickIndex(self) -> int:
        num = random.random()
        l = 0
        r = self.l
        while l < r:
            mid = l + ( r - l) // 2
            if self.plist[mid] >= num:
                r = mid
            else:
                l = mid + 1
        
        if l == self.l:
            return l - 1
        return l
    ''' 
    
    def __init__(self, w: List[int]):
        sm = sum(w)
        plist = [i / sm for i in w ]
        self.plist = [plist[0]]
        self.l = len(w)
        for i in range(1, self.l):
            self.plist.append(plist[i] + self.plist[i-1])

    def pickIndex(self) -> int:
        num = random.random()
        l = 0
        r = self.l
        
        while l < r:
            mid = l + (r - l) // 2
            if self.plist[mid] >= num:
                r = mid
            else:
                l = mid + 1
        
        if l == self.l:return self.l-1
        return l
    '''