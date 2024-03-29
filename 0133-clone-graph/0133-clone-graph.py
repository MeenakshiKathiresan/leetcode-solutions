"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
from collections import deque
class Solution(object):

    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """

        if not node:
            return node

        visited = {}

        queue = deque([node])
        
        visited[node] = Node(node.val, [])

        while queue:
           
            n = queue.popleft()
            
            for neighbor in n.neighbors:
                if neighbor not in visited:
                   
                    visited[neighbor] = Node(neighbor.val, [])
                    
                    queue.append(neighbor)
               
                visited[n].neighbors.append(visited[neighbor])

        return visited[node]