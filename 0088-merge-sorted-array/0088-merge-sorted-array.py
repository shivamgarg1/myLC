class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        
        nums1 = [1, 1, 1, 1, 0 0 0 0 ]
        nums2 = [2, 3, 4, 5]
        
        nums1 = [3, 4, 5, 0 0 0 ]
        nums2 = [1, 2, 2]
        
        
        [1, 2, 2, 0 0 0 ]
                  ^
        [3, 4, 5]
        
        nusm1 = []
        
        algo:
        1) 2 pointer aproach
        while ptr2 < len(nums2)
            2) if ptr1 <= ptr2: do nothing
            3) else: start a while loop until greater index is reached. 
                4) For this range of elements in nums2, swap with nums1[ptr1:ptr1 + l]
        
        
        Time : O(M + N)
        Space: O(1), assuming nums2 could be used for swapping
        
        """
        
        
        k = m + n
        
        while m > 0 and n > 0:
            if nums1[m-1] >= nums2[n-1]:
                nums1[k-1] = nums1[m-1]
                k -= 1
                m -=1
            else:
                nums1[k-1] = nums2[n-1]
                n-= 1
                k -=1
        
        if n <= 0 :return
        while n > 0:
            nums1[k-1] = nums2[n-1]
            n -=1
            k -= 1
        
        return