class RandomizedSet:

    def __init__(self):
        self.m = {}
        self.l = 0
        self.vec = []

    def insert(self, val: int) -> bool:
        if val not in self.m:
            self.m[val] = self.l
            self.l += 1
            self.vec.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.m:
            last_elem, idx = self.vec[-1], self.m[val]
            self.vec[idx] = last_elem
            self.m[last_elem] = idx
            self.vec.pop()
            self.l -= 1
            del self.m[val]
            return True
        return False

    def getRandom(self) -> int:
        return choice(self.vec)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()