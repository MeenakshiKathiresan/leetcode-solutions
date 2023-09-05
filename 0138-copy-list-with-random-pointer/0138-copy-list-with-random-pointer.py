"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    
    def __init__(self):
        self.visited = {}
    
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head == None: return None
        
        if head in self.visited:
            return self.visited[head]
        
        n = Node(head.val)
        self.visited[head] = n
        
        
        n.random = self.copyRandomList(head.random)
        n.next = self.copyRandomList(head.next)
        
        return n
        
        