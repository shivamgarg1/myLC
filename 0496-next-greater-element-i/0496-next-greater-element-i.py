class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        m = {}
        
        stack = []
        
        for num in nums2:
            while stack and num > stack[-1]:
                m[stack.pop()] = num
            stack.append(num)
        
        while stack:
            m[stack.pop()] = -1
        res = []
        for num in nums1:
            res.append(m[num])
        return res