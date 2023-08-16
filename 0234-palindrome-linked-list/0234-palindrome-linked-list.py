# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        l = 0
        node = head
        while node:
            l += 1
            node = node.next
        
        i = 0
        node = head
        prev = None
        while i < l // 2:
            next_node = node.next
            node.next = prev
            prev = node
            node = next_node
            i += 1
        
        # node represents second half
        # prev represents first half
        if l % 2 == 1:
            node = node.next
        
        while node and prev:
            if node.val != prev.val:
                return False
            node = node.next
            prev = prev.next
        
        return True
        