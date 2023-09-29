# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        
        '''
        
        L >= N
        
        1 -> 2 -> 3
        N = 1 1-> 2
        N = 2, 1-> 3
        N=3, 2->3
        N=4, return -1
        
        3 1
        
        Algo:
        1
        
        
        '''
        
        count = 0
        node = head
        while node:
            count += 1
            node = node.next
        
        if count == n:return head.next
        if n > count: return None
        node = head
        prev = None
        while count - n > 0:
            prev = node
            node = node.next
            count -= 1
        prev.next = node.next
        return head
        