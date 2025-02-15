"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def __init__(self):
        self.nodes = {}

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head:
            if head in self.nodes:
                return self.nodes[head]
            new = ListNode(head.val, None)
            self.nodes[head] = new

            new.next = self.copyRandomList(head.next)
            new.random = self.copyRandomList(head.random)

            return new

        
        