"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        
        queue = [root]
        res = []
        if root == None: return None
        
        while queue:
            n = len(queue)
            res.append([])
            for i in range(n):
                curr = queue.pop(0)
                res[-1].append(curr.val)
                for child in curr.children:
                    queue.append(child)
        
        return res