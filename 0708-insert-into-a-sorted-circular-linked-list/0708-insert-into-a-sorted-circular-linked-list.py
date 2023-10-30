"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if not head:
            new_node = Node(insertVal)
            new_node.next = new_node
            return new_node

        
        prev = head
        curr = head.next
        flag = False
        while True:
            if prev.val <= insertVal <= curr.val:
                flag = True
            elif prev.val > curr.val:
                if insertVal > prev.val or insertVal < curr.val:
                    flag = True
            elif curr == head:break
            
            if flag:
                prev.next = Node(insertVal, curr)
                return head
            
            prev = curr
            curr = curr.next
        
        prev.next = Node(insertVal, curr)
        return head
            
            