class SparseVector:
    def __init__(self, nums: List[int]):
        self.vec = []
        for i, num in enumerate(nums):
            if num != 0:
                self.vec.append((i, num))

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        i1 = 0
        i2 = 0
        l1 = len(self.vec)
        l2 = len(vec.vec)
        
        res = 0
        
        while i1 < l1 and i2 < l2:
            if self.vec[i1][0] < vec.vec[i2][0]:
                i1 += 1
            elif self.vec[i1][0] > vec.vec[i2][0]:
                i2 += 1
            else:
                res += self.vec[i1][1] * vec.vec[i2][1]
                i1 += 1
                i2 += 1
                
        return res

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)