# """
# This is the ImmutableListNode's API interface.
# You should not implement it, or speculate about its implementation.
# """
# class ImmutableListNode:
#     def printValue(self) -> None: # print the value of this node.
#     def getNext(self) -> 'ImmutableListNode': # return the next node.

class Solution:
    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
        # constant space 
        # time O(N**2)
        
        end = None
        while end != head:
            node = head
            while node.getNext() != end:
                node = node.getNext()
            node.printValue()
            end = node