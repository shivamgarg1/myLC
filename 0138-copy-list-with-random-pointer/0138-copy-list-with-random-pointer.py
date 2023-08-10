"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        '''
        
        '''
        
        new_head = Node(0)
        curr = new_head
        node = head
        m = {}
        while node:
            if node not in m:
                curr.next = Node(node.val)
                m[node] = curr.next
            else:
                curr.next = m[node]
            
            curr = curr.next
            
            if node.random:
                if node.random not in m:
                    new_node = Node(node.random.val)
                    m[node.random] = new_node
                    curr.random = new_node
                else:
                    curr.random = m[node.random]

            node = node.next
        
        
        return new_head.next